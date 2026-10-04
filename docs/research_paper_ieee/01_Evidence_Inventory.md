# Evidence Inventory

## Freeze definition

- Freeze date: **2026-07-27**
- Scope: **25 POLIX Level-2 observations included in the project archive**
- Source observations: **10**
- Blank-sky observations: **15**
- Source targets represented: Crab (3 observations), Sco X-1, Her X-1, GX 301-2, Cyg X-1, 4U 1700-37, Cen X-3, and Cas-A SNR
- Observation-level roles and target names: `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\04_polarimetry_results\path2_final_polarization_xai_result_table_with_roles.csv`
- File-level SHA-256 inventory: `supplementary_experiments/evidence_file_hashes.csv`

## Primary source hierarchy

1. Numerical result CSV or saved model artifact.
2. Notebook or deployed code that generated/interprets the result.
3. Reviewed report for narrative context.
4. Superseded report only if a fact is unavailable elsewhere; no paper value currently relies on it.

## Dataset composition

| Role | Observation count | Target labels |
|---|---:|---|
| Source | 10 | Crab; Sco X-1; Her X-1; GX 301-2; Cyg X-1; 4U 1700-37; Cen X-3; Cas-A SNR |
| Blank sky | 15 | Blank Sky-1 through Blank Sky-15 labels in project metadata; “Blank Sky-2” is used for two observation IDs |
| Total | 25 | 22 target/role labels including source and blank-sky labels |

The repeated “Blank Sky-2” display label should be reviewed by the project guide; the observation IDs remain unique.

## Feature matrices

| Matrix | Exact path | Rows | Deployed/diagnostic features | Missing values | Role |
|---|---|---:|---:|---:|---|
| A | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\02_feature_engineering\polix_matrix_v2_A_primary_final_chain.csv` | 25 | 8 | 0 | Exposure + energy-resolution chain |
| B | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\02_feature_engineering\polix_matrix_v2_B_primary_plus_source_diag.csv` | 25 | 11 | 0 | Matrix A + source azimuth |
| C | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\02_feature_engineering\polix_matrix_v2_C_primary_plus_supporting.csv` | 25 | 15 | 0 | Final deployed representation |
| WR | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\02_feature_engineering\polix_matrix_v2_WR_weightedroll_diagnostic.csv` | 25 | 6 | 0 | Separate WeightedRoll diagnostic |

## Exact Matrix-C feature set

1. `t1A_exp_uniformity_cv`
2. `t1A_exp_max_to_min_roll`
3. `t1A_energy_peak_channel`
4. `t1A_energy_weighted_mean_channel`
5. `t1A_energy_weighted_std_channel`
6. `t1A_energy_high_channel_fraction`
7. `t1A_energy_channel_entropy`
8. `t1A_energy_anode_balance_cv`
9. `t1B_src_peak_to_median_roll`
10. `t1B_src_roll_entropy`
11. `t1B_src_roll_smoothness_norm`
12. `t2_lc_rate_cv`
13. `t2_lc_peak_to_median_rate`
14. `t2_det_lc_rate_balance_cv`
15. `t2_det_pha_centroid_spread`

The deployed model artifact contains the same ordered list.

## Model and software

- Model artifact: `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\03_ml_xai_results\polix_v2_matrixC_unsupervised_xai_model.pkl`
- Web deployment copy: `D:\polix_xai_webapp\model\polix_v2_matrixC_unsupervised_xai_model.pkl`
- Components: `StandardScaler`, two-component PCA, KMeans with \(k=5\), and Isolation Forest.
- Isolation Forest: 100 trees, contamination 0.16, random state 42.
- KMeans: \(k=5\), `n_init=20`, random state 42.
- PCA: two components, random state 42.
- Current audit environment: Python 3.11.0; NumPy 2.4.6; pandas 3.0.3; scikit-learn 1.9.0; SciPy 1.17.1; Astropy 8.0.1; Flask 3.1.3.
- Machine-readable versions: `supplementary_experiments/software_versions.csv`.
- The original development environment was not independently reconstructed from a lockfile. `requirements.txt` is unpinned.

## Numerical evidence map

