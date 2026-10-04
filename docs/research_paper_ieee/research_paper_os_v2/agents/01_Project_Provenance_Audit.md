# Agent 1 — Project Provenance Audit

**Audit date:** 2026-07-27  
**Role:** Project Provenance Auditor  
**Scope:** Read-only inspection of `D:\polix_xai_webapp`, `D:\ISROtrial\Polix_L2_full_archive`, and `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs`  
**Manuscript status:** IEEE Draft 1 was not edited. No project notebook, source file, model, result, figure, report, or dataset was modified. No experiment was run.

## 1. Audit verdict

The project has a traceable frozen analysis chain, but it is distributed across three locations:

1. the raw and extracted Level-2 archive in `D:\ISROtrial\Polix_L2_full_archive`;
2. the organized but incomplete convenience copy in `final_project_outputs`;
3. the Git-versioned deployed implementation in `D:\polix_xai_webapp`, plus later paper-specific audit outputs in `research_paper_ieee\supplementary_experiments`.

The strongest numerical claims can be tied to CSVs and a saved model. The organized output folder is not itself a version-control system and must not be treated as the sole source of truth. Forty-four root-level archive files have same-named copies under `final_project_outputs`; every one of those 44 pairs is byte-identical. However, 22 archive-root result or intermediate files have no same-named copy in `final_project_outputs`, including the complete Notebook-10 feature-contribution tables and branch-aware exploratory outputs. The folders `06_website_screenshots` and `08_final_tables` are empty.

The deployable web application is in Git at commit `15628ee7cc434de9ba03caaae5dd115d8cd09f9a`. The repository has only one commit. Consequently, Git cannot reconstruct an earlier website implementation that might have produced the historical entropy-first Sco X-1 narrative.

## 2. Proposed controlling project-truth hierarchy

When two artifacts disagree, use this hierarchy within the type of claim being evaluated.

| Priority | Evidence class | Controlling use | Important condition |
|---:|---|---|---|
| 1 | Original immutable inputs | Establish which files were in the project archive | Use the 25 `.tgz` files in `data_raw` and their identifier-matched extracted folders; this does not establish that they were all publicly available POLIX observations. |
| 2 | Machine-readable result CSV plus the exact generating notebook/code | Establish numerical results | The CSV value controls over prose, provided the producing stage and candidate definition are identified. |
| 3 | Saved deployed model plus versioned deployed code | Establish the frozen website model and current local XAI function | Use the byte-identical PKL copies, Git commit, exact `model_service.py`, and Matrix-C row in a compatible environment. |
| 4 | Versioned supplementary script plus its CSV/JSON output | Establish later robustness or version-audit results | These are paper-stage evidence, not original project outputs. Preserve script, environment record, inputs, and hashes together. |
| 5 | Official POLIX documentation | Establish product meaning and scientific interpretation boundaries | Product semantics are a domain claim, not inferable from filenames alone. Agent 2 should control that assessment. |
| 6 | Reviewed report plus additive errata/audits | Explain project intent and narrative | Prose is secondary evidence. The errata and XAI version audit supersede conflicting report sentences without overwriting the reviewed report. |
| 7 | Manuscript, slides, screenshots, summaries, and generated figures | Communication only | Never use these as the sole source for a number or algorithmic claim. |

This hierarchy does not mean that a derived CSV is intrinsically “truer” than raw data. It means that a paper-level numerical claim must cite the exact derived artifact and its method, rather than being recopied from narrative prose.

## 3. Frozen archive and identity checks

### 3.1 Project archive

