# BHUTAN Knowledge Card 05 — Isolation Forest

## Beginner explanation

Isolation Forest finds observations that are comparatively easy to separate from the rest of the archive using random decision trees. In the frozen project, Isolation Forest alone supplies the Normal or anomaly-candidate label.

## Technical theory

Isolation Forest recursively partitions standardized feature space. Shorter average tree paths indicate observations that are easier to isolate. The service reports

\[
a_i=-\operatorname{score\_samples}(z_i),
\]

so larger reported values indicate greater archive-relative unusualness. The fixed class is `Anomaly candidate` only when `IsolationForest.predict(z_i)=-1`. Contamination defines the fitted screening threshold; it is not an empirical estimate of true anomaly prevalence.

## Exact project implementation and parameters

- Input: all 15 standardized Matrix-C features.
- `n_estimators=100`.
- `contamination=0.16`.
- `random_state=42`.
- Score: negative `score_samples`.
- Label: `IsolationForest.predict` only. PCA and KMeans do not vote on it.
- The saved scores and labels were reproduced exactly with maximum score difference zero.
- The fixed four candidates are distinct from the six exploratory XAI cases.

## Verified numerical results

| Rank | Observation | Score | Fixed result |
|---:|---|---:|---|
| 1 | Blank Sky-13 (`C24_0018`) | 0.615963875 | Anomaly candidate |
| 2 | Sco X-1 (`G01_0006`) | 0.593516133 | Anomaly candidate |
| 3 | Her X-1 (`G01_0003`) | 0.572308197 | Anomaly candidate |
| 4 | Blank Sky-5 (`C24_0010`) | 0.517611306 | Anomaly candidate |

Overall: 21 Normal and four anomaly candidates.

Existing checks found Blank Sky-13, Sco X-1 and Her X-1 in 100/100 tested seeds; Blank Sky-5 in 29/100; and the fixed-Normal Blank Sky-15 in 68/100. In included-observation jackknife refits, the first three remained selected in 24/24 eligible runs and Blank Sky-5 in 19/24. Only Blank Sky-13 and Sco X-1 persist across Matrix A/B/C. These are retrospective procedure checks, not probabilities or future-data tests.

## Controlling sources and cells

- `D:\ISROtrial\Polix_L2_full_archive\10_Unsupervised_XAI_Model_Explanations.ipynb`: displayed position 3 for the frozen Isolation Forest and position 8 for package save.
- `D:\polix_xai_webapp\model\polix_v2_matrixC_unsupervised_xai_model.pkl`: frozen object.
- `D:\polix_xai_webapp\model_service.py`: `predict_dataframe`, authoritative score and label rule.
- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\deployed_model_reproduction.csv`: exact replay.
- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\isolation_seed_stability_summary.csv`: seed frequency.
- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\jackknife_observation_stability.csv`: included-observation persistence.

## Safe inference

The frozen model ranks four observations as statistically unusual relative to the 25-row Matrix-C archive. Three exhibit persistence under the existing tested procedures, whereas Blank Sky-5 is sensitive to algorithmic seed and feature-tier context.

## Unsupported inference

Do not claim confirmed anomalies, anomaly probability, a true 16% prevalence, predictive accuracy, physical cause, future-data generalization, superiority over other methods, or joint PCA/KMeans voting.

## Paper-ready wording

> Isolation Forest was fitted to the standardized 15-feature Matrix-C representation using 100 trees, contamination 0.16 and random state 42. Contamination is treated as the frozen screening assumption defining the archive-relative threshold, not an estimate of anomaly prevalence. `IsolationForest.predict` alone produced the fixed labels: 21 observations were labelled Normal and four were flagged as anomaly candidates. Blank Sky-13, Sco X-1 and Her X-1 were selected in all 100 tested seeds, whereas Blank Sky-5 was selected in 29. These are selection frequencies under the tested procedure, not probabilities or confidence levels.

## Likely reviewer challenge and safe answer

**Question:** With no anomaly labels, how can the four observations be defended as results?

**Safe answer:** They are not presented as confirmed anomalies. The defensible result is reproducible archive-relative screening under a frozen model. Existing sensitivity checks distinguish persistent candidates from fragile ones, while scientific interpretation remains separate and requires domain-expert inspection.

