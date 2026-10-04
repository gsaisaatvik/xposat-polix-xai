# Experiment and Robustness Audit

## Audit conclusion

The completed project is sufficient for a cautious applied methodology paper draft, but not for a strong generalization or astrophysical claim. The fixed deployed model and primary physical results are reproducible. New stability experiments reveal a robust three-candidate core and a seed-sensitive fourth deployed candidate.

## Primary-result verification

| Check | Result | Evidence |
|---|---|---|
| All archive observations processed | PASS: 25/25 | Matrix-C CSV; physical fit CSV; reviewed report |
| Matrix-C feature count | PASS: 15 | Matrix-C CSV; saved model |
| Frozen Matrix-C missing values | PASS: 0 | `matrix_ablation_summary.csv` |
| Final deployed output | PASS: 21 Normal; 4 Anomaly | saved model; `deployed_model_reproduction.csv` |
| Deployed candidates | PASS | C24_0010, C24_0018, G01_0003, G01_0006 |
| Exploratory/deployed distinction | PASS | six-row exploratory faithfulness set versus four saved-model predictions |
| Faithfulness counts | PASS: 5 Strong; 1 Moderate; 0 Weak | original and reproduced verdict CSVs |
| Blank sky analyzed | PASS: 15 | role and fit CSVs |
| Empirical Q/U baseline | PASS: 13 `acceptable` fits | fractional Q/U CSV and config |
| Source physical results | PASS: 10/10 | source comparison and source-only CSVs |
| Calibrated PD/PA absent | PASS | calibration-audit files and config |

## Deployed anomaly candidates and local drivers

| Candidate | Target/role | Isolation score | Top combined driver | Product family | 100-seed flag frequency |
|---|---|---:|---|---|---:|
| X01_PLX_C24_0018_000000 | Blank Sky-13 / blank sky | 0.615964 | `t1A_energy_weighted_std_channel` | EnergyRes | 100% |
| X01_PLX_G01_0006_000000 | Sco X-1 / source | 0.593516 | `t1A_energy_peak_channel` (2.454499); next: weighted mean (2.207369), entropy (1.813968) | EnergyRes | 100% |
| X01_PLX_G01_0003_000000 | Her X-1 / source | 0.572308 | `t2_lc_rate_cv` | Light curve | 100% |
| X01_PLX_C24_0010_000000 | Blank Sky-5 / blank sky | 0.517611 | `t1B_src_roll_smoothness_norm` | Source azimuth | 29% |

The score is archive- and model-specific and is not a probability.

### Accepted Sco X-1 version audit

Draft 1 treats the exact imported `model_service.py::PolixXAIPredictor.explain_one` result as authoritative. It agrees with Notebook 10 and the supplementary reproduction: peak channel ranks first, weighted mean channel second, and entropy third. The historical entropy-first narrative is not reproducible from any located versioned artifact and is superseded. No anomaly prediction, anomaly score, physical result, robustness result, or faithfulness verdict changed.

## New experiments

### 1. Isolation Forest random-seed stability

- Seeds: 0–99.
- Fixed assumptions: Matrix C, StandardScaler, 100 trees, contamination 0.16.
- Three candidates were flagged in 100/100 runs.
- C24_0020 was flagged in 68/100 runs.
- The deployed fourth candidate, C24_0010, was flagged in 29/100 runs.
- Crab P01_0005 was flagged in 3/100 runs.

Interpretation: the top three are robust to the tested seed range. The fourth fixed-seed boundary is not.

### 2. Contamination sensitivity

Tested values: 0.12, 0.16, 0.20, and 0.24, corresponding to small candidate sets in a 25-observation archive.

| Observation | Settings flagged |
|---|---:|
| C24_0018 | 4/4 |
| G01_0006 | 4/4 |
| G01_0003 | 4/4 |
| C24_0010 | 3/4 |
| C24_0020 | 2/4 |
| P01_0005 | 1/4 |

The three-candidate core is stable across the tested range. Additional candidates depend on the assumed candidate fraction.

### 3. Leave-one-out jackknife

For each omitted observation, the scaler and Isolation Forest were refit on the remaining 24 observations with contamination 0.16 and seed 42.

- Spearman correlation between full-data and jackknife anomaly scores on common observations: median 0.9896; minimum 0.9687.
- C24_0018, G01_0006, and G01_0003 were flagged in 24/24 runs in which they remained in training.
- C24_0010 was flagged in 19/24 included runs.
- C24_0020 was flagged in 7/24 included runs.
- Held-out flagging is reported separately and is not treated as equivalent to within-archive refit stability.

### 4. Feature-tier ablation

| Matrix | Features | PC1+PC2 variance | KMeans silhouette | Isolation candidates |
|---|---:|---:|---:|---|
| A | 8 | 0.7518 | 0.4133 | C24_0018; C24_0020; G01_0006; P01_0005 |
| B | 11 | 0.7570 | 0.3586 | C24_0010; C24_0018; C24_0020; G01_0006 |
| C | 15 | 0.6125 | 0.3109 | C24_0010; C24_0018; G01_0003; G01_0006 |
| WR | 6 | 0.9484 | 0.4848 | C24_0023; G01_0003; G01_0004; T24_0007 |