| Claim | Exact value | Primary evidence file | Notebook/code source | Verification status |
|---|---|---|---|---|
| Archive size | 25 observations | Matrix-C CSV; role table | Notebooks 08–11; `feature_extractor.py` | VERIFIED |
| Composition | 10 source; 15 blank sky | `path2_final_polarization_xai_result_table_with_roles.csv` | Notebook 11; `observation_metadata.json` | VERIFIED |
| Matrix-C size | 25 × 15 features plus ID | Matrix-C CSV | Notebook 08 | VERIFIED |
| Deployed predictions | 21 Normal; 4 Anomaly | Saved model arrays; `deployed_model_reproduction.csv` | Notebook 10; `model_service.py` | REPRODUCED |
| Four deployed candidates | C24_0010, C24_0018, G01_0003, G01_0006 | Saved model; `deployed_model_reproduction.csv` | Notebook 10; `model_service.py` | REPRODUCED |
| Exploratory candidates | 6 rows in faithfulness test | `v2_unsupervised_xai_faithfulness_verdict.csv` | Notebook 10 | VERIFIED; distinct from deployed result |
| Top deployed Her X-1 driver | `t2_lc_rate_cv` | `deployed_xai_reproduction.csv` | `model_service.py` | REPRODUCED |
| Sco X-1 deployed XAI rank 1 | `t1A_energy_peak_channel`; 2.454499 | `deployed_xai_exact_from_model_service.csv`; `XAI_Version_Mismatch_Audit.md` | Exact imported `model_service.py::explain_one` | ACCEPTED VERSIONED RESULT |
| Sco X-1 deployed XAI rank 2 | `t1A_energy_weighted_mean_channel`; 2.207369 | `deployed_xai_exact_from_model_service.csv`; Notebook-10 contribution CSV | Exact imported `model_service.py::explain_one` | ACCEPTED VERSIONED RESULT |
| Sco X-1 deployed XAI rank 3 | `t1A_energy_channel_entropy`; 1.813968 | `deployed_xai_exact_from_model_service.csv`; Notebook-10 contribution CSV | Exact imported `model_service.py::explain_one` | ACCEPTED VERSIONED RESULT |
| Historical Sco X-1 entropy-first narrative | Not reproducible from any located versioned artifact; excluded from Draft 1 | `XAI_Version_Mismatch_Audit.md`; `POLIX_XAI_Final_Report_Errata.md` | Git/model/code/hash audit | SUPERSEDED |
| Top deployed Blank Sky-13 driver | `t1A_energy_weighted_std_channel` | `deployed_xai_reproduction.csv` | `model_service.py` | REPRODUCED |
| Top deployed Blank Sky-5 driver | `t1B_src_roll_smoothness_norm` | `deployed_xai_reproduction.csv` | `model_service.py` | REPRODUCED |
| Faithfulness verdicts | 5 Strong; 1 Moderate; 0 Weak | Original verdict CSV; reproduction CSV | Notebook 10 | REPRODUCED |
| WeightedRoll fits | 25/25 | `polix_weightedroll_raw_modulation_fits.csv` | Notebook 11; `polarization_service.py` | VERIFIED |
| All-observation fit quality | 19 acceptable; 3 caution; 3 poor | Role table joined to fit CSV | Notebook 11; `polarization_service.py` | VERIFIED |
| Blank-sky fits | 15 analyzed | Role table; fit CSV | Notebook 11 | VERIFIED |
| Empirical Q/U baseline | 13 `acceptable` blank-sky fits | `path2_all_observations_fractional_qu_vectors.csv`; config | Notebook 11; `polarimetry_config.json` | VERIFIED |
| Baseline selection rule | `fit_quality == acceptable`, i.e. reduced chi-square ≤ 2.0 | Role/vector CSV and fit-quality code | `polarization_service.py` | VERIFIED; corrects report text |
| Blank-sky raw modulation | mean 1.147820%; sample SD 0.565960% | `path2_blank_sky_modulation_baseline.csv` | Notebook 11 | VERIFIED |
| Blank-sky mean normalized Q/U | \(Q/C=0.0090920\); \(U/C=-0.0064782\) | fractional Q/U CSV; config | Notebook 11 | VERIFIED |
| Blank-sky Q/U sample scatter | 0.0048569; 0.0040190 | fractional Q/U CSV; config | Notebook 11 | VERIFIED |
| Source scalar comparison | all 10 within blank-sky baseline range | `path2_source_vs_blank_sky_modulation_comparison.csv` | Notebook 11 | VERIFIED |
| Highest source raw modulation | Crab P01_0005: 1.697346 ± 0.031042% | source comparison CSV | Notebook 11 | VERIFIED |
| Her X-1 physical diagnostic | 0.596632 ± 0.016717%; reduced chi-square 57.4335; vector distance 2.3174 | source-only candidate CSV | Notebook 11 | VERIFIED; poor fit |
| Sco X-1 physical diagnostic | 1.139578 ± 0.019877%; reduced chi-square 2.0308; vector distance 0.3005 | source-only candidate CSV | Notebook 11 | VERIFIED; caution fit |
| No calibrated PD/PA output | No official PD or PA claimed | calibration-audit CSVs; config | Notebook 11; `polarization_service.py` | VERIFIED |
| Seed stability | three candidates 100/100; Blank Sky-5 29/100 | `isolation_seed_stability_summary.csv` | `robustness_audit.py` | NEW, EXECUTED |
| Jackknife rank stability | median Spearman 0.9896; minimum 0.9687 | `jackknife_run_summary.csv` | `robustness_audit.py` | NEW, EXECUTED |

