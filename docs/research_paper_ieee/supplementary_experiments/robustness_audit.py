"""Publication-focused robustness audit for the POLIX project archive.

This script is intentionally read-only with respect to the completed project.
Every generated artifact is written beside this script.
"""

from __future__ import annotations

import hashlib
import importlib.metadata
import json
import platform
import sys
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import scipy
import sklearn
from scipy.stats import spearmanr
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.ensemble import IsolationForest
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


ARCHIVE = Path(r"D:\ISROtrial\Polix_L2_full_archive")
FINAL = ARCHIVE / "final_project_outputs"
WEBAPP = Path(r"D:\polix_xai_webapp")
OUTPUT = Path(__file__).resolve().parent

MATRIX_FILES = {
    "A": FINAL
    / "02_feature_engineering"
    / "polix_matrix_v2_A_primary_final_chain.csv",
    "B": FINAL
    / "02_feature_engineering"
    / "polix_matrix_v2_B_primary_plus_source_diag.csv",
    "C": FINAL
    / "02_feature_engineering"
    / "polix_matrix_v2_C_primary_plus_supporting.csv",
    "WR": FINAL
    / "02_feature_engineering"
    / "polix_matrix_v2_WR_weightedroll_diagnostic.csv",
}

MODEL_FILE = (
    FINAL
    / "03_ml_xai_results"
    / "polix_v2_matrixC_unsupervised_xai_model.pkl"
)

ORIGINAL_FAITHFULNESS_TEST = (
    FINAL
    / "03_ml_xai_results"
    / "v2_unsupervised_xai_faithfulness_test.csv"
)
ORIGINAL_FAITHFULNESS_VERDICT = (
    FINAL
    / "03_ml_xai_results"
    / "v2_unsupervised_xai_faithfulness_verdict.csv"
)
TOP_XAI_FILE = ARCHIVE / "v2_unsupervised_xai_top_feature_contributions.csv"
FINAL_PRIMARY_XAI = (
    FINAL
    / "03_ml_xai_results"
    / "v2_final_primary_unsupervised_xai_explanations.csv"
)

RANDOM_SEEDS = list(range(100))
CONTAMINATION_VALUES = [0.12, 0.16, 0.20, 0.24]
DEPLOYED_CONTAMINATION = 0.16
DEPLOYED_SEED = 42
MATRIX_K = {"A": 4, "B": 3, "C": 5, "WR": 3}


def save_csv(frame: pd.DataFrame, name: str) -> None:
    frame.to_csv(OUTPUT / name, index=False, encoding="utf-8")


def load_matrix(name: str) -> tuple[pd.DataFrame, list[str], np.ndarray]:
    frame = pd.read_csv(MATRIX_FILES[name])
    features = [column for column in frame.columns if column != "observation_id"]
    values = frame[features].to_numpy(dtype=float)
    return frame, features, values


def rank_descending(values: np.ndarray) -> np.ndarray:
    return pd.Series(values).rank(method="average", ascending=False).to_numpy()


def safe_spearman(a: np.ndarray, b: np.ndarray) -> tuple[float, float]:
    result = spearmanr(a, b)
    return float(result.statistic), float(result.pvalue)


def normalize_component(values: np.ndarray) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    maximum = np.nanmax(np.abs(values))
    if not np.isfinite(maximum) or maximum == 0:
        return np.zeros_like(values)
    return np.abs(values) / maximum


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def deployed_model_reproduction() -> tuple[dict, pd.DataFrame]:
    package = joblib.load(MODEL_FILE)
    frame, features, values = load_matrix("C")
    if features != package["feature_cols"]:
        raise RuntimeError("Matrix-C columns do not match the deployed model.")

    scaled = package["scaler"].transform(values)
    scores = -package["isolation_forest"].score_samples(scaled)
    predictions = package["isolation_forest"].predict(scaled)
    stored_scores = np.asarray(package["training_isolation_scores"])
    stored_predictions = np.asarray(package["training_isolation_predictions"])

    output = pd.DataFrame(
        {
            "observation_id": frame["observation_id"],
            "recomputed_anomaly_score": scores,
            "stored_anomaly_score": stored_scores,
            "absolute_score_difference": np.abs(scores - stored_scores),
            "recomputed_prediction": np.where(
                predictions == -1, "Anomaly", "Normal"
            ),
            "stored_prediction": np.where(
                stored_predictions == -1, "Anomaly", "Normal"
            ),
            "prediction_match": predictions == stored_predictions,
        }
    ).sort_values("recomputed_anomaly_score", ascending=False)
    save_csv(output, "deployed_model_reproduction.csv")
    return package, output


