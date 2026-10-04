# BHUTAN Knowledge Card 03 — StandardScaler and Principal Component Analysis

## Beginner explanation

The 15 features have different ranges. Standardization puts them on comparable numerical scales. Principal Component Analysis (PCA) then provides a two-dimensional summary of dominant archive variation. The PCA plot is descriptive; it does not assign the deployed anomaly label.

## Technical theory

For feature \(j\),

\[
z_{ij}=\frac{x_{ij}-\mu_j}{s_j},
\]

where \(\mu_j\) and \(s_j\) are fitted from the 25 Matrix-C rows. PCA projects the standardized row \(z_i\) onto orthogonal directions \(w_k\):

\[
\mathrm{PC}_{ik}=z_i^\mathsf{T}w_k.
\]

The coordinates show geometry in the fitted archive and are neither probabilities nor calibrated physical coordinates.

## Exact project implementation

- Input: 25-by-15 Matrix C.
- Preprocessing: `StandardScaler`; no imputer.
- PCA components: 2; recorded random state 42.
- PCA, KMeans and Isolation Forest each receive the same standardized rows. They are parallel analytical views, not a sequential chain.
- PCA supplies descriptive coordinates and one component of the local feature-ranking heuristic.
- PCA does not set the fixed candidate label.

For the local-ranking PCA component only,

\[
P_j=|z_jw_{1j}|r_1+|z_jw_{2j}|r_2,
\]

where \(r_1,r_2\) are the explained-variance ratios. This is a project-specific heuristic term, not an exact decomposition of the deployed label.

## Parameters and verified numerical results

\[
\operatorname{EVR}(\mathrm{PC1})=0.387435,\quad
\operatorname{EVR}(\mathrm{PC2})=0.225051,
\]

\[
\operatorname{EVR}(\mathrm{PC1:2})=0.612486.
\]

PCA-distance and Isolation-Forest-score ranks have Spearman \(\rho=0.894615\) within the archive. This association is descriptive and not independent validation. The 38.75% of standardized variance outside PC1–PC2 limits the two-dimensional view.

## Controlling sources and cells

- `D:\ISROtrial\Polix_L2_full_archive\10_Unsupervised_XAI_Model_Explanations.ipynb`: displayed position 3 for standardization/two-component PCA and position 8 for the frozen package save.
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\02_feature_engineering\polix_matrix_v2_C_primary_plus_supporting.csv`: input.
- `D:\polix_xai_webapp\model\polix_v2_matrixC_unsupervised_xai_model.pkl`: frozen scaler and PCA objects.
- `D:\polix_xai_webapp\model_service.py`: `predict_dataframe` scaler and PCA transformations.
- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\ranking_metrics.csv`: rank-correlation output.

## Safe inference

The first two PCs provide a compact descriptive view of dominant standardized variation in this 25-observation archive. Their rank agreement with Isolation Forest may be reported as complementary within-archive evidence.

## Unsupported inference

Do not claim that two PCs preserve all relevant information, that visual separation proves an anomaly or physical class, that PCA validates candidates, or that the geometry generalizes to future observations.

## Paper-ready wording

> Matrix-C features were standardized using parameters fitted to the 25-row project archive. A two-component PCA projection was retained for descriptive visualization and for one term in the local feature-ranking heuristic. PC1 and PC2 account for 38.74% and 22.51% of standardized Matrix-C variance. Because the projection preserves 61.25% of the variance and was fitted retrospectively to the same archive, it is interpreted as a descriptive view rather than independent validation.

## Likely reviewer challenge and safe answer

**Question:** Why show only two components when 38.75% of variance lies outside the projection?

**Safe answer:** The two components are used for visualization and a bounded geometric contribution to the local ranking, not as the complete anomaly input. KMeans and Isolation Forest operate on all 15 standardized features, and the retained variance is reported to prevent overinterpretation.

