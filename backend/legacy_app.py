from pathlib import Path
import uuid
import json

import pandas as pd
from flask import Flask, render_template, request, send_from_directory

from model_service import PolixXAIPredictor
from feature_extractor import extract_matrix_c_from_uploaded_archive
from visualization_service import create_result_visualizations
from polarization_service import PolixPolarimetryService
from result_exporter import results_to_dataframe


BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
STATIC_DIR = BASE_DIR / "static"
PLOT_ROOT = STATIC_DIR / "plots"

MODEL_PATH = BASE_DIR / "model" / "polix_v2_matrixC_unsupervised_xai_model.pkl"

POLARIMETRY_CONFIG_PATH = (
    BASE_DIR / "config" / "polarimetry_config.json"
)

OBSERVATION_METADATA_PATH = (
    BASE_DIR / "config" / "observation_metadata.json"
)

UPLOAD_DIR.mkdir(exist_ok=True)
PLOT_ROOT.mkdir(parents=True, exist_ok=True)

app = Flask(__name__)

predictor = PolixXAIPredictor(MODEL_PATH)

polarimetry_service = PolixPolarimetryService(
    POLARIMETRY_CONFIG_PATH
)

with OBSERVATION_METADATA_PATH.open(
    "r",
    encoding="utf-8"
) as file:
    observation_metadata = json.load(file)


def get_observation_metadata(observation_id):
    """
    Convert:
    X01_PLX_G01_0003_000000
    into proposal ID:
    G01_0003
    """
    parts = str(observation_id).split("_")

    if len(parts) < 4:
        return {
            "proposal_id": "unknown",
            "target_name": "Unknown target",
            "observation_role": "unknown",
        }

    proposal_id = f"{parts[2]}_{parts[3]}"

    metadata = observation_metadata.get(
        proposal_id,
        {}
    )

    return {
        "proposal_id": proposal_id,
        "target_name": metadata.get(
            "target_name",
            "Unknown target"
        ),
        "observation_role": metadata.get(
            "observation_role",
            "unknown"
        ),
    }


def build_scientific_interpretation(result):
    """
    Combine source metadata, XAI output and polarimetry diagnostics
    into one scientifically cautious interpretation.
    """

    target_name = result.get(
        "target_name",
        "Unknown target"
    )

    observation_role = result.get(
        "observation_role",
        "unknown"
    )

    prediction = result.get(
        "prediction",
        "Unknown"
    )

    top_features = result.get(
        "top_xai_features"
    ) or []

    if top_features:
        strongest_feature = top_features[0].get(
            "feature",
            "unknown feature"
        )

        strongest_family = top_features[0].get(
            "product_family",
            "unknown product family"
        )
    else:
        strongest_feature = "unavailable"
        strongest_family = "unavailable"

    polarimetry = result.get("polarimetry")

    # CSV uploads do not contain WeightedRoll FITS products.
    if not polarimetry:
        return (
            f"{target_name} is classified as {prediction}. "
            f"The strongest XAI driver is {strongest_feature} "
            f"from {strongest_family}. Physical polarimetry analysis "
            f"is unavailable because this input contains extracted "
            f"features rather than raw POLIX Level-2 products."
        )

    if polarimetry.get("polarimetry_error"):
        return (
            f"{target_name} is classified as {prediction}. "
            f"The strongest XAI driver is {strongest_feature} "
            f"from {strongest_family}. Polarimetry processing could "
            f"not be completed for this observation."
        )

    fit_quality = polarimetry.get(
        "fit_quality",
        "unknown"
    )

    vector_status = polarimetry.get(
        "background_relative_vector_status",
        "unknown"
    )

    confidence_status = polarimetry.get(
        "polarimetry_confidence_status",
        "unknown"
    )

    pd_proxy = polarimetry.get(
        "selected_background_relative_pd_proxy_percent"
    )

    if isinstance(pd_proxy, (int, float)):
        pd_proxy_text = f"{pd_proxy:.3f}%"
    else:
        pd_proxy_text = "unavailable"

    # Blank-sky observations are references, not astrophysical sources.
    if observation_role == "blank_sky":
        if prediction == "Anomaly":
            return (
                f"{target_name} is a blank-sky reference that was flagged "
                f"as anomalous. Its strongest XAI driver is "
                f"{strongest_feature} from {strongest_family}. This result "
                f"should be interpreted as unusual background or instrument "
                f"behaviour, not source polarization."
            )

        return (
            f"{target_name} is a blank-sky background reference and was "
            f"classified as normal. It contributes to understanding the "
            f"instrument/background modulation baseline."
        )

    # Source observation: anomaly + vector difference + acceptable fit.
    if (
        prediction == "Anomaly"
        and vector_status in {
            "moderate_background_relative_vector_difference",
            "strong_background_relative_vector_difference",
        }
        and fit_quality == "acceptable"
    ):
        return (
            f"{target_name} is an XAI anomaly and also shows a "
            f"background-relative modulation-vector difference. "
            f"The selected background-relative PD proxy is "
            f"{pd_proxy_text}. This is a priority inspection candidate, "
            f"but it is not a final calibrated polarization detection."
        )

    # Source observation: vector difference exists, but fit is limited.
    if (
        vector_status in {
            "moderate_background_relative_vector_difference",
            "strong_background_relative_vector_difference",
        }
        and fit_quality != "acceptable"
    ):
        return (
            f"{target_name} shows a background-relative modulation-vector "
            f"difference and has a selected PD proxy of {pd_proxy_text}, "
            f"but the modulation fit quality is {fit_quality}. "
            f"It is therefore a low-confidence inspection candidate and "
            f"must not be reported as a polarization detection."
        )

    # XAI anomaly, but no polarization-like difference.
    if (
        prediction == "Anomaly"
        and vector_status == "within_blank_sky_vector_scatter"
    ):
        return (
            f"{target_name} is flagged as anomalous mainly because of "
            f"{strongest_feature} from {strongest_family}. However, its "
            f"modulation vector remains within blank-sky scatter. "
            f"The anomaly is therefore not interpreted as evidence of "
            f"polarization-like behaviour."
        )

    # Normal source and modulation inside background behaviour.
    if (
        prediction == "Normal"
        and vector_status == "within_blank_sky_vector_scatter"
    ):
        return (
            f"{target_name} is not flagged as anomalous, and its "
            f"modulation vector remains within blank-sky scatter. "
            f"The selected background-relative PD proxy is "
            f"{pd_proxy_text}, but it is only a sensitivity estimate "
            f"and not a final calibrated polarization measurement."
        )

    return (
        f"{target_name} is classified as {prediction}. "
        f"The polarimetry confidence status is {confidence_status}, "
        f"and the selected background-relative PD proxy is "
        f"{pd_proxy_text}. Final calibrated PD and official PA "
        f"are not claimed."
    )


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route(
    "/download/<session_id>/<filename>",
    methods=["GET"]
)
def download_result(session_id, filename):
    session_dir = UPLOAD_DIR / session_id

    return send_from_directory(
        directory=session_dir,
        path=filename,
        as_attachment=True
    )


