# Version-3 Candidate and Comparison Case Studies

## Evidence basis

The fixed score and label come from `research_paper_ieee/supplementary_experiments/deployed_model_reproduction.csv`. Seed, contamination, included-observation jackknife, and A/B/C results come from the corresponding supplementary CSVs. PCA coordinates, KMeans cluster membership, and the local top-five rankings were reproduced read-only from the saved PKL and Matrix C using the current `model_service.py`; no estimator was fitted. Harmonic values come from `final_project_outputs/04_polarimetry_results/polix_weightedroll_raw_modulation_fits.csv`. Source-versus-blank scalar status comes from `path2_source_vs_blank_sky_modulation_comparison.csv`.

“Anomaly” in the stored model is reported below as **candidate**. It is not anomaly ground truth.

## 1. Sco X-1

### Identity and screening evidence

| Field | Verified value |
|---|---|
| Observation name | Sco X-1 |
| Full observation ID | `X01_PLX_G01_0006_000000` |
| Project role | Source |
| Fixed Isolation Forest score | 0.593516132746 |
| Fixed label | Candidate; Matrix-C rank 2 |
| Random-seed result | 100/100; rank range 1–3 |
| Contamination sensitivity | Selected at all four tested values: 0.12, 0.16, 0.20, 0.24 |
| Included-observation jackknife | 24/24 applicable refits |
| Held-out refit | Not selected; rank 7 in its single held-out run |
| Matrix A/B/C | Selected in A (rank 1), B (rank 1), and C (rank 2) |
| PCA coordinates / distance | PC1 -0.537402; PC2 -3.393377; two-PC distance 3.435667 |
| KMeans | Cluster 3; cluster size 1; assigned-centroid distance therefore zero |

### Current exact local ranking

| Rank | Feature | Score | Raw value | Archive-relative z | Product family |
|---:|---|---:|---:|---:|---|
| 1 | Energy peak channel | 2.454499 | 465 | +4.894106 | Tier-1A EnergyRes |
| 2 | Count-weighted mean channel | 2.207369 | 1648.3309997 | -3.432505 | Tier-1A EnergyRes |
| 3 | Channel-distribution entropy | 1.813968 | 11.9933947 | -2.855662 | Tier-1A EnergyRes |

These are within-observation heuristic scores. They do not form a probability or physical effect scale.

### Neutralization check

The three features above were jointly replaced with zero in standardized space, corresponding to the fitted archive mean for each feature while all other coordinates were held fixed.

| Metric | Before | After | Change |
|---|---:|---:|---:|
| Two-PC PCA distance | 3.435667 | 1.402399 | decreased by 2.033268 |
| Isolation Forest score | 0.593516 | 0.429706 | decreased by 0.163810 |
| KMeans distance | 0.000000 | 6.624890 | increased because the original cluster is a singleton |

Project verdict: `Strong`, defined only by decreases in PCA distance and Isolation Forest score. KMeans did not enter that verdict.

### Separate WeightedRoll evidence

| Quantity | Verified value |
|---|---:|
| C | 170.9322321582 |
| Q cosine coefficient | 1.7045938152 |
| U sine coefficient | -0.9427094972 |
| Harmonic amplitude | 1.9479068948 |
| Raw modulation | 1.1395784576% |
| Fitted phase | 165.5278135509° |
| Reduced chi-square | 2.0307608048 |
| Degrees of freedom / bins | 357 / 360 |
| Project fit category | Caution |
| Declared scalar blank-sky rule | Within; z = -0.014563 |

The audited figure shows a clear two-fold component together with systematic residual structure; the simple harmonic is only a caution-category summary.

### WHY THIS OBSERVATION IS INTERESTING TO THE FRAMEWORK

Sco X-1 is the clearest cross-tier screening case: it remains selected in A/B/C and under all tested seeds and contamination values while included in fitting. The local ranking sends the researcher specifically to the EnergyRes product family. The separate harmonic result is not exceptional under the declared scalar blank-sky rule. This discordance demonstrates why the two branches answer different questions.

