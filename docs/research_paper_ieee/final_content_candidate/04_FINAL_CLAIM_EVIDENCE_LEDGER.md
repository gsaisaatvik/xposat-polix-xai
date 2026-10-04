# Final Claim–Evidence Ledger

**Status:** Draft-2 control ledger  
**Evidence rule:** Original identifiers → numerical CSV plus generating code → saved PKL plus versioned service → supplementary reproductions → official handbook/guidance → verified primary literature → reviewed report plus errata → drafts.  
**Confidence:** HIGH means directly reproduced or authoritative; MODERATE means defensible only with the stated archive-specific qualification.

## A. Accepted controlling claims C001–C041

| ID | Controlled claim | Primary evidence | Confidence / permitted interpretation |
|---|---|---|---|
| C001 | The frozen archive contains 25 identifier-matched POLIX Level-2 observations. | Archive inventory; Matrix-C IDs | HIGH; not “all available data” |
| C002 | Project metadata maps 10 observations as source and 15 as blank sky. | Role metadata CSV | HIGH numerically; project labels require guide/domain awareness |
| C003 | Matrix C contains 15 deployed features for 25 observations. | Matrix-C CSV; Notebook 08; PKL feature list | HIGH |
| C004 | Frozen Matrix C has zero missing values and the deployed path contains no imputer. | Matrix-C audit; extractor; PKL | HIGH; no median-imputation claim |
| C005 | Matrix C summarizes exposure, channel-distribution, source-azimuth, delivered-light-curve, and cross-detector families. | Notebook 08; feature audit | HIGH |
| C006 | The high-channel fraction uses channel index 4000. | Notebook 08; extractor | HIGH; not calibrated high energy |
| C007 | The source-roll smoothness field is an order-dependent normalized first-difference roughness proxy without circular closure. | Notebook 08; extractor | HIGH |
| C008 | Light-curve features summarize delivered RATE arrays and do not establish intrinsic source variability. | Extractor; handbook | HIGH |
| C009 | Channel-derived features are in channel space, not calibrated keV. | Extractor; handbook | HIGH |
| C010 | WeightedRoll is excluded from Matrix C. | Matrix-C header; Notebook 08 | HIGH |
| C011 | The saved pipeline contains StandardScaler, PCA, KMeans, and Isolation Forest. | PKL inspection; Notebook 10 | HIGH; components, not “four models” |
| C012 | The fixed model returns 21 Normal outputs and four candidates. | PKL; deployed reproduction CSV | HIGH; candidates, not confirmed anomalies |
| C013 | The fixed four are Blank Sky-13, Sco X-1, Her X-1, and Blank Sky-5 by project mapping. | Reproduction CSV; metadata | HIGH numerically |
| C014 | Six detailed XAI/faithfulness cases are an exploratory set distinct from the fixed four. | Notebooks 09–10; XAI CSVs | HIGH |
| C015 | Sco X-1 ranks peak channel 2.454499, weighted mean channel 2.207369, and entropy 1.813968. | Exact-function CSV; versioned service | HIGH |
| C016 | The historical entropy-first Sco X-1 narrative is superseded. | XAI mismatch audit | HIGH provenance |
| C017 | In 100 recorded seeds, three fixed candidates appear 100/100 and Blank Sky-5 appears 29/100. | Seed-stability CSV and script | HIGH for tested procedure only |
| C018 | The four-component XAI score is a project-specific model-informed local ranking and is not SHAP. | `model_service.py`; Agent 5 audit | HIGH implementation; MODERATE contribution |
| C019 | WeightedRoll is exposure-weighted and contains source and background contributions. | POLIX handbook | HIGH |
| C020 | Notebook 11 fits \(C+Q\cos2\phi+U\sin2\phi\) by inverse-variance weighted linear least squares. | Notebook 11; harmonic CSV | HIGH implementation |
| C021 | Thirteen blank-sky fits at reduced chi-square \(\le2\) define the archive reference. | Baseline CSV; fit code | HIGH number; MODERATE scientific suitability |
| C022 | Raw modulation is not calibrated PD; assumed-\(\mu_{100}\) values are sensitivity proxies only. | Handbook; configuration | HIGH boundary |
| C023 | Fitted modulation phase is not official sky PA. | Handbook and missing conversion audit | HIGH boundary |
| C024 | Within this archive, Matrix-C unusualness and harmonic behaviour are non-equivalent diagnostic questions. | Fixed predictions plus harmonic CSVs | MODERATE, bounded descriptive conclusion |
| C025 | Limited directly comparable published work was identified. | Agent 7 literature audit | MODERATE; no first/novel claim |
| C026 | Matrix C is product-aware early feature integration, not demonstrated multi-view representation learning. | Implementation audit | HIGH |
| C027 | Handbook V1.0 places release-specific limits on polarization measurement with documented variable background. | POLIX handbook | HIGH; do not generalize beyond release |
| C028 | Flask is a researcher-facing proof-of-concept implementation, not the principal contribution. | Application source; Agent 8 | MODERATE contribution framing |
| C029 | Contamination 0.16 yields four candidates but does not estimate anomaly prevalence. | PKL; reproduction | HIGH |
| C030 | Saved contamination sensitivity varies thresholds over one fixed ordering. | Sensitivity CSV/script | HIGH; not independent replication |
| C031 | Jackknife persistence is retrospective influence sensitivity, not held-out validation; Sco X-1 was not selected in its held-out refit. | Jackknife CSV/script | HIGH |
| C032 | Matrix-C KMeans contains two singleton clusters, giving Sco X-1 and Blank Sky-13 zero assigned-centroid distance. | PKL metadata; assignments | HIGH; zero does not mean ordinary |
| C033 | Across A/B/C sets, only Sco X-1 and Blank Sky-13 persist; Her X-1 is Matrix-C-specific. | Matrix-comparison CSVs | HIGH |
| C034 | The deployed label is set solely by `IsolationForest.predict`; the XAI score does not decompose it. | `model_service.py` | HIGH |
| C035 | Six neutralization cases reproduce five Strong and one Moderate project verdict; KMeans is absent from the verdict. | Faithfulness CSVs; Notebook 10 | HIGH protocol; sanity check only |
| C036 | Combined XAI scores are normalized within observation and are not calibrated across observations. | Exact normalization function | HIGH |
| C037 | Notebook 11 and the current service propagate raw-modulation uncertainty differently; manuscript values use frozen CSV provenance. | Notebook 11; service audit | HIGH |
| C038 | All ten source raw-modulation values fall within the declared empirical blank-sky mean ±2 sample-SD scalar range. | Source-comparison CSV | HIGH numerically; not an unpolarized finding |
| C039 | The diagonal harmonic-coordinate distance ignores covariance, fit uncertainty, reference-estimation uncertainty, and condition matching. | Notebook 11; Agent 6 | HIGH |
| C040 | Fit-quality bands are project-defined screening classes, not p-values or detection thresholds. | Notebook 11; code | HIGH |
| C041 | Assumed-\(\mu_{100}\) PD values are sensitivity proxies and supplementary at most. | Configuration; proxy CSV | HIGH boundary |

