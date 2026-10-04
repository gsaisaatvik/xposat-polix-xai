# Agent 4 — Machine-Learning and Statistical Audit

**Audit date:** 2026-07-28  
**Scope:** existing frozen project artifacts and already-generated supplementary experiments only.  
**Execution boundary:** no model, notebook, source file, feature matrix, original result, or experiment was modified or rerun.

## 1. Overall verdict

The saved Matrix-C implementation is reproducible as an **archive-relative descriptive screening procedure**. Its fixed output of 21 Normal labels and four anomaly candidates is verified exactly against the saved model. Existing sensitivity checks support a three-observation group that is stable to the tested Isolation Forest seeds, contamination thresholds, and in-training leave-one-out refits. That result does not establish anomaly truth, predictive accuracy, population prevalence, or future-observation generalization.

The unqualified phrase **“robust core” is not defensible**. A qualified phrase such as **“three-candidate Matrix-C core stable under the tested seed, threshold, and included-observation jackknife procedures”** is defensible. “Procedure-stable Matrix-C core” is safer. The qualification matters because:

- the three cases do not form a common candidate set across Matrices A, B, and C;
- only C24_0018 and G01_0006 are selected by all three A/B/C Isolation Forest fits;
- G01_0003 enters the candidate set only in Matrix C;
- G01_0006 is not flagged in the one refit where it is held out;
- no external or prospective observations were tested.

The fourth fixed candidate, C24_0010, is fragile at the threshold. C24_0020 is selected more often across random seeds despite not belonging to the fixed four. The evidence therefore supports an uncertain boundary neighborhood rather than four equally stable cases.

## 2. Controlling evidence reviewed