def deployed_xai_reproduction(package: dict) -> None:
    frame, features, values = load_matrix("C")
    scaled = package["scaler"].transform(values)
    predictions = package["isolation_forest"].predict(scaled)
    rows: list[dict] = []

    for index, vector in enumerate(scaled):
        pca_contribution = (
            np.abs(vector * package["pca"].components_[0])
            * package["pca"].explained_variance_ratio_[0]
            + np.abs(vector * package["pca"].components_[1])
            * package["pca"].explained_variance_ratio_[1]
        )
        cluster = package["kmeans"].predict(vector.reshape(1, -1))[0]
        centroid = package["kmeans"].cluster_centers_[cluster]
        kmeans_contribution = np.square(vector - centroid)
        base_score = float(
            -package["isolation_forest"].score_samples(
                vector.reshape(1, -1)
            )[0]
        )
        isolation_delta = np.zeros(len(features))
        for feature_index in range(len(features)):
            neutralized = vector.copy()
            neutralized[feature_index] = 0.0
            neutralized_score = float(
                -package["isolation_forest"].score_samples(
                    neutralized.reshape(1, -1)
                )[0]
            )
            isolation_delta[feature_index] = base_score - neutralized_score

        absolute_z = np.abs(vector)
        combined = (
            normalize_component(pca_contribution)
            + normalize_component(kmeans_contribution)
            + normalize_component(np.maximum(isolation_delta, 0))
            + normalize_component(absolute_z)
        )
        order = np.argsort(-combined)
        for rank, feature_index in enumerate(order[:5], start=1):
            rows.append(
                {
                    "observation_id": frame.iloc[index]["observation_id"],
                    "prediction": (
                        "Anomaly" if predictions[index] == -1 else "Normal"
                    ),
                    "rank": rank,
                    "feature": features[feature_index],
                    "combined_xai_score": combined[feature_index],
                    "z_score": vector[feature_index],
                    "pca_contribution": pca_contribution[feature_index],
                    "kmeans_contribution": kmeans_contribution[feature_index],
                    "isolation_contribution": isolation_delta[feature_index],
                }
            )
    save_csv(pd.DataFrame(rows), "deployed_xai_reproduction.csv")


def seed_stability(frame: pd.DataFrame, values: np.ndarray) -> None:
    scaled = StandardScaler().fit_transform(values)
    rows: list[dict] = []
    for seed in RANDOM_SEEDS:
        model = IsolationForest(
            n_estimators=100,
            contamination=DEPLOYED_CONTAMINATION,
            random_state=seed,
        )
        predictions = model.fit_predict(scaled)
        scores = -model.score_samples(scaled)
        ranks = rank_descending(scores)
        for observation_id, score, rank, prediction in zip(
            frame["observation_id"], scores, ranks, predictions
        ):
            rows.append(
                {
                    "seed": seed,
                    "observation_id": observation_id,
                    "anomaly_score": score,
                    "anomaly_rank": rank,
                    "flagged": prediction == -1,
                }
            )

    results = pd.DataFrame(rows)
    summary = (
        results.groupby("observation_id", as_index=False)
        .agg(
            seeds_evaluated=("seed", "nunique"),
            times_flagged=("flagged", "sum"),
            flag_frequency=("flagged", "mean"),
            mean_anomaly_score=("anomaly_score", "mean"),
            std_anomaly_score=("anomaly_score", "std"),
            mean_rank=("anomaly_rank", "mean"),
            min_rank=("anomaly_rank", "min"),
            max_rank=("anomaly_rank", "max"),
        )
        .sort_values(["flag_frequency", "mean_anomaly_score"], ascending=False)
    )
    save_csv(results, "isolation_seed_stability.csv")
    save_csv(summary, "isolation_seed_stability_summary.csv")


