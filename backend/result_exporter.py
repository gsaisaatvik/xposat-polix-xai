from __future__ import annotations

import pandas as pd


def results_to_dataframe(results):
    """
    Convert website XAI + polarimetry results into one downloadable table.
    One row is produced for each POLIX observation.
    """

    rows = []

    for result in results:
        top_features = result.get("top_xai_features") or []
        polarimetry = result.get("polarimetry") or {}

        row = {
            # Observation metadata
            "observation_id": result.get("observation_id"),
            "proposal_id": result.get("proposal_id"),
            "target_name": result.get("target_name"),
            "observation_role": result.get("observation_role"),

            # XAI model output
            "prediction": result.get("prediction"),
            "anomaly_score": result.get("anomaly_score"),
            "pca_pc1": result.get("pca_pc1"),
            "pca_pc2": result.get("pca_pc2"),
            "kmeans_cluster": result.get("kmeans_cluster"),

            # Physical modulation output
            "raw_modulation_percent": polarimetry.get(
                "raw_modulation_percent"
            ),
            "raw_modulation_percent_error": polarimetry.get(
                "raw_modulation_percent_error"
            ),
            "modulation_phase_deg": polarimetry.get(
                "modulation_phase_deg"
            ),
            "modulation_phase_error_deg": polarimetry.get(
                "modulation_phase_error_deg"
            ),
            "amplitude_snr": polarimetry.get(
                "amplitude_snr"
            ),
            "reduced_chi2": polarimetry.get(
                "reduced_chi2"
            ),
            "fit_quality": polarimetry.get(
                "fit_quality"
            ),

            # Blank-sky-relative analysis
            "background_relative_modulation_percent": polarimetry.get(
                "background_relative_modulation_percent"
            ),
            "background_relative_phase_deg": polarimetry.get(
                "background_relative_phase_deg"
            ),
            "source_vs_blank_z": polarimetry.get(
                "source_vs_blank_z"
            ),
            "source_modulation_vs_blank_status": polarimetry.get(
                "source_modulation_vs_blank_status"
            ),
            "background_relative_vector_distance": polarimetry.get(
                "background_relative_vector_distance"
            ),
            "background_relative_vector_status": polarimetry.get(
                "background_relative_vector_status"
            ),

            # Central PD proxy scenario
            "selected_proxy_mu100": polarimetry.get(
                "selected_proxy_mu100"
            ),
            "selected_raw_pd_proxy_percent": polarimetry.get(
                "selected_raw_pd_proxy_percent"
            ),
            "selected_background_relative_pd_proxy_percent": polarimetry.get(
                "selected_background_relative_pd_proxy_percent"
            ),

            # Angle and confidence status
            "reported_angle_value_deg": polarimetry.get(
                "reported_angle_value_deg"
            ),
            "reported_angle_type": polarimetry.get(
                "reported_angle_type"
            ),
            "polarimetry_confidence_status": polarimetry.get(
                "polarimetry_confidence_status"
            ),
            "final_calibrated_pd_claimed": polarimetry.get(
                "final_calibrated_pd_claimed"
            ),
            "official_pa_claimed": polarimetry.get(
                "official_pa_claimed"
            ),

            # Combined deterministic interpretation
            "scientific_interpretation": result.get(
                "scientific_interpretation"
            ),
        }

        # Save the first five XAI drivers in separate columns
        for index in range(5):
            rank = index + 1

            if index < len(top_features):
                feature = top_features[index]

                row[f"xai_rank_{rank}_feature"] = feature.get(
                    "feature"
                )
                row[f"xai_rank_{rank}_product_family"] = feature.get(
                    "product_family"
                )
                row[f"xai_rank_{rank}_score"] = feature.get(
                    "xai_score"
                )
                row[f"xai_rank_{rank}_z_score"] = feature.get(
                    "z_score"
                )
            else:
                row[f"xai_rank_{rank}_feature"] = None
                row[f"xai_rank_{rank}_product_family"] = None
                row[f"xai_rank_{rank}_score"] = None
                row[f"xai_rank_{rank}_z_score"] = None

        rows.append(row)

    return pd.DataFrame(rows)
