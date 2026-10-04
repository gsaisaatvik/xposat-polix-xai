from __future__ import annotations

import json
from pathlib import Path
import sys
import uuid

import pandas as pd
from flask import Flask, jsonify, request, send_from_directory
from werkzeug.utils import secure_filename

BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from feature_extractor import extract_matrix_c_from_uploaded_archive
from model_service import PolixXAIPredictor
from polarization_service import PolixPolarimetryService
from result_exporter import results_to_dataframe
from visualization_service import create_result_visualizations

MODEL_PATH = BASE_DIR / "model" / "polix_v2_matrixC_unsupervised_xai_model.pkl"
POLARIMETRY_CONFIG_PATH = BASE_DIR / "config" / "polarimetry_config.json"
OBSERVATION_METADATA_PATH = BASE_DIR / "config" / "observation_metadata.json"

RUNTIME_ROOT = BASE_DIR / "runtime"
UPLOAD_ROOT = RUNTIME_ROOT / "uploads"
PLOT_ROOT = RUNTIME_ROOT / "generated"
UPLOAD_ROOT.mkdir(parents=True, exist_ok=True)
PLOT_ROOT.mkdir(parents=True, exist_ok=True)

REPRODUCTION_PATH = BASE_DIR / "data" / "deployed_model_reproduction.csv"
SEED_PATH = BASE_DIR / "data" / "isolation_seed_stability_summary.csv"

# Fallback to research_paper_ieee if data dir doesn't exist
if not REPRODUCTION_PATH.exists():
    REPRODUCTION_PATH = (
        BASE_DIR.parent
        / "docs"
        / "research"
        / "research_paper_ieee"
        / "supplementary_experiments"
        / "deployed_model_reproduction.csv"
    )
if not SEED_PATH.exists():
    SEED_PATH = (
        BASE_DIR.parent
        / "docs"
        / "research"
        / "research_paper_ieee"
        / "supplementary_experiments"
        / "isolation_seed_stability_summary.csv"
    )

predictor = PolixXAIPredictor(MODEL_PATH)
polarimetry_service = PolixPolarimetryService(POLARIMETRY_CONFIG_PATH)

with OBSERVATION_METADATA_PATH.open("r", encoding="utf-8") as file:
    observation_metadata = json.load(file)


def get_observation_metadata(observation_id: str):
    """
    Convert: X01_PLX_G01_0003_000000 into proposal ID: G01_0003
    """
    parts = str(observation_id).split("_")
    if len(parts) < 4:
        return {
            "proposal_id": "unknown",
            "target_name": "Unknown target",
            "observation_role": "unknown",
        }

    proposal_id = f"{parts[2]}_{parts[3]}"
    metadata = observation_metadata.get(proposal_id, {})
    return {
        "proposal_id": proposal_id,
        "target_name": metadata.get("target_name", "Unknown target"),
        "observation_role": metadata.get("observation_role", "unknown"),
    }


def build_scientific_interpretation(result: dict) -> str:
    """
    Combine source metadata, XAI output and polarimetry diagnostics
    into one scientifically cautious interpretation.
    """
    target_name = result.get("target_name", "Unknown target")
    observation_role = result.get("observation_role", "unknown")
    prediction = result.get("prediction", "Unknown")
    top_features = result.get("top_xai_features") or []

    if top_features:
        strongest_feature = top_features[0].get("feature", "unknown feature")
        strongest_family = top_features[0].get("product_family", "unknown product family")
    else:
        strongest_feature = "unavailable"
        strongest_family = "unavailable"

    polarimetry = result.get("polarimetry")

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

    fit_quality = polarimetry.get("fit_quality", "unknown")
    vector_status = polarimetry.get("background_relative_vector_status", "unknown")
    confidence_status = polarimetry.get("polarimetry_confidence_status", "unknown")
    pd_proxy = polarimetry.get("selected_background_relative_pd_proxy_percent")

    if isinstance(pd_proxy, (int, float)):
        pd_proxy_text = f"{pd_proxy:.3f}%"
    else:
        pd_proxy_text = "unavailable"

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

    if prediction == "Anomaly" and vector_status == "within_blank_sky_vector_scatter":
        return (
            f"{target_name} is flagged as anomalous mainly because of "
            f"{strongest_feature} from {strongest_family}. However, its "
            f"modulation vector remains within blank-sky scatter. "
            f"The anomaly is therefore not interpreted as evidence of "
            f"polarization-like behaviour."
        )

    if prediction == "Normal" and vector_status == "within_blank_sky_vector_scatter":
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


app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 800 * 1024 * 1024


@app.get("/api/health")
def health():
    return jsonify(
        {
            "status": "ready",
            "service": "POLIX scientific API adapter",
            "model": "frozen Matrix-C deployment",
        }
    )