def contamination_sensitivity(frame: pd.DataFrame, values: np.ndarray) -> None:
    scaled = StandardScaler().fit_transform(values)
    rows: list[dict] = []
    for contamination in CONTAMINATION_VALUES:
        model = IsolationForest(
            n_estimators=100,
            contamination=contamination,
            random_state=DEPLOYED_SEED,
        )
        predictions = model.fit_predict(scaled)
        scores = -model.score_samples(scaled)
        ranks = rank_descending(scores)
        for observation_id, score, rank, prediction in zip(
            frame["observation_id"], scores, ranks, predictions
        ):
            rows.append(
                {
                    "contamination": contamination,
                    "expected_fraction_of_25": contamination * len(frame),
                    "observation_id": observation_id,
                    "anomaly_score": score,
                    "anomaly_rank": rank,
                    "flagged": prediction == -1,
                }
            )

    results = pd.DataFrame(rows)
    summary = (
        results.groupby("observation_id", as_index=False)
        .agg(
            settings_evaluated=("contamination", "nunique"),
            settings_flagged=("flagged", "sum"),
            flag_frequency=("flagged", "mean"),
            best_rank=("anomaly_rank", "min"),
            worst_rank=("anomaly_rank", "max"),
        )
        .sort_values(["flag_frequency", "best_rank"], ascending=[False, True])
    )
    save_csv(results, "contamination_sensitivity.csv")
    save_csv(summary, "contamination_candidate_stability.csv")


def jackknife_stability(
    frame: pd.DataFrame, values: np.ndarray, deployed_package: dict
) -> None:
    observation_ids = frame["observation_id"].to_numpy()
    full_scaled = deployed_package["scaler"].transform(values)
    full_scores = -deployed_package["isolation_forest"].score_samples(full_scaled)
    full_score_by_id = dict(zip(observation_ids, full_scores))

    run_rows: list[dict] = []
    observation_rows: list[dict] = []
    for omitted_index, omitted_id in enumerate(observation_ids):
        keep = np.arange(len(frame)) != omitted_index
        train_ids = observation_ids[keep]
        train_values = values[keep]

        scaler = StandardScaler()
        train_scaled = scaler.fit_transform(train_values)
        model = IsolationForest(
            n_estimators=100,
            contamination=DEPLOYED_CONTAMINATION,
            random_state=DEPLOYED_SEED,
        )
        train_predictions = model.fit_predict(train_scaled)
        train_scores = -model.score_samples(train_scaled)
        baseline_common = np.array([full_score_by_id[item] for item in train_ids])
        rho, pvalue = safe_spearman(baseline_common, train_scores)

        all_scaled = scaler.transform(values)
        all_scores = -model.score_samples(all_scaled)
        all_predictions = model.predict(all_scaled)
        all_ranks = rank_descending(all_scores)

        run_rows.append(
            {
                "omitted_observation_id": omitted_id,
                "n_training_observations": int(keep.sum()),
                "training_anomalies": int((train_predictions == -1).sum()),
                "spearman_rho_vs_full_on_common_observations": rho,
                "spearman_pvalue": pvalue,
                "held_out_anomaly_score": all_scores[omitted_index],
                "held_out_rank_among_25": all_ranks[omitted_index],
                "held_out_flagged_by_refit_model": all_predictions[omitted_index]
                == -1,
            }
        )

        for index, observation_id in enumerate(observation_ids):
            observation_rows.append(
                {
                    "omitted_observation_id": omitted_id,
                    "observation_id": observation_id,
                    "was_in_training_set": bool(keep[index]),
                    "anomaly_score": all_scores[index],
                    "anomaly_rank_among_25": all_ranks[index],
                    "flagged": all_predictions[index] == -1,
                }
            )

    runs = pd.DataFrame(run_rows)
    long_results = pd.DataFrame(observation_rows)
    included = long_results[long_results["was_in_training_set"]]
    included_summary = (
        included.groupby("observation_id", as_index=False)
        .agg(
            included_runs=("omitted_observation_id", "nunique"),
            times_flagged_when_in_training=("flagged", "sum"),
            flag_frequency_when_in_training=("flagged", "mean"),
            mean_rank_when_in_training=("anomaly_rank_among_25", "mean"),
            min_rank_when_in_training=("anomaly_rank_among_25", "min"),
            max_rank_when_in_training=("anomaly_rank_among_25", "max"),
        )
        .sort_values(
            ["flag_frequency_when_in_training", "mean_rank_when_in_training"],
            ascending=[False, True],
        )
    )
    held_out = long_results[~long_results["was_in_training_set"]][
        [
            "observation_id",
            "anomaly_score",
            "anomaly_rank_among_25",
            "flagged",
        ]
    ].rename(
        columns={
            "anomaly_score": "held_out_anomaly_score",
            "anomaly_rank_among_25": "held_out_rank_among_25",
            "flagged": "held_out_flagged",
        }
    )
    summary = included_summary.merge(held_out, on="observation_id", how="left")
    save_csv(runs, "jackknife_run_summary.csv")
    save_csv(long_results, "jackknife_all_scores.csv")
    save_csv(summary, "jackknife_observation_stability.csv")