| Evidence | Exact path | Audit use | Status |
|---|---|---|---|
| Frozen Matrix C | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\02_feature_engineering\polix_matrix_v2_C_primary_plus_supporting.csv` | 25 rows, 15 inputs, zero missing values | **VERIFIED** |
| Matrix A | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\02_feature_engineering\polix_matrix_v2_A_primary_final_chain.csv` | Feature-tier comparison | **VERIFIED** |
| Matrix B | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\02_feature_engineering\polix_matrix_v2_B_primary_plus_source_diag.csv` | Feature-tier comparison | **VERIFIED** |
| WR matrix | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\02_feature_engineering\polix_matrix_v2_WR_weightedroll_diagnostic.csv` | Separate diagnostic comparison | **VERIFIED AS SEPARATE** |
| Saved model | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\03_ml_xai_results\polix_v2_matrixC_unsupervised_xai_model.pkl` | Frozen preprocessing and model state | **VERIFIED by saved-artifact audit** |
| Original matrix analysis | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\03_ml_xai_results\v2_matrix_analysis_summary.csv` | PCA, KMeans, and fixed-seed matrix results | **VERIFIED** |
| Original analysis implementation | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\01_notebooks\09_V2_Matrix_Audit_and_Unsupervised_Analysis.ipynb` | Parameter and cluster-selection trace | **VERIFIED** |
| Robustness implementation | `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\robustness_audit.py` | Exact procedure for all supplementary checks | **VERIFIED** |
| Fixed-model replay | `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\deployed_model_reproduction.csv` | Prediction and score equality | **VERIFIED** |
| Seed results | `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\isolation_seed_stability.csv` and `isolation_seed_stability_summary.csv` | Seed sensitivity | **VERIFIED** |
| Contamination results | `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\contamination_sensitivity.csv` and `contamination_candidate_stability.csv` | Threshold sensitivity | **VERIFIED** |
| Jackknife results | `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\jackknife_run_summary.csv`, `jackknife_all_scores.csv`, and `jackknife_observation_stability.csv` | Leave-one-out refit behavior | **VERIFIED** |
| Matrix comparison | `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\matrix_ablation_results.csv`, `matrix_ablation_summary.csv`, and `matrix_flag_and_rank_agreement.csv` | Tier dependence and WR separation | **VERIFIED** |
| Rank comparison | `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\ranking_metrics.csv` and `ranking_agreement.csv` | Within-archive rank association | **VERIFIED** |
| Machine summary | `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\audit_summary.json` | Cross-check of principal counts | **VERIFIED** |

The reviewed report and Draft 1 were consulted only to identify language requiring audit. They do not control disputed statistical claims.

## 3. Data and inferential boundary

The frozen input contains 25 observations, comprising 10 source observations and 15 blank-sky observations. There is no trusted anomaly ground truth. The archive is a small, deliberately assembled, heterogeneous collection rather than a documented random sample from a defined population. It includes repeated target classes, so the 25 rows should not automatically be treated as independent astronomical replicates.

Consequences:

- “Anomaly” is an algorithmic candidate label relative to these 25 rows, not an error-checked scientific class.
- There is no basis for accuracy, precision, recall, specificity, receiver-operating-characteristic area, false-discovery rate, or superiority claims.
- Four of 25 is not an estimated anomaly prevalence.
- The replayed fixed output measures implementation reproducibility, not model accuracy.
- Statistical uncertainty in the feature construction is not propagated into scaling, PCA, clustering, or isolation scores.
- Archive-relative rankings may change when the feature distribution changes or future observations are added.

## 4. Component-by-component review

### 4.1 StandardScaler

The saved `StandardScaler` applies mean centering and variance scaling to all 15 Matrix-C features. Standardization is appropriate for preventing raw numerical scale from mechanically dominating Euclidean PCA and KMeans geometry. The frozen matrix has zero missing values, so no imputation was needed or performed.

This preprocessing is nevertheless archive-dependent. With \(n=25\), the sample mean and variance can be influenced strongly by unusual rows. The same 25 observations define the center, scale, downstream structure, and retrospective candidate results. That is acceptable for a descriptive archive screen, but it is not independent validation. No existing output tests a robust scaler, alternative transformations, or sensitivity to measurement uncertainty.

**Classification:** implementation **VERIFIED**; methodological use **REASONABLE FOR DESCRIPTIVE SCREENING**; future-data stability **UNVERIFIED**.

### 4.2 PCA

The frozen model uses two principal components. For Matrix C, PC1 explains 0.387435 and PC2 explains 0.225051 of standardized variance; together they explain 0.612486. The reported PCA distance is Euclidean distance in this two-component projection, not distance in the full 15-dimensional standardized space.

PCA supplies a useful visualization and a low-dimensional geometric summary. It does not validate candidate labels. Approximately 38.75% of standardized variance is outside the displayed two-component subspace, so an observation can be unusual in omitted directions. With 25 rows and 15 features, loading and coordinate stability cannot be assumed. No existing bootstrap or leave-one-out PCA-loading stability output was located.

**Classification:** variance and coordinates **VERIFIED AND DESCRIPTIVE**; stable latent structure **UNVERIFIED**; physical interpretation of components **UNSUPPORTED without feature-level review**.

### 4.3 KMeans

For Matrix C, \(k=5\) was selected from \(k=2,\ldots,5\) using the largest in-sample silhouette value, 0.310936, with `n_init=20` and random state 42. The resulting cluster sizes are 1, 9, 10, 1, and 4. Thus, two clusters are singletons.

The assigned-centroid distance is exactly zero for C24_0018 and G01_0006 because each is its own cluster centroid. This is a critical interpretive limitation: a zero KMeans distance does not mean those observations are ordinary. It is a consequence of singleton assignment. Conversely, KMeans distance is not an anomaly probability or an independent anomaly decision.

The selected \(k\) is descriptive and in-sample. The search range was limited, and no saved KMeans seed stability, cluster-membership stability, or resampling validation was found. The silhouette value should not be presented as evidence that five scientifically meaningful populations exist.

**Classification:** fixed clustering and distances **VERIFIED**; cluster ontology or generalizable structure **UNSUPPORTED**; complementary local geometry **DESCRIPTIVE WITH SINGLETON CAVEAT**.

### 4.4 Isolation Forest

The saved Isolation Forest has 100 trees, contamination 0.16, and random state 42. Its archived scores and predictions are reproduced with zero numerical difference. The reported score is the negative of `score_samples`; larger values indicate greater isolation under this fitted model. It is not a probability, calibrated risk, confidence, or physical significance.

Isolation Forest is the component that supplies the deployed binary candidate threshold. Contamination 0.16 corresponds to four of 25 observations and therefore imposes the approximate size of the fixed candidate set. It was not estimated from labels or physical prevalence.

**Classification:** fixed output **EXACTLY REPRODUCIBLE**; archive-relative ordering **DESCRIPTIVE**; anomaly truth and external generalization **UNVERIFIED**.

## 5. Existing robustness results

### 5.1 Fixed four-candidate result

| Rank | Observation | Frozen score | Frozen label | Audit interpretation |
|---:|---|---:|---|---|
| 1 | X01_PLX_C24_0018_000000 | 0.615964 | Anomaly | High archive-relative score; procedure-stable within the tested Matrix-C checks |
| 2 | X01_PLX_G01_0006_000000 | 0.593516 | Anomaly | High archive-relative score; procedure-stable while included in fitting |
| 3 | X01_PLX_G01_0003_000000 | 0.572308 | Anomaly | Matrix-C-specific procedure stability; not stable across feature tiers |
| 4 | X01_PLX_C24_0010_000000 | 0.517611 | Anomaly | Threshold-neighborhood candidate; seed-sensitive |

The numerical replay is exact. The scientific status of the four cases is not validated because no labels or expert adjudications exist.

### 5.2 Random-seed stability

Seeds 0–99 were tested while Matrix C, the scaler fit, 100 trees, and contamination 0.16 were held fixed.

| Observation | Flagged runs | Rank range | Assessment |
|---|---:|---:|---|
| C24_0018 | 100/100 | 1–3 | Stable under tested Isolation Forest seeds |
| G01_0006 | 100/100 | 1–3 | Stable under tested Isolation Forest seeds |
| G01_0003 | 100/100 | 1–4 | Stable under tested Isolation Forest seeds |
| C24_0020 | 68/100 | 3–6 | Uncertain boundary neighborhood |
| C24_0010 | 29/100 | 4–7 | Seed-sensitive fixed candidate |
| P01_0005 | 3/100 | 4–10 | Rare boundary entry |

These frequencies are descriptive algorithmic frequencies across the specified 100 seeds. They are not estimated probabilities that an observation is anomalous. The seeds are not independent datasets.

**Result classification:** three-case seed stability **ROBUST UNDER THE TESTED PROCEDURE**; fixed fourth case **FRAGILE**.

### 5.3 Contamination sensitivity

The tested contamination values were 0.12, 0.16, 0.20, and 0.24, producing candidate-set sizes of three, four, five, and six. C24_0018, G01_0006, and G01_0003 were selected at all four thresholds; C24_0010 at three; C24_0020 at two; and P01_0005 at one.

The saved scores and ranks are unchanged across these settings. In this implementation, the contamination variation changes the Isolation Forest decision threshold; it does not provide an independent ordering or independent data replication. The result shows how candidate membership changes when the assumed screening fraction moves from 12% to 24%. It does not validate 0.16 as the correct value.

**Result classification:** top-three persistence across tested thresholds **VERIFIED BUT PARTLY ORDER-IMPLIED**; contamination choice **SUBJECTIVE AND UNVALIDATED**.

### 5.4 Leave-one-out jackknife

For each omitted row, a new scaler and Isolation Forest were fitted on the other 24 rows with seed 42 and contamination 0.16. On the 24 common observations, rank correlation with the fixed full-data scores had median \(\rho=0.989565\) and minimum \(\rho=0.968696\). Each refit selected four in-training candidates.

When each observation remained in the fitting set:

- C24_0018, G01_0006, and G01_0003 were selected in 24/24 applicable refits;
- C24_0010 was selected in 19/24;
- C24_0020 was selected in 7/24;
- P01_0005 was selected in 2/24.

This demonstrates high retrospective rank stability to removal of one *other* row. It is not out-of-sample validation because the summarized observation remains in the fit. The 24 jackknife refits are highly dependent, not 24 independent trials.

Held-out behavior is separately recorded. When G01_0006 itself was omitted, the refit model did not flag it after transformation; C24_0018, G01_0003, and C24_0010 were flagged in their respective held-out runs. These individual held-out decisions should not be mixed with the included-observation frequency, and \(n=1\) per held-out case does not estimate predictive performance.

**Result classification:** common-observation ranking **ROBUST UNDER THE SPECIFIED JACKKNIFE**; candidate boundary **LOCALLY FRAGILE**; external prediction **UNVERIFIED**.

### 5.5 Matrix A/B/C feature-tier comparison

| Matrix | Features | PC1+PC2 variance | Silhouette | Fixed-seed candidates |
|---|---:|---:|---:|---|
| A | 8 | 0.751788 | 0.413328 | C24_0018, C24_0020, G01_0006, P01_0005 |
| B | 11 | 0.757038 | 0.358563 | C24_0010, C24_0018, C24_0020, G01_0006 |
| C | 15 | 0.612486 | 0.310936 | C24_0010, C24_0018, G01_0003, G01_0006 |

Pairwise A/B/C Isolation Forest score-rank correlations are 0.913077–0.952308, while thresholded candidate-set Jaccard values are 0.333333–0.600000. The broad ordering is similar, but candidate membership changes materially. Only C24_0018 and G01_0006 are common to all three sets.

This is a feature-tier sensitivity analysis, not proof that Matrix C is optimal. The KMeans comparison also changes \(k\) by matrix (4, 3, and 5), so differences in KMeans metrics are not attributable solely to added features. Silhouette values across different feature dimensions should be interpreted descriptively rather than as a universal ranking of scientific quality.

**Result classification:** broad A/B/C rank agreement **ROBUST UNDER TESTED TIERS**; exact candidate membership **FEATURE-SENSITIVE**; Matrix-C superiority **UNSUPPORTED**.

### 5.6 WR separation

The WR matrix has six WeightedRoll-derived features and is labeled in the supplementary output as `independent_weightedroll_diagnostic`. It is not a Matrix-C input and is not part of the primary deployed anomaly decision. The WR fixed-seed candidate set is C24_0023, G01_0003, G01_0004, and T24_0007, which differs from the Matrix-C set.

This separation is methodologically important because it prevents WeightedRoll information from entering the primary feature representation and then being cited as independent physical confirmation. The WR model row is a separate descriptive comparison, not an A/B/C ablation tier and not a validation set.

**Result classification:** branch separation **VERIFIED AND DEFENSIBLE**; cross-branch confirmation **UNSUPPORTED**.

### 5.7 Ranking correlations

For the 25 Matrix-C observations:

| Pair | Spearman \(\rho\) | Nominal two-sided \(p\) | Safe reading |
|---|---:|---:|---|
| PCA distance vs. Isolation Forest score | 0.894615 | \(1.6365\times10^{-9}\) | Strong descriptive rank agreement within this archive |
| PCA distance vs. KMeans centroid distance | 0.155799 | 0.457074 | Weak descriptive rank association |
| KMeans centroid distance vs. Isolation Forest score | 0.186574 | 0.371863 | Weak descriptive rank association |

PCA distance and Isolation Forest score are computed from the same standardized observations, so their agreement is not independent validation. Low KMeans correlations do not prove that KMeans supplies scientifically complementary evidence. They show only that assigned-centroid distance orders these 25 rows differently, with the additional distortion that two Matrix-C clusters are singletons.

**Result classification:** coefficients **VERIFIED AND DESCRIPTIVE**; independence or complementary validation **UNSUPPORTED**.

## 6. Statistical terminology and p-value audit

The `ranking_agreement.csv`, `matrix_flag_and_rank_agreement.csv`, and `jackknife_run_summary.csv` files contain two-sided Spearman \(p\)-values. The calculations are reproducible, but population-level interpretation is not justified:

- the archive is not documented as a random sample from a defined population;
- repeated source targets and heterogeneous source/blank-sky roles may violate an independence interpretation;
- the metrics are post hoc functions of the same fitted archive;
- PCA and Isolation Forest use the same standardized features;
- the 25 jackknife refits overlap almost completely and are not independent studies;
- several pairwise correlations were inspected without a prespecified multiplicity plan.

Accordingly, the \(p\)-values should be treated as nominal descriptive annotations or omitted from the main claims. A small \(p\)-value does not demonstrate model validity, candidate truth, robustness, or scientific significance. A large \(p\)-value does not establish independence or useful complementarity. “Nonsignificant” is potentially misleading here because no defensible population-sampling inference has been established.

Permitted wording:

> Within the 25-observation archive, PCA distance and Isolation Forest score had Spearman rank correlation \(\rho=0.8946\).

Avoid:

> PCA and Isolation Forest independently agree with statistically significant confidence.

No p-value was calculated for the candidate labels, and none should be implied. Terms such as “statistically unusual” must mean unusual relative to the fitted archive distribution, not a formal hypothesis-test rejection.

## 7. Evidence classes

### Descriptive and verified

- The frozen archive has \(n=25\), with 15 Matrix-C features and no missing values.
- The saved pipeline contains StandardScaler, two-component PCA, five-cluster KMeans, and Isolation Forest.
- PC1+PC2 explain 61.2486% of Matrix-C standardized variance.
- The saved Isolation Forest gives 21 Normal labels and four candidates.
- All frozen anomaly scores and predictions replay exactly.
- A/B/C rank correlations, candidate overlaps, silhouette values, seed frequencies, contamination-threshold memberships, and jackknife summaries match the saved outputs.
- WR is separate from Matrix C.

### Robust under the tested procedure

- C24_0018, G01_0006, and G01_0003 are selected in 100/100 tested Matrix-C Isolation Forest seeds.
- The same three occupy the candidate set at all four tested contamination thresholds.
- The same three are selected in every leave-one-out refit in which they remain in the fitting data.
- Overall common-observation rank ordering changes little across the specified leave-one-out refits.
- A/B/C Isolation Forest rankings are broadly similar.

### Fragile or conditional

- C24_0010 is a fixed-seed candidate but is selected in only 29/100 seed fits.
- C24_0020 is excluded from the fixed four but selected in 68/100 seed fits.
- Thresholded candidate membership changes across Matrix A/B/C.
- G01_0003 is part of the Matrix-C three-case core but is absent from Matrix A and B candidate sets.
- KMeans contains two singleton clusters, making assigned-centroid distance zero for two high Isolation Forest candidates.
- Matrix-C PCA uses only 61.25% of standardized variance.
- Contamination sensitivity is threshold sensitivity over one fixed ordering, not independent model validation.

### Unsupported or non-generalizable

- Four candidates are the true anomalies.
- The anomaly prevalence is 16%.
- The fixed model has known accuracy.
- The three-case core will persist in a new POLIX release.
- \(k=5\) represents five scientifically real observation populations.
- PCA, KMeans, and Isolation Forest provide independent confirmations.
- Matrix C is superior to A, B, or WR.
- A low rank-correlation \(p\)-value validates the method.
- A candidate label identifies an astrophysical, instrumental, or processing cause.

## 8. Wording decision: “robust core”

**Decision:** allowed only with immediate procedural qualification.

Safe:

> Under the tested Matrix-C Isolation Forest seed, contamination-threshold, and included-observation jackknife procedures, C24_0018, G01_0006, and G01_0003 formed a stable three-candidate core.

Safer:

> The tested procedures identified a three-candidate Matrix-C stability core.

Unsafe:

- “The model discovered a robust core of true anomalies.”
- “Three anomalies are statistically confirmed.”
- “The robust core generalizes to POLIX observations.”
- “The three cases are robust across feature representations.”
- “The fixed four candidates are robust.”

The paper should distinguish **reproducible**, **stable under a named sensitivity procedure**, and **externally validated**. Only the first two are supported.

## 9. Disagreements for the controlling register

| ID | Issue | Existing or possible wording | Agent 4 position |
|---|---|---|---|
| ML-D01 | Four fixed candidates versus stability evidence | The fixed model has four anomaly candidates. | Numerically correct, but only three are stable across all 100 tested seeds; C24_0010 is seed-sensitive and C24_0020 is a competing boundary case. |
| ML-D02 | “Robust core” | Three candidates form a robust core. | Permit only as a Matrix-C, procedure-qualified term; it is not robust across A/B/C tiers or external data. |
| ML-D03 | Contamination sensitivity | Four contamination settings independently support the top three. | The scores/ranks are identical; the test varies the threshold over one ordering. It supports threshold persistence, not independent replication or correctness of 0.16. |
| ML-D04 | Jackknife interpretation | The top three are stable under leave-one-out validation. | They are stable in the 24 refits where each remains in training. This is retrospective influence sensitivity, not external validation; G01_0006 is not flagged in its held-out refit. |
| ML-D05 | KMeans complementarity | Weak correlation proves complementary local evidence. | Different ordering is descriptive only. Two singleton clusters yield zero centroid distance for C24_0018 and G01_0006, limiting anomaly interpretation. |
| ML-D06 | Matrix-C choice | Matrix C is the best or most complete model input. | It is the frozen deployed choice. Existing ablation shows feature-tier sensitivity and does not establish superiority. |
| ML-D07 | Rank-correlation p-values | Small \(p\) demonstrates statistically significant method agreement. | Treat \(p\)-values as nominal/descriptive or omit them; they do not validate models or candidates. |
| ML-D08 | “Statistically unusual” | Candidate is statistically significant. | “Statistically unusual relative to the project archive” is acceptable. “Statistically significant” is unsupported because no candidate-level hypothesis test exists. |
| ML-D09 | WR matrix comparison | WR candidates confirm Matrix-C candidates. | WR is an independent diagnostic feature branch, not confirmation, ground truth, or an A/B/C tier. |

## 10. Safe and unsafe claims

### Safe claims

- “The frozen saved model reproducibly flagged four archive-relative anomaly candidates.”
- “Three observations were flagged in all 100 tested Matrix-C Isolation Forest seed fits.”
- “Blank Sky-5 was seed-sensitive, appearing in 29 of 100 fits.”
- “Candidate membership near the threshold depended on the assumed contamination fraction and feature tier.”
- “The common-observation score ordering was stable under the specified leave-one-out refits.”
- “PCA, KMeans, and Isolation Forest provide different descriptive views of the same standardized archive.”
- “The WR matrix was kept outside the primary Matrix-C deployment.”
- “No anomaly ground truth was available.”

### Unsafe claims

- “Four anomalies were detected or confirmed.”
- “The model achieved robust accuracy.”
- “Contamination 0.16 is the anomaly prevalence.”
- “The 100 seeds provide a 100% confidence level.”
- “The jackknife proves future-data generalization.”
- “The low p-value confirms the anomaly model.”
- “KMeans validates the Isolation Forest result.”
- “Matrix C is statistically superior.”
- “WR independently proves that an ML candidate is physically polarized.”

## 11. Additional work identified but not executed

- **NOT EXECUTED — REASON — PRIORITY:** independent prospective or external-release validation — no separate frozen release with comparable features was placed in scope, and Phase 4 prohibits new experiments — **HIGH**.
- **NOT EXECUTED — REASON — PRIORITY:** leave-one-target-out or grouped resampling — repeated targets mean row-wise leave-one-out does not assess target-level transfer; no existing output was located — **HIGH**.
- **NOT EXECUTED — REASON — PRIORITY:** PCA loading/subspace stability under resampling — no saved experiment exists, and a new run is not authorized — **HIGH**.
- **NOT EXECUTED — REASON — PRIORITY:** KMeans seed, \(k\)-range, and cluster-membership stability — the existing notebook checks \(k=2,\ldots,5\) at one seed but does not quantify stability, especially of singleton clusters — **HIGH**.
- **NOT EXECUTED — REASON — PRIORITY:** preprocessing sensitivity using robust scaling or justified transformations — existing results use only StandardScaler, and a new comparison is not authorized — **MEDIUM**.
- **NOT EXECUTED — REASON — PRIORITY:** uncertainty propagation or noise perturbation of engineered features — feature-level measurement uncertainties were not supplied to the ML pipeline — **MEDIUM**.
- **NOT EXECUTED — REASON — PRIORITY:** domain-expert adjudication of candidate relevance — this requires external scientific judgment rather than another unsupervised fit — **HIGH**.

## 12. Final Agent 4 judgment

The existing ML evidence is sufficient for a cautious applied scientific-computing paper that presents a reproducible archive-relative screening workflow and explicitly reports sensitivity. Its strongest ML result is not “four robust anomalies”; it is:

> The fixed Matrix-C artifact reproducibly returns four candidates, while the tested sensitivity procedures identify three observations with consistent Matrix-C membership and reveal instability in the threshold neighborhood.

This result is descriptive and methodologically useful. It must remain bounded by the small heterogeneous archive, absence of labels, in-sample preprocessing and model fitting, feature-tier dependence, singleton KMeans clusters, and lack of independent prospective evaluation.
