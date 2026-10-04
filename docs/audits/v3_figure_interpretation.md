# Version-3 Scientific Interpretation of Audited Figures

## Figure 1 — Corrected architecture

### Evidence role

This is an explanatory diagram, not an empirical result. It should show:

- selected Level-2 product families mapped into 15 Matrix-C features;
- one saved StandardScaler feeding PCA, KMeans, and Isolation Forest in parallel;
- Isolation Forest alone setting the fixed Normal/candidate label;
- the four-component local ranking using the standardized row and saved objects;
- WeightedRoll excluded from Matrix C and analysed in a separate harmonic branch;
- researcher comparison without automated confidence fusion.

### Safe inference

The workflow preserves product provenance and prevents WeightedRoll from being used both as a primary anomaly input and as apparent physical confirmation.

### Unsafe inference

The branches are not proven statistically independent. PCA and KMeans do not vote on the fixed label. The architecture does not establish model accuracy or physical validity.

## Figure 2 — Matrix-C PCA projection

### Evidence role

The saved PC1 and PC2 coordinates provide a partial two-dimensional view of archive geometry. PC1 explains 38.7435% and PC2 22.5051%; together they explain 61.2486% of standardized variance.

### Safe inference

The four fixed candidates occupy visible positions in the first-two-component projection, and Her X-1 and Blank Sky-13 are visibly separated in different directions.

### Unsafe inference

Two-dimensional visual separation does not determine or validate the Isolation Forest label. Approximately 38.75% of standardized variance lies outside the displayed subspace. This is the first figure to move to supplementary material if space is limited.

## Figure 3 — Isolation Forest ranking and seed frequency

### Evidence role

This is the primary machine-learning result figure. It shows all 25 fixed scores, the four fixed candidates, and each observation's selection count across seeds 0–99 at contamination 0.16.

### Safe inference

- Fixed result: 21 Normal and four candidates.
- Blank Sky-13, Sco X-1, and Her X-1: 100/100 seed selections.
- Blank Sky-5: 29/100 and therefore seed-sensitive.
- Blank Sky-15: fixed Normal but selected in 68/100, revealing a boundary neighborhood.

### Unsafe inference

Selection frequency is not an anomaly probability or confidence. Score magnitude is not physical significance. The fixed candidate count is contamination-defined.

## Figure 4 — Fractional second-harmonic coordinates

### Evidence role

This figure plots q=Q/C and u=U/C for all 25 saved WeightedRoll fits. The 13 filled blank-sky points meet the declared reduced-chi-square ≤2 rule. The cross is their component-wise sample mean ± sample standard deviation.

### Safe inference

Candidate outlines and source/blank roles do not occupy a unique or one-to-one harmonic region. The plot supports descriptive diagnostic discordance within this archive.

### Unsafe inference

q and u are not calibrated Stokes parameters. The cross is not a confidence ellipse, detection contour, official background model, or significance region.

## New Figure A — Representative delivered WeightedRoll curves and saved fits

### Source trace

Each panel reads 360 rows directly from the named `WeightedRoll_L2.fits` file. The blue points use `ROLL_AZ_ANG` and `TOTAL_COUNTRATE`; vertical bars use the supplied `ERROR`. The orange curve evaluates the already-saved C, Q, and U values from `polix_weightedroll_raw_modulation_fits.csv`; no refit is performed. The lower panels show `(delivered rate - saved fit)/supplied error`.

Numerical and SHA-256 provenance is recorded in `figure_audit_support/weightedroll_figure_verification.csv` and `figure_audit_support/figure_provenance.csv`.

### Sco X-1

| Quantity | Value |
|---|---:|
| C | 170.9322321582 |
| Q | 1.7045938152 |
| U | -0.9427094972 |
| Amplitude | 1.9479068948 |
| Raw modulation | 1.1395784576% |
| Fitted phase | 165.5278135509° |
| Reduced chi-square | 2.0307608048 |
| Degrees of freedom / bins | 357 / 360 |
| Project category | Caution |
| Fixed ML label | Candidate |

The delivered curve has an evident second-harmonic component, but the residuals retain broad angle-dependent structure. The saved fit is a caution-category summary rather than an adequate physical model.

### Crab P01_0005

| Quantity | Value |
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
| Fixed ML label | Normal |

