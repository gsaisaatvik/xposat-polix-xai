# BHUTAN Knowledge Card 07 — Existing Robustness and Ranking Evidence

## Beginner explanation

The fixed model produces four candidates for one saved configuration. Existing supplementary checks ask whether candidates remain prominent when the random seed, threshold, included observations or feature tier changes. They produce different groups: fixed four, tested-procedure stable three, cross-tier two and six exploratory XAI cases. These groups must never be merged.

## Technical theory and exact implementation

1. **Seed stability:** Matrix C, 100 trees and contamination 0.16 are held fixed while Isolation Forest random state varies from 0 to 99.
2. **Contamination sensitivity:** contamination 0.12, 0.16, 0.20 and 0.24 selects 3, 4, 5 and 6 rows from one fixed score ordering.
3. **Included-observation jackknife:** each observation is omitted in turn; persistence is measured in the 24 refits where the observation remains included. A held-out row is not treated as prospective validation.
4. **Feature-tier comparison:** the frozen procedure is applied to Matrix A, B and C. WR remains separate.
5. **Ranking agreement:** Spearman correlation compares PCA distance, assigned-centroid KMeans distance and negative Isolation Forest `score_samples` across the same 25 rows.

These are retrospective sensitivity analyses without ground truth, predictive accuracy or confidence intervals.

## Exact project implementation and parameters

The existing audit preserves the frozen feature definitions and basic model assumptions. Seed runs vary random state 0–99 at contamination 0.16 and 100 trees. Contamination runs use 0.12, 0.16, 0.20 and 0.24 at seed 42. Twenty-five leave-one-out refits produce included-observation persistence and common-row ranking correlations. Matrix A/B/C are compared separately, while WR is excluded from confirmation. Ranking agreement uses Spearman correlation over the 25 archived rows.

## Controlling sources and functions

- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\robustness_audit.py`: `seed_stability`, `contamination_sensitivity`, `jackknife_stability`, `matrix_ablation`, `ranking_agreement`, and `reproduce_faithfulness`.
- Outputs in the same folder: `isolation_seed_stability_summary.csv`, `contamination_candidate_stability.csv`, `jackknife_observation_stability.csv`, `jackknife_run_summary.csv`, `matrix_ablation_summary.csv`, `ranking_metrics.csv`, and `ranking_agreement.csv`.

## Verified numerical results

### Seed frequency

Blank Sky-13, Sco X-1 and Her X-1: 100/100; Blank Sky-15: 68/100 but fixed Normal; Blank Sky-5: 29/100 but fixed candidate; Crab P01_0005: 3/100 and fixed Normal. These are selection frequencies, not probabilities.

### Contamination sensitivity

The stable three are selected under 4/4 thresholds; Blank Sky-5 under 3/4; Blank Sky-15 under 2/4; Crab P01_0005 under 1/4. This is threshold sensitivity along one ordering, not four independent confirmations.

### Included-observation jackknife

The stable three are selected in 24/24 eligible refits; Blank Sky-5 in 19/24; Blank Sky-15 in 7/24; Crab P01_0005 in 2/24. Common-observation ranking has median Spearman \(\rho=0.989565\) and minimum \(0.968696\). Sco X-1 is not selected in its single held-out refit, reinforcing that this is not prospective validation.

### Feature-tier persistence

- Matrix A: C24_0018, C24_0020, G01_0006, P01_0005.
- Matrix B: C24_0010, C24_0018, C24_0020, G01_0006.
- Matrix C: C24_0010, C24_0018, G01_0003, G01_0006.

Only Blank Sky-13 and Sco X-1 persist across A/B/C. Her X-1 is Matrix-C-specific.

### Ranking agreement

| Pair | Spearman \(\rho\) | Nominal two-sided \(p\) |
|---|---:|---:|
| PCA distance vs Isolation Forest score | 0.894615 | \(1.6365\times10^{-9}\) |
| PCA distance vs KMeans distance | 0.155799 | 0.457074 |
| KMeans distance vs Isolation Forest score | 0.186574 | 0.371863 |

The nominal p-values describe correlations within this archive; they do not validate candidates or establish method independence.

## Safe inference

Blank Sky-13, Sco X-1 and Her X-1 form a three-candidate Matrix-C core stable under the tested seed, contamination-threshold and included-observation procedures. Blank Sky-5 is seed-sensitive. Only Blank Sky-13 and Sco X-1 show cross-tier persistence. PCA and Isolation Forest produce similar within-archive rankings.

## Unsupported inference

Do not call the stable three “robust anomalies”; convert 100/100 or 29/100 to probability/confidence; call the seeds scientific replications; claim contamination estimates prevalence; claim jackknife establishes future performance; assert Matrix-C superiority; or treat a small p-value as candidate validation.

## Paper-ready wording

> The frozen Matrix-C configuration labelled 21 observations Normal and flagged four archive-relative candidates. Blank Sky-13, Sco X-1 and Her X-1 were selected under all 100 tested seeds, all four tested contamination settings and every eligible included-observation jackknife refit. We therefore describe them as a three-candidate Matrix-C core stable under the tested procedures. Blank Sky-5 was selected in 29 of 100 seed runs and is treated as a seed-sensitive boundary case.

> Feature-tier comparison addressed a different question. Only Blank Sky-13 and Sco X-1 appeared in candidate sets for Matrix A, B and C. This cross-tier persistence does not establish Matrix-C superiority and remains distinct from the fixed four and the tested-procedure stable three.

## Likely reviewer challenge and safe answer

**Question:** With only 25 observations and no ground truth, why describe any subset as stable?

**Safe answer:** “Stable” is qualified by the exact procedures tested. It means retrospective persistence within the same archive, not correctness, predictive accuracy, astrophysical significance or generalization to future observations.
