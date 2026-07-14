from pathlib import Path
import re

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def safe_filename(text):
    text = str(text)
    text = re.sub(r"[^A-Za-z0-9_\-]+", "_", text)
    return text[:120]


def create_result_visualizations(results, plot_dir, url_prefix):
    plot_dir = Path(plot_dir)
    plot_dir.mkdir(parents=True, exist_ok=True)

    summary_plots = {}
    result_plot_map = {}

    # ---------------------------------------------------------
    # 1. Batch anomaly score ranking plot
    # ---------------------------------------------------------
    sorted_results = sorted(results, key=lambda r: r["anomaly_score"])

    labels = [r["observation_id"] for r in sorted_results]
    scores = [r["anomaly_score"] for r in sorted_results]

    plt.figure(figsize=(11, max(6, len(results) * 0.35)))
    plt.barh(labels, scores)
    plt.xlabel("Isolation Forest anomaly score")
    plt.ylabel("Observation ID")
    plt.title("Anomaly Score Ranking")
    plt.tight_layout()

    anomaly_plot_path = plot_dir / "anomaly_score_ranking.png"
    plt.savefig(anomaly_plot_path, dpi=180)
    plt.close()

    summary_plots["anomaly_score_ranking"] = f"{url_prefix}/anomaly_score_ranking.png"

    # ---------------------------------------------------------
    # 2. PCA scatter plot
    # ---------------------------------------------------------
    pc1 = [r["pca_pc1"] for r in results]
    pc2 = [r["pca_pc2"] for r in results]

    plt.figure(figsize=(9, 7))

    for r in results:
        marker = "x" if r["prediction"] == "Anomaly" else "o"
        plt.scatter(r["pca_pc1"], r["pca_pc2"], marker=marker)

        short_label = (
            r["observation_id"]
            .replace("X01_PLX_", "")
            .replace("_000000", "")
        )

        if r["prediction"] == "Anomaly":
            plt.text(r["pca_pc1"], r["pca_pc2"], short_label, fontsize=8)

    plt.axhline(0, linewidth=0.8)
    plt.axvline(0, linewidth=0.8)
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.title("PCA Observation Space")
    plt.tight_layout()

    pca_plot_path = plot_dir / "pca_observation_space.png"
    plt.savefig(pca_plot_path, dpi=180)
    plt.close()

    summary_plots["pca_observation_space"] = f"{url_prefix}/pca_observation_space.png"

    # ---------------------------------------------------------
    # 3. Per-observation XAI plots
    # ---------------------------------------------------------
    for r in results:
        obs_id = r["observation_id"]
        obs_safe = safe_filename(obs_id)

        xai = r["top_xai_features"]

        features = [x["feature"] for x in xai]
        readable_features = [x.get("feature_readable", x["feature"]) for x in xai]

        xai_scores = [x["xai_score"] for x in xai]
        z_scores = [abs(x["z_score"]) for x in xai]
        pca_contrib = [x["pca_contribution"] for x in xai]
        kmeans_contrib = [x["kmeans_contribution"] for x in xai]
        isolation_contrib = [max(x["isolation_contribution"], 0) for x in xai]

        # XAI score bar chart
        plt.figure(figsize=(9, 5))
        plt.barh(readable_features[::-1], xai_scores[::-1])
        plt.xlabel("Combined XAI score")
        plt.ylabel("Feature")
        plt.title(f"Top XAI Features - {obs_id}")
        plt.tight_layout()

        xai_bar_path = plot_dir / f"{obs_safe}_xai_score_bar.png"
        plt.savefig(xai_bar_path, dpi=180)
        plt.close()

        # XAI component chart
        x = np.arange(len(readable_features))
        width = 0.22

        plt.figure(figsize=(11, 5))
        plt.bar(x - width, pca_contrib, width, label="PCA")
        plt.bar(x, kmeans_contrib, width, label="KMeans")
        plt.bar(x + width, isolation_contrib, width, label="Isolation")

        plt.xticks(x, readable_features, rotation=30, ha="right")
        plt.ylabel("Contribution value")
        plt.title(f"XAI Contribution Components - {obs_id}")
        plt.legend()
        plt.tight_layout()

        component_path = plot_dir / f"{obs_safe}_xai_components.png"
        plt.savefig(component_path, dpi=180)
        plt.close()

        result_plot_map[obs_id] = {
            "xai_bar_url": f"{url_prefix}/{xai_bar_path.name}",
            "xai_component_url": f"{url_prefix}/{component_path.name}",
        }

    return summary_plots, result_plot_map