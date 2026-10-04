"""Generate manuscript figures from frozen POLIX project artifacts.

This script performs visualization only. It loads the saved scaler/PCA state
and calls transform; it does not alter features, estimators, thresholds, or
scientific result files.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import pandas as pd


PROJECT = Path(r"D:\polix_xai_webapp")
ARCHIVE = Path(r"D:\ISROtrial\Polix_L2_full_archive")
PAPER = PROJECT / "research_paper_ieee"
OUT_ROOT = PAPER / "final_content_candidate"
FIG_DIR = OUT_ROOT / "figures"

MATRIX_C = (
    ARCHIVE
    / "final_project_outputs"
    / "02_feature_engineering"
    / "polix_matrix_v2_C_primary_plus_supporting.csv"
)
MODEL = PROJECT / "model" / "polix_v2_matrixC_unsupervised_xai_model.pkl"
PREDICTIONS = PAPER / "supplementary_experiments" / "deployed_model_reproduction.csv"
SEED_SUMMARY = PAPER / "supplementary_experiments" / "isolation_seed_stability_summary.csv"
ROLES = ARCHIVE / "path2_observation_role_metadata_filled.csv"
FRACTIONAL = ARCHIVE / "path2_all_observations_fractional_qu_vectors.csv"
POLARIMETRY_CONFIG = PROJECT / "config" / "polarimetry_config.json"
MANIFEST = OUT_ROOT / "figure_generation" / "figure_source_manifest.csv"

FIXED_IDS = {
    "X01_PLX_C24_0018_000000",
    "X01_PLX_G01_0006_000000",
    "X01_PLX_G01_0003_000000",
    "X01_PLX_C24_0010_000000",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def readable_label(row: pd.Series) -> str:
    name = str(row.get("target_name", "")).strip()
    if name and name.lower() != "nan":
        return name
    return str(row["observation_id"]).replace("X01_PLX_", "").replace("_000000", "")


def save_figure(fig: plt.Figure, stem: str) -> None:
    fig.savefig(FIG_DIR / f"{stem}.png", dpi=300, bbox_inches="tight")
    fig.savefig(FIG_DIR / f"{stem}.svg", bbox_inches="tight")
    plt.close(fig)


def draw_framework() -> None:
    fig, ax = plt.subplots(figsize=(12.0, 5.3))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis("off")

    boxes = {
        "products": (0.35, 2.2, 2.2, 1.55, "Heterogeneous POLIX\nLevel-2 products"),
        "features": (3.05, 3.6, 2.25, 1.25, "Matrix C\n15 traceable features"),
        "ml": (5.85, 3.6, 2.25, 1.25, "Unsupervised screening\nScaler + PCA\nKMeans + Isolation Forest"),
        "xai": (8.65, 3.6, 2.8, 1.25, "Local feature ranking\nfour project-specific\ncomponents"),
        "wr": (3.05, 0.85, 2.25, 1.25, "WeightedRoll\nexcluded from Matrix C"),
        "harm": (5.85, 0.85, 2.25, 1.25, "Second-harmonic fit\nraw diagnostic"),
        "blank": (8.65, 0.85, 2.8, 1.25, "13-fit empirical\nblank-sky reference"),
    }
    colors = {
        "products": "#E8EEF7",
        "features": "#D9EAD3",
        "ml": "#D9EAD3",
        "xai": "#D9EAD3",
        "wr": "#FCE5CD",
        "harm": "#FCE5CD",
        "blank": "#FCE5CD",
    }
    for key, (x, y, width, height, text) in boxes.items():
        patch = FancyBboxPatch(
            (x, y),
            width,
            height,
            boxstyle="round,pad=0.04,rounding_size=0.08",
            linewidth=1.4,
            edgecolor="#263238",
            facecolor=colors[key],
        )
        ax.add_patch(patch)
        ax.text(x + width / 2, y + height / 2, text, ha="center", va="center", fontsize=8.4)

    def arrow(start: tuple[float, float], end: tuple[float, float]) -> None:
        ax.add_patch(
            FancyArrowPatch(
                start,
                end,
                arrowstyle="-|>",
                mutation_scale=13,
                linewidth=1.4,
                color="#455A64",
            )
        )

    arrow((2.55, 3.25), (3.05, 4.1))
    arrow((5.3, 4.22), (5.85, 4.22))
    arrow((8.1, 4.22), (8.65, 4.22))
    arrow((2.55, 2.7), (3.05, 1.5))
    arrow((5.3, 1.47), (5.85, 1.47))
    arrow((8.1, 1.47), (8.65, 1.47))
    ax.plot([2.78, 11.65], [3.0, 3.0], linestyle="--", color="#78909C", linewidth=1.1)
    ax.text(
        7.15,
        2.72,
        "scientifically separate diagnostic branches",
        ha="center",
        va="center",
        fontsize=9.5,
        color="#455A64",
    )
    ax.text(
        6,
        5.55,
        "Archive-relative screening and independent harmonic diagnostics",
        ha="center",
        va="center",
        fontsize=11,
        fontweight="bold",
    )
    save_figure(fig, "fig1_framework_flow")


def draw_pca() -> None:
    sys.path.insert(0, str(PROJECT))
    from model_service import PolixXAIPredictor

    matrix = pd.read_csv(MATRIX_C)
    roles = pd.read_csv(ROLES)
    predictor = PolixXAIPredictor(str(MODEL))
    scaled = predictor.scaler.transform(matrix[predictor.feature_cols])
    coords = predictor.pca.transform(scaled)
    frame = pd.DataFrame(
        {
            "observation_id": matrix["observation_id"],
            "PC1": coords[:, 0],
            "PC2": coords[:, 1],
        }
    ).merge(
        roles[["observation_id", "observation_role", "target_name"]],
        on="observation_id",
        how="left",
    )

    fig, ax = plt.subplots(figsize=(8.2, 5.8))
    style = {
        "source": ("#2468A2", "o", "Source"),
        "blank_sky": ("#8C8C8C", "s", "Blank sky"),
    }
    for role, (color, marker, label) in style.items():
        subset = frame[frame["observation_role"] == role]
        ax.scatter(
            subset["PC1"],
            subset["PC2"],
            s=46,
            marker=marker,
            color=color,
            alpha=0.82,
            label=label,
            zorder=2,
        )
    fixed = frame[frame["observation_id"].isin(FIXED_IDS)]
    ax.scatter(
        fixed["PC1"],
        fixed["PC2"],
        s=125,
        facecolors="none",
        edgecolors="#B71C1C",
        linewidths=1.8,
        label="Fixed candidate",
        zorder=4,
    )
    for _, row in fixed.iterrows():
        ax.annotate(
            readable_label(row),
            (row["PC1"], row["PC2"]),
            xytext=(5, 6),
            textcoords="offset points",
            fontsize=8.5,
        )
    evr = predictor.pca.explained_variance_ratio_
    ax.set_xlabel(f"PC1 ({100 * evr[0]:.1f}% variance)")
    ax.set_ylabel(f"PC2 ({100 * evr[1]:.1f}% variance)")
    ax.set_title("Matrix-C observation space (frozen PCA transform)")
    ax.axhline(0, color="#D0D0D0", linewidth=0.8)
    ax.axvline(0, color="#D0D0D0", linewidth=0.8)
    ax.grid(alpha=0.16)
    ax.legend(frameon=False, fontsize=9)
    save_figure(fig, "fig2_matrix_c_pca")


def draw_ranking() -> None:
    pred = pd.read_csv(PREDICTIONS)
    seeds = pd.read_csv(SEED_SUMMARY)
    roles = pd.read_csv(ROLES)
    frame = pred.merge(seeds[["observation_id", "times_flagged"]], on="observation_id")
    frame = frame.merge(
        roles[["observation_id", "target_name", "observation_role"]],
        on="observation_id",
        how="left",
    )
    frame = frame.sort_values("recomputed_anomaly_score", ascending=True).reset_index(drop=True)
    colors = ["#B71C1C" if value == "Anomaly" else "#A9B6C2" for value in frame["recomputed_prediction"]]
    fig, ax = plt.subplots(figsize=(9.0, 7.2))
    ax.barh(range(len(frame)), frame["recomputed_anomaly_score"], color=colors, height=0.72)
    labels = [
        str(obs).replace("X01_PLX_", "").replace("_000000", "")
        for obs in frame["observation_id"]
    ]
    ax.set_yticks(range(len(frame)))
    ax.set_yticklabels(labels, fontsize=7.6)
    ax.set_xlabel("Frozen Isolation Forest anomaly score (larger = more unusual)")
    ax.set_title("Archive-relative anomaly-score ranking and seed frequency")
    ax.grid(axis="x", alpha=0.18)
    for y, row in frame.iterrows():
        if row["observation_id"] in FIXED_IDS:
            text = f"{readable_label(row)}; {int(row['times_flagged'])}/100 seeds"
            ax.text(
                float(row["recomputed_anomaly_score"]) + 0.004,
                y,
                text,
                va="center",
                fontsize=8.1,
                color="#7F0000",
            )
    legend = [
        Line2D([0], [0], color="#B71C1C", lw=7, label="Fixed candidate"),
        Line2D([0], [0], color="#A9B6C2", lw=7, label="Fixed Normal"),
    ]
    ax.legend(handles=legend, loc="lower right", frameon=False, fontsize=9)
    ax.set_xlim(0, max(frame["recomputed_anomaly_score"]) + 0.13)
    save_figure(fig, "fig3_fixed_candidate_ranking")


def draw_fractional_space() -> None:
    frame = pd.read_csv(FRACTIONAL)
    with POLARIMETRY_CONFIG.open("r", encoding="utf-8") as handle:
        config = json.load(handle)
    baseline = config["blank_sky_vector_baseline"]

    fig, ax = plt.subplots(figsize=(8.0, 6.0))
    style = {
        "source": ("#2468A2", "o", "Source"),
        "blank_sky": ("#8C8C8C", "s", "Blank sky"),
    }
    for role, (color, marker, label) in style.items():
        subset = frame[frame["observation_role"] == role]
        ax.scatter(
            subset["q_frac"],
            subset["u_frac"],
            s=48,
            marker=marker,
            color=color,
            alpha=0.82,
            label=label,
            zorder=2,
        )
    fixed = frame[frame["observation_id"].isin(FIXED_IDS)]
    ax.scatter(
        fixed["q_frac"],
        fixed["u_frac"],
        s=130,
        facecolors="none",
        edgecolors="#B71C1C",
        linewidths=1.8,
        label="Fixed candidate",
        zorder=4,
    )
    ax.errorbar(
        baseline["q_fraction_mean"],
        baseline["u_fraction_mean"],
        xerr=baseline["q_fraction_std"],
        yerr=baseline["u_fraction_std"],
        fmt="X",
        markersize=9,
        color="#111111",
        ecolor="#111111",
        elinewidth=1.2,
        capsize=3,
        label="13-fit mean ± axis-wise sample SD",
        zorder=5,
    )
    labels = {
        "X01_PLX_G01_0006_000000",
        "X01_PLX_G01_0003_000000",
        "X01_PLX_P01_0005_000000",
        "X01_PLX_C24_0018_000000",
        "X01_PLX_C24_0010_000000",
    }
    for _, row in frame[frame["observation_id"].isin(labels)].iterrows():
        ax.annotate(
            readable_label(row),
            (row["q_frac"], row["u_frac"]),
            xytext=(5, 5),
            textcoords="offset points",
            fontsize=8.4,
        )
    ax.axhline(0, color="#D0D0D0", linewidth=0.8)
    ax.axvline(0, color="#D0D0D0", linewidth=0.8)
    ax.set_xlabel(r"Fractional cosine harmonic coordinate $q=Q/C$")
    ax.set_ylabel(r"Fractional sine harmonic coordinate $u=U/C$")
    ax.set_title("Archive-specific source and blank-sky harmonic diagnostic space")
    ax.grid(alpha=0.16)
    ax.legend(frameon=False, fontsize=8.7, loc="best")
    save_figure(fig, "fig4_fractional_harmonic_space")


def write_manifest() -> None:
    inputs = [
        MATRIX_C,
        MODEL,
        PREDICTIONS,
        SEED_SUMMARY,
        ROLES,
        FRACTIONAL,
        POLARIMETRY_CONFIG,
        Path(__file__),
    ]
    records = [
        {
            "artifact": str(path),
            "sha256": sha256(path),
            "role": "frozen input" if path != Path(__file__) else "figure-generation source",
        }
        for path in inputs
    ]
    pd.DataFrame(records).to_csv(MANIFEST, index=False)


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    draw_framework()
    draw_pca()
    draw_ranking()
    draw_fractional_space()
    write_manifest()
    print(f"Created figures in {FIG_DIR}")
    print(f"Created manifest {MANIFEST}")


if __name__ == "__main__":
    main()
