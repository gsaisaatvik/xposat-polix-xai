import numpy as np
import pandas as pd
import joblib


def product_family(feature):
    if feature.startswith("t1A_exp"):
        return "Tier1A Exposure"
    if feature.startswith("t1A_energy"):
        return "Tier1A EnergyRes"
    if feature.startswith("t1B_src"):
        return "Tier1B Source Azimuth"
    if feature.startswith("t2_lc"):
        return "Tier2 Light Curve"
    if feature.startswith("t2_det"):
        return "Tier2 Detector Balance"
    if feature.startswith("t2_pha"):
        return "Tier2 Spectrum"
    if feature.startswith("t3_wr"):
        return "Tier3 WeightedRoll"
    return "Other"


def normalize_score(values):
    values = np.asarray(values, dtype=float)
    max_val = np.nanmax(np.abs(values))

    if not np.isfinite(max_val) or max_val == 0:
        return np.zeros_like(values)

    return np.abs(values) / max_val


def clean_feature_name(feature):
    names = {
        "t1A_exp_uniformity_cv": "exposure non-uniformity",
        "t1A_exp_max_to_min_roll": "maximum-to-minimum roll exposure ratio",

        "t1A_energy_peak_channel": "energy peak channel",
        "t1A_energy_weighted_mean_channel": "energy weighted mean channel",
        "t1A_energy_weighted_std_channel": "energy spread",
        "t1A_energy_high_channel_fraction": "high-energy channel fraction",
        "t1A_energy_channel_entropy": "energy distribution entropy",
        "t1A_energy_anode_balance_cv": "anode balance variation",

        "t1B_src_peak_to_median_roll": "source roll peak-to-median ratio",
        "t1B_src_roll_entropy": "source roll entropy",
        "t1B_src_roll_smoothness_norm": "source roll smoothness variation",

        "t2_lc_rate_cv": "light curve rate variability",
        "t2_lc_peak_to_median_rate": "light curve peak-to-median rate ratio",

        "t2_det_lc_rate_balance_cv": "detector light-curve rate imbalance",
        "t2_det_pha_centroid_spread": "detector spectral centroid spread",
    }

    return names.get(feature, feature.replace("_", " "))