@app.get("/api/project")
def project():
    return jsonify(
        {
            "title": "An Explainable AI Framework for Analysis of X-Ray Polarimetry Data from XPoSat",
            "archive_observations": 25,
            "source_observations": 10,
            "blank_sky_observations": 15,
            "matrix_c_features": 15,
            "fixed_candidates": 4,
            "seed_stable_core": 3,
            "boundaries": [
                "Archive-relative screening, not confirmed anomaly detection.",
                "Raw harmonic diagnostics, not calibrated polarization degree.",
                "Fitted modulation phase, not official sky polarization angle.",
            ],
        }
    )


@app.get("/api/study-archive")
def study_archive():
    """Return the saved 25-observation study result without recomputation."""
    reproduced = pd.read_csv(REPRODUCTION_PATH)
    seeds = pd.read_csv(SEED_PATH).set_index("observation_id")
    rows = []

    for _, row in reproduced.iterrows():
        observation_id = str(row["observation_id"])
        parts = observation_id.split("_")
        proposal_id = f"{parts[2]}_{parts[3]}"
        meta = observation_metadata.get(proposal_id, {})
        seed = seeds.loc[observation_id]
        rows.append(
            {
                "observation_id": observation_id,
                "proposal_id": proposal_id,
                "target_name": meta.get("target_name", proposal_id),
                "observation_role": meta.get("observation_role", "unknown"),
                "prediction": str(row["stored_prediction"]),
                "anomaly_score": float(row["stored_anomaly_score"]),
                "times_flagged": int(seed["times_flagged"]),
                "seeds_evaluated": int(seed["seeds_evaluated"]),
                "flag_frequency": float(seed["flag_frequency"]),
            }
        )

    rows.sort(key=lambda item: item["anomaly_score"], reverse=True)
    return jsonify(
        {
            "source": "saved deployed-model reproduction and 100-seed summary",
            "count": len(rows),
            "observations": rows,
        }
    )


@app.post("/api/analyze")
def analyze():
    upload_mode = request.form.get("upload_mode", "raw")
    uploaded = request.files.get("file")

    if uploaded is None or not uploaded.filename:
        return jsonify({"success": False, "error": "No file was uploaded."}), 400

    if upload_mode not in {"raw", "csv"}:
        return jsonify({"success": False, "error": "Invalid upload mode."}), 400

    filename = secure_filename(uploaded.filename)
    if not filename:
        return jsonify({"success": False, "error": "Invalid filename."}), 400

    session_id = str(uuid.uuid4())
    session_dir = UPLOAD_ROOT / session_id
    plot_dir = PLOT_ROOT / session_id
    session_dir.mkdir(parents=True, exist_ok=False)
    plot_dir.mkdir(parents=True, exist_ok=False)
    upload_path = session_dir / filename
    uploaded.save(upload_path)

    try:
        polarimetry_results = []

        if upload_mode == "csv":
            dataframe = pd.read_csv(upload_path)
        else:
            extracted_dir = session_dir / "extracted"
            dataframe = extract_matrix_c_from_uploaded_archive(
                upload_path,
                extracted_dir,
            )
            polarimetry_results = polarimetry_service.analyze_extracted_root(
                extracted_dir
            )

        results = predictor.predict_dataframe(dataframe)
        polarimetry_by_id = {
            item["observation_id"]: item for item in polarimetry_results
        }

        for item in results:
            observation_id = item["observation_id"]
            item["polarimetry"] = polarimetry_by_id.get(observation_id)
            metadata = get_observation_metadata(observation_id)
            item.update(metadata)
            if item["polarimetry"] is not None:
                item["polarimetry"].update(metadata)
            item["scientific_interpretation"] = build_scientific_interpretation(item)

        export_name = "polix_xai_polarimetry_combined_results.csv"
        results_to_dataframe(results).to_csv(session_dir / export_name, index=False)

        summary_plots, plot_map = create_result_visualizations(
            results=results,
            plot_dir=plot_dir,
            url_prefix=f"/generated/{session_id}",
        )
        for item in results:
            plot_info = plot_map.get(item["observation_id"], {})
            item["xai_bar_url"] = plot_info.get("xai_bar_url")
            item["xai_component_url"] = plot_info.get("xai_component_url")

        anomaly_count = sum(
            1 for item in results if item["prediction"] == "Anomaly"
        )

        return jsonify(
            {
                "success": True,
                "session_id": session_id,
                "upload_mode": upload_mode,
                "row_count": len(results),
                "anomaly_count": anomaly_count,
                "normal_count": len(results) - anomaly_count,
                "results": results,
                "summary_plots": summary_plots,
                "download_url": f"/api/download/{session_id}/{export_name}",
            }
        )
    except Exception as exc:
        return (
            jsonify(
                {
                    "success": False,
                    "session_id": session_id,
                    "error": str(exc),
                }
            ),
            500,
        )


@app.get("/api/download/<session_id>/<filename>")
def download(session_id: str, filename: str):
    return send_from_directory(
        UPLOAD_ROOT / session_id,
        filename,
        as_attachment=True,
    )


@app.get("/generated/<session_id>/<filename>")
def generated(session_id: str, filename: str):
    return send_from_directory(PLOT_ROOT / session_id, filename)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=False)