**Supported:** persistently unusual Matrix-C feature pattern under the tested procedures; energy-channel summaries are the leading local evidence.

**Not supported:** spectral or astrophysical cause, calibrated energy shift, polarization detection, official PD/PA, or future-data generalization.

## 2. Her X-1

### Identity and screening evidence

| Field | Verified value |
|---|---|
| Observation name | Her X-1 |
| Full observation ID | `X01_PLX_G01_0003_000000` |
| Project role | Source |
| Fixed Isolation Forest score | 0.572308197266 |
| Fixed label | Candidate; Matrix-C rank 3 |
| Random-seed result | 100/100; rank range 1–4 |
| Contamination sensitivity | Selected at all four tested values |
| Included-observation jackknife | 24/24 |
| Held-out refit | Selected; rank 3 |
| Matrix A/B/C | Not selected in A (rank 9) or B (rank 8); selected in C (rank 3) |
| PCA coordinates / distance | PC1 -1.183065; PC2 +4.857296; distance 4.999296 |
| KMeans | Cluster 4; cluster size 4 |

### Current exact local ranking

| Rank | Feature | Score | Raw value | Archive-relative z | Product family |
|---:|---|---:|---:|---:|---|
| 1 | Delivered-light-curve rate coefficient of variation | 4.000000 | 0.164126787 | +4.196257 | Tier-2 Light Curve |
| 2 | Delivered-light-curve peak-to-median ratio | 3.030829 | 7.718954248 | +3.806515 | Tier-2 Light Curve |
| 3 | Source-azimuth roll entropy | 1.481219 | 8.300590654 | +1.724774 | Tier-1B Source Azimuth |

### Neutralization check

| Metric | Before | After | Result |
|---|---:|---:|---|
| Two-PC PCA distance | 4.999296 | 2.173506 | decreased |
| Isolation Forest score | 0.572308 | 0.454444 | decreased |
| KMeans distance | 4.418462 | 2.247871 | decreased |

Project verdict: `Strong`.

### Separate WeightedRoll evidence

| Quantity | Verified value |
|---|---:|
| C | 154.6131073683 |
| Q | -0.3263876873 |
| U | -0.8628001664 |
| Amplitude | 0.9224711647 |
| Raw modulation | 0.5966319288% |
| Fitted phase | 124.6394640851° |
| Reduced chi-square | 57.4335137536 |
| Degrees of freedom / bins | 357 / 360 |
| Project fit category | Poor simple-harmonic fit |
| Declared scalar blank-sky rule | Within; z = -0.973901 |

The audited curve visibly contains large localized excursions around approximately 45–115 degrees and residuals reaching many tens of supplied-error units. The saved second harmonic does not describe that structure.

### WHY THIS OBSERVATION IS INTERESTING TO THE FRAMEWORK

Her X-1 appears only when Matrix-C supporting light-curve and detector-context features are present. Its leading local evidence is dominated by delivered-light-curve summaries, not WeightedRoll. Simultaneously, the separate WeightedRoll fit is extremely poor. The observation therefore demonstrates both feature-tier dependence and the danger of interpreting a fitted harmonic amplitude when the model does not summarize the curve adequately.

**Supported:** Matrix-C-specific candidate status under tested procedures; strong delivered-light-curve deviations; visually and numerically poor second-harmonic summary.

**Not supported:** intrinsic source variability, instrumental fault, astrophysical anomaly, or polarization inference.

## 3. Blank Sky-13

### Identity and screening evidence

