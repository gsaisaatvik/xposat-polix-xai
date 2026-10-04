"""Generate the four Phase-4 paper figures from frozen project artifacts.

This script performs visualization-only transformations. It does not train,
refit, tune, or change any scientific result.
"""

from __future__ import annotations

import csv
import hashlib
import warnings
from pathlib import Path

import joblib
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Patch


ROOT = Path(r"D:\polix_xai_webapp")
ARCHIVE = Path(r"D:\ISROtrial\Polix_L2_full_archive")
PHASE = ROOT / "research_paper_ieee" / "guide_approved_final_run" / "04_SRI_LANKA_FIGURES"
OUT = PHASE / "figures"
GEN = PHASE / "figure_generation"

MATRIX_C = ARCHIVE / "final_project_outputs" / "02_feature_engineering" / "polix_matrix_v2_C_primary_plus_supporting.csv"
MODEL = ROOT / "model" / "polix_v2_matrixC_unsupervised_xai_model.pkl"
PREDICTIONS = ROOT / "research_paper_ieee" / "supplementary_experiments" / "deployed_model_reproduction.csv"
SEEDS = ROOT / "research_paper_ieee" / "supplementary_experiments" / "isolation_seed_stability_summary.csv"
TRUTH = ROOT / "research_paper_ieee" / "guide_approved_final_run" / "01_NEPAL_EVIDENCE" / "NEPAL_Part_03_All_25_Observation_Truth_Table.csv"
HARMONIC = ARCHIVE / "final_project_outputs" / "04_polarimetry_results" / "path2_all_observations_fractional_qu_vectors.csv"
KB_INDEX = ROOT / "research_paper_ieee" / "guide_approved_final_run" / "02_BHUTAN_KNOWLEDGE_BASE" / "BHUTAN_KB_INDEX.md"
KB_XAI = ROOT / "research_paper_ieee" / "guide_approved_final_run" / "02_BHUTAN_KNOWLEDGE_BASE" / "BHUTAN_KB_06_Local_XAI_Heuristic.md"
KB_HARMONIC = ROOT / "research_paper_ieee" / "guide_approved_final_run" / "02_BHUTAN_KNOWLEDGE_BASE" / "BHUTAN_KB_08_WeightedRoll_Harmonic_Fit.md"

BLUE = "#1f5a99"
ORANGE = "#c65a1e"
GRAY = "#b8bec5"
DARK = "#202428"
LIGHT_BLUE = "#e8f0f8"
LIGHT_ORANGE = "#faeee8"
LIGHT_GRAY = "#f2f3f4"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def configure_style() -> None:
    mpl.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 9,
            "axes.labelsize": 9,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "legend.fontsize": 8,
            "axes.linewidth": 0.8,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "savefig.bbox": None,
        }
    )


def save_pair(fig: plt.Figure, stem: str) -> tuple[Path, Path]:
    png = OUT / f"{stem}.png"
    pdf = OUT / f"{stem}.pdf"
    fig.savefig(png, dpi=300, facecolor="white")
    fig.savefig(pdf, facecolor="white")
    plt.close(fig)
    return png, pdf


def box(ax, xy, width, height, text, *, face=LIGHT_GRAY, edge=DARK, fontsize=8.2, lw=1.0):
    patch = FancyBboxPatch(
        xy,
        width,
        height,
        boxstyle="round,pad=0.02,rounding_size=0.02",
        linewidth=lw,
        edgecolor=edge,
        facecolor=face,
    )
    ax.add_patch(patch)
    ax.text(xy[0] + width / 2, xy[1] + height / 2, text, ha="center", va="center", fontsize=fontsize)
    return patch


def arrow(ax, start, end, *, color=DARK, style="-"):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=9,
            linewidth=1.0,
            linestyle=style,
            color=color,
            shrinkA=2,
            shrinkB=2,
        )
    )


