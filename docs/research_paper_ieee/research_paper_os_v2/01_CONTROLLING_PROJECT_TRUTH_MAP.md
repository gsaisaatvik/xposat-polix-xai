# Controlling Project Truth Map

## 1. Rule

Authority depends on the kind of claim. A numerical CSV cannot define physical meaning, and a handbook cannot establish what a local script actually computed.

## 2. Hierarchy by claim type

| Priority | Evidence class | Controls | Does not control |
|---:|---|---|---|
| 1 | Original local archives and extracted observation folders | Which 25 identifiers are in the project freeze | Completeness of the public POLIX archive |
| 2 | Result CSV plus exact generating notebook/code | Numerical values, matrix columns, fit rows, and selected cases | Physical validity beyond the implemented calculation |
| 3 | Saved deployed PKL plus versioned deployed code | Frozen deployed predictions and current XAI behavior | Historical unversioned website behavior or future-data performance |
| 4 | Versioned supplementary script plus its CSV/JSON/hash | Later reproducibility and robustness results | Original-project status or independent validation |
| 5 | Current POLIX handbook and official ISRO/ISSDC guidance | Product semantics, calibration limits, data-use wording | The local code path or local numerical results |
| 6 | Peer-reviewed primary literature | General method foundations and bounded research context | POLIX-release-specific semantics or project-specific validation |
| 7 | Reviewed report plus additive errata/audits | Project intent and narrative context | Any disputed number or current implementation behavior |
| 8 | Drafts, figures, screenshots, slides, and summaries | Communication | Sole evidence for any scientific or numerical claim |

## 3. Controlling artifacts

| Research object | Controlling evidence |
|---|---|
| Archive identity | 25 `.tgz` files in `D:\ISROtrial\Polix_L2_full_archive\data_raw` and 25 identifier-matched extracted folders |
| Observation roles | `path2_observation_role_metadata_filled.csv`, with friendly-label caveat |
| Matrix A/B/C/WR | CSVs in `final_project_outputs\02_feature_engineering` plus Notebook 08 |
| Deployed model | Byte-identical PKL copies; authoritative deployment copy at `D:\polix_xai_webapp\model\polix_v2_matrixC_unsupervised_xai_model.pkl` |
| Fixed predictions | Saved PKL and `deployed_model_reproduction.csv` |
| Current local XAI | `model_service.py::PolixXAIPredictor.explain_one`, exact-function CSV, and XAI mismatch audit |
| Exploratory six-case XAI/faithfulness | Notebook 09 selection and Notebook 10 result CSVs |
| ML robustness interpretation | `agents/04_ML_Statistics_Audit.md` plus the existing supplementary-experiment CSVs/scripts it cites |
| XAI-method interpretation | `agents/05_XAI_Method_Audit.md` plus deployed code, Notebook 10, exact-function CSV, and faithfulness CSVs |
| Physical diagnostics | Notebook 11 and exact result CSVs; handbook controls interpretation |
| Physical-diagnostic interpretation | `agents/06_Physical_Diagnostic_Audit.md`; frozen Notebook 11/CSVs control saved numbers, while the handbook controls physical meaning |
| Product semantics | *XPoSat-POLIX User Handbook*, V1.0, Oct. 2025 |
| Literature claims | `literature/Verified_Reference_Library.md` and `Reference_Claim_Map.csv` |

## 4. Frozen facts

