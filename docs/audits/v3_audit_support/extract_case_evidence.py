from __future__ import annotations

import json
from pathlib import Path
import sys

import joblib
import numpy as np
import pandas as pd

sys.path.insert(0, r"D:\polix_xai_webapp")
from model_service import PolixXAIPredictor


ROOT = Path(r"D:\polix_xai_webapp")
ARCHIVE = Path(r"D:\ISROtrial\Polix_L2_full_archive")
SUPP = ROOT / "research_paper_ieee" / "supplementary_experiments"
OUT = ROOT / "v3_audit_support"
FEATURE_DIR = ARCHIVE / "final_project_outputs" / "02_feature_engineering"
PHYS_DIR = ARCHIVE / "final_project_outputs" / "04_polarimetry_results"

MATRIX = FEATURE_DIR / "polix_matrix_v2_C_primary_plus_supporting.csv"
MODEL = ROOT / "model" / "polix_v2_matrixC_unsupervised_xai_model.pkl"
META = ROOT / "config" / "observation_metadata.json"

CASES = [
    "X01_PLX_G01_0006_000000",
    "X01_PLX_G01_0003_000000",
    "X01_PLX_C24_0018_000000",
    "X01_PLX_C24_0010_000000",
    "X01_PLX_P01_0005_000000",
]