## Result files

### ML and XAI

- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\03_ml_xai_results\v2_matrix_analysis_summary.csv`
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\03_ml_xai_results\v2_consensus_anomaly_table.csv`
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\03_ml_xai_results\v2_final_primary_unsupervised_xai_explanations.csv`
- `D:\ISROtrial\Polix_L2_full_archive\v2_unsupervised_xai_top_feature_contributions.csv`
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\03_ml_xai_results\v2_unsupervised_xai_faithfulness_test.csv`
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\03_ml_xai_results\v2_unsupervised_xai_faithfulness_verdict.csv`

### Physical and blank-sky diagnostics

- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\04_polarimetry_results\polix_weightedroll_raw_modulation_fits.csv`
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\04_polarimetry_results\path2_blank_sky_modulation_baseline.csv`
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\04_polarimetry_results\path2_all_observations_fractional_qu_vectors.csv`
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\04_polarimetry_results\path2_source_vs_blank_sky_modulation_comparison.csv`
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\04_polarimetry_results\path2_source_background_relative_modulation_vector_proxy.csv`
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\04_polarimetry_results\path2_final_source_only_pd_pa_candidate_table.csv`
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\04_polarimetry_results\path2_pd_pa_calibration_candidate_files.csv`
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\04_polarimetry_results\path2_pd_pa_calibration_fits_header_matches.csv`
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\04_polarimetry_results\path2_pd_pa_calibration_text_matches.csv`
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\04_polarimetry_results\path2_pd_proxy_sensitivity_table.csv`

## Code and notebooks

- Notebooks 01–11: `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\01_notebooks`
- Web app: `D:\polix_xai_webapp\app.py`
- Feature extraction: `D:\polix_xai_webapp\feature_extractor.py`
- Model/XAI: `D:\polix_xai_webapp\model_service.py`
- Physical branch: `D:\polix_xai_webapp\polarization_service.py`
- Export: `D:\polix_xai_webapp\result_exporter.py`
- Visualization: `D:\polix_xai_webapp\visualization_service.py`
- Metadata/configuration: `D:\polix_xai_webapp\config`

## Official documentation

- Reviewed report: `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\07_documentation\POLIX_XAI_Final_Report_Reviewed.md`
- Official handbook: `C:\Users\Saatvik\Downloads\POLIX_User_Handbook.pdf`
- Handbook title/version visually verified: *XPoSat-POLIX User Handbook: User Guide for Scientific Data Analysis Level2*, V1.0, October 2025.
- Handbook p. 26 states that WeightedRoll includes source and background count-rate modulation.
- Handbook p. 57 states that polarization measurement is not possible with the currently released source/blank-sky configuration and describes a newer nearby-blank-sky strategy for future releases.

## Pending or unverified

- Original package versions used when the model was first trained; only the current audit environment is frozen.
- Independent future-release performance and data-drift behavior.
- Official flight-calibrated \(\mu_{100}\) for the relevant conditions.
- Mission-approved phase-to-sky-PA conversion.
- Official source-specific background subtraction for these releases.
- Domain-expert confirmation of any anomaly candidate.
- Browser-level verification of the downloadable result CSV.
- Exact venue page count and final figure resolution.