def matrix_ablation() -> None:
    rows: list[dict] = []
    summaries: list[dict] = []
    flag_sets: dict[str, set[str]] = {}
    score_maps: dict[str, dict[str, float]] = {}

    for name in ["A", "B", "C", "WR"]:
        frame, features, values = load_matrix(name)
        scaled = StandardScaler().fit_transform(values)
        pca = PCA(n_components=2, random_state=DEPLOYED_SEED)
        coordinates = pca.fit_transform(scaled)
        kmeans = KMeans(
            n_clusters=MATRIX_K[name],
            random_state=DEPLOYED_SEED,
            n_init=20,
        )
        labels = kmeans.fit_predict(scaled)
        silhouette = silhouette_score(scaled, labels)
        centroid_distances = np.linalg.norm(
            scaled - kmeans.cluster_centers_[labels], axis=1
        )
        model = IsolationForest(
            n_estimators=100,
            contamination=DEPLOYED_CONTAMINATION,
            random_state=DEPLOYED_SEED,
        )
        predictions = model.fit_predict(scaled)
        scores = -model.score_samples(scaled)
        pca_distances = np.linalg.norm(coordinates, axis=1)
        score_maps[name] = dict(zip(frame["observation_id"], scores))
        flag_sets[name] = set(frame.loc[predictions == -1, "observation_id"])

        for observation_id, score, prediction, pca_distance, kmeans_distance in zip(
            frame["observation_id"],
            scores,
            predictions,
            pca_distances,
            centroid_distances,
        ):
            rows.append(
                {
                    "matrix": name,
                    "branch_role": (
                        "independent_weightedroll_diagnostic"
                        if name == "WR"
                        else "primary_feature_tier_ablation"
                    ),
                    "observation_id": observation_id,
                    "isolation_anomaly_score": score,
                    "isolation_rank": np.nan,
                    "isolation_flagged": prediction == -1,
                    "pca_distance": pca_distance,
                    "kmeans_centroid_distance": kmeans_distance,
                }
            )

        summaries.append(
            {
                "matrix": name,
                "branch_role": (
                    "independent_weightedroll_diagnostic"
                    if name == "WR"
                    else "primary_feature_tier_ablation"
                ),
                "n_observations": len(frame),
                "n_features": len(features),
                "missing_values": int(np.isnan(values).sum()),
                "pc1_variance": pca.explained_variance_ratio_[0],
                "pc2_variance": pca.explained_variance_ratio_[1],
                "pc1_pc2_variance": pca.explained_variance_ratio_[:2].sum(),
                "kmeans_k": MATRIX_K[name],
                "kmeans_silhouette": silhouette,
                "isolation_anomaly_count": int((predictions == -1).sum()),
                "isolation_anomaly_ids": " | ".join(sorted(flag_sets[name])),
            }
        )

    results = pd.DataFrame(rows)
    results["isolation_rank"] = results.groupby("matrix")[
        "isolation_anomaly_score"
    ].rank(method="average", ascending=False)
    save_csv(results, "matrix_ablation_results.csv")
    save_csv(pd.DataFrame(summaries), "matrix_ablation_summary.csv")

    pair_rows: list[dict] = []
    matrix_names = ["A", "B", "C"]
    for index, left in enumerate(matrix_names):
        for right in matrix_names[index + 1 :]:
            union = flag_sets[left] | flag_sets[right]
            intersection = flag_sets[left] & flag_sets[right]
            common_ids = sorted(set(score_maps[left]) & set(score_maps[right]))
            rho, pvalue = safe_spearman(
                np.array([score_maps[left][item] for item in common_ids]),
                np.array([score_maps[right][item] for item in common_ids]),
            )
            pair_rows.append(
                {
                    "matrix_left": left,
                    "matrix_right": right,
                    "flag_intersection_count": len(intersection),
                    "flag_union_count": len(union),
                    "flag_jaccard": len(intersection) / len(union),
                    "score_spearman_rho": rho,
                    "score_spearman_pvalue": pvalue,
                    "shared_flagged_observation_ids": " | ".join(
                        sorted(intersection)
                    ),
                }
            )
    save_csv(pd.DataFrame(pair_rows), "matrix_flag_and_rank_agreement.csv")


