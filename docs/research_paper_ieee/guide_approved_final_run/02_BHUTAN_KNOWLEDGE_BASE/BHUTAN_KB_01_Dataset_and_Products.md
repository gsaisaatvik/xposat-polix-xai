# BHUTAN Knowledge Card 01 — Dataset and Level-2 Product Families

## Beginner explanation

The project archive contains 25 POLIX Level-2 observation folders: 10 are mapped by the project as source observations and 15 as blank-sky observations. Each folder contains several products with different shapes and meanings. The study summarizes selected information from these products into one row per observation. The source/blank-sky mapping describes observational role; it is not anomaly ground truth.

## Technical theory

The implemented products are heterogeneous: a 360-row exposure-azimuth table; an energy-resolved source-azimuth array with operational shape `(360, 8192, 48)` for roll, PHA channel and anode; a 360-row source-azimuth product containing 48 anode counts per row; a delivered source light curve; four detector light curves; four detector PHA products; and a 360-bin WeightedRoll curve containing roll angle, total count rate and error. Feature engineering maps these arrays to a fixed observation vector while retaining the product family from which each summary was derived.

## Exact project implementation

- Matrix A: eight Tier-1A exposure and energy-resolved features.
- Matrix B: Matrix A plus three source-azimuth features, for 11 features.
- Matrix C: Matrix B plus four light-curve and detector-context features, for 15 features.
- WR matrix: six separate WeightedRoll summaries; it is not a fourth feature tier and is not an input to the deployed Matrix-C model.
- Matrix C has 25 rows, 15 numeric feature columns and zero missing values.
- The deployed path applies `StandardScaler` directly; no imputer is present.
- Full observation identifiers are the unique keys. `C24_0001` and `C24_0008` both have the friendly label `Blank Sky-2`; the supplied mapping is preserved without silent renumbering.
- Notebooks 03–07 describe a superseded 14-feature V1 representation that included WeightedRoll. Its parameters and candidates do not control the final study.

## Parameters and compact representation

\[
X_A\in\mathbb{R}^{25\times8},\qquad
X_B\in\mathbb{R}^{25\times11},\qquad
X_C\in\mathbb{R}^{25\times15}.
\]

For observation folder \(o_i\),

\[
o_i\mapsto [\text{exposure},\text{channel-space},\text{source-azimuth},
\text{light-curve},\text{detector-balance}]_i.
\]

WeightedRoll follows a separate mapping and does not enter \(X_C\).

## Controlling sources and cells

- `D:\ISROtrial\Polix_L2_full_archive\02_Primary_POLIX_Products_Inspection.ipynb`: primary product inspection and operational dimensions.
- `D:\ISROtrial\Polix_L2_full_archive\08_Feature_Set_V2_Product_Tier_Engineering.ipynb`: JSON indices 3–6 for corrected extraction, index 8 for the zero-missing audit, and index 9 for final A/B/C/WR definitions and saves.
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\02_feature_engineering\polix_matrix_v2_C_primary_plus_supporting.csv`: controlling Matrix-C values.
- `D:\polix_xai_webapp\feature_extractor.py`: deployed schema and `extract_matrix_c_features` implementation.
- `D:\polix_xai_webapp\research_paper_ieee\guide_approved_final_run\01_NEPAL_EVIDENCE\NEPAL_Part_03_All_25_Observation_Truth_Table.csv`: verified all-observation join and role mapping.

## Verified numerical results

- 25 observations: 10 project-labelled source and 15 project-labelled blank sky.
- Matrix A/B/C contain 8/11/15 features, respectively.
- Matrix C contains zero missing values.
- WeightedRoll is absent from Matrix C.
- The fixed saved-model output is 21 Normal observations and four anomaly candidates.

## Safe inference

The archive demonstrates that heterogeneous delivered products can be compressed into a traceable observation-level representation whose features retain product-family provenance.

## Unsupported inference

The paper must not imply that the 25 observations are all available POLIX data, that source/blank-sky roles are anomaly labels, that Matrix C is physically complete or calibrated, that Matrix C is universally superior, or that the archive supports population-level generalization.

## Paper-ready wording

> The study uses 25 POLIX Level-2 observations included in the project archive, comprising 10 project-labelled source observations and 15 project-labelled blank-sky observations. Heterogeneous exposure, energy-resolved azimuthal, source-azimuth, delivered-light-curve and detector products were summarized into a 15-feature observation-level Matrix-C representation. WeightedRoll was excluded from Matrix C and retained as an independent harmonic diagnostic. Matrix C contains no missing values, and the deployed processing path applies no imputation.

## Likely reviewer challenge and safe answer

**Question:** Why combine source and blank-sky observations in one unsupervised representation?

**Safe answer:** The role mapping is not used as a target. The method screens all 25 observations relative to the project archive; roles are retained only for interpretation and the separate blank-sky comparison. The candidates therefore require role-aware expert inspection and are not ground-truth anomalies.
