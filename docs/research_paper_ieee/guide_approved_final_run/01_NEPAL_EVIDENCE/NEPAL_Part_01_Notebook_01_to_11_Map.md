# NEPAL Part 01 - Notebook 01 to 11 Map

**Inspection mode:** static, targeted and read-only. No notebook was executed. Image payloads were not ingested.  
**Cell convention:** where useful, both the one-based displayed position and zero-based JSON cell index are stated.

## Notebook 01 - WeightedRoll exploration

**Path:** `D:\ISROtrial\Polix_L2_full_archive\01_WeightedRoll_Exploration.ipynb`

- JSON cells 2–12 inspect one 360-bin `WeightedRoll_L2.fits` curve and compute descriptive summaries.
- The example table contains `ROLL_AZ_ANG`, `TOTAL_COUNTRATE` and `ERROR`.
- The notebook records the project decision to keep WeightedRoll in a diagnostic branch rather than the primary ML representation.
- No result CSV is saved.

**Boundary:** product-processing explanations in narrative text are not treated as established facts unless code or another permitted primary source supports them.

## Notebook 02 - Primary product inspection

**Path:** `D:\ISROtrial\Polix_L2_full_archive\02_Primary_POLIX_Products_Inspection.ipynb`

- Source-azimuth example: 360 roll rows with a 48-element `ANODE_COUNTS` vector.
- Exposure example: 360 rows and four detector-exposure columns.
- Energy-resolved example: Astropy array shape `(360, 8192, 48)`, interpreted operationally as roll, PHA-channel and anode axes.
- A simple anode-sum divided by exposure resembles but does not exactly reproduce WeightedRoll.
- The proposed physical causes of this mismatch are not demonstrated and will not be repeated as evidence.

## Notebook 03 - Historical V1 feature table

**Path:** `D:\ISROtrial\Polix_L2_full_archive\03_Observation_Feature_Table.ipynb`

- Finds 25 observation directories.
- Confirms the inspected core polarization products for all 25.
- Displayed cell 9 saves `polix_observation_features_v1.csv`.
- V1 contains 14 numeric features and uses WeightedRoll directly.
- Zero missing values were reported in the V1 table.

**Status:** superseded development stage; not Matrix C.

## Notebook 04 - Historical V1 exploratory analysis

**Path:** `D:\ISROtrial\Polix_L2_full_archive\04_Exploratory_Data_Analysis.ipynb`

- Loads the 25-row V1 feature table.
- Applies `StandardScaler` without an imputer.
- Performs descriptive distribution and correlation inspection.

**Status:** superseded development stage.

## Notebook 05 - Historical V1 PCA

**Path:** `D:\ISROtrial\Polix_L2_full_archive\05_PCA_and_Structure_Discovery.ipynb`

- Applies PCA to the standardized V1 table.
- Displayed cells 12–13 save `polix_pca_coordinates.csv` and `polix_pca_loadings.csv`.

**Status:** superseded; its V1 explained-variance values are not deployed Matrix-C values.

## Notebook 06 - Historical V1 unsupervised analysis

**Path:** `D:\ISROtrial\Polix_L2_full_archive\06_Unsupervised_Analysis.ipynb`

- Uses KMeans with `k=4`, `n_init=10`, DBSCAN and Isolation Forest contamination 0.15.
- Displayed cell 8 saves `polix_unsupervised_results.csv`.
- Its four V1 Isolation Forest flags differ from the deployed Matrix-C result.

**Status:** superseded; neither parameters nor candidates control the paper.

## Notebook 07 - Historical V1 interpretation

**Path:** `D:\ISROtrial\Polix_L2_full_archive\07_Result_Interpretation_and_Visualization.ipynb`

- Saves `polix_consistent_anomalies.csv` and `final_polix_summary.csv`.
- Textual PCA/KMeans/DBSCAN/Isolation statuses are hard-coded for the V1 flags.

**Status:** historical only. “Consistent anomalies” is not ground truth or the deployed result.