## B. Draft-2 synthesis claims C042–C064

| ID | Draft-2 claim | Evidence | Confidence / approval |
|---|---|---|---|
| C042 | XPoSat carries POLIX, a Thomson-scattering polarimeter. | R01, R05, R06 | HIGH |
| C043 | Official archive sources establish XPoSat/POLIX archive context but not project completeness. | R03 | HIGH |
| C044 | Calibrated polarization inference requires response, background, and coordinate treatment beyond raw harmonic fitting. | R02, R06, R07 | HIGH; domain review desirable |
| C045 | PCA, KMeans, and Isolation Forest are established general methods with complementary roles. | R08–R11 | HIGH as context |
| C046 | Astronomical work uses unsupervised ranking and expert inspection in label-poor settings. | R12–R14 | HIGH as context; different data domains |
| C047 | Explainable-anomaly literature distinguishes anomaly explanation from supervised-label explanation and motivates behavioural checking. | R15, R16 | HIGH as context |
| C048 | Unlabeled outlier evaluation is method- and dataset-sensitive. | R17 | HIGH as general limitation |
| C049 | SHAP was considered in the initial project concept but was not implemented or benchmarked in the final pipeline. | Proposal history; R19 identity; code audit | HIGH project history |
| C050 | Agent 8 rates the primary contribution Moderate and permits three Moderate secondary contributions. | Agent 8 audit | MODERATE; guide approval required |
| C051 | Agent 9 found no contradiction invalidating the bounded archive-screening result and no essential new experiment for the narrow case study. | Agent 9 review | HIGH review provenance |
| C052 | Agent 11 passes Draft 2 with mandatory bounded-framing and approval qualifications. | Agent 11 reconstruction plan | HIGH review provenance |
| C053 | The primary contribution is the integrated traceable product-aware archive-screening framework. | C003, C005, C010–C018, C050 | MODERATE; guide approval |
| C054 | Secondary contribution 1 is the 15-feature provenance-preserving representation. | C003, C005–C009, C050 | MODERATE; guide approval |
| C055 | Secondary contribution 2 is the deterministic project-specific local ranking. | C015, C018, C034–C036, C050 | MODERATE; guide approval |
| C056 | Secondary contribution 3 is the independent WeightedRoll/blank-sky harmonic branch. | C010, C019–C024, C050 | MODERATE; POLIX-aware approval |
| C057 | Robustness experiments, neutralization, and Flask implementation are supporting evidence rather than standalone major contributions. | Agents 4, 5, 8, 9 | HIGH framing |
| C058 | Four paper figures are visualization-only products derived from frozen data or the saved transform, without model fitting. | Figure script and source manifest | HIGH |
| C059 | Figure 4 shows descriptive empirical scatter without sigma/confidence contours. | Figure script; Agent 6 boundary | HIGH |
| C060 | Official acknowledgment text was rechecked on 2026-07-28. | R04 authoritative page | HIGH at audit date; recheck before submission |
| C061 | The abstract identifies XPoSat and POLIX as required by current official guidance. | Abstract; R04 | HIGH |
| C062 | The model artifact records scikit-learn 1.9 while the figure/audit environment loaded it under 1.6.1; the environment is not identical. | PKL warning and audit record | HIGH; disclose, do not claim identity |
| C063 | The exact paper title is the college project title and intentionally broader than the internal scope description. | User/guide instruction | HIGH; fixed unless guide changes |
| C064 | No astrophysical discovery, calibrated PD, official PA, official background subtraction, or general anomaly accuracy was established. | C022–C027, C038–C041; Agents 2, 6, 9 | HIGH boundary |

