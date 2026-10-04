# NEPAL Part 04 - Controlling Numerical Results

## Data and representation

| Quantity | Verified value | Primary control |
|---|---:|---|
| Observations | 25 | Matrix C and role table |
| Project-labelled sources | 10 | Role table |
| Project-labelled blank skies | 15 | Role table |
| Matrix A features | 8 | Matrix A CSV |
| Matrix B features | 11 | Matrix B CSV |
| Matrix C features | 15 | Matrix C CSV |
| WR diagnostic features | 6 | WR CSV |
| Matrix-C missing values | 0 | Matrix-C cell audit |

The full observation ID is the unique key. The friendly label `Blank Sky-2` occurs for both C24_0001 and C24_0008 and must not be silently corrected.

## Frozen deployed model

- `StandardScaler`; no imputer.
- PCA: two components. PC1 explains 0.387435 and PC2 explains 0.225051 of standardized Matrix-C variance; combined 0.612486.
- KMeans: `k=5`, `n_init=20`, random state 42; in-sample silhouette 0.310936.
- Isolation Forest: 100 trees, contamination 0.16, random state 42.
- Only `IsolationForest.predict` defines the fixed label.

### Fixed output

| Rank | Observation | Project label | Score | Fixed result |
|---:|---|---|---:|---|
| 1 | C24_0018 | Blank Sky-13 | 0.615963875 | Anomaly candidate |
| 2 | G01_0006 | Sco X-1 | 0.593516133 | Anomaly candidate |
| 3 | G01_0003 | Her X-1 | 0.572308197 | Anomaly candidate |
| 4 | C24_0010 | Blank Sky-5 | 0.517611306 | Anomaly candidate |

**Count:** 21 Normal and four archive-relative anomaly candidates. All 25 saved labels and scores were reproduced exactly in the existing audit, with maximum score difference zero.

## Procedure-qualified stability

### Isolation Forest seeds 0–99

| Observation | Times selected |
|---|---:|
| Blank Sky-13 | 100/100 |
| Sco X-1 | 100/100 |
| Her X-1 | 100/100 |
| Blank Sky-15 | 68/100; fixed label Normal |
| Blank Sky-5 | 29/100; fixed label Anomaly |
| Crab P01_0005 | 3/100; fixed label Normal |

These frequencies are not probabilities or confidence levels.

### Contamination sensitivity

The existing audit tested contamination 0.12, 0.16, 0.20 and 0.24, which selected the first 3, 4, 5 and 6 rows of one fixed score ordering.

- Blank Sky-13, Sco X-1 and Her X-1: selected under 4/4 settings.
- Blank Sky-5: 3/4.
- Blank Sky-15: 2/4.
- Crab P01_0005: 1/4.

This is threshold sensitivity, not independent validation.

### Included-observation jackknife

- Blank Sky-13, Sco X-1 and Her X-1: flagged in all 24/24 refits in which each remained in the training subset.
- Blank Sky-5: 19/24.
- Blank Sky-15: 7/24.
- Crab P01_0005: 2/24.
- Common-observation ranking: median Spearman rho 0.989565; minimum 0.968696.
- In Sco X-1’s single held-out refit, it was not flagged.

This is retrospective influence analysis, not held-out generalization.

### Feature-tier persistence

| Matrix | Candidate IDs |
|---|---|
| A | C24_0018, C24_0020, G01_0006, P01_0005 |
| B | C24_0010, C24_0018, C24_0020, G01_0006 |
| C | C24_0010, C24_0018, G01_0003, G01_0006 |

Only Blank Sky-13 and Sco X-1 persist across A/B/C. Her X-1 is Matrix-C-specific. This does not prove Matrix C is superior.

## Ranking agreement

| Pair | Spearman rho | Nominal p-value |
|---|---:|---:|
| PCA distance vs. Isolation Forest score | 0.894615 | 1.6365e-9 |
| PCA distance vs. KMeans distance | 0.155799 | 0.457074 |
| KMeans distance vs. Isolation Forest score | 0.186574 | 0.371863 |

These are descriptive within-archive correlations. Their p-values do not validate the candidates or establish independence among components.

## Current Sco X-1 local ranking