@app.route("/predict", methods=["POST"])
def predict():
    upload_mode = request.form.get("upload_mode")
    file = request.files.get("file")

    if file is None or file.filename == "":
        return "No file uploaded", 400

    session_id = str(uuid.uuid4())

    session_upload_dir = UPLOAD_DIR / session_id
    session_upload_dir.mkdir(parents=True, exist_ok=True)

    session_plot_dir = PLOT_ROOT / session_id
    session_plot_dir.mkdir(parents=True, exist_ok=True)

    upload_path = session_upload_dir / file.filename
    file.save(upload_path)

    polarimetry_results = []

    try:
        if upload_mode == "csv":
            df = pd.read_csv(upload_path)

        elif upload_mode == "raw":
            extracted_dir = session_upload_dir / "extracted"

            df = extract_matrix_c_from_uploaded_archive(
                upload_path,
                extracted_dir
            )

            polarimetry_results = (
                polarimetry_service.analyze_extracted_root(
                    extracted_dir
                )
            )

        else:
            return "Invalid upload mode", 400

        results = predictor.predict_dataframe(df)

        polarimetry_by_id = {
            item["observation_id"]: item
            for item in polarimetry_results
        }

        for result in results:
            observation_id = result["observation_id"]

            result["polarimetry"] = polarimetry_by_id.get(
                observation_id
            )

            metadata = get_observation_metadata(
                observation_id
            )

            result.update(metadata)

            if result["polarimetry"] is not None:
                result["polarimetry"].update(metadata)

            result["scientific_interpretation"] = (
                build_scientific_interpretation(result)
            )

        combined_results_df = results_to_dataframe(results)

        result_csv_filename = (
            "polix_xai_polarimetry_combined_results.csv"
        )

        result_csv_path = (
            session_upload_dir / result_csv_filename
        )

        combined_results_df.to_csv(
            result_csv_path,
            index=False
        )

        download_url = (
            f"/download/{session_id}/{result_csv_filename}"
        )

        summary_plots, result_plot_map = create_result_visualizations(
            results=results,
            plot_dir=session_plot_dir,
            url_prefix=f"/static/plots/{session_id}"
        )

        for r in results:
            plot_info = result_plot_map.get(r["observation_id"], {})
            r["xai_bar_url"] = plot_info.get("xai_bar_url")
            r["xai_component_url"] = plot_info.get("xai_component_url")

        anomaly_count = sum(1 for r in results if r["prediction"] == "Anomaly")
        normal_count = len(results) - anomaly_count

        return render_template(
            "result.html",
            results=results,
            row_count=len(results),
            upload_mode=upload_mode,
            anomaly_count=anomaly_count,
            normal_count=normal_count,
            summary_plots=summary_plots,
            download_url=download_url,
        )

    except Exception as e:
        return f"<h3>Error</h3><pre>{str(e)}</pre>", 500


if __name__ == "__main__":
    app.run(debug=True)