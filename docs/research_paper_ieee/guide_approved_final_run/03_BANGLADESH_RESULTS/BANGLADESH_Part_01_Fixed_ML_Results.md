# BANGLADESH Part 01 — Fixed Machine-Learning Results

## Scope

This file defines the exact machine-learning results that may enter the paper. It uses the approved Bhutan knowledge base and the integrated 25-observation truth table. It does not reinterpret historical V1 results or the six exploratory XAI cases.

## Dataset and deployed configuration

- Project archive: 25 observations, comprising 10 project-labelled source observations and 15 project-labelled blank-sky observations.
- Matrix C: 15 product-aware features, zero missing values and no imputation.
- Standardization: `StandardScaler` fitted to the 25 Matrix-C rows.
- PCA: two components used descriptively; explained-variance ratios 0.387435 and 0.225051.
- KMeans: five clusters, `n_init=20`, random state 42; cluster sizes 1, 9, 10, 1 and 4.
- Isolation Forest: 100 trees, contamination 0.16 and random state 42.
- Only `IsolationForest.predict` defines the fixed Normal/candidate label.
- Reported anomaly score: negative `score_samples`; it is not a probability.

## Fixed deployed result

| Rank | Observation | Role | Fixed score | Fixed label |
|---:|---|---|---:|---|
| 1 | Blank Sky-13 (`C24_0018`) | Blank sky | 0.615963875 | Anomaly candidate |
| 2 | Sco X-1 (`G01_0006`) | Source | 0.593516133 | Anomaly candidate |
| 3 | Her X-1 (`G01_0003`) | Source | 0.572308197 | Anomaly candidate |
| 4 | Blank Sky-5 (`C24_0010`) | Blank sky | 0.517611306 | Anomaly candidate |

The exact fixed count is **21 Normal observations and four anomaly candidates**. The existing reproduction matched all 25 saved labels and scores, with maximum score difference zero.

## Procedure-qualified stability

### Random seeds 0–99

| Observation | Times selected | Interpretation |
|---|---:|---|
| Blank Sky-13 | 100/100 | Stable under the tested seeds |
| Sco X-1 | 100/100 | Stable under the tested seeds |
| Her X-1 | 100/100 | Stable under the tested seeds |
| Blank Sky-15 | 68/100 | Fixed Normal; nearby competing observation |
| Blank Sky-5 | 29/100 | Fixed candidate; seed-sensitive boundary case |
| Crab P01_0005 | 3/100 | Fixed Normal |

These are algorithmic selection frequencies, not anomaly probabilities or confidence levels.

### Contamination sensitivity

The existing analysis tested contamination 0.12, 0.16, 0.20 and 0.24. With 25 rows, the settings selected the first 3, 4, 5 and 6 observations in one fixed ordering.

- Blank Sky-13, Sco X-1 and Her X-1: selected under 4/4 settings.
- Blank Sky-5: 3/4.
- Blank Sky-15: 2/4.
- Crab P01_0005: 1/4.

This is threshold sensitivity, not four independent model confirmations and not an estimate of anomaly prevalence.

### Included-observation jackknife

- Blank Sky-13, Sco X-1 and Her X-1: 24/24 eligible refits.
- Blank Sky-5: 19/24.
- Blank Sky-15: 7/24.
- Crab P01_0005: 2/24.
- Common-observation ranking: median Spearman \(\rho=0.989565\); minimum \(\rho=0.968696\).
- Sco X-1 was not flagged in its single held-out refit.

The jackknife measures retrospective influence within this archive; it does not establish prediction for omitted or future observations.

## Cross-feature-tier persistence

| Matrix | Candidate observations |
|---|---|
| A, 8 features | Blank Sky-13, Blank Sky-15, Sco X-1, Crab P01_0005 |
| B, 11 features | Blank Sky-5, Blank Sky-13, Blank Sky-15, Sco X-1 |
| C, 15 features | Blank Sky-5, Blank Sky-13, Her X-1, Sco X-1 |

Only Blank Sky-13 and Sco X-1 persist across Matrix A/B/C. This cross-tier result is distinct from the three-candidate Matrix-C tested-procedure core and does not prove that Matrix C is superior.

## Descriptive ranking agreement

| Ranking pair | Spearman \(\rho\) | Nominal \(p\)-value |
|---|---:|---:|
| PCA distance vs Isolation Forest score | 0.894615 | \(1.6365\times10^{-9}\) |
| PCA distance vs KMeans distance | 0.155799 | 0.457074 |
| KMeans distance vs Isolation Forest score | 0.186574 | 0.371863 |

The PCA–Isolation Forest association is descriptive within these 25 rows. The p-values do not validate the labels, establish method independence or support generalization.

## Four result sets that must remain distinct

1. **Fixed four:** Blank Sky-13, Sco X-1, Her X-1 and Blank Sky-5.
2. **Tested-procedure stable three:** Blank Sky-13, Sco X-1 and Her X-1.
3. **Cross-tier persistent two:** Blank Sky-13 and Sco X-1.
4. **Exploratory XAI six:** Sco X-1, Blank Sky-13, Her X-1, Blank Sky-5, Blank Sky-15 and Blank Sky-6.

## Exact proposed Results claims

**ML-R1.** The frozen Matrix-C model labelled 21 observations Normal and flagged four as anomaly candidates: Blank Sky-13, Sco X-1, Her X-1 and Blank Sky-5.

**ML-R2.** Blank Sky-13, Sco X-1 and Her X-1 were selected in all 100 tested seed runs, all four tested contamination settings and all 24 eligible included-observation jackknife refits; they are therefore described as a three-candidate Matrix-C core stable under the tested procedures.

**ML-R3.** Blank Sky-5 was selected in 29 of 100 seed runs and 19 of 24 eligible jackknife refits, so its fixed candidate label is reported as seed-sensitive.

**ML-R4.** Blank Sky-15 was Normal in the frozen model but selected in 68 of 100 seed runs, demonstrating competition near the contamination-defined screening boundary.

**ML-R5.** Only Blank Sky-13 and Sco X-1 persisted across the Matrix A, B and C candidate sets; this feature-tier persistence is separate from the Matrix-C stability result.

**ML-R6.** PCA distance and Isolation Forest score exhibited strong within-archive rank agreement, whereas KMeans assigned-centroid distance showed weak rank agreement with both. These correlations are descriptive and do not validate candidate status.

## Controlling evidence

- `D:\polix_xai_webapp\research_paper_ieee\guide_approved_final_run\01_NEPAL_EVIDENCE\NEPAL_Part_03_All_25_Observation_Truth_Table.csv`
- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\deployed_model_reproduction.csv`
- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\isolation_seed_stability_summary.csv`
- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\contamination_candidate_stability.csv`
- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\jackknife_observation_stability.csv`
- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\jackknife_run_summary.csv`
- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\matrix_ablation_summary.csv`
- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\ranking_metrics.csv`