def ranking_agreement(package: dict) -> None:
    frame, _, values = load_matrix("C")
    scaled = package["scaler"].transform(values)
    coordinates = package["pca"].transform(scaled)
    labels = package["kmeans"].predict(scaled)
    pca_distance = np.linalg.norm(coordinates, axis=1)
    kmeans_distance = np.linalg.norm(
        scaled - package["kmeans"].cluster_centers_[labels], axis=1
    )
    isolation_score = -package["isolation_forest"].score_samples(scaled)

    metrics = pd.DataFrame(
        {
            "observation_id": frame["observation_id"],
            "pca_distance": pca_distance,
            "pca_rank": rank_descending(pca_distance),
            "kmeans_centroid_distance": kmeans_distance,
            "kmeans_rank": rank_descending(kmeans_distance),
            "isolation_anomaly_score": isolation_score,
            "isolation_rank": rank_descending(isolation_score),
        }
    ).sort_values("isolation_rank")
    save_csv(metrics, "ranking_metrics.csv")

    arrays = {
        "PCA distance": pca_distance,
        "KMeans centroid distance": kmeans_distance,
        "Isolation Forest anomaly score": isolation_score,
    }
    rows: list[dict] = []
    names = list(arrays)
    for index, left in enumerate(names):
        for right in names[index + 1 :]:
            rho, pvalue = safe_spearman(arrays[left], arrays[right])
            rows.append(
                {
                    "metric_left": left,
                    "metric_right": right,
                    "spearman_rho": rho,
                    "two_sided_pvalue": pvalue,
                    "n_observations": len(frame),
                }
            )
    save_csv(pd.DataFrame(rows), "ranking_agreement.csv")