class PolixXAIPredictor:
    def __init__(self, model_path):
        self.package = joblib.load(model_path)

        self.feature_cols = self.package["feature_cols"]
        self.scaler = self.package["scaler"]
        self.pca = self.package["pca"]
        self.kmeans = self.package["kmeans"]
        self.iso = self.package["isolation_forest"]

    def validate_input(self, df):
        missing = [c for c in self.feature_cols if c not in df.columns]

        if missing:
            raise ValueError(f"Missing required feature columns: {missing}")

        df = df.copy()

        if "observation_id" not in df.columns:
            df["observation_id"] = [f"uploaded_sample_{i + 1}" for i in range(len(df))]

        return df

    def predict_dataframe(self, df):
        df = self.validate_input(df)

        X = df[self.feature_cols].copy()
        X_scaled = self.scaler.transform(X)

        pca_coords = self.pca.transform(X_scaled)
        cluster_labels = self.kmeans.predict(X_scaled)

        anomaly_scores = -self.iso.score_samples(X_scaled)
        anomaly_preds = self.iso.predict(X_scaled)

        results = []

        for i in range(len(df)):
            obs_id = df.iloc[i]["observation_id"]
            x = X_scaled[i]

            xai = self.explain_one(x)

            pred_label = "Anomaly" if anomaly_preds[i] == -1 else "Normal"

            explanation_sentence = self.make_explanation_sentence(
                prediction=pred_label,
                anomaly_score=float(anomaly_scores[i]),
                top_xai_features=xai,
            )

            results.append({
                "observation_id": obs_id,
                "prediction": pred_label,
                "anomaly_score": float(anomaly_scores[i]),
                "pca_pc1": float(pca_coords[i, 0]),
                "pca_pc2": float(pca_coords[i, 1]),
                "kmeans_cluster": int(cluster_labels[i]),
                "top_xai_features": xai,
                "explanation_sentence": explanation_sentence,
            })

        return results

    def explain_one(self, x):
        feature_cols = self.feature_cols

        # 1. PCA contribution:
        # how much each standardized feature contributes to PC1/PC2 separation
        pca_contrib = (
            np.abs(x * self.pca.components_[0]) * self.pca.explained_variance_ratio_[0]
            +
            np.abs(x * self.pca.components_[1]) * self.pca.explained_variance_ratio_[1]
        )

        # 2. KMeans contribution:
        # feature-wise distance from assigned cluster centroid
        cluster = self.kmeans.predict(x.reshape(1, -1))[0]
        centroid = self.kmeans.cluster_centers_[cluster]
        kmeans_contrib = (x - centroid) ** 2

        # 3. Isolation Forest occlusion contribution:
        # neutralize one feature and check how anomaly score changes
        base_score = -self.iso.score_samples(x.reshape(1, -1))[0]

        iso_delta = []

        for j in range(len(feature_cols)):
            x_masked = x.copy()
            x_masked[j] = 0.0

            masked_score = -self.iso.score_samples(x_masked.reshape(1, -1))[0]
            delta = base_score - masked_score

            iso_delta.append(delta)

        iso_delta = np.array(iso_delta)

        # 4. Statistical abnormality
        z_abs = np.abs(x)

        # 5. Combined unsupervised XAI score
        combined = (
            normalize_score(pca_contrib)
            + normalize_score(kmeans_contrib)
            + normalize_score(np.maximum(iso_delta, 0))
            + normalize_score(z_abs)
        )

        rows = []

        for j, feature in enumerate(feature_cols):
            rows.append({
                "feature": feature,
                "feature_readable": clean_feature_name(feature),
                "product_family": product_family(feature),
                "xai_score": float(combined[j]),
                "z_score": float(x[j]),
                "direction": "higher than usual" if x[j] > 0 else "lower than usual",
                "pca_contribution": float(pca_contrib[j]),
                "kmeans_contribution": float(kmeans_contrib[j]),
                "isolation_contribution": float(iso_delta[j]),
            })

        rows = sorted(rows, key=lambda r: r["xai_score"], reverse=True)

        return rows[:5]

    def make_explanation_sentence(self, prediction, anomaly_score, top_xai_features):
        if not top_xai_features:
            return (
                "No feature-level explanation could be generated because no XAI features "
                "were returned by the model."
            )

        top1 = top_xai_features[0]
        top2 = top_xai_features[1] if len(top_xai_features) > 1 else None
        top3 = top_xai_features[2] if len(top_xai_features) > 2 else None

        feature_1 = top1["feature_readable"]
        raw_feature_1 = top1["feature"]
        family_1 = top1["product_family"]
        direction_1 = top1["direction"]
        z1 = top1["z_score"]
        xai1 = top1["xai_score"]

        if prediction == "Anomaly":
            sentence = (
                f"This observation is flagged as anomalous mainly because "
                f"{feature_1} ({raw_feature_1}) from {family_1} is {direction_1} "
                f"compared with the training observations. "
                f"This feature has the highest XAI score ({xai1:.2f}) and a standardized "
                f"z-score of {z1:.2f}. "
            )
        else:
            sentence = (
                f"This observation is not flagged as anomalous, but its strongest local "
                f"explanation comes from {feature_1} ({raw_feature_1}) in {family_1}. "
                f"This feature is {direction_1} compared with the training observations, "
                f"with an XAI score of {xai1:.2f} and a standardized z-score of {z1:.2f}. "
            )

        if top2:
            feature_2 = top2["feature_readable"]
            raw_feature_2 = top2["feature"]
            family_2 = top2["product_family"]
            direction_2 = top2["direction"]
            z2 = top2["z_score"]
            xai2 = top2["xai_score"]

            sentence += (
                f"The second strongest driver is {feature_2} ({raw_feature_2}) "
                f"from {family_2}, which is {direction_2} "
                f"(XAI score {xai2:.2f}, z-score {z2:.2f}). "
            )

        if top3:
            feature_3 = top3["feature_readable"]
            raw_feature_3 = top3["feature"]
            family_3 = top3["product_family"]
            direction_3 = top3["direction"]
            z3 = top3["z_score"]
            xai3 = top3["xai_score"]

            sentence += (
                f"Additional supporting evidence comes from {feature_3} ({raw_feature_3}) "
                f"in {family_3}, which is {direction_3} "
                f"(XAI score {xai3:.2f}, z-score {z3:.2f}). "
            )

        sentence += (
            "The explanation is generated from the unsupervised XAI layer using "
            "PCA separation contribution, KMeans centroid-distance contribution, "
            "Isolation Forest occlusion contribution, and standardized feature abnormality."
        )

        return sentence