WR remains a separate diagnostic. Its candidates are not used as confirmation of Matrix-C candidates.

Matrix A/B/C anomaly-score rank correlations are high (0.913–0.952), but candidate-set Jaccard agreement is only 0.333–0.600. Feature-tier choice therefore affects the thresholded candidate set even when broad ranking is similar.

### 5. Ranking agreement

| Metrics | Spearman \(\rho\) | Two-sided \(p\) |
|---|---:|---:|
| PCA distance vs. Isolation Forest score | 0.8946 | \(1.64\times10^{-9}\) |
| PCA distance vs. KMeans centroid distance | 0.1558 | 0.457 |
| KMeans centroid distance vs. Isolation Forest score | 0.1866 | 0.372 |

PCA and Isolation Forest broadly agree on global unusualness. KMeans centroid distance supplies different local structure and should not be described as an independent anomaly classifier.

### 6. XAI faithfulness reproduction

The original six-candidate neutralization experiment was reconstructed from the saved model and top-contribution file.

- Maximum numeric difference from the original metrics: below \(9\times10^{-16}\).
- Verdicts reproduced exactly: five Strong, one Moderate, zero Weak.
- Strong requires reduced PCA distance and reduced Isolation Forest anomaly score.
- The Moderate case is C24_0023, for which PCA distance falls but Isolation Forest score does not.
- The six cases are the exploratory candidate set, not the four deployed predictions.

## Physical branch audit

### Fit counts

| Subset | Acceptable | Caution | Poor simple sinusoid | Total |
|---|---:|---:|---:|---:|
| Source | 6 | 2 | 2 | 10 |
| Blank sky | 13 | 1 | 1 | 15 |
| All | 19 | 3 | 3 | 25 |

### Empirical blank-sky reference

- Selection: 13 blank-sky fits labeled `acceptable` (reduced chi-square ≤ 2.0).
- Mean raw modulation: 1.147820%.
- Sample standard deviation: 0.565960%.
- Median: 1.492835%.
- Range: 0.294127–1.778927%.
- Mean \(Q/C\): 0.0090920; sample SD 0.0048569.
- Mean \(U/C\): -0.0064782; sample SD 0.0040190.

### All ten source results

| Observation | Target | Raw modulation (%) | Fit quality | Reduced chi-square | Blank-sky vector distance | Status |
|---|---|---:|---|---:|---:|---|
| G01_0003 | Her X-1 | 0.5966 ± 0.0167 | poor | 57.4335 | 2.3174 | moderate vector difference; low confidence |
| G01_0006 | Sco X-1 | 1.1396 ± 0.0199 | caution | 2.0308 | 0.3005 | within scatter |
| P01_0005 | Crab | 1.6973 ± 0.0310 | acceptable | 1.0625 | 1.2649 | within scatter |
| G01_0004 | GX 301-2 | 0.7223 ± 0.0295 | caution | 4.3745 | 1.2514 | within scatter |
| T24_0007 | Cyg X-1 | 0.6811 ± 0.0153 | poor | 5.4080 | 1.1480 | within scatter |
| T24_0001 | Crab | 1.3955 ± 0.0627 | acceptable | 0.8146 | 1.1352 | within scatter |
| C24_0026 | Cas-A SNR | 0.6927 ± 0.0294 | acceptable | 1.7030 | 0.9385 | within scatter |
| G01_0002 | Cen X-3 | 0.9286 ± 0.0220 | acceptable | 1.8972 | 0.7748 | within scatter |
| G01_0005 | 4U 1700-37 | 1.0806 ± 0.0581 | acceptable | 1.2291 | 0.6305 | within scatter |
| T24_0002 | Crab | 1.2008 ± 0.0220 | acceptable | 1.3671 | 0.5152 | within scatter |

Every source has scalar raw-modulation z-score between -0.974 and 0.971 relative to the empirical baseline and is labeled within the baseline range.

## Audit discrepancies requiring manuscript correction

1. Report: blank-sky baseline described as reduced chi-square ≤ 5. Actual baseline: only `acceptable` fits, reduced chi-square ≤ 2.
2. Report/historical narrative: Sco X-1 entropy named first. Accepted exact versioned result: peak channel (2.454499), weighted mean channel (2.207369), and entropy (1.813968); the entropy-first narrative is superseded.
3. Report: median imputation claimed. Saved artifact and deployed code: no imputer; frozen matrix happens to contain no missing values.
4. Physical summary tables: exploratory six-candidate flag. Deployed result: four candidates.

## Not executed

- **NOT EXECUTED — REASON:** external holdout validation; no independent release was placed in scope.
- **NOT EXECUTED — REASON:** supervised accuracy, precision, recall, or ROC benchmarking; no trusted anomaly labels exist.
- **NOT EXECUTED — REASON:** official PD/PA calibration; no verified official \(\mu_{100}\), background product, or phase-to-sky convention was available.
- **NOT EXECUTED — REASON:** causal timing/spectral investigation of individual candidates; outside project evidence.
- **NOT EXECUTED — REASON:** domain-expert candidate adjudication; requires external scientific review.
