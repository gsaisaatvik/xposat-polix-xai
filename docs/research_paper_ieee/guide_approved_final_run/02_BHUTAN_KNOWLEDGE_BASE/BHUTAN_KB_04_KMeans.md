# BHUTAN Knowledge Card 04 — KMeans

## Beginner explanation

KMeans groups standardized observations by similarity. Each row is assigned to its nearest fitted group centre. In this study, KMeans supplies descriptive cluster structure and one term in the local feature ranking. It does not decide whether an observation is Normal or an anomaly candidate.

## Technical theory

KMeans minimizes

\[
\min_{\{\mu_c\},\{a_i\}}
\sum_{i=1}^{n}\lVert z_i-\mu_{a_i}\rVert_2^2,
\]

where \(z_i\) is a standardized Matrix-C row, \(a_i\) its assigned cluster and \(\mu_{a_i}\) the centroid. The project’s local KMeans feature term is

\[
K_j=(z_j-\mu_{a,j})^2.
\]

It is normalized within the observation before combination with three other explanation components.

## Exact project implementation and parameters

- Input: all 15 standardized Matrix-C features.
- Candidate counts: \(k=2,3,4,5\).
- Selection rule: highest in-sample silhouette score.
- Frozen configuration: \(k=5\), `n_init=20`, `random_state=42`.
- Silhouette: 0.310936.
- Cluster sizes: 1, 9, 10, 1 and 4.
- Sco X-1 and Blank Sky-13 are singleton clusters. Each equals its assigned fitted centroid, giving zero assigned-centroid distance and zero KMeans feature contribution.
- KMeans never sets or votes on the deployed label.

For observation \(i\), silhouette is

\[
s(i)=\frac{b(i)-a(i)}{\max\{a(i),b(i)\}},
\]

where \(a(i)\) is mean within-cluster distance and \(b(i)\) the lowest mean distance to another cluster. This is an in-sample selection summary, not evidence of validated scientific classes.

## Controlling sources and cells

- `D:\ISROtrial\Polix_L2_full_archive\10_Unsupervised_XAI_Model_Explanations.ipynb`: displayed position 2 for `choose_best_k`, position 3 for fitted KMeans, and position 8 for package save.
- `D:\polix_xai_webapp\model\polix_v2_matrixC_unsupervised_xai_model.pkl`: frozen KMeans object.
- `D:\polix_xai_webapp\model_service.py`: `predict_dataframe` and `explain_one` cluster assignment and feature-wise centroid distance.
- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\ranking_metrics.csv`: ranking agreement.

## Verified numerical results

- KMeans-distance rank agreement with PCA distance: Spearman \(\rho=0.155799\).
- KMeans-distance rank agreement with Isolation Forest score: \(\rho=0.186574\).
- These weak associations describe different within-archive geometries; they do not establish statistical independence.

## Safe inference

KMeans provides complementary descriptive geometry. The uneven and singleton clusters are important limitations and explain why the local centroid-distance term vanishes for some observations.

## Unsupported inference

Do not call the five clusters astrophysical classes, claim \(k=5\) is universally optimal, treat the silhouette as strong validation, interpret singleton clusters as confirmed anomalies, or claim that zero centroid distance indicates normality.

## Paper-ready wording

> KMeans was fitted to the 15-dimensional standardized representation. Candidate values \(k=2,\ldots,5\) were compared using the in-sample silhouette score, yielding \(k=5\), `n_init=20` and a silhouette of 0.311 for the frozen configuration. The cluster sizes were 1, 9, 10, 1 and 4. Sco X-1 and Blank Sky-13 consequently formed singleton clusters and had zero assigned-centroid distance. KMeans is used only as descriptive geometric evidence and as one component of the local ranking; it does not determine the deployed label.

## Likely reviewer challenge and safe answer

**Question:** Does selecting five clusters with two singletons overfit 25 observations?

**Safe answer:** The singleton structure is a limitation of this small retrospective archive. The study does not treat the clusters as validated classes or use KMeans to set labels. It discloses the singletons and restricts KMeans to complementary descriptive and local-ranking roles.