| Item | Verified value | Evidence |
|---|---:|---|
| Raw Level-2 archives | 25 `.tgz` files | `D:\ISROtrial\Polix_L2_full_archive\data_raw` |
| Total raw-archive bytes | 493,911,778 | Read-only file inventory |
| Raw manifest SHA-256 | `678DF50E6096FF31197130917FB4FEAD9B28888542904DC9BA3728731E45560F` | SHA-256 of the UTF-8 text formed by sorted `filename|byte_length|file_SHA256` lines |
| Extracted observation folders | 25 | `D:\ISROtrial\Polix_L2_full_archive\data_extracted` |
| Extracted files | 1,025 | Recursive read-only count |
| Matrix-C observation identifiers | 25 | `polix_matrix_v2_C_primary_plus_supporting.csv` |
| WeightedRoll-fit observation identifiers | 25 | `polix_weightedroll_raw_modulation_fits.csv` |
| Role-metadata observation identifiers | 25 | `path2_observation_role_metadata_filled.csv` |
| Identifier agreement | Exact 25-of-25 set agreement | Matrix C versus extracted folders, fit table, and role table |
| Project-role composition | 10 source; 15 blank sky | `path2_observation_role_metadata_filled.csv` and deployed `observation_metadata.json` |

The raw filenames and extracted directory names indicate Level-2 version `V1P1`/`V1p1`. The local archive does not contain a download manifest with source URLs, download timestamps, checksums issued by ISSDC, or a proof that the 25 files exhaust the public archive. Allowed wording is therefore **“25 POLIX Level-2 observations included in the project archive.”**

### 3.2 High-value artifact hashes

| Artifact | Absolute path | SHA-256 | Status |
|---|---|---|---|
| Matrix A | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\02_feature_engineering\polix_matrix_v2_A_primary_final_chain.csv` | `C9031C30B8BD05CED089ED7B863B4BB9E189BC04F17075BD99CAB0F8B05ED6C4` | Current matrix-comparison evidence |
| Matrix B | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\02_feature_engineering\polix_matrix_v2_B_primary_plus_source_diag.csv` | `21411E20D55C94704E6E26FC87A3570CBD9B3A8CECF8E2930FE9954DB5F723C8` | Current matrix-comparison evidence |
| Matrix C | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\02_feature_engineering\polix_matrix_v2_C_primary_plus_supporting.csv` | `3936E1B0AAF44ACFF39597BEFEC1B466A26511123655946F8829A4E6263DB0FA` | Deployed model input |
| Matrix WR | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\02_feature_engineering\polix_matrix_v2_WR_weightedroll_diagnostic.csv` | `B8A49EE9FB205C607B160CAB19DFFCEBFC187DD256757421C590AF3987B811DB` | Separate diagnostic matrix |
| Deployed model PKL | `D:\polix_xai_webapp\model\polix_v2_matrixC_unsupervised_xai_model.pkl` | `D8EFD73C9744ED1CA1098A4599DA91ACDEDC250BB2B6639728364AEF6B8C180D` | Current deployed artifact |
| Notebook 08 | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\01_notebooks\08_Feature_Set_V2_Product_Tier_Engineering.ipynb` | `D83C1ADE91B3B61E9783B275692A5965B85D7874342C7BDD2E4645450956190F` | Matrix-generation source |
| Notebook 09 | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\01_notebooks\09_V2_Matrix_Audit_and_Unsupervised_Analysis.ipynb` | `57FE81B243A55FB78C349543946FE01485F9406AF2F6B7EA6AB585C92EC93F1D` | Matrix comparison and exploratory consensus source |
| Notebook 10 | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\01_notebooks\10_Unsupervised_XAI_Model_Explanations.ipynb` | `0F93867D8A565ABCFD7D880D10059ED11C180A850ED19A8593A2CC9926448304` | XAI, faithfulness, and model-save source |
| Notebook 11 | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\01_notebooks\11_POLIX_Polarization_Parameter_Analysis.ipynb` | `90D7AE3DC2DADD28924FC9BBDF5AFC302C9B5022C6DA6FEB87D1EF78B2657086` | Physical-diagnostic source |
| Deployed XAI code | `D:\polix_xai_webapp\model_service.py` | `F749FFD0E79A951F42555F5083D2056567DE9CCAAF721772601EA0A79856C877` | Current Git-versioned function |
| Deployed feature extractor | `D:\polix_xai_webapp\feature_extractor.py` | `45A9AE59E9822528C1E6D64AC107A121BB7291D7C352BF744E6FC9D06F0569CB` | Current Git-versioned extractor |
| Physical diagnostic code | `D:\polix_xai_webapp\polarization_service.py` | `9F93886080C9D6378C670D6365C17A12FE4DDDAECAE145EEFED34A6718C5D738` | Current Git-versioned implementation |
| Physical config | `D:\polix_xai_webapp\config\polarimetry_config.json` | `DB0A644AAC6EB52EA20DF3856FFC707586AF1246FFA3BA9F7E532E7E50A4D6C5` | Byte-identical to the archive deployment config |
| Reviewed report | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\07_documentation\POLIX_XAI_Final_Report_Reviewed.md` | `5D37B4A43901C86C697F83E31F138384CE320470ECB6BE2E887861E3A2C3229F` | Best narrative description, not primary numerical evidence |
| Superseded report | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\07_documentation\POLIX_XAI_Final_Report.md` | `C981A259BF39036465CDBD0701C2712B4981ACBA0540EC631D7077BD859BF513` | Historical; do not cite when reviewed report exists |