def reproduce_faithfulness(package: dict) -> None:
    frame, features, values = load_matrix("C")
    observation_ids = frame["observation_id"].to_numpy()
    scaled = package["scaler"].transform(values)
    coordinates = package["pca"].transform(scaled)
    labels = package["kmeans"].predict(scaled)
    centroids = package["kmeans"].cluster_centers_

    candidates = pd.read_csv(FINAL_PRIMARY_XAI)["observation_id"].tolist()
    xai = pd.read_csv(TOP_XAI_FILE)
    xai = xai[xai["matrix"] == "C_primary_plus_supporting"]

    rows: list[dict] = []
    for observation_id in candidates:
        index = int(np.where(observation_ids == observation_id)[0][0])
        vector = scaled[index].copy()
        top_features = (
            xai[xai["observation_id"] == observation_id]
            .sort_values("combined_xai_score", ascending=False)
            .head(3)["feature"]
            .tolist()
        )
        top_indices = [features.index(feature) for feature in top_features]

        original_pca_distance = float(np.linalg.norm(coordinates[index]))
        original_cluster = labels[index]
        original_kmeans_distance = float(
            np.linalg.norm(vector - centroids[original_cluster])
        )
        original_isolation_score = float(
            -package["isolation_forest"].score_samples(vector.reshape(1, -1))[0]
        )

        neutralized = vector.copy()
        neutralized[top_indices] = 0.0
        new_pca_distance = float(
            np.linalg.norm(
                package["pca"].transform(neutralized.reshape(1, -1))[0]
            )
        )
        new_kmeans_distance = float(
            np.linalg.norm(neutralized - centroids[original_cluster])
        )
        new_isolation_score = float(
            -package["isolation_forest"].score_samples(
                neutralized.reshape(1, -1)
            )[0]
        )
        rows.append(
            {
                "observation_id": observation_id,
                "neutralized_top_xai_features": " | ".join(top_features),
                "original_pca_distance": original_pca_distance,
                "new_pca_distance": new_pca_distance,
                "pca_distance_reduction": original_pca_distance
                - new_pca_distance,
                "original_kmeans_distance": original_kmeans_distance,
                "new_kmeans_distance": new_kmeans_distance,
                "kmeans_distance_reduction": original_kmeans_distance
                - new_kmeans_distance,
                "original_isolation_score": original_isolation_score,
                "new_isolation_score": new_isolation_score,
                "isolation_score_reduction": original_isolation_score
                - new_isolation_score,
            }
        )

    reproduced = pd.DataFrame(rows)
    original = pd.read_csv(ORIGINAL_FAITHFULNESS_TEST)
    numeric_columns = [
        column
        for column in reproduced.columns
        if column not in {"observation_id", "neutralized_top_xai_features"}
    ]
    comparison = reproduced.merge(
        original,
        on=["observation_id", "neutralized_top_xai_features"],
        suffixes=("_reproduced", "_original"),
        validate="one_to_one",
    )
    for column in numeric_columns:
        comparison[f"{column}_absolute_difference"] = np.abs(
            comparison[f"{column}_reproduced"]
            - comparison[f"{column}_original"]
        )
    save_csv(comparison, "faithfulness_reproduction.csv")

    verdict = reproduced.copy()
    verdict["pca_pass"] = verdict["pca_distance_reduction"] > 0
    verdict["isolation_pass"] = verdict["isolation_score_reduction"] > 0
    verdict["kmeans_pass"] = verdict["kmeans_distance_reduction"] > 0
    verdict["overall_xai_faithfulness"] = verdict.apply(
        lambda row: (
            "Strong"
            if row["pca_pass"] and row["isolation_pass"]
            else (
                "Moderate"
                if row["pca_pass"] or row["isolation_pass"]
                else "Weak"
            )
        ),
        axis=1,
    )
    original_verdict = pd.read_csv(ORIGINAL_FAITHFULNESS_VERDICT)[
        ["observation_id", "overall_xai_faithfulness"]
    ].rename(
        columns={
            "overall_xai_faithfulness": "original_overall_xai_faithfulness"
        }
    )
    verdict = verdict.merge(original_verdict, on="observation_id", how="left")
    verdict["verdict_match"] = (
        verdict["overall_xai_faithfulness"]
        == verdict["original_overall_xai_faithfulness"]
    )
    save_csv(verdict, "faithfulness_verdict_reproduction.csv")


def evidence_hashes() -> None:
    paths = [
        *MATRIX_FILES.values(),
        MODEL_FILE,
        ORIGINAL_FAITHFULNESS_TEST,
        ORIGINAL_FAITHFULNESS_VERDICT,
        TOP_XAI_FILE,
        FINAL_PRIMARY_XAI,
        FINAL
        / "03_ml_xai_results"
        / "v2_consensus_anomaly_table.csv",
        FINAL
        / "03_ml_xai_results"
        / "v2_matrix_analysis_summary.csv",
        FINAL
        / "04_polarimetry_results"
        / "polix_weightedroll_raw_modulation_fits.csv",
        FINAL
        / "04_polarimetry_results"
        / "path2_blank_sky_modulation_baseline.csv",
        FINAL
        / "04_polarimetry_results"
        / "path2_all_observations_fractional_qu_vectors.csv",
        FINAL
        / "04_polarimetry_results"
        / "path2_source_vs_blank_sky_modulation_comparison.csv",
        FINAL
        / "04_polarimetry_results"
        / "path2_final_polarization_xai_result_table_with_roles.csv",
        FINAL
        / "07_documentation"
        / "POLIX_XAI_Final_Report_Reviewed.md",
        Path(r"C:\Users\Saatvik\Downloads\POLIX_User_Handbook.pdf"),
        WEBAPP / "PS1_Review1_Introduction_Literature_Survey.md",
        WEBAPP / "PS1_Review1_Literature_Comparison_Table.md",
        WEBAPP / "PS1_Review1_Citation_Audit.md",
        WEBAPP / "app.py",
        WEBAPP / "feature_extractor.py",
        WEBAPP / "model_service.py",
        WEBAPP / "polarization_service.py",
        WEBAPP / "result_exporter.py",
        WEBAPP / "visualization_service.py",
        WEBAPP / "config" / "observation_metadata.json",
        WEBAPP / "config" / "polarimetry_config.json",
        WEBAPP / "requirements.txt",
        *sorted((FINAL / "01_notebooks").glob("*.ipynb")),
    ]
    rows = []
    for path in paths:
        rows.append(
            {
                "path": str(path),
                "exists": path.exists(),
                "size_bytes": path.stat().st_size if path.exists() else np.nan,
                "last_modified_local": (
                    pd.Timestamp(path.stat().st_mtime, unit="s").isoformat()
                    if path.exists()
                    else ""
                ),
                "sha256": sha256_file(path) if path.exists() else "",
            }
        )
    save_csv(pd.DataFrame(rows), "evidence_file_hashes.csv")