def figure_1_framework() -> tuple[Path, Path]:
    fig, ax = plt.subplots(figsize=(7.16, 3.85))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Primary product-aware screening branch.
    box(ax, (0.02, 0.68), 0.17, 0.20, "Level-2 product families\nExposure · channel space\nsource azimuth · light curve\ndetector context", face=LIGHT_BLUE)
    box(ax, (0.24, 0.72), 0.14, 0.12, "Matrix C\n15 features", face=LIGHT_BLUE)
    box(ax, (0.43, 0.72), 0.13, 0.12, "StandardScaler", face=LIGHT_BLUE)
    arrow(ax, (0.19, 0.78), (0.24, 0.78))
    arrow(ax, (0.38, 0.78), (0.43, 0.78))

    box(ax, (0.63, 0.82), 0.11, 0.10, "PCA\ndescriptive", face=LIGHT_BLUE)
    box(ax, (0.63, 0.68), 0.11, 0.10, "KMeans\ndescriptive", face=LIGHT_BLUE)
    box(ax, (0.63, 0.54), 0.11, 0.10, "Isolation Forest\nfixed label", face=LIGHT_BLUE, lw=1.4)
    arrow(ax, (0.56, 0.78), (0.63, 0.87))
    arrow(ax, (0.56, 0.78), (0.63, 0.73))
    arrow(ax, (0.56, 0.78), (0.63, 0.59))

    box(ax, (0.80, 0.63), 0.18, 0.23, "Local feature ranking\nPCA contribution\nKMeans contribution\nIsolation Forest occlusion\nabsolute |z|\nProduct-family mapping", face=LIGHT_BLUE, fontsize=7.2)
    arrow(ax, (0.74, 0.87), (0.80, 0.81))
    arrow(ax, (0.74, 0.73), (0.80, 0.74))
    arrow(ax, (0.74, 0.59), (0.80, 0.68))
    ax.text(0.685, 0.485, "Only Isolation Forest sets\nthe Normal/candidate label", ha="center", va="top", fontsize=7.5)

    # Independent physical diagnostic branch.
    box(ax, (0.02, 0.16), 0.17, 0.16, "WeightedRoll\n360-bin delivered\ntotal-count-rate curve", face=LIGHT_ORANGE)
    box(ax, (0.27, 0.16), 0.19, 0.16, "Weighted second harmonic\nC + Q cos(2φ) + U sin(2φ)\nraw modulation · fitted phase", face=LIGHT_ORANGE)
    box(ax, (0.55, 0.16), 0.17, 0.16, "15 blank skies\n13-fit empirical reference\nχ²red ≤ 2", face=LIGHT_ORANGE)
    arrow(ax, (0.19, 0.24), (0.27, 0.24), color=ORANGE)
    arrow(ax, (0.46, 0.24), (0.55, 0.24), color=ORANGE)

    box(ax, (0.80, 0.16), 0.18, 0.16, "Researcher comparison\nML unusualness versus\nharmonic behaviour", face=LIGHT_GRAY)
    arrow(ax, (0.72, 0.24), (0.80, 0.24), color=ORANGE)
    arrow(ax, (0.89, 0.63), (0.89, 0.32), color=BLUE, style="--")
    ax.text(0.50, 0.04, "Independent branches; no confidence fusion and no calibrated polarization quantities", ha="center", va="center", fontsize=8, color=DARK)

    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    return save_pair(fig, "Fig1_corrected_framework")


def load_pca_plot_data() -> pd.DataFrame:
    matrix = pd.read_csv(MATRIX_C)
    truth = pd.read_csv(TRUTH)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        package = joblib.load(MODEL)

    features = list(package["feature_cols"])
    assert features == [c for c in matrix.columns if c != "observation_id"]
    assert set(matrix["observation_id"]) == set(package["training_observation_ids"])

    x = matrix[features].to_numpy(dtype=float)
    scaler = package["scaler"]
    pca = package["pca"]
    z = (x - np.asarray(scaler.mean_)) / np.asarray(scaler.scale_)
    coords = (z - np.asarray(pca.mean_)) @ np.asarray(pca.components_[:2]).T
    method_coords = np.asarray(pca.transform(z))[:, :2]
    assert np.allclose(coords, method_coords, atol=1e-12)

    result = matrix[["observation_id"]].copy()
    result["PC1"] = coords[:, 0]
    result["PC2"] = coords[:, 1]
    result = result.merge(
        truth[["observation_id", "proposal_id", "observation_role", "target_name", "fixed_prediction"]],
        on="observation_id",
        how="left",
        validate="one_to_one",
    )
    assert result[["PC1", "PC2"]].notna().all().all()
    result.to_csv(GEN / "phase4_pca_coordinates.csv", index=False)
    return result