## C. Section-to-claim control

| Manuscript part | Controlling IDs |
|---|---|
| Abstract | C001–C003, C010–C018, C021, C024, C028, C064 |
| I. Introduction | C018, C019, C025, C028, C042, C046, C049, C053–C057 |
| II. Related Work | C018, C020, C025–C027, C042–C048 |
| III. Dataset and Scope | C001, C002, C005, C019, C027, C043, C064 |
| IV. Feature Engineering | C003–C010, C026, C033 |
| V. Methodology | C011, C014, C018, C029, C032, C034–C036, C045, C047–C049 |
| VI. Harmonic Diagnostic | C019–C023, C027, C037, C039–C041, C044 |
| VII. Results | C012–C017, C021, C030–C040, C058, C059 |
| VIII. Discussion | C024, C033, C038–C040, C064 |
| IX. Limitations | C004, C006–C009, C018, C021–C023, C027, C029–C032, C035–C041, C062, C064 |
| X. Conclusion | C012, C017, C024, C053–C057, C064 |
| Acknowledgment | C060, C061 |

## D. Claims intentionally excluded

- Astrophysical discovery, confirmed anomaly, causal source state, or detection of new behaviour.
- Calibrated polarization degree, official sky polarization angle, official \(\mu_{100}\), or official background subtraction.
- “First,” “novel,” “unique,” “superior,” “breakthrough,” or a benchmark-superiority claim.
- Generalization to future observations, official anomaly accuracy, or completeness over all public POLIX data.
- SHAP/LIME deployment, exact Isolation Forest label decomposition, or cross-observation calibration of local feature scores.