## Notebook 08 - V2 product-tier engineering

**Path:** `D:\ISROtrial\Polix_L2_full_archive\08_Feature_Set_V2_Product_Tier_Engineering.ipynb`

- JSON cell 0 identifies 25 observations.
- JSON cell 1 contains an initial source-azimuth glob that can match EnergyRes.
- JSON cell 2 corrects the search through an explicit `EnergyRes` exclusion; the final extractor uses this corrected function.
- JSON cells 3–6 inspect products, define helper computations and extract 51 candidate features for all 25 observations with zero failures.
- JSON cell 7 saves the all-tier and tier-specific intermediate CSVs.
- JSON cell 8 audits the candidate features and reports zero missing values.
- Displayed position 10 / JSON index 9 removes constants or redundant fields, defines Matrix A/B/C and the separate WR matrix, then saves them.

### Final Matrix-C features

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

## Notebook 09 - V2 matrix audit and exploratory consensus

**Path:** `D:\ISROtrial\Polix_L2_full_archive\09_V2_Matrix_Audit_and_Unsupervised_Analysis.ipynb`

- Displayed position 2 / JSON index 1 compares A/B/C/WR with standardized PCA, KMeans and Isolation Forest.
- Its Matrix-C Isolation Forest ranking agrees with the later frozen deployed four.
- JSON indices 2–4 construct an exploratory cross-matrix/method consensus, include WR, select six cases and initially use absolute standardized deviations as feature evidence.
- Later cells save matrix summaries, consensus tables, exploratory drivers, loadings and branch-aware files.

**Boundary:** the six-case consensus is not the fixed label rule and its absolute-z drivers are not the deployed four-component XAI method.

## Notebook 10 - Unsupervised XAI and saved model

**Path:** `D:\ISROtrial\Polix_L2_full_archive\10_Unsupervised_XAI_Model_Explanations.ipynb`

- Displayed position 2 defines max-absolute component normalization and KMeans `k` selection over 2–5.
- Displayed positions 3–5 save all-feature, top-feature and six-case explanation tables.
- Displayed position 6 jointly neutralizes the top three standardized features for each exploratory case and saves the perturbation values.
- Displayed position 7 assigns the project-defined verdict categories.
- Displayed position 8 saves the final Matrix-C model package.

**Controlling correction:** the current versioned service audit controls Sco X-1. Its order is peak channel, weighted mean channel and channel entropy. The historical entropy-first narrative is superseded.

## Notebook 11 - Independent harmonic diagnostic

**Path:** `D:\ISROtrial\Polix_L2_full_archive\11_POLIX_Polarization_Parameter_Analysis.ipynb`

- Displayed position 7 fits `C + Q cos(2phi) + U sin(2phi)` by weighted least squares.
- Displayed position 8 fits all 25 observations and saves `polix_weightedroll_raw_modulation_fits.csv`.
- Displayed positions 12–13 construct and merge the project observation-role table.
- Displayed position 14 constructs the all-blank and 13-acceptable-fit blank-sky summaries and the ten-source scalar comparison.
- Displayed position 15 creates fractional harmonic coordinates and the project’s diagonal standardized-distance diagnostic.
- Displayed position 17 creates a historical source-only table containing unsafe PD/PA candidate labels; these labels are excluded.
- Displayed position 21 creates assumed-modulation-factor sensitivity proxies; these are supplementary at most.
- Displayed position 22 saves the later deployment configuration.

**Uncertainty control:** the saved Notebook-11 CSV controls project uncertainty values. The later Flask service uses a different full-gradient propagation and must not be described as numerically identical.

## Controlling notebook conclusion

- Notebooks 01–07 document development history.
- Notebook 08 controls final feature and matrix construction.
- Notebook 09 controls matrix-comparison lineage but not the deployed XAI label.
- Notebook 10 controls the saved model and six-case explanation experiment, subject to the accepted versioned service audit.
- Notebook 11 controls the frozen harmonic-result CSVs, subject to the uncertainty provenance disclosure.