All 11 root notebooks and their copies under `final_project_outputs\01_notebooks` are byte-identical. The model PKL at the archive root, in `final_project_outputs`, and in the web application is also byte-identical.

## 4. Result-to-source provenance map

| Result or claim | Controlling machine-readable evidence | Generating or consuming source | Verification |
|---|---|---|---|
| Product-tier feature tables and matrices A/B/C/WR | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\02_feature_engineering\*.csv` | Notebook 08, especially its saved-output cells; deployed Matrix-C extraction is in `D:\polix_xai_webapp\feature_extractor.py` | CSV shapes and hashes verified; exact all-observation equality between Notebook-08 extraction and the deployed upload extractor was not re-tested |
| Matrix comparison, PCA variance, selected K, and multi-matrix flags | `v2_matrix_analysis_summary.csv`, `v2_consensus_anomaly_table.csv` | Notebook 09 | Verified as the exploratory multi-matrix analysis stage |
| Six observations selected for detailed XAI | `v2_compact_anomaly_explanations.csv` and `v2_final_primary_unsupervised_xai_explanations.csv` | Notebook 09 defines `selected_anomalies = total_flags >= 3`; Notebook 10 consumes that list | Verified; this is not the final deployed candidate definition |
| Saved Matrix-C model | PKL with hash above | Notebook 10, model-save cell | Model contents verified read-only: 15 features, StandardScaler, two-component PCA, five-cluster KMeans, Isolation Forest |
| Fixed deployed predictions | PKL plus `deployed_model_reproduction.csv` | `D:\polix_xai_webapp\model_service.py`; supplementary `robustness_audit.py` | Verified as 21 Normal and 4 Anomaly labels |
| Current local explanations | `deployed_xai_exact_from_model_service.csv` | Exact imported `PolixXAIPredictor.explain_one`; audit script `xai_version_audit.py` | Verified for current versioned function; historical entropy-first website artifact not found |
| Six-case XAI faithfulness | `v2_unsupervised_xai_faithfulness_test.csv` and `v2_unsupervised_xai_faithfulness_verdict.csv` | Notebook 10 | Verified: five Strong, one Moderate, zero Weak; applies to the six exploratory cases |
| Raw WeightedRoll fits | `polix_weightedroll_raw_modulation_fits.csv` | Notebook 11; deployed analogue in `polarization_service.py` | 25 rows verified; use as raw physical-diagnostic evidence |
| Blank-sky scalar baseline | `path2_blank_sky_modulation_baseline.csv` | Notebook 11 | Verified: both an all-15 row and an acceptable-13 row exist |
| Blank-sky normalized Q/U baseline | `path2_all_observations_fractional_qu_vectors.csv` and config | Notebook 11; deployed config | The config records 13 acceptable fits and Q/U means; domain interpretation remains Agent-2 scope |
| Source versus blank-sky results | `path2_source_vs_blank_sky_modulation_comparison.csv` | Notebook 11 | Ten source rows verified |
| PD sensitivity proxies | `path2_pd_proxy_sensitivity_table.csv` and `path2_polarimetry_deployment_config.json` | Notebook 11 and `polarization_service.py` | Sensitivity assumptions only; not calibrated PD |
| Figures | `final_project_outputs\05_figures` | Notebook 09 or 11 | Secondary visual derivatives; paper numbers must come from CSVs |

## 5. Verified current results and their boundaries

### 5.1 Dataset and Matrix C

- Matrix C has 25 rows and 16 columns: one `observation_id` plus exactly 15 deployed features.
- A direct blank-cell audit found zero missing cells in Matrix C.
- `model_service.py` validates column presence and passes the 15 features directly to the saved `StandardScaler`. It does not execute an imputer.
- The saved PKL contains no imputer.
- These facts support “no missing values in the frozen Matrix-C run.” They do not define a safe missing-value policy for future uploads.

### 5.2 Fixed deployed model

The saved Isolation Forest has `contamination=0.16`, `random_state=42`, `n_estimators=100`, and returns four anomaly labels:

| Observation | Project label | Fixed anomaly score | Current status |
|---|---|---:|---|
| `X01_PLX_C24_0018_000000` | Blank Sky-13 | 0.615963875 | Anomaly candidate |
| `X01_PLX_G01_0006_000000` | Sco X-1 | 0.593516133 | Anomaly candidate |
| `X01_PLX_G01_0003_000000` | Her X-1 | 0.572308197 | Anomaly candidate |
| `X01_PLX_C24_0010_000000` | Blank Sky-5 | 0.517611306 | Anomaly candidate |

Evidence: PKL training arrays and `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\deployed_model_reproduction.csv` (SHA-256 `3E6B88BC77917C07DB7BEF8021B7E3B10741314657A12E654F919D1B2923BAD1`). The reproduction records a zero maximum score difference.

The KMeans choice stored in the PKL is `k=5` with silhouette score `0.3109359358759356`. PCA has two components. KMeans, PCA, and Isolation Forest are complementary elements of one pipeline; they are not “four models.”

### 5.3 Exploratory six-case set is separate

Notebook 09 aggregates PCA, Isolation Forest, and small-cluster flags across matrices A, B, C, and WR. It then selects six observations with `total_flags >= 3`:

`G01_0006`, `C24_0018`, `G01_0003`, `C24_0010`, `C24_0020`, and `C24_0023`.

This set is the input to Notebook 10’s detailed explanations and faithfulness evaluation. It includes two observations that are not fixed deployed Matrix-C Isolation Forest candidates. Because the exploratory consensus includes the WR diagnostic matrix, it must not be presented as the primary deployed anomaly input or used as circular confirmation of the independent physical branch.

### 5.4 Current Sco X-1 XAI result

The current versioned-function result is:

1. `t1A_energy_peak_channel` — `2.4544990315347768`;
2. `t1A_energy_weighted_mean_channel` — `2.2073686584810000`;
3. `t1A_energy_channel_entropy` — `1.8139679863052869`.

This agrees with the original Notebook-10 Matrix-C contribution output and the current exact-function audit. The earlier entropy-first narrative is not reproducible from a located versioned artifact and is superseded for manuscript use. The controlling detailed audit is `D:\polix_xai_webapp\research_paper_ieee\XAI_Version_Mismatch_Audit.md`; its current hash is `4E210F6EA93AB8D613436BDDE4C02DF0034FE42E4371037BC5830C2FED24089C`.

This ranking supports only the statement that energy-distribution summary features dominate the current local explanation for Sco X-1. It does not establish a physical cause, detector fault, source state, or polarization.

### 5.5 Robustness evidence provenance

The robustness outputs dated 2026-07-27 are supplementary paper-stage evidence, not original notebook results. The 100-seed summary records:

- `C24_0018`, `G01_0006`, and `G01_0003`: flagged in 100 of 100 seeds;
- `C24_0010` (Blank Sky-5): flagged in 29 of 100 seeds;
- `C24_0020`: flagged in 68 of 100 seeds despite not being in the fixed four;
- `P01_0005`: flagged in 3 of 100 seeds.

Controlling file: `isolation_seed_stability_summary.csv`, SHA-256 `5125A5D60491FF8DA656CFC83A4D995BC380E737A0D65290FE2730C3B4654DF2`. These counts should be stated as stability under the recorded seed experiment, not as candidate probabilities.

### 5.6 Physical branch

The WeightedRoll fit table has 25 rows and no failed-fit row; the failure CSV is a one-byte empty CSV. The blank-sky baseline CSV contains:

- 15 blank-sky observations in the all-blank-sky summary;
- 13 observations in `acceptable_blank_sky_only`;
- for the acceptable subset, mean raw modulation `1.147820338848039%` and sample standard deviation `0.565959672908476%`.

The 13 qualifying observations are exactly the blank-sky rows labelled `acceptable`, with reduced \(\chi^2 \le 2.0\). The two excluded rows are Blank Sky-13 (`caution`, reduced \(\chi^2=2.565811346028652\)) and Blank Sky-6 (`poor_simple_sinusoid_fit`, reduced \(\chi^2=6.920303782270831\)).

These are empirical project diagnostics. The fit table’s phase is a fitted modulation phase, not official sky polarization angle. The μ100 values in the deployment config are sensitivity scenarios, not an official calibration. The file named `path2_final_source_only_pd_pa_candidate_table.csv` is an earlier interpretive candidate table with potentially misleading filename and wording; it must not be used to support calibrated PD or official PA claims.

## 6. Current, exploratory, historical, and superseded artifacts

| Classification | Artifacts | Permitted use |
|---|---|---|
| Current primary numerical evidence | Final Matrix A/B/C/WR CSVs; PKL; raw fit CSV; accepted blank-sky baseline CSV; fractional Q/U CSV; source-versus-blank CSV; PD proxy sensitivity CSV | Paper numbers, with method and boundaries stated |
| Current deployed implementation | Git commit `15628ee...`; `feature_extractor.py`; `model_service.py`; `polarization_service.py`; configs; model | Describe website behavior and the frozen implementation |
| Current paper-stage audits | `supplementary_experiments` scripts and outputs; `XAI_Version_Mismatch_Audit.md`; report errata | Robustness, reproducibility, and discrepancy resolution |
| Exploratory V2 evidence | Multi-matrix consensus, branch-aware CSVs, six selected cases, six-case XAI/faithfulness | Clearly labelled exploratory analysis; never substitute for fixed deployed four |
| Historical V1 evidence | `polix_observation_features_v1.csv`, `polix_pca_coordinates.csv`, `polix_pca_loadings.csv`, `polix_unsupervised_results.csv`, `polix_consistent_anomalies.csv`, `final_polix_summary.csv`, Notebooks 01–07 | Project-development history only unless a claim explicitly concerns the exploratory stage |
| Historical physical-interpretation tables | `polarization_xai_comparison.csv`, `path2_final_polarization_xai_result_table.csv`, `path2_final_source_only_pd_pa_candidate_table.csv` | Trace development; do not use for official PD/PA claims |
| Superseded prose | `POLIX_XAI_Final_Report.md` | Do not use when the reviewed report exists |
| Reviewed prose with additive corrections | `POLIX_XAI_Final_Report_Reviewed.md`, `POLIX_XAI_Final_Report_Errata.md` | Project understanding; verify every number against CSV |

## 7. Conflicts, ambiguities, and provenance risks

### P1 — Six exploratory candidates versus four deployed candidates

**Status:** Resolved as two different analysis stages.  
**Evidence:** Notebook 09’s `total_flags >= 3` rule versus the PKL’s Matrix-C Isolation Forest labels.  
**Required wording:** “six exploratory multi-matrix cases” and “four fixed deployed anomaly candidates.” Do not merge the counts.

### P2 — Sco X-1 entropy-first historical narrative

**Status:** Current implementation resolved; historical provenance unresolved.  
**Evidence:** Current code, PKL, Matrix C, Notebook 10, and exact-function CSV agree on peak channel first. No historical website screenshot/export or earlier code version was located.  
**Control:** Use peak channel, weighted mean channel, then entropy. Preserve the mismatch audit and errata.

### P3 — Organized output folder is incomplete

**Status:** Verified packaging limitation.  
**Evidence:** 44 root/final same-name pairs are identical, but 22 archive-root results are absent by name from `final_project_outputs`. Notably, `v2_unsupervised_xai_all_feature_contributions.csv` and `v2_unsupervised_xai_top_feature_contributions.csv` remain at the archive root. `06_website_screenshots` and `08_final_tables` are empty.  
**Control:** Use absolute paths and hashes; do not infer absence merely because a file is missing from the organized copy.

### P4 — Python/scikit-learn environment dependency

**Status:** Verified reproducibility risk.  
**Evidence:** The PKL embeds scikit-learn `1.9.0`. The paper-stage `software_versions.csv` records Python `3.11.0`, NumPy `2.4.6`, pandas `3.0.3`, and scikit-learn `1.9.0`, using `D:\polix_xai_webapp\venv\Scripts\python.exe`. The system-default `python.exe` observed during this audit has scikit-learn `1.6.1` and emits `InconsistentVersionWarning` when loading the PKL. `requirements.txt` lists package names without pinned versions.  
**Control:** Reproduction instructions must identify the project virtual environment or pin a compatible environment. Do not claim environment-independent PKL portability.

### P5 — Source/blank-sky metadata is externally mapped

**Status:** Counts verified; naming provenance needs domain confirmation.  
**Evidence:** `path2_observation_role_metadata_filled.csv` labels every row `mapped_from_isro_archive_page`; the web-app JSON reproduces the same 10/15 classification. No captured archive-page snapshot or machine-readable download manifest was located. Both `C24_0001` and `C24_0008` are labelled `Blank Sky-2`, while no `Blank Sky-12` label appears.  
**Control:** Use proposal/observation identifiers as primary keys. Ask the guide/domain expert to confirm friendly labels before publication.

### P6 — Current web extractor versus frozen Notebook-08 matrix

**Status:** Unverified equivalence.  
**Evidence:** Matrix C was saved by Notebook 08. The deployed application uses `feature_extractor.py`. Both target the same 15 feature names, but no located frozen regression report proves that the deployed extractor reproduces every Notebook-08 Matrix-C value from the 25 archives.  
**Control:** For current paper numbers, treat the frozen Matrix-C CSV as the model input. Before a stronger end-to-end reproducibility claim, execute and record an extractor-to-matrix regression check in a later authorized phase.

### P7 — Git coverage is partial

**Status:** Verified.  
**Evidence:** The web application is tracked in a one-commit Git repository. The research-paper workspace is untracked, and the archive/notebooks/results are outside this repository.  
**Control:** Hashes and the evidence ledger are necessary; Git commit alone does not freeze the full research project.

### P8 — “Acceptable” fit threshold wording

**Status:** Resolved by code and CSV.  
**Evidence:** Notebook 11 and `polarization_service.py` classify reduced \(\chi^2 \le 2.0\) as acceptable, \(2.0 < \chi_\nu^2 \le 5.0\) as caution, and larger values as poor. The 13-row blank baseline uses only acceptable rows.  
**Control:** Do not state that the 13-row baseline used a threshold of 5.0.

## 8. Evidence versus interpretation

| Evidence established by artifacts | Interpretation that is not established |
|---|---|
| Four observations receive `-1` from the fixed saved Isolation Forest. | They are confirmed scientific anomalies. |
| Three of the fixed candidates are flagged for every one of 100 tested seeds; Blank Sky-5 is flagged for 29. | The frequencies are posterior probabilities or ground-truth confidence. |
| Sco X-1’s top current local XAI features are three energy-distribution summaries. | A particular source state, calibration error, detector effect, or physical cause produced the score. |
| Six exploratory cases have five Strong and one Moderate faithfulness verdict after feature neutralization. | The explanations are causally correct or validated by domain experts. |
| WeightedRoll curves were fitted with a second-harmonic model and compared with an empirical blank-sky baseline. | The released products provide official background subtraction, calibrated PD, or official sky PA. |
| Statistical anomaly labels and blank-sky-relative modulation diagnostics can disagree. | Either branch confirms or falsifies astrophysical polarization. |

## 9. Items still unverified or requiring approval

1. **Archive acquisition provenance:** exact official URLs, download date, release notice, and official checksums were not found locally.
2. **Observation friendly names:** confirm the duplicated `Blank Sky-2` label and the absence of `Blank Sky-12`.
3. **Feature semantic validity:** Agent 3 and a POLIX-aware reviewer must confirm product axes, units, physical meaning, and whether all 15 definitions are defensible.
4. **WeightedRoll interpretation:** Agent 2 and the guide must approve the language for source/background contributions, empirical blank-sky Q/U comparison, phase, and μ100 sensitivity proxies.
5. **End-to-end extractor reproducibility:** no all-25 deployed-extractor versus frozen-Matrix-C equality test was found.
6. **Environment packaging:** `requirements.txt` is unpinned; a later reproducibility phase should record an installable lock or environment file without changing the frozen model.
7. **Historical website output:** no screenshot/export or earlier code artifact supports entropy-first Sco X-1.
8. **Domain-expert confirmation:** none of the candidate labels, XAI interpretations, or physical diagnostic interpretations is recorded as approved by a POLIX domain expert.

## 10. Agent 1 disagreement register entries

| ID | Conflicting statements or artifacts | Agent 1 position | Resolution owner |
|---|---|---|---|
| A1-D01 | Six exploratory cases versus four deployed candidates | Both are valid only when labelled as separate stages; the deployed paper result is four | Orchestrator and guide |
| A1-D02 | Historical entropy-first Sco X-1 prose versus versioned peak-first artifacts | Versioned peak-first result controls the manuscript; historical cause remains unknown | Orchestrator |
| A1-D03 | `final_project_outputs` implied as complete versus 22 root-only result files | It is an organized subset, not a complete evidence store | Orchestrator |
| A1-D04 | `requirements.txt` suggests a generic environment versus PKL and audit requiring scikit-learn 1.9.0 | Reproduction must record the compatible environment explicitly | Reproducibility owner |
| A1-D05 | Two observation IDs both mapped to `Blank Sky-2` | Use IDs as primary keys and obtain domain confirmation before final tables | Guide/domain expert |
| A1-D06 | Early “PD/PA candidate” filename versus later explicit proxy/phase limitations | Later proxy config and claim boundaries control; the earlier filename is not evidence of calibration | Agent 2 and guide |

## 11. Provenance conclusion

The evidence supports a bounded, reproducible statement: the project processed 25 identifier-matched POLIX Level-2 observations in its local archive into frozen product-aware feature matrices; the saved Matrix-C model gives four anomaly candidates; detailed six-case explanation and faithfulness results belong to an earlier exploratory consensus stage; and WeightedRoll results form a separate empirical physical-diagnostic branch.

The evidence does not support claims of complete public-archive coverage, official anomaly ground truth, calibrated polarization degree, official sky polarization angle, official POLIX background subtraction, or a reconstructed historical website XAI version. Those boundaries should remain explicit in every later paper phase.