- The project archive contains 25 identifier-matched observations: 10 mapped as source and 15 as blank sky.
- Matrix C contains one identifier and 15 feature columns; the frozen CSV has no missing cells.
- The deployed core contains StandardScaler, two-component PCA, five-cluster KMeans, and Isolation Forest. These are pipeline components, not “four models.”
- The fixed saved model gives 21 Normal labels and four anomaly candidates.
- The four fixed candidates and the six exploratory multi-matrix cases are different analysis stages.
- The current versioned Sco X-1 ranking is peak channel, weighted mean channel, then channel entropy.
- The fixed four-candidate output is distinct from a three-candidate Matrix-C core stable under the tested seed, threshold, and included-observation jackknife procedures; the latter is not an external-generalization result.
- Across Matrix A/B/C candidate sets, only Sco X-1 and Blank Sky-13 persist; Her X-1 is Matrix-C-specific in that ablation.
- Two Matrix-C KMeans clusters are singletons, giving zero assigned-centroid distance for Sco X-1 and Blank Sky-13.
- The deployed anomaly label comes solely from `IsolationForest.predict`; the four-component explanation score ranks composite local evidence within one observation.
- The six-case neutralization result is an in-sample, method-aligned perturbation sanity check with project-defined sign-only verdicts; KMeans does not determine the overall verdict.
- WeightedRoll is outside Matrix C and contains source and background modulation contributions.
- Fifteen blank-sky fits exist; thirteen satisfying the project rule reduced chi-square <=2 define the archive-specific empirical reference.
- All ten source raw-modulation values lie within the empirical blank-sky mean plus or minus two sample standard deviations under the declared scalar rule.
- The frozen notebook and current Flask service use different \(A/C\) uncertainty propagation; saved CSV uncertainties are notebook-method results.
- The diagonal fractional-harmonic-coordinate distance and its 2/3 cutoffs are descriptive project diagnostics, not calibrated confidence contours or sigma levels.
- Current evidence does not establish official background subtraction, calibrated PD, official sky PA, anomaly ground truth, or astrophysical discovery.

## 5. Facts with unresolved provenance or semantics

- Exact official download URLs, download dates, and archive-issued checksums were not located.
- Two observation IDs share the friendly label “Blank Sky-2.”
- The current Flask extractor has not been regression-compared across all 25 observations against the frozen Notebook-08 Matrix C.
- The PKL was created with scikit-learn 1.9.0, while the generic environment is unpinned.
- Exact scientific interpretation of several Matrix-C proxies requires domain approval.
- The physical fit's coefficient convention and detector-to-sky phase conversion are not officially verified.
- The historical entropy-first Sco X-1 narrative has no located versioned artifact.
- Explanation-rank stability, alternative neutralization baselines, and matched random/bottom-feature perturbation comparisons were not tested.
- The notebook/service \(A/C\) uncertainty formulas have not been numerically reconciled.
- Blank-sky covariance-aware, resampled, robust-centre, or observation-matched baselines were not tested.

## 6. Wording controlled by this map

Use:

> 25 POLIX Level-2 observations included in the project archive.

Do not use:

> all available POLIX observations.

Use:

> archive-relative anomaly candidate; raw modulation; fitted modulation phase; empirical blank-sky reference.

Use:

> project-specific, model-informed local feature ranking; three-candidate Matrix-C core stable under the tested procedures.

Do not use:

> confirmed anomaly; polarization detection; calibrated PD; official PA; official background subtraction.

Do not use:

> statistically significant anomaly; generally robust core; exact attribution of the deployed label; four independent XAI models; generally faithful explanation.

## Final Draft-2 controlling synthesis

- Exact title: **An Explainable AI Framework for Analysis of X-Ray Polarimetry Data from XPoSat**.
- Scope: 25 observations in the frozen project archive; 10 project-labelled source and 15 project-labelled blank sky.
- Fixed saved result: 21 Normal and four candidates.
- Procedure-qualified result: Blank Sky-13, Sco X-1, and Her X-1 appear in 100/100 tested seeds; Blank Sky-5 appears in 29/100.
- Cross-tier result: Sco X-1 and Blank Sky-13 persist across A/B/C; Her X-1 is Matrix-C-specific; Blank Sky-5 appears in B/C.
- XAI: within-observation project-specific local ranking; current Sco X-1 order is peak channel, weighted mean channel, entropy.
- Physical branch: source-plus-background WeightedRoll, raw harmonic fit, and 13-fit empirical blank-sky reference at reduced chi-square \(\le2\).
- Central conclusion: statistical unusualness and modulation-like harmonic behaviour are non-equivalent **within the frozen archive**.
- Uncertainty: central physical values use frozen Notebook-11 CSV provenance; later Flask \(A/C\) propagation differs and is supplementary.
- Contribution hierarchy: one Moderate primary integrated-framework contribution and three Moderate secondary contributions; robustness and deployment are supporting evidence.
