# MALDIVES Part 05 — Claim–Evidence Ledger

## Control rule

This ledger controls the Phase-5 manuscript. Numerical claims use original CSVs plus their generating notebook or code; fixed prediction and local-ranking claims use the saved PKL and versioned deployed function; robustness claims use the existing supplementary outputs. Literature supports general context only. No 2025 handbook claim or citation is used.

## Dataset, method, and numerical claims

| ID | Manuscript claim | Controlling evidence | Manuscript location | Confidence and boundary |
|---|---|---|---|---|
| M001 | The project archive contains 25 observations: 10 project-labelled sources and 15 project-labelled blank skies. | `01_NEPAL_EVIDENCE/NEPAL_Part_03_All_25_Observation_Truth_Table.csv`; Matrix-C CSV | Abstract; III; VII | High. Scope is the project archive, not all public data. |
| M002 | Matrix C contains 25 rows, 15 numeric features, zero missing values, and no imputation in the deployed path. | `polix_matrix_C_all_tiers_with_roles.csv`; `feature_extractor.py`; `01_NEPAL_EVIDENCE/NEPAL_Part_02_Code_CSV_Model_Lineage.md` | III; IV | High. No median-imputation claim. |
| M003 | Matrix A/B/C contain 8/11/15 features; WR is a separate six-feature diagnostic matrix. | Matrix A/B/C/WR CSVs; Notebook 08; `NEPAL_Part_02_Code_CSV_Model_Lineage.md` | IV-A | High. No Matrix-C superiority claim. |
| M004 | The 15 Matrix-C features and their product-family provenance follow the frozen extractor. | Notebook 08 feature construction; `feature_extractor.py`; Matrix-C schema | IV-B; Table II | High. Channel-space and delivered-product boundaries retained. |
| M005 | StandardScaler feeds PCA, KMeans, and Isolation Forest in parallel; only Isolation Forest defines the deployed label. | Saved PKL; Notebook 10; `model_service.py`; exact reproduction audit | Fig. 1; V | High. The four XAI components are not four models. |
| M006 | PCA variance ratios are 0.387435 and 0.225051, totaling 0.612486. | Saved PKL; existing PCA output; Phase-4 Fig. 2 source manifest | V-A | High. PCA view is descriptive. |
| M007 | KMeans uses k=5, n_init=20, random state 42, silhouette 0.310936, and cluster sizes 1, 9, 10, 1, 4. | Saved PKL; Notebook 10; KMeans evaluation CSV/output | V-A; IX | High. In-sample description only; singleton limitation disclosed. |
| M008 | Isolation Forest uses 100 trees, contamination 0.16, random state 42; anomaly score is negative `score_samples`; `predict` alone sets labels. | Saved PKL; Notebook 10; `model_service.py` | V-B | High. Contamination is a frozen screening assumption, not prevalence. |
| M009 | The fixed output is 21 Normal and four candidates: Blank Sky-13, Sco X-1, Her X-1, Blank Sky-5. | `supplementary_experiments/deployed_model_reproduction.csv`; frozen prediction CSV; saved PKL | Abstract; VII-A; Table III | High. Candidates are inspection priorities, not confirmed anomalies. |
| M010 | Fixed candidate scores are 0.615964, 0.593516, 0.572308, and 0.517611 in the stated order. | `deployed_model_reproduction.csv` | Table III | High. Six decimal places retained for model scores. |
| M011 | Blank Sky-13, Sco X-1, and Her X-1 were selected in 100/100 seeds; Blank Sky-5 in 29/100; Blank Sky-15 in 68/100. | `supplementary_experiments/isolation_seed_stability_summary.csv` | VII-B; Fig. 3 | High within tested seeds. Frequencies are not probabilities. |
| M012 | Contamination settings 0.12/0.16/0.20/0.24 produced 3/4/5/6 selected rows with the stated persistence. | `supplementary_experiments/contamination_candidate_stability.csv` | VII-B | High for tested settings. No parameter optimization or prevalence claim. |
| M013 | Included-observation jackknife counts and rank correlations are as reported. | `jackknife_observation_stability.csv`; `jackknife_run_summary.csv` | VII-B | High for retrospective refits; not prospective validation. |
| M014 | Only Blank Sky-13 and Sco X-1 persist across Matrix A/B/C; the complete tier-specific candidate lists are as reported. | `matrix_ablation_summary.csv`; Matrix A/B/C comparison outputs | VII-C | High. Cross-tier two is distinct from fixed four and stable three. |
| M015 | Spearman correlations are 0.894615, 0.155799, and 0.186574 for the stated ranking pairs. | `ranking_agreement.csv`; `ranking_metrics.csv` | VII-C | High descriptively. Nominal p-values are not used for validation. |
| M016 | The local score sums normalized PCA, KMeans, non-negative Isolation-Forest occlusion, and absolute-standardized-value components. | `model_service.py::PolixXAIPredictor.explain_one`; saved PKL; `XAI_Version_Mismatch_Audit.md` | V-C | High for current versioned implementation. Project-specific heuristic only. |
| M017 | Sco X-1 ranks peak channel 2.454, weighted mean channel 2.207, entropy 1.814 in the main paper. | `deployed_xai_exact_from_model_service.csv`; versioned audit | VII-A; Table III | High. Six-decimal values remain in supplementary evidence; entropy-first history is superseded. |
| M018 | Six exploratory neutralization cases yielded five Strong, one Moderate, zero Weak. | `faithfulness_verdict_reproduction.csv`; original faithfulness output | V-D; VII-D | High for the saved in-sample sign check; not a general faithfulness proof. |
| M019 | WeightedRoll is excluded from Matrix C and fitted with weighted least squares as C + Q cos(2φ) + U sin(2φ). | Matrix-C schema; Notebook 11; frozen physical-results CSV | VI-A | High. Coefficients are harmonic, not calibrated Stokes parameters. |
| M020 | Fits exist for all 25 observations; 19 acceptable, 3 caution, 3 poor under project rules. | Notebook-11 fit-results CSV; `BANGLADESH_Part_03_Harmonic_Results.md` | VII-E | High under declared categories; not p-value or detection classes. |
| M021 | Fifteen blank skies were fitted; 13 with reduced chi-square ≤ 2 define the reference. | blank-sky baseline CSV; Notebook 11 | VI-B; VII-E | High. Empirical selected reference, not official background subtraction. |
| M022 | Reference mean raw modulation is 1.147820% with sample SD 0.565960%; mean q/u are 0.009092005 and −0.006478172. | blank-sky baseline CSV; Phase-4 Fig. 4 manifest | VII-E | High. Descriptive coordinates, not a confidence region. |
| M023 | All ten source raw-modulation values are within the declared empirical rule. | source-versus-blank comparison CSV | VII-E | High for the declared scalar rule; not evidence of no polarization. |
| M024 | Representative Sco X-1, Her X-1, Crab P01_0005, Blank Sky-13, and Blank Sky-5 harmonic values and categories match Table IV. | frozen Notebook-11 source and blank-sky result CSVs joined to `deployed_model_reproduction.csv` by full observation ID | Table IV; VIII-B | High. Historical six-case priority labels are ignored. |
| M025 | Notebook 11 and the later Flask service use different A/C uncertainty propagation; manuscript values follow the frozen notebook CSV. | Notebook 11; `polarization_service.py`; Phase-1 lineage audit | VI-C; IX | High. Implementations are not merged or claimed identical. |
| M026 | Statistical unusualness and modulation-like harmonic behaviour answer different questions within the archive. | M009–M024; separate-input architecture | Abstract; VIII-A; X | Moderate–High, archive-specific. Non-equivalence does not imply statistical independence. |
| M027 | No anomaly ground truth, calibrated polarization degree, official sky polarization angle, official background subtraction, accuracy, or future-data performance is established. | Scope decision; code/output limits; absence of labels/calibration implementation | Abstract; III; IX; X | High as a claim boundary. |