def figure_2_pca(data: pd.DataFrame) -> tuple[Path, Path]:
    fig, ax = plt.subplots(figsize=(3.50, 3.30))
    groups = [
        ("source", "Source", "o", BLUE),
        ("blank_sky", "Blank sky", "s", ORANGE),
    ]
    for role, label, marker, color in groups:
        part = data[data["observation_role"] == role]
        ax.scatter(part["PC1"], part["PC2"], s=28, marker=marker, color=color, alpha=0.84, edgecolor="white", linewidth=0.45, label=label, zorder=2)

    candidates = data[data["fixed_prediction"] == "Anomaly"]
    ax.scatter(candidates["PC1"], candidates["PC2"], s=76, marker="D", facecolors="none", edgecolors=DARK, linewidth=1.15, label="Fixed candidate", zorder=3)

    offsets = {
        "C24_0018": (-5, 5, "right"),
        "G01_0006": (4, 8, "left"),
        "G01_0003": (4, 5, "left"),
        "C24_0010": (-5, 5, "right"),
    }
    labels = {"C24_0018": "Blank Sky-13", "G01_0006": "Sco X-1", "G01_0003": "Her X-1", "C24_0010": "Blank Sky-5"}
    for row in candidates.itertuples():
        dx, dy, align = offsets[row.proposal_id]
        ax.annotate(labels[row.proposal_id], (row.PC1, row.PC2), xytext=(dx, dy), textcoords="offset points", fontsize=7.2, ha=align, va="center")

    ax.axhline(0, color="#d8dadd", lw=0.6, zorder=0)
    ax.axvline(0, color="#d8dadd", lw=0.6, zorder=0)
    ax.set_xlim(float(data["PC1"].min()) - 0.4, float(data["PC1"].max()) + 1.7)
    ax.set_ylim(float(data["PC2"].min()) - 0.4, float(data["PC2"].max()) + 0.4)
    ax.set_xlabel("PC1 (38.74% variance)")
    ax.set_ylabel("PC2 (22.51% variance)")
    ax.legend(frameon=False, loc="best", handletextpad=0.4, borderaxespad=0.2)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(False)
    fig.subplots_adjust(left=0.18, right=0.97, bottom=0.16, top=0.98)
    return save_pair(fig, "Fig2_matrixC_PCA_space")


def load_ranking_data() -> pd.DataFrame:
    truth = pd.read_csv(TRUTH)
    seeds = pd.read_csv(SEEDS)[["observation_id", "times_flagged"]]
    data = truth[
        ["observation_id", "proposal_id", "observation_role", "target_name", "fixed_prediction", "fixed_anomaly_score"]
    ].merge(seeds, on="observation_id", how="left", validate="one_to_one")
    assert len(data) == 25 and data["times_flagged"].notna().all()
    data = data.sort_values("fixed_anomaly_score", ascending=True).reset_index(drop=True)
    data.to_csv(GEN / "phase4_ranking_plot_data.csv", index=False)
    return data


def figure_3_ranking(data: pd.DataFrame) -> tuple[Path, Path]:
    fig, ax = plt.subplots(figsize=(7.16, 6.15))
    colors = [BLUE if role == "source" else ORANGE for role in data["observation_role"]]
    bars = ax.barh(np.arange(len(data)), data["fixed_anomaly_score"], color=colors, alpha=0.82, edgecolor="white", linewidth=0.5)
    for bar, pred in zip(bars, data["fixed_prediction"]):
        if pred == "Anomaly":
            bar.set_edgecolor(DARK)
            bar.set_linewidth(1.25)
            bar.set_hatch("///")

    labels = [f"{row.target_name} ({row.proposal_id})" for row in data.itertuples()]
    ax.set_yticks(np.arange(len(data)), labels)
    ax.tick_params(axis="y", labelsize=7.6)
    ax.set_xlabel("Isolation Forest anomaly score (−score_samples)")
    xmax = float(data["fixed_anomaly_score"].max())
    ax.set_xlim(0.37, xmax + 0.115)
    for idx, row in data.iterrows():
        ax.text(row["fixed_anomaly_score"] + 0.004, idx, f"{int(row['times_flagged'])}/100", va="center", ha="left", fontsize=7.2, color=DARK)
    ax.text(xmax + 0.045, len(data) - 0.15, "seed selections", fontsize=7.2, ha="center", va="bottom", color=DARK)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.xaxis.grid(True, color="#e0e2e4", linewidth=0.6)
    ax.set_axisbelow(True)
    legend = [
        Patch(facecolor=BLUE, edgecolor="none", label="Source"),
        Patch(facecolor=ORANGE, edgecolor="none", label="Blank sky"),
        Patch(facecolor="white", edgecolor=DARK, hatch="///", label="Fixed candidate"),
    ]
    ax.legend(handles=legend, frameon=False, loc="lower right")
    fig.subplots_adjust(left=0.30, right=0.98, bottom=0.09, top=0.99)
    return save_pair(fig, "Fig3_fixed_score_ranking_seed_frequency")