| Field | Verified value |
|---|---|
| Observation name | Blank Sky-13 |
| Full observation ID | `X01_PLX_C24_0018_000000` |
| Project role | Blank sky |
| Fixed Isolation Forest score | 0.615963874890 |
| Fixed label | Candidate; Matrix-C rank 1 |
| Random-seed result | 100/100; rank range 1–3 |
| Contamination sensitivity | Selected at all four tested values |
| Included-observation jackknife | 24/24 |
| Held-out refit | Selected; rank 5 |
| Matrix A/B/C | Selected in A, B, and C; rank 2, 2, and 1 |
| PCA coordinates / distance | PC1 +3.812983; PC2 +2.570696; distance 4.598621 |
| KMeans | Cluster 0; cluster size 1; assigned-centroid distance zero |

### Current exact local ranking

| Rank | Feature | Score | Raw value | Archive-relative z | Product family |
|---:|---|---:|---:|---:|---|
| 1 | Weighted channel spread | 2.902010 | 1273.187277 | +3.683385 | Tier-1A EnergyRes |
| 2 | High-channel fraction | 2.544842 | 0.0633350 | +3.249521 | Tier-1A EnergyRes |
| 3 | Channel-distribution entropy | 2.049469 | 12.1320146 | +2.448832 | Tier-1A EnergyRes |

### Neutralization check

PCA distance decreased from 4.598621 to 1.087332 and Isolation Forest score from 0.615964 to 0.474996. KMeans distance increased from zero to 5.488487 because the original cluster is a singleton. Project verdict: `Strong`.

### Separate WeightedRoll evidence

Raw modulation is 0.8539506415%; fitted phase 158.7833540871°; reduced chi-square 2.5658113460; 357 degrees of freedom and 360 bins; project category `caution`. It is excluded from the 13-fit blank-sky reference because it fails the declared reduced-chi-square ≤2 rule. Separate visual inspection was not part of the new three-case figure: **NOT VERIFIED visually** beyond the saved fit statistics.

### WHY THIS OBSERVATION IS INTERESTING TO THE FRAMEWORK

Blank Sky-13 is the highest-scoring and most cross-tier persistent case, and its leading evidence comes from channel-space summaries. Its blank-sky role demonstrates that the model is not a source classifier or polarization classifier. Its singleton KMeans assignment also exposes an important explanation edge case: zero centroid distance here is structural, not evidence of normality.

**Not supported:** a background defect, detector fault, or physical origin for its channel-space pattern.

## 4. Blank Sky-5

### Identity and screening evidence

| Field | Verified value |
|---|---|
| Observation name | Blank Sky-5 |
| Full observation ID | `X01_PLX_C24_0010_000000` |
| Project role | Blank sky |
| Fixed Isolation Forest score | 0.517611306034 |
| Fixed label | Candidate; Matrix-C rank 4 |
| Random-seed result | 29/100; rank range 4–7 |
| Contamination sensitivity | Selected at 0.16, 0.20, and 0.24; not 0.12 |
| Included-observation jackknife | 19/24 |
| Held-out refit | Selected; rank 5 |
| Matrix A/B/C | Not selected in A (rank 5); selected in B (rank 3) and C (rank 4) |
| PCA coordinates / distance | PC1 +3.099324; PC2 -2.919586; distance 4.257909 |
| KMeans | Cluster 2; cluster size 10 |

### Current exact local ranking

| Rank | Feature | Score | Raw value | Archive-relative z | Product family |
|---:|---|---:|---:|---:|---|
| 1 | Order-dependent source-azimuth roughness proxy | 3.894028 | 0.2956445 | +2.237486 | Tier-1B Source Azimuth |
| 2 | Source-azimuth peak-to-median ratio | 3.438471 | 62.3518762 | +2.237753 | Tier-1B Source Azimuth |
| 3 | Maximum-to-minimum roll-exposure ratio | 3.355138 | 69.2869898 | +2.172355 | Tier-1A Exposure |

### Neutralization check

PCA distance decreased from 4.257909 to 1.453484, Isolation Forest score from 0.517611 to 0.437459, and KMeans distance from 3.430534 to 2.994384. Project verdict: `Strong`.

### Separate WeightedRoll evidence