## Literature and official-context claims

| ID | Claim supported | Reference key(s) | Inspected support and limitation | Manuscript location |
|---|---|---|---|---|
| L001 | XPoSat carries POLIX and XSPECT; POLIX operates broadly in 8–30 keV. | `isro_xposat` | Official ISRO mission page inspected 2026-08-03. It does not support project results. | I; II-A |
| L002 | POLIX uses a Thomson-scattering geometry with a low-Z scatterer and proportional counters. | `rishin2010thomson`; `fabiani2018instrumentation` | Primary instrument-development paper and peer-reviewed instrumentation review. Neither validates the project feature engineering. | I; II-A |
| L003 | Calibrated polarization interpretation requires response/modulation/background/reference-frame treatment. | `fabiani2018instrumentation`; `kislat2015stokes` | Peer-reviewed sources support general polarimetry, not project-specific calibration. | I; II-A; VI-A |
| L004 | Official archive context and observation access are provided by ISSDC. | `issdc_xposat_archive` | Authoritative archive landing page inspected 2026-08-03; local files control actual sample membership. | I |
| L005 | Astronomical anomaly methods can rank unusual objects for expert inspection without establishing cause. | `baron2017weirdest`; `giles2019serendipity`; `lochner2021astronomaly` | Peer-reviewed astronomy studies; different data domains and not quantitative baselines for this paper. | II-B |
| L006 | Explainable anomaly detection includes multiple explanation settings distinct from the detector. | `li2024explainable_anomaly` | Peer-reviewed survey; used for taxonomy, not a priority claim. | II-C |
| L007 | SHAP is a general Shapley-based post-hoc framework but was not deployed here. | `lundberg2017shap` | Primary method paper; conceptual comparison only. | II-C; IX |
| L008 | Perturbation can test whether explanations track model behaviour under an intervention. | `yeh2019infidelity` | Primary explanation-evaluation paper; the project does not reproduce its metric or guarantees. | II-C; V-D |
| L009 | Evaluation of unsupervised outlier detection is difficult without labels and depends on procedure choices. | `campos2016evaluation` | Peer-reviewed evaluation study; does not validate the present archive. | II-D |
| L010 | PCA, KMeans, Isolation Forest, and scikit-learn implementation context. | `pearson1901pca`; `macqueen1967kmeans`; `liu2008isolation`; `pedregosa2011sklearn` | Primary methods/software sources; project parameters are controlled by code and PKL. | V-A; V-B |
| L011 | Current data-use guidance requires the exact acknowledgment and names XPoSat and payload in the abstract. | `issdc_xposat_ack` | Official ISSDC page inspected 2026-08-03. Citation is placed outside the prescribed sentence. | Abstract; Acknowledgment |

## Phase-5 ledger status

- Numerical claims mapped: 27
- Literature/context claim groups mapped: 11
- Handbook claims or references: 0
- Unsupported novelty or superiority claims: 0
- Claims requiring guide/domain review before submission: feature semantics, empirical blank-sky interpretation, author order, venue/page limit, and final figure selection