def load_harmonic_plot_data() -> tuple[pd.DataFrame, tuple[float, float, float, float]]:
    physical = pd.read_csv(HARMONIC)
    predictions = pd.read_csv(PREDICTIONS)[["observation_id", "recomputed_prediction"]]
    data = physical[
        ["observation_id", "proposal_id", "observation_role", "target_name", "q_frac", "u_frac", "reduced_chi2", "fit_quality"]
    ].merge(predictions, on="observation_id", how="left", validate="one_to_one")
    data["reference_member"] = (data["observation_role"] == "blank_sky") & (data["reduced_chi2"] <= 2.0)
    data["fixed_candidate"] = data["recomputed_prediction"] == "Anomaly"
    reference = data[data["reference_member"]]
    assert len(data) == 25 and len(reference) == 13
    values = (
        float(reference["q_frac"].mean()),
        float(reference["q_frac"].std(ddof=1)),
        float(reference["u_frac"].mean()),
        float(reference["u_frac"].std(ddof=1)),
    )
    expected = (0.009092005, 0.004856906, -0.006478172, 0.004019024)
    assert np.allclose(values, expected, atol=5e-10)
    data.to_csv(GEN / "phase4_harmonic_plot_data.csv", index=False)
    return data, values


def figure_4_harmonic(data: pd.DataFrame, baseline: tuple[float, float, float, float]) -> tuple[Path, Path]:
    q_mean, q_sd, u_mean, u_sd = baseline
    fig, ax = plt.subplots(figsize=(7.16, 4.75))

    source = data[data["observation_role"] == "source"]
    reference = data[data["reference_member"]]
    excluded_blank = data[(data["observation_role"] == "blank_sky") & (~data["reference_member"])]
    ax.scatter(source["q_frac"], source["u_frac"], s=38, marker="o", color=BLUE, edgecolor="white", linewidth=0.5, alpha=0.88, label="Source", zorder=2)
    ax.scatter(reference["q_frac"], reference["u_frac"], s=38, marker="s", color=ORANGE, edgecolor="white", linewidth=0.5, alpha=0.88, label="Blank sky (13-fit reference)", zorder=2)
    ax.scatter(excluded_blank["q_frac"], excluded_blank["u_frac"], s=42, marker="s", facecolors="none", edgecolors=ORANGE, linewidth=1.1, label="Blank sky excluded by fit rule", zorder=2)

    candidates = data[data["fixed_candidate"]]
    ax.scatter(candidates["q_frac"], candidates["u_frac"], s=105, marker="D", facecolors="none", edgecolors=DARK, linewidth=1.2, label="Fixed ML candidate", zorder=3)

    ax.errorbar(q_mean, u_mean, xerr=q_sd, yerr=u_sd, fmt="+", color=DARK, capsize=3, elinewidth=0.9, markersize=8, label="13-fit mean ± sample SD (componentwise)", zorder=4)

    annotations = {
        "G01_0006": (6, 8, "Sco X-1"),
        "G01_0003": (-55, 7, "Her X-1"),
        "P01_0005": (6, -11, "Crab P01_0005"),
        "C24_0018": (6, 8, "Blank Sky-13"),
        "C24_0010": (6, -12, "Blank Sky-5"),
    }
    for row in data[data["proposal_id"].isin(annotations)].itertuples():
        dx, dy, label = annotations[row.proposal_id]
        ax.annotate(label, (row.q_frac, row.u_frac), xytext=(dx, dy), textcoords="offset points", fontsize=7.3, ha="left", va="center")

    ax.axhline(0, color="#d8dadd", lw=0.6, zorder=0)
    ax.axvline(0, color="#d8dadd", lw=0.6, zorder=0)
    ax.set_xlabel("Fractional cosine harmonic coordinate, q = Q/C")
    ax.set_ylabel("Fractional sine harmonic coordinate, u = U/C")
    ax.ticklabel_format(axis="both", style="plain")
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=2, columnspacing=1.0, handletextpad=0.5, fontsize=7.4)
    fig.subplots_adjust(left=0.12, right=0.99, bottom=0.31, top=0.98)
    return save_pair(fig, "Fig4_fractional_harmonic_diagnostic_space")


