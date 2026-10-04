# NEPAL Part 05 - Evidence Contradictions

## Gate verdict

**No contradiction was found that invalidates the central 25-observation, 15-feature Matrix-C archive-screening result. Phase 2 may proceed after user approval.**

The issues below control later writing and must not be silently resolved.

## C01 - Historical V1 versus deployed V2

**Conflict:** Notebooks 03–07 use a 14-feature V1 representation containing WeightedRoll, KMeans `k=4`, DBSCAN and Isolation Forest contamination 0.15. Their candidate set differs.

**Resolution:** historical development only. Notebook 08 Matrix C, Notebook 10 saved PKL, deployed code and reproduction CSV control the paper.

## C02 - Median-imputation architecture label

**Conflict:** a communication architecture shows median imputation.

**Evidence:** Matrix C has zero missing values. No imputer appears in Notebook 08, the saved package interface, `model_service.py` or `feature_extractor.py`.

**Resolution:** remove the imputation block and make no imputation claim.

## C03 - Sequential model diagram

**Conflict:** the communication architecture visually chains PCA to KMeans to Isolation Forest.

**Evidence:** deployed code applies PCA, KMeans and Isolation Forest to the same standardized feature row. Only Isolation Forest supplies the label.

**Resolution:** use a scaler fan-out diagram and a separate XAI aggregation block.

## C04 - Six exploratory cases versus four fixed candidates

**Conflict:** Notebook 09 and several Notebook-11 physical tables carry a six-case consensus flag and priority fields.

**Evidence:** the frozen saved-model output has four candidates. The six cases are Sco X-1, Blank Sky-13, Her X-1, Blank Sky-5, Blank Sky-15 and Blank Sky-6.

**Resolution:** ignore `is_xai_consensus_anomaly`, `total_flags` and `path2_priority` when reporting the fixed model. Join physical values to `deployed_model_reproduction.csv` by full observation ID.

## C05 - Historical absolute-z drivers versus deployed XAI

**Conflict:** Notebook 09’s early driver table uses absolute standardized deviation.

**Evidence:** the deployed XAI combines four normalized components from PCA, KMeans, Isolation Forest occlusion and absolute standardized abnormality.

**Resolution:** use `model_service.py` and the accepted XAI audit. Do not describe Notebook-09 drivers as the deployed explanation method.

## C06 - Sco X-1 entropy-first narrative

**Conflict:** an unversioned historical website narrative ranked entropy first.

**Evidence:** current service code, saved PKL, exact-function CSV and located Notebook-10 output all rank peak channel first, weighted mean second and entropy third.

**Resolution:** the entropy-first narrative is superseded and excluded.

## C07 - “Four models” and causal driver language

**Conflict:** some narrative material can imply four independent models or causal feature drivers.

**Evidence:** the score has four correlated explanation components and does not decompose the Isolation Forest label.

**Resolution:** say “four-component local feature-ranking heuristic” and “highest-ranked features under the local explanation score.”

## C08 - High-energy terminology

**Conflict:** the service display map says “high-energy channel fraction.”

**Evidence:** the feature is the fraction of counts in PHA channels at or above index 4000; no calibrated energy conversion is part of this computation.

**Resolution:** paper term is “high-channel fraction.”

## C09 - Smoothness terminology

**Conflict:** “roll smoothness” can imply unrestricted circular smoothness.

**Evidence:** implementation uses mean absolute adjacent-bin difference and omits the last-to-first wrap.

**Resolution:** call it an “order-dependent roughness proxy” or state the computation exactly.

## C10 - Light-curve variability terminology

**Conflict:** rate features may be interpreted as intrinsic source variability.

**Evidence:** features summarize the delivered `RATE` array without additional timing or physical correction.

**Resolution:** call them delivered-light-curve diagnostic proxies.

## C11 - WeightedRoll semantics without an approved external product source

**Conflict:** older prose states that WeightedRoll contains source and background contributions or makes detailed processing claims.

**Evidence:** permitted code/data establish a 360-bin total-count-rate curve with errors and the project’s exposure-weighted/downstream interpretation, but not an explicit source/background decomposition or official correction status.

**Resolution:** use the narrower operational statement: the project analyses the delivered exposure-weighted WeightedRoll total-count-rate curve and does not apply an independently verified background-subtraction procedure.

## C12 - Harmonic coefficient names

**Conflict:** CSV columns use `Q` and `U`, which can be read as calibrated Stokes parameters.

**Evidence:** they are coefficients of cosine and sine terms in the project’s second-harmonic fit.

**Resolution:** use “cosine/sine second-harmonic coefficients” and “fractional harmonic coordinates.” Avoid unqualified Stokes terminology.

## C13 - Blank-sky “scatter” and significance language

**Conflict:** saved strings use “within blank-sky scatter” and standardized coordinate distances with thresholds 2 and 3.

**Evidence:** the reference uses 13 selected fits, coordinate-wise sample means/standard deviations and a diagonal distance that ignores covariance and fit/baseline uncertainty.

**Resolution:** say “within the declared empirical blank-sky reference rule.” Do not call it confidence, sigma significance or a detection region.

## C14 - Notebook-11 versus Flask uncertainty propagation

**Conflict:** the two implementations propagate `A/C` uncertainty differently.

**Resolution:** Notebook-11 CSV controls any reported project uncertainty. Disclose the later service difference; do not merge results. Prefer central values in the main paper.

## C15 - Historical PD/PA candidate labels

**Conflict:** Notebook 11 contains “Strong PD/PA candidate” and related historical labels and assumed-modulation-factor sensitivity scenarios.

**Resolution:** exclude these labels from the main paper. State only that the study reports raw harmonic diagnostics and does not report calibrated polarization degree, official sky polarization angle, polarization significance or official background subtraction.

## C16 - Duplicate friendly blank-sky label

**Conflict:** C24_0001 and C24_0008 are both labelled `Blank Sky-2`; no `Blank Sky-12` appears.

**Resolution:** preserve the provided mapping and use full observation IDs as unique keys. Do not silently renumber. Guide clarification may be requested later if friendly labels are prominent.

## C17 - Matrix organization provenance

**Issue:** the operation copying archive-root matrices/results into `final_project_outputs` is not documented in the inspected notebook sequence.

**Evidence:** source and organized copies are byte-identical by SHA-256.

**Resolution:** content identity is verified; the organizational step is a reproducibility limitation, not a numerical contradiction.

## C18 - Unexecuted desirable validation

The following were not executed and do not invalidate the bounded result:

- independent future-release validation;
- anomaly ground truth or expert adjudication;
- KMeans membership/seed stability;
- PCA subspace stability;
- explanation-rank stability;
- random-feature or bottom-feature neutralization comparator;
- residual/higher-harmonic model checks;
- covariance-aware or matched blank-sky modelling;
- benchmark comparison with SHAP or another explainer.

These belong in limitations or Future Work. They must not be approximated or invented.

## Phase-1 recommendation

Proceed to the knowledge-base phase. Use the all-25 truth table as the integration layer, preserve the full IDs, and retain the central claim only in its bounded form:

> Statistical unusualness and raw modulation-like harmonic behaviour answer different diagnostic questions within the project archive.