Crab is useful because it is fixed Normal despite a larger raw harmonic amplitude than Sco X-1 and Her X-1. Its simple harmonic meets the declared fit rule. This makes it a direct counterexample to interpreting raw amplitude as the ML decision variable.

### Her X-1

| Quantity | Value |
|---|---:|
| C | 154.6131073683 |
| Q | -0.3263876873 |
| U | -0.8628001664 |
| Amplitude | 0.9224711647 |
| Raw modulation | 0.5966319288% |
| Fitted phase | 124.6394640851° |
| Reduced chi-square | 57.4335137536 |
| Degrees of freedom / bins | 357 / 360 |
| Project category | Poor simple-harmonic fit |
| Fixed ML label | Candidate |

Her X-1 contains large localized excursions and residuals reaching many tens of supplied-error units. The curve visibly contains structure that the saved second harmonic cannot describe. The high reduced chi-square is therefore not merely a numerical label; it is visually supported by the residual pattern.

### Cross-panel conclusion

The panels strengthen the non-equivalence result:

- a candidate can have a raw harmonic value within the declared empirical blank-sky rule;
- a fixed-Normal observation can have a larger raw harmonic amplitude than candidates;
- a candidate can coexist with an inadequate harmonic summary.

They do not show calibrated polarization, physical cause, or instrumental fault.

### Publication-safe caption basis

“Delivered 360-bin WeightedRoll total-count-rate curves with supplied uncertainties and saved weighted second-harmonic summaries. Lower panels show residuals divided by supplied errors. These are raw delivered and harmonic diagnostics, not calibrated polarization measurements.”

## New Figure B — Archive-relative explanation of Sco X-1

### Exact verified values

| Feature | Raw Matrix-C value | Standardized z | Project local-ranking score | Product family |
|---|---:|---:|---:|---|
| Energy peak channel | 465 | +4.894105812 | 2.454499032 | Tier-1A EnergyRes |
| Count-weighted mean channel | 1648.330999702 | -3.432505250 | 2.207368658 | Tier-1A EnergyRes |
| Channel-distribution entropy | 11.993394700 | -2.855661897 | 1.813967986 | Tier-1A EnergyRes |

The raw values come from the frozen Matrix-C row. The z-values are produced by the saved StandardScaler fitted on all 25 Matrix-C rows. The scores come from the exact current `model_service.py` function and saved PKL. The figure-generation verification confirms the saved-scaler z-values equal the deployed XAI CSV values to numerical precision.

### Why these three rank highest

The ranking is not determined by the z-value alone. Each feature receives four within-observation components:

1. magnitude along the first two PCA loading directions, weighted by explained-variance ratios;
2. squared deviation from the assigned KMeans centroid;
3. positive change in Isolation Forest score when that standardized coordinate is replaced with zero;
4. absolute standardized magnitude.

Each component is separately divided by its maximum absolute value across the 15 features and the four normalized values are added with equal implicit weight. For Sco X-1, its KMeans cluster is a singleton, so every KMeans contribution is exactly zero. The top three therefore rank highly because they combine large archive-relative deviations, material PCA terms, and positive Isolation Forest occlusion changes. Peak channel has the largest positive z and the largest occlusion term; weighted mean and entropy have large negative z-values and large PCA/positive occlusion terms.

### Interpretation boundary

- Ranking magnitude is ordinal within Sco X-1. It is not calibrated across observations.
- z-values are relative to the means and scales fitted on this 25-row archive.
- Peak and mean are channel indices, not calibrated energies.
- Entropy is a Shannon summary of the collapsed channel-count distribution, not physical entropy.
- The reader may conclude that the current framework directs inspection toward the EnergyRes product family for Sco X-1.
- The reader may not conclude that an energy-spectrum change caused the label or has an astrophysical origin.

### Publication-safe factual interpretation

Sco X-1 lies far from the archive centre in three channel-space summaries, and those same summaries receive the highest composite local-ranking scores under the deployed heuristic. This identifies where a researcher should inspect the underlying EnergyRes product. It does not establish a calibrated spectral anomaly or physical cause.

## Figure-space recommendation

Main-paper priority:

1. Isolation Forest ranking;
2. Sco X-1 XAI case study;
3. representative WeightedRoll curves;
4. fractional harmonic-coordinate plot;
5. architecture diagram;
6. PCA projection.

If page space is strict, move the PCA projection to supplementary material before removing either new figure.