| Rank | Feature | Exact score | Main-paper score |
|---:|---|---:|---:|
| 1 | `t1A_energy_peak_channel` | 2.4544990315 | 2.454 |
| 2 | `t1A_energy_weighted_mean_channel` | 2.2073686585 | 2.207 |
| 3 | `t1A_energy_channel_entropy` | 1.8139679863 | 1.814 |
| 4 | `t1B_src_roll_smoothness_norm` | 0.7066471342 | supplementary |
| 5 | `t1A_energy_high_channel_fraction` | 0.6878486945 | supplementary |

The remaining exact order is preserved in `deployed_xai_exact_from_model_service.csv`. Sco X-1 is a singleton KMeans cluster, so its KMeans contribution is zero for every feature. The historical entropy-first narrative is not reproducible from a located versioned artifact and is superseded.

## Six-case perturbation check

Cases: Sco X-1, Blank Sky-13, Her X-1, Blank Sky-5, Blank Sky-15 and Blank Sky-6.

- Five Strong.
- One Moderate: Blank Sky-6.
- Zero Weak.

Strong means PCA distance and Isolation Forest score both decrease after jointly setting the top three standardized features to zero. Moderate means exactly one decreases. KMeans is calculated but does not enter the verdict. This is a sign-only, in-sample sanity check.

## Harmonic fitting

The saved Notebook-11 analysis fits

\[
y(\phi)=C+Q\cos(2\phi)+U\sin(2\phi)
\]

to 360 WeightedRoll bins using inverse-variance weighted least squares. All saved fits have 357 degrees of freedom.

Project definitions:

- amplitude: `sqrt(Q^2 + U^2)`;
- raw modulation: `100 sqrt(Q^2 + U^2) / C`;
- fitted modulation phase: `0.5 atan2(U,Q) mod 180 degrees`;
- fractional harmonic coordinates: `q=Q/C`, `u=U/C`.

These quantities are not calibrated polarization degree, official sky polarization angle or polarization significance.

### Fit categories

| Category | Declared rule | Count |
|---|---|---:|
| Acceptable | reduced chi-square <= 2 | 19 |
| Caution | 2 < reduced chi-square <= 5 | 3 |
| Poor simple-harmonic fit | reduced chi-square > 5 | 3 |

These are project-defined descriptive categories, not p-values or detection thresholds.

## Empirical blank-sky reference

- Blank-sky observations fitted: 15.
- Qualifying fits: 13, selected by reduced chi-square <= 2.
- Mean raw modulation: 1.147820%.
- Sample standard deviation: 0.565960%.
- Median: 1.492835%.
- Minimum: 0.294127%.
- Maximum: 1.778927%.
- Mean fractional cosine coordinate: 0.009092005; sample SD 0.004856906.
- Mean fractional sine coordinate: -0.006478172; sample SD 0.004019024.

All ten source raw-modulation values lie within the declared empirical mean plus or minus two sample-standard-deviation scalar rule. This is descriptive; it is not a confidence interval and does not imply zero polarization.

## Representative values

| Observation | Fixed ML result | Raw modulation (%) | Fitted phase (deg) | Reduced chi-square | Fit class | q | u |
|---|---|---:|---:|---:|---|---:|---:|
| Sco X-1 | Candidate | 1.139578 | 165.527814 | 2.030761 | caution | 0.0099723 | -0.0055151 |
| Her X-1 | Candidate | 0.596632 | 124.639464 | 57.433514 | poor | -0.0021110 | -0.0055804 |
| Crab P01_0005 | Normal | 1.697346 | 163.346589 | 1.062540 | acceptable | 0.0141854 | -0.0093205 |
| Blank Sky-13 | Candidate | 0.853951 | 158.783354 | 2.565811 | caution | 0.0063027 | -0.0057619 |
| Blank Sky-5 | Candidate | 1.518535 | 158.002153 | 0.713428 | acceptable | 0.0109242 | -0.0105478 |

The representative cases support only the within-archive non-equivalence of Matrix-C unusualness and raw harmonic behaviour.

## Controlling conclusion

> The frozen Matrix-C artifact returned four archive-relative anomaly candidates. Three form a Matrix-C core stable under the tested seed, contamination-threshold and included-observation procedures, while Blank Sky-5 is seed-sensitive. The separate WeightedRoll analysis provides raw harmonic summaries and an empirical 13-fit blank-sky reference. The two branches do not agree one-to-one within the 25-observation project archive.

