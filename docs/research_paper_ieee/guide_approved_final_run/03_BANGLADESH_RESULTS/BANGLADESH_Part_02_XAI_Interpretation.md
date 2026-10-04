# BANGLADESH Part 02 — Local XAI Results and Interpretation

## What the deployed explanation measures

The project-specific local feature-ranking heuristic orders evidence within one standardized Matrix-C observation. It combines four separately normalized vectors:

1. feature contributions to the first two PCA directions;
2. squared feature distance from the assigned KMeans centroid;
3. positive change in Isolation Forest anomaly score after neutralizing one standardized feature;
4. absolute standardized feature deviation.

The normalized components are summed with equal implicit weight. The resulting score is a within-observation ranking, not a calibrated importance scale, probability, causal attribution or exact decomposition of the Isolation Forest label. Only Isolation Forest sets that label.

## Current versioned Sco X-1 result

| Rank | Feature | Product family | Exact audit score | Main-paper score |
|---:|---|---|---:|---:|
| 1 | `t1A_energy_peak_channel` | Energy-resolved channel summary | 2.4544990315 | 2.454 |
| 2 | `t1A_energy_weighted_mean_channel` | Energy-resolved channel summary | 2.2073686585 | 2.207 |
| 3 | `t1A_energy_channel_entropy` | Energy-resolved channel summary | 1.8139679863 | 1.814 |

The three-decimal values are appropriate for the main paper because the scores are heuristic rankings rather than calibrated measurements. Six-decimal values remain in the supplementary audit.

Sco X-1 is a singleton KMeans cluster; its KMeans contribution is therefore zero for every feature. Its combined order is driven by the PCA, positive Isolation Forest occlusion and absolute standardized-deviation components. The ranking links the observation’s archive-relative unusualness to channel-space summaries. It does not identify an energy calibration effect, spectral cause, instrument cause or astrophysical cause.

The historical entropy-first narrative was not reproducible from a located versioned artifact and is superseded by the exact deployed-function audit. It must not be used in the manuscript.

## Six-case feature-neutralization sanity check

The exploratory cases were Sco X-1, Blank Sky-13, Her X-1, Blank Sky-5, Blank Sky-15 and Blank Sky-6. For each case, the three highest-ranked standardized features were jointly set to zero.

- Strong: five cases.
- Moderate: one case, Blank Sky-6.
- Weak: zero cases.

Strong means both PCA distance and Isolation Forest anomaly score decreased after neutralization. Moderate means exactly one decreased. KMeans distance was recorded but does not enter the verdict.

This check establishes only the direction of change for two in-sample quantities under one joint perturbation. It does not test unseen observations, rank recovery, explanation uniqueness, causal validity or equivalence to SHAP.

## Product-aware interpretation

The defensible explanatory contribution is traceability. A ranked feature can be mapped back to exposure, energy-resolved channel space, source azimuth, delivered light curve or detector balance. This helps a researcher identify which delivered product family to inspect next. The mapping does not convert the ranking into a physical explanation.

## Exact proposed Results claims

**XAI-R1.** The accepted exact-function audit ranks Sco X-1’s energy peak channel first (2.454), energy weighted mean channel second (2.207) and energy-channel entropy third (1.814).

**XAI-R2.** All three leading Sco X-1 features originate from the energy-resolved product family, showing product-family traceability under the project heuristic without establishing a physical cause.

**XAI-R3.** Joint neutralization of the top three features reduced both PCA distance and Isolation Forest score in five of six exploratory cases and reduced one of the two in the remaining case.

**XAI-R4.** The six-case perturbation result is an in-sample sensitivity sanity check; it does not establish general explanation faithfulness or causal attribution.

## Exact proposed Discussion claims

**XAI-D1.** The custom score is best described as a deterministic, project-specific, model-informed local feature-ranking heuristic rather than SHAP, causal attribution or exact label decomposition.

**XAI-D2.** The method’s practical value lies in linking archive-relative unusualness to explicit Matrix-C features and their originating product families.

**XAI-D3.** Equal weighting and per-observation normalization make the score suitable for local ordering but prevent calibrated comparison of score magnitudes between observations.

**XAI-D4.** The six exploratory cases provide bounded supporting evidence, not standalone validation of explanation quality.

## Controlling evidence

- `D:\polix_xai_webapp\model_service.py`, especially `normalize_score` and `PolixXAIPredictor.explain_one`.
- `D:\polix_xai_webapp\model\polix_v2_matrixC_unsupervised_xai_model.pkl`.
- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\deployed_xai_exact_from_model_service.csv`.
- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\faithfulness_verdict_reproduction.csv`.
- `D:\polix_xai_webapp\research_paper_ieee\guide_approved_final_run\02_BHUTAN_KNOWLEDGE_BASE\BHUTAN_KB_06_Local_XAI_Heuristic.md`.