Raw modulation 1.5185353234%; fitted phase 158.0021530363°; reduced chi-square 0.7134283152; 357 degrees of freedom and 360 bins; project category `acceptable`. It is included in the 13-fit blank-sky reference. Separate visual inspection was not part of the new figure: **NOT VERIFIED visually** beyond saved statistics.

### WHY THIS OBSERVATION IS INTERESTING TO THE FRAMEWORK

Blank Sky-5 illustrates the threshold neighborhood. It is fixed candidate number four but is selected in only 29/100 seeds and is feature-tier dependent. Its leading evidence points to source-azimuth and exposure summaries, while its WeightedRoll fit is acceptable and part of the empirical reference. It should be described as seed-sensitive, not as part of an unqualified robust set.

**Not supported:** confirmed anomaly or a physical explanation for the exposure/source-azimuth values.

## 5. Crab P01_0005 — fixed-Normal comparison

### Identity and screening evidence

| Field | Verified value |
|---|---|
| Observation name | Crab |
| Full observation ID | `X01_PLX_P01_0005_000000` |
| Project role | Source |
| Fixed Isolation Forest score | 0.504655627700 |
| Fixed label | Normal; Matrix-C rank 6 |
| Random-seed result | 3/100; rank range 4–10 |
| Contamination sensitivity | Selected only at contamination 0.24 |
| Included-observation jackknife | 2/24 |
| Held-out refit | Not selected; rank 7 |
| Matrix A/B/C | Selected in A (rank 4); not selected in B (rank 6) or C (rank 6) |
| PCA coordinates / distance | PC1 -3.651387; PC2 -0.615167; distance 3.702845 |
| KMeans | Cluster 1; cluster size 9 |

### Current exact local ranking

The current deployed function can rank any row, including a fixed-Normal row:

| Rank | Feature | Score | Raw value | Archive-relative z | Product family |
|---:|---|---:|---:|---:|---|
| 1 | Cross-detector PHA-centroid spread | 3.225533 | 148.133373 | +1.965285 | Tier-2 Detector Balance |
| 2 | Count-weighted mean channel | 2.886397 | 1711.619489 | -1.921544 | Tier-1A EnergyRes |
| 3 | Channel-distribution entropy | 2.395070 | 12.0232346 | -1.713794 | Tier-1A EnergyRes |

Crab P01_0005 was not one of the six neutralization cases: **NOT TESTED**.

### Separate WeightedRoll evidence

| Quantity | Verified value |
|---|---:|
| C | 174.0500616110 |
| Q | 2.4689753581 |
| U | -1.6222345736 |
| Amplitude | 2.9542315973 |
| Raw modulation | 1.6973459073% |
| Fitted phase | 163.3465886107° |
| Reduced chi-square | 1.0625397079 |
| Degrees of freedom / bins | 357 / 360 |
| Project category | Acceptable |
| Declared scalar blank-sky rule | Within; z = +0.970962 |

The audited figure shows a clearly represented second-harmonic pattern and residuals small enough to meet the declared rule.

### WHY THIS OBSERVATION IS INTERESTING TO THE FRAMEWORK

Crab P01_0005 has a larger raw modulation than Sco X-1, Her X-1, and Blank Sky-13, yet it is fixed Normal in Matrix C. Its earlier Matrix-A selection and later disappearance also demonstrate feature-tier dependence. It is therefore a strong counterexample to any claim that raw harmonic amplitude defines the ML candidate label.

**Supported:** useful fixed-Normal comparison and evidence of branch non-equivalence.

**Not supported:** “normal” meaning scientifically uninteresting, unpolarized, or free from product-level structure.

## Cross-case conclusion

These five cases jointly support only an archive-bounded triage interpretation. Matrix-C labels identify observations that are comparatively isolated in the selected 15-feature representation. Local ranking identifies which engineered features contribute most strongly under the project heuristic. WeightedRoll separately reports how well a second harmonic summarizes the delivered curve. None of the three outputs supplies anomaly ground truth or calibrated polarization.
