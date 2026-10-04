from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from astropy.io import fits


ROOT = Path(r"D:\polix_xai_webapp")
ARCHIVE = Path(r"D:\ISROtrial\Polix_L2_full_archive")
OUTPUT = ROOT / "figure_audit_figures"
SUPPORT = ROOT / "figure_audit_support"

MATRIX_C = ARCHIVE / "final_project_outputs" / "02_feature_engineering" / "polix_matrix_v2_C_primary_plus_supporting.csv"
FIT_RESULTS = ARCHIVE / "final_project_outputs" / "04_polarimetry_results" / "polix_weightedroll_raw_modulation_fits.csv"
MODEL_REPRO = ROOT / "research_paper_ieee" / "supplementary_experiments" / "deployed_model_reproduction.csv"
XAI_EXACT = ROOT / "research_paper_ieee" / "supplementary_experiments" / "deployed_xai_exact_from_model_service.csv"
MODEL = ROOT / "model" / "polix_v2_matrixC_unsupervised_xai_model.pkl"
METADATA = ROOT / "config" / "observation_metadata.json"

BLUE = "#3C78A8"
ORANGE = "#C85A1A"
DARK = "#252A2E"
GRID = "#D9DDE1"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def save_figure(fig: plt.Figure, stem: str) -> list[Path]:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    paths = [OUTPUT / f"{stem}.png", OUTPUT / f"{stem}.pdf", OUTPUT / f"{stem}.svg"]
    fig.savefig(paths[0], dpi=300, bbox_inches="tight", facecolor="white")
    fig.savefig(paths[1], bbox_inches="tight", facecolor="white")
    fig.savefig(paths[2], bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return paths


def short_id(observation_id: str) -> str:
    return observation_id.removeprefix("X01_PLX_").removesuffix("_000000")


def read_weightedroll(path: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    with fits.open(path, memmap=False) as hdul:
        table = hdul[1].data
        angle = np.asarray(table["ROLL_AZ_ANG"], dtype=float)
        rate = np.asarray(table["TOTAL_COUNTRATE"], dtype=float)
        error = np.asarray(table["ERROR"], dtype=float)
    valid = np.isfinite(angle) & np.isfinite(rate) & np.isfinite(error) & (error > 0)
    return angle[valid], rate[valid], error[valid]


def weightedroll_figure() -> tuple[list[Path], pd.DataFrame]:
    fits_table = pd.read_csv(FIT_RESULTS).set_index("observation_id")
    predictions = pd.read_csv(MODEL_REPRO).set_index("observation_id")
    metadata = json.loads(METADATA.read_text(encoding="utf-8"))

    # These three cases were chosen before plotting because they answer distinct
    # questions: stable candidate with a near-boundary fit, fixed-Normal source
    # with an acceptable fit and larger raw modulation, and a visibly poor fit.
    cases = [
        ("X01_PLX_G01_0006_000000", "Sco X-1"),
        ("X01_PLX_P01_0005_000000", "Crab P01_0005"),
        ("X01_PLX_G01_0003_000000", "Her X-1"),
    ]

    fig = plt.figure(figsize=(7.16, 5.05), constrained_layout=True)
    grid = fig.add_gridspec(2, 3, height_ratios=[3.1, 1.0], hspace=0.04)
    verification: list[dict[str, object]] = []

    for index, (observation_id, display_name) in enumerate(cases):
        row = fits_table.loc[observation_id]
        folder = ARCHIVE / "data_extracted" / str(row["observation_folder"]) / "Polix_l2_polarization"
        source = folder / str(row["weightedroll_file"])
        angle, rate, error = read_weightedroll(source)

        phi = np.deg2rad(angle)
        model_rate = (
            float(row["C_mean_level"])
            + float(row["Q_cos2_coeff"]) * np.cos(2.0 * phi)
            + float(row["U_sin2_coeff"]) * np.sin(2.0 * phi)
        )
        normalized_residual = (rate - model_rate) / error
        direct_chi2 = float(np.sum(normalized_residual**2))
        direct_reduced_chi2 = direct_chi2 / (len(rate) - 3)
        if not np.isclose(direct_reduced_chi2, float(row["reduced_chi2"]), rtol=0, atol=1e-10):
            raise RuntimeError(f"Reduced chi-square mismatch for {observation_id}")

        stored_prediction = str(predictions.loc[observation_id, "stored_prediction"])
        prediction = "Candidate" if stored_prediction == "Anomaly" else "Normal"
        category = "acceptable" if float(row["reduced_chi2"]) <= 2 else ("caution" if float(row["reduced_chi2"]) <= 5 else "poor")

        ax = fig.add_subplot(grid[0, index])
        ax.errorbar(
            angle,
            rate,
            yerr=error,
            fmt=".",
            ms=1.9,
            lw=0.35,
            elinewidth=0.35,
            capsize=0,
            color=BLUE,
            alpha=0.62,
            rasterized=True,
            label="Delivered curve ± supplied error",
        )
        order = np.argsort(angle)
        ax.plot(angle[order], model_rate[order], color=ORANGE, lw=1.25, label="Saved second-harmonic fit")
        ax.set_title(f"({chr(97 + index)}) {display_name}", fontsize=8.4, fontweight="bold")
        ax.text(
            0.03,
            0.97,
            f"ML: {prediction}\n$\\chi^2_{{red}}$ = {float(row['reduced_chi2']):.2f} ({category})",
            transform=ax.transAxes,
            va="top",
            fontsize=6.8,
            bbox=dict(boxstyle="round,pad=0.22", facecolor="white", edgecolor=GRID, alpha=0.93),
        )
        ax.set_xlim(0, 359)
        ax.set_xticks([0, 90, 180, 270, 360])
        ax.grid(True, color=GRID, lw=0.5, alpha=0.8)
        ax.tick_params(labelsize=6.8)
        if index == 0:
            ax.set_ylabel("Delivered total count rate", fontsize=7.7)
        if index == 2:
            ax.legend(loc="lower right", fontsize=5.8, frameon=True)

        residual_ax = fig.add_subplot(grid[1, index], sharex=ax)
        residual_ax.axhline(0, color=DARK, lw=0.65)
        residual_ax.scatter(angle, normalized_residual, s=3.0, color=BLUE, alpha=0.58, rasterized=True)
        residual_ax.set_xlabel("Delivered roll-azimuth angle (deg)", fontsize=7.1)
        residual_ax.grid(True, color=GRID, lw=0.45, alpha=0.8)
        residual_ax.tick_params(labelsize=6.5)
        if index == 0:
            residual_ax.set_ylabel("Residual / error", fontsize=7.1)

        verification.append(
            {
                "observation_id": observation_id,
                "display_name": display_name,
                "observation_role": metadata[short_id(observation_id)]["observation_role"],
                "fixed_ml_label": stored_prediction,
                "weightedroll_fits_path": str(source),
                "weightedroll_fits_sha256": sha256(source),
                "plotted_points": len(rate),
                "C_from_saved_csv": float(row["C_mean_level"]),
                "Q_from_saved_csv": float(row["Q_cos2_coeff"]),
                "U_from_saved_csv": float(row["U_sin2_coeff"]),
                "stored_raw_modulation_percent": float(row["raw_modulation_percent"]),
                "stored_reduced_chi2": float(row["reduced_chi2"]),
                "direct_reduced_chi2_from_fits_and_saved_coefficients": direct_reduced_chi2,
                "fit_category_used_in_figure": category,
            }
        )

    fig.suptitle("Representative delivered WeightedRoll curves and saved second-harmonic fits", fontsize=9.2, fontweight="bold")
    outputs = save_figure(fig, "FigA_representative_weightedroll_fits")
    return outputs, pd.DataFrame(verification)


def xai_figure() -> tuple[list[Path], pd.DataFrame]:
    matrix = pd.read_csv(MATRIX_C)
    package = joblib.load(MODEL)
    features = list(package["feature_cols"])
    scaled = np.asarray(package["scaler"].transform(matrix[features]), dtype=float)
    ids = matrix["observation_id"].astype(str).to_numpy()
    sco_id = "X01_PLX_G01_0006_000000"
    sco_index = int(np.flatnonzero(ids == sco_id)[0])

    exact = pd.read_csv(XAI_EXACT)
    exact = exact[exact["observation_id"] == sco_id].copy()
    exact = exact.sort_values("xai_score", ascending=False).head(3)
    top_features = exact["feature"].tolist()

    feature_labels = {
        "t1A_energy_peak_channel": "Energy peak channel",
        "t1A_energy_weighted_mean_channel": "Weighted mean channel",
        "t1A_energy_channel_entropy": "Channel entropy",
    }

    fig = plt.figure(figsize=(7.16, 3.15), constrained_layout=True)
    grid = fig.add_gridspec(1, 2, width_ratios=[2.2, 1.0])
    ax = fig.add_subplot(grid[0, 0])
    bar_ax = fig.add_subplot(grid[0, 1])
    verification: list[dict[str, object]] = []

    for y_position, feature in enumerate(top_features[::-1]):
        feature_index = features.index(feature)
        values = scaled[:, feature_index]
        y = np.full(len(values), y_position, dtype=float)
        ax.scatter(values, y, s=18, facecolors="white", edgecolors="#7A858D", linewidths=0.6, alpha=0.9, zorder=2)
        ax.scatter(
            [values[sco_index]],
            [y_position],
            marker="D",
            s=58,
            color=ORANGE,
            edgecolor=DARK,
            linewidth=0.8,
            zorder=4,
        )
        raw_value = float(matrix.loc[sco_index, feature])
        xai_row = exact.loc[exact["feature"] == feature].iloc[0]
        if not np.isclose(values[sco_index], float(xai_row["z_score"]), rtol=0, atol=1e-10):
            raise RuntimeError(f"Saved/deployed standardized-value mismatch for {feature}")
        annotation_offsets = {
            "t1A_energy_peak_channel": (-8, -28, "right"),
            "t1A_energy_weighted_mean_channel": (8, 12, "left"),
            "t1A_energy_channel_entropy": (8, 12, "left"),
        }
        dx, dy, horizontal_alignment = annotation_offsets[feature]
        ax.annotate(
            f"Sco X-1: z={values[sco_index]:+.2f}\nraw={raw_value:.3f}",
            (values[sco_index], y_position),
            xytext=(dx, dy),
            textcoords="offset points",
            ha=horizontal_alignment,
            fontsize=6.2,
            color=DARK,
        )
        verification.append(
            {
                "observation_id": sco_id,
                "feature": feature,
                "product_family": str(xai_row["product_family"]),
                "raw_feature_value": raw_value,
                "standardized_value_from_saved_scaler": values[sco_index],
                "saved_deployed_z_score": float(xai_row["z_score"]),
                "saved_project_local_ranking_score": float(xai_row["xai_score"]),
            }
        )

    ax.axvline(0, color=DARK, lw=0.75, ls="--")
    ax.set_yticks(range(3), [feature_labels[name] for name in top_features[::-1]], fontsize=7.4)
    ax.set_xlabel("Standardized Matrix-C value (archive-relative z)", fontsize=7.5)
    ax.set_title("(a) Feature value relative to the 25-observation archive", fontsize=8.2, fontweight="bold")
    ax.grid(axis="x", color=GRID, lw=0.5)
    ax.tick_params(axis="x", labelsize=6.8)

    bars = exact.iloc[::-1]
    bar_ax.barh(
        range(3),
        bars["xai_score"].astype(float),
        color=BLUE,
        edgecolor=DARK,
        linewidth=0.6,
    )
    for idx, value in enumerate(bars["xai_score"].astype(float)):
        bar_ax.text(value + 0.035, idx, f"{value:.3f}", va="center", fontsize=6.8)
    bar_ax.set_yticks(range(3), [feature_labels[name] for name in top_features[::-1]], fontsize=7.1)
    bar_ax.set_xlabel("Project local-ranking score", fontsize=7.5)
    bar_ax.set_title("(b) Separate heuristic ranking", fontsize=8.2, fontweight="bold")
    bar_ax.set_xlim(0, max(exact["xai_score"].astype(float)) * 1.22)
    bar_ax.grid(axis="x", color=GRID, lw=0.5)
    bar_ax.tick_params(axis="x", labelsize=6.8)
    bar_ax.text(
        0.02,
        0.02,
        "Product family: Tier-1A EnergyRes\nScore is ordinal, not probability or cause",
        transform=bar_ax.transAxes,
        fontsize=6.1,
        va="bottom",
        bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor=GRID),
    )

    fig.suptitle("Archive-relative explanation of Sco X-1", fontsize=9.2, fontweight="bold")
    outputs = save_figure(fig, "FigB_sco_x1_archive_relative_xai")
    return outputs, pd.DataFrame(verification)


def notebook_inventory() -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    terms = (
        "weightedroll",
        "matrix_c",
        "matrix c",
        "standardscaler",
        "pca",
        "kmeans",
        "isolationforest",
        "explain",
        "faithfulness",
        "cos(2",
        "raw_modulation",
        "blank_sky",
    )
    for path in sorted(ARCHIVE.glob("*.ipynb")):
        notebook = json.loads(path.read_text(encoding="utf-8"))
        cells = notebook.get("cells", [])
        code_cells = [cell for cell in cells if cell.get("cell_type") == "code"]
        matched = []
        for index, cell in enumerate(cells):
            source = "".join(cell.get("source", []))
            if any(term in source.lower() for term in terms):
                matched.append(index)
        rows.append(
            {
                "notebook": path.name,
                "path": str(path),
                "sha256": sha256(path),
                "total_cells": len(cells),
                "code_cells": len(code_cells),
                "relevant_cell_indices_zero_based": ";".join(map(str, matched)),
            }
        )
    return pd.DataFrame(rows)


def csv_inventory() -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for path in sorted((ARCHIVE / "final_project_outputs").rglob("*.csv")):
        try:
            frame = pd.read_csv(path)
        except pd.errors.EmptyDataError:
            rows.append(
                {
                    "path": str(path),
                    "sha256": sha256(path),
                    "rows": 0,
                    "columns": 0,
                    "column_names": "EMPTY_FILE",
                }
            )
            continue
        rows.append(
            {
                "path": str(path),
                "sha256": sha256(path),
                "rows": len(frame),
                "columns": len(frame.columns),
                "column_names": ";".join(map(str, frame.columns)),
            }
        )
    return pd.DataFrame(rows)


def write_provenance(outputs: dict[str, list[Path]]) -> None:
    source_map = {
        "FigA_representative_weightedroll_fits": [FIT_RESULTS, MODEL_REPRO, METADATA],
        "FigB_sco_x1_archive_relative_xai": [MATRIX_C, XAI_EXACT, MODEL],
    }
    rows: list[dict[str, str]] = []
    for figure, source_paths in source_map.items():
        for path in source_paths:
            rows.append({"figure": figure, "role": "source", "path": str(path), "sha256": sha256(path)})
        for path in outputs[figure]:
            rows.append({"figure": figure, "role": "output", "path": str(path), "sha256": sha256(path)})
    with (SUPPORT / "figure_provenance.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=["figure", "role", "path", "sha256"])
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    SUPPORT.mkdir(parents=True, exist_ok=True)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.edgecolor": DARK,
            "axes.linewidth": 0.8,
            "figure.facecolor": "white",
            "savefig.facecolor": "white",
        }
    )

    weighted_outputs, weighted_verification = weightedroll_figure()
    xai_outputs, xai_verification = xai_figure()
    weighted_verification.to_csv(SUPPORT / "weightedroll_figure_verification.csv", index=False)
    xai_verification.to_csv(SUPPORT / "xai_figure_verification.csv", index=False)
    notebook_inventory().to_csv(SUPPORT / "notebook_audit_summary.csv", index=False)
    csv_inventory().to_csv(SUPPORT / "final_outputs_csv_inventory.csv", index=False)
    outputs = {
        "FigA_representative_weightedroll_fits": weighted_outputs,
        "FigB_sco_x1_archive_relative_xai": xai_outputs,
    }
    write_provenance(outputs)


if __name__ == "__main__":
    main()