def write_manifest(outputs: dict[str, tuple[Path, Path]]) -> None:
    rows: list[dict[str, str]] = [
        {
            "figure_id": "ALL",
            "artifact_type": "GENERATOR",
            "evidence_class": "VISUALIZATION_CODE",
            "path": str(Path(__file__).resolve()),
            "sha256": sha256(Path(__file__).resolve()),
            "usage": "Visualization-only generation; no fitting or model training",
        }
    ]
    sources = {
        "Fig1": [
            (KB_INDEX, "APPROVED_KNOWLEDGE_BASE", "Architecture and branch separation"),
            (KB_XAI, "APPROVED_KNOWLEDGE_BASE", "Four-component local ranking"),
            (KB_HARMONIC, "APPROVED_KNOWLEDGE_BASE", "Independent harmonic branch"),
        ],
        "Fig2": [
            (MATRIX_C, "CONTROLLING_NUMERICAL_CSV", "Frozen 25×15 input"),
            (MODEL, "VERSIONED_MODEL_ARTIFACT", "Saved scaler and PCA parameters; transform only"),
            (TRUTH, "VERIFIED_JOIN", "Roles, labels and fixed candidate status"),
            (GEN / "phase4_pca_coordinates.csv", "PLOTTING_DERIVATIVE", "Saved PCA plotting coordinates"),
        ],
        "Fig3": [
            (PREDICTIONS, "CONTROLLING_REPRODUCTION_CSV", "Fixed scores and labels"),
            (SEEDS, "CONTROLLING_ROBUSTNESS_CSV", "100-seed selection frequency"),
            (TRUTH, "VERIFIED_JOIN", "Roles and target names"),
            (GEN / "phase4_ranking_plot_data.csv", "PLOTTING_DERIVATIVE", "Joined ranking data"),
        ],
        "Fig4": [
            (HARMONIC, "CONTROLLING_NUMERICAL_CSV", "Fractional harmonic coordinates and fit quality"),
            (PREDICTIONS, "CONTROLLING_REPRODUCTION_CSV", "Fixed candidate status"),
            (GEN / "phase4_harmonic_plot_data.csv", "PLOTTING_DERIVATIVE", "Joined plotting data and reference membership"),
        ],
    }
    for figure_id, entries in sources.items():
        for path, evidence_class, usage in entries:
            rows.append(
                {
                    "figure_id": figure_id,
                    "artifact_type": "SOURCE",
                    "evidence_class": evidence_class,
                    "path": str(path),
                    "sha256": sha256(path),
                    "usage": usage,
                }
            )
        for output in outputs[figure_id]:
            rows.append(
                {
                    "figure_id": figure_id,
                    "artifact_type": "OUTPUT",
                    "evidence_class": "PAPER_FIGURE",
                    "path": str(output),
                    "sha256": sha256(output),
                    "usage": "300-dpi PNG" if output.suffix.lower() == ".png" else "Vector PDF",
                }
            )

    manifest = PHASE / "SRI_LANKA_Part_01_Figure_Source_Manifest.csv"
    with manifest.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    GEN.mkdir(parents=True, exist_ok=True)
    configure_style()
    pca_data = load_pca_plot_data()
    ranking_data = load_ranking_data()
    harmonic_data, baseline = load_harmonic_plot_data()
    outputs = {
        "Fig1": figure_1_framework(),
        "Fig2": figure_2_pca(pca_data),
        "Fig3": figure_3_ranking(ranking_data),
        "Fig4": figure_4_harmonic(harmonic_data, baseline),
    }
    write_manifest(outputs)


if __name__ == "__main__":
    main()