def software_versions() -> None:
    packages = [
        "astropy",
        "Flask",
        "joblib",
        "matplotlib",
        "numpy",
        "pandas",
        "scikit-learn",
        "scipy",
    ]
    rows = [
        {"component": "Python", "version": platform.python_version()},
        {"component": "platform", "version": platform.platform()},
    ]
    for package in packages:
        try:
            version = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            version = "NOT INSTALLED"
        rows.append({"component": package, "version": version})
    save_csv(pd.DataFrame(rows), "software_versions.csv")


def write_machine_summary(
    package: dict, reproduction: pd.DataFrame, matrix_c: pd.DataFrame
) -> None:
    seed_summary = pd.read_csv(OUTPUT / "isolation_seed_stability_summary.csv")
    jackknife_runs = pd.read_csv(OUTPUT / "jackknife_run_summary.csv")
    faithfulness = pd.read_csv(
        OUTPUT / "faithfulness_verdict_reproduction.csv"
    )
    summary = {
        "data_freeze_date": "2026-07-27",
        "matrix_c_observations": int(len(matrix_c)),
        "matrix_c_features": int(len(package["feature_cols"])),
        "matrix_c_missing_values": int(
            matrix_c[package["feature_cols"]].isna().sum().sum()
        ),
        "deployed_model_anomaly_count": int(
            (reproduction["recomputed_prediction"] == "Anomaly").sum()
        ),
        "deployed_model_normal_count": int(
            (reproduction["recomputed_prediction"] == "Normal").sum()
        ),
        "deployed_model_predictions_exactly_reproduced": bool(
            reproduction["prediction_match"].all()
        ),
        "max_deployed_score_reproduction_difference": float(
            reproduction["absolute_score_difference"].max()
        ),
        "seed_count": len(RANDOM_SEEDS),
        "seed_always_flagged_observations": seed_summary.loc[
            seed_summary["flag_frequency"] == 1.0, "observation_id"
        ].tolist(),
        "contamination_values": CONTAMINATION_VALUES,
        "jackknife_median_spearman_rho": float(
            jackknife_runs[
                "spearman_rho_vs_full_on_common_observations"
            ].median()
        ),
        "jackknife_min_spearman_rho": float(
            jackknife_runs[
                "spearman_rho_vs_full_on_common_observations"
            ].min()
        ),
        "faithfulness_verdict_counts": {
            str(key): int(value)
            for key, value in faithfulness[
                "overall_xai_faithfulness"
            ].value_counts().items()
        },
        "faithfulness_all_verdicts_reproduced": bool(
            faithfulness["verdict_match"].all()
        ),
        "python_executable": sys.executable,
        "numpy_version": np.__version__,
        "pandas_version": pd.__version__,
        "scipy_version": scipy.__version__,
        "scikit_learn_version": sklearn.__version__,
    }
    (OUTPUT / "audit_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    matrix_c, _, matrix_c_values = load_matrix("C")
    package, reproduction = deployed_model_reproduction()
    deployed_xai_reproduction(package)
    seed_stability(matrix_c, matrix_c_values)
    contamination_sensitivity(matrix_c, matrix_c_values)
    jackknife_stability(matrix_c, matrix_c_values, package)
    matrix_ablation()
    ranking_agreement(package)
    reproduce_faithfulness(package)
    evidence_hashes()
    software_versions()
    write_machine_summary(package, reproduction, matrix_c)
    print(f"Robustness audit complete. Outputs: {OUTPUT}")


if __name__ == "__main__":
    main()
