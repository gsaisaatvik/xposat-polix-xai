# POLIX XAI Final Report — Errata

This document is an additive errata record for `POLIX_XAI_Final_Report_Reviewed.md`. It does not overwrite or replace the reviewed report.

## 1. Blank-sky baseline selection

The empirical normalized Q/U baseline uses **13 blank-sky fits classified as `acceptable`**, corresponding to reduced \(\chi^2 \le 2.0\).

It should not be described as 13 fits selected using reduced \(\chi^2 \le 5.0\). Fits with \(2.0 < \chi_\nu^2 \le 5.0\) are classified as `caution` and are not included in the 13-fit baseline.

## 2. Missing values and imputation

The frozen Matrix-C CSV contains **zero missing values** across its 25 observations and 15 deployed features.

The deployed `model_service.py` calls the saved `StandardScaler` directly. The saved PKL contains `feature_cols`, `scaler`, `pca`, `kmeans`, and `isolation_forest`; no imputer is stored or executed. Consequently, no median imputation occurred in the reported frozen Matrix-C inference run.

Future data with missing values require an explicit, versioned handling policy.

## 3. Sco X-1 top XAI feature

**Current deployed version resolved; historical website-output provenance remains unresolved.**

The exact imported function audit gives:

1. `t1A_energy_peak_channel`, score 2.454499;
2. `t1A_energy_weighted_mean_channel`, score 2.207369;
3. `t1A_energy_channel_entropy`, score 1.813968.

This agrees with Notebook 10 and the current deployed reproduction. It conflicts with the reviewed-report statement and the user-reported historical website ranking in which entropy was approximately 2.814 and peak channel was second.

The historical website screenshot/export and its exact input row were not located. Until that artifact is supplied, use `XAI_Version_Mismatch_Audit.md` as the controlling version audit and do not silently alter the reviewed report.

## 4. Exploratory and deployed candidate stages

The **six exploratory candidates** used for the Notebook-10 XAI and faithfulness analysis and the **four deployed candidates** returned by the saved Matrix-C Isolation Forest are separate analysis stages.

The six-case faithfulness verdict count—five Strong, one Moderate, and zero Weak—must not be presented as a validation set containing only the four deployed website candidates.