def short_id(observation_id: str) -> str:
    return observation_id.removeprefix("X01_PLX_").removesuffix("_000000")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    frame = pd.read_csv(MATRIX)
    package = joblib.load(MODEL)
    predictor = PolixXAIPredictor(MODEL)
    features = list(package["feature_cols"])
    z = package["scaler"].transform(frame[features])
    pca = package["pca"].transform(z)
    pca_distance = np.linalg.norm(pca, axis=1)
    cluster = package["kmeans"].predict(z)
    cluster_sizes = pd.Series(cluster).value_counts().to_dict()

    fixed = pd.read_csv(SUPP / "deployed_model_reproduction.csv").set_index("observation_id")
    seeds = pd.read_csv(SUPP / "isolation_seed_stability_summary.csv").set_index("observation_id")
    contamination = pd.read_csv(SUPP / "contamination_candidate_stability.csv").set_index("observation_id")
    jackknife = pd.read_csv(SUPP / "jackknife_observation_stability.csv").set_index("observation_id")
    ablation = pd.read_csv(SUPP / "matrix_ablation_results.csv")
    faith = pd.read_csv(SUPP / "faithfulness_verdict_reproduction.csv").set_index("observation_id")
    harmonic = pd.read_csv(PHYS_DIR / "polix_weightedroll_raw_modulation_fits.csv").set_index("observation_id")
    source_compare = pd.read_csv(PHYS_DIR / "path2_source_vs_blank_sky_modulation_comparison.csv").set_index("observation_id")
    metadata = json.loads(META.read_text(encoding="utf-8"))

    case_rows: list[dict[str, object]] = []
    xai_rows: list[dict[str, object]] = []
    for observation_id in CASES:
        idx = int(frame.index[frame["observation_id"] == observation_id][0])
        explanation = predictor.explain_one(np.asarray(z[idx], dtype=float))
        for rank, item in enumerate(explanation, start=1):
            xai_rows.append(
                {
                    "observation_id": observation_id,
                    "rank": rank,
                    **item,
                    "raw_feature_value": float(frame.loc[idx, item["feature"]]),
                }
            )

        matrix_membership = {}
        for matrix in ["A", "B", "C"]:
            row = ablation[(ablation["matrix"] == matrix) & (ablation["observation_id"] == observation_id)].iloc[0]
            matrix_membership[matrix] = {
                "flagged": bool(row["isolation_flagged"]),
                "score": float(row["isolation_anomaly_score"]),
                "rank": int(row["isolation_rank"]),
            }

        harmonic_row = harmonic.loc[observation_id]
        red_chi = float(harmonic_row["reduced_chi2"])
        fit_category = "acceptable" if red_chi <= 2 else ("caution" if red_chi <= 5 else "poor")
        if observation_id in source_compare.index:
            blank_rule = str(source_compare.loc[observation_id, "source_modulation_vs_blank_status"])
            source_z = float(source_compare.loc[observation_id, "source_vs_blank_z"])
        else:
            blank_rule = "included_in_13_fit_reference" if red_chi <= 2 else "excluded_from_13_fit_reference"
            source_z = np.nan

        faith_row = faith.loc[observation_id] if observation_id in faith.index else None
        case_rows.append(
            {
                "observation_name": metadata[short_id(observation_id)]["target_name"],
                "observation_id": observation_id,
                "project_role": metadata[short_id(observation_id)]["observation_role"],
                "fixed_score": float(fixed.loc[observation_id, "stored_anomaly_score"]),
                "fixed_label": str(fixed.loc[observation_id, "stored_prediction"]),
                "seed_times_flagged": int(seeds.loc[observation_id, "times_flagged"]),
                "seed_min_rank": int(seeds.loc[observation_id, "min_rank"]),
                "seed_max_rank": int(seeds.loc[observation_id, "max_rank"]),
                "contamination_settings_flagged": int(contamination.loc[observation_id, "settings_flagged"]),
                "contamination_settings_evaluated": int(contamination.loc[observation_id, "settings_evaluated"]),
                "jackknife_included_times_flagged": int(jackknife.loc[observation_id, "times_flagged_when_in_training"]),
                "jackknife_included_runs": int(jackknife.loc[observation_id, "included_runs"]),
                "jackknife_held_out_flagged": bool(jackknife.loc[observation_id, "held_out_flagged"]),
                "jackknife_held_out_rank": int(jackknife.loc[observation_id, "held_out_rank_among_25"]),
                "matrix_A_flagged": matrix_membership["A"]["flagged"],
                "matrix_A_score": matrix_membership["A"]["score"],
                "matrix_A_rank": matrix_membership["A"]["rank"],
                "matrix_B_flagged": matrix_membership["B"]["flagged"],
                "matrix_B_score": matrix_membership["B"]["score"],
                "matrix_B_rank": matrix_membership["B"]["rank"],
                "matrix_C_flagged": matrix_membership["C"]["flagged"],
                "matrix_C_score": matrix_membership["C"]["score"],
                "matrix_C_rank": matrix_membership["C"]["rank"],
                "pca_pc1": float(pca[idx, 0]),
                "pca_pc2": float(pca[idx, 1]),
                "pca_distance": float(pca_distance[idx]),
                "kmeans_cluster": int(cluster[idx]),
                "kmeans_cluster_size": int(cluster_sizes[int(cluster[idx])]),
                "neutralization_tested": faith_row is not None,
                "neutralized_features": "" if faith_row is None else str(faith_row["neutralized_top_xai_features"]),
                "neutralization_pca_before": np.nan if faith_row is None else float(faith_row["original_pca_distance"]),
                "neutralization_pca_after": np.nan if faith_row is None else float(faith_row["new_pca_distance"]),
                "neutralization_iso_before": np.nan if faith_row is None else float(faith_row["original_isolation_score"]),
                "neutralization_iso_after": np.nan if faith_row is None else float(faith_row["new_isolation_score"]),
                "neutralization_kmeans_before": np.nan if faith_row is None else float(faith_row["original_kmeans_distance"]),
                "neutralization_kmeans_after": np.nan if faith_row is None else float(faith_row["new_kmeans_distance"]),
                "neutralization_verdict": "NOT_TESTED" if faith_row is None else str(faith_row["overall_xai_faithfulness"]),
                "C": float(harmonic_row["C_mean_level"]),
                "Q": float(harmonic_row["Q_cos2_coeff"]),
                "U": float(harmonic_row["U_sin2_coeff"]),
                "amplitude": float(harmonic_row["modulation_amplitude"]),
                "raw_modulation_percent": float(harmonic_row["raw_modulation_percent"]),
                "fitted_phase_deg": float(harmonic_row["modulation_phase_deg"]),
                "reduced_chi2": red_chi,
                "degrees_of_freedom": int(harmonic_row["dof"]),
                "n_bins": int(harmonic_row["n_points"]),
                "fit_category": fit_category,
                "blank_sky_rule_interpretation": blank_rule,
                "source_vs_blank_z": source_z,
            }
        )

    pd.DataFrame(case_rows).to_csv(OUT / "case_evidence.csv", index=False)
    pd.DataFrame(xai_rows).to_csv(OUT / "case_top5_exact_deployed_xai.csv", index=False)


if __name__ == "__main__":
    main()
