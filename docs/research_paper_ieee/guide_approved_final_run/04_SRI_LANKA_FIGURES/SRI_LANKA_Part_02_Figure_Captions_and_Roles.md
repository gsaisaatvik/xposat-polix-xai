# SRI LANKA Part 02 — Figure Captions and Roles

## Main-paper figure set

### Fig. 1 — Corrected framework architecture

**Role:** Explanatory methodology diagram; proposed two-column width.

**Caption:** Product-aware screening and independent harmonic-diagnostic architecture. Exposure, channel-space, source-azimuth, delivered-light-curve and detector-context products are summarized in the 15-feature Matrix C and standardized. Principal Component Analysis (PCA), KMeans and Isolation Forest receive the same standardized representation; only Isolation Forest determines the fixed Normal/candidate label. The deterministic local ranking combines feature-level PCA, KMeans, Isolation Forest occlusion and absolute standardized-deviation evidence. WeightedRoll is excluded from Matrix C and fitted separately using a weighted second harmonic and the 13-fit empirical blank-sky reference. The two branches are compared for researcher interpretation without confidence fusion or calibrated polarization output.

**What the reader should learn:** The architecture is a fan-out from standardized Matrix C, not a sequential PCA-to-KMeans-to-Isolation-Forest chain. WeightedRoll is intentionally separate.

**What the figure must not imply:** Joint model voting, confidence fusion, official background subtraction, calibrated polarization degree or official sky polarization angle.

### Fig. 2 — Matrix-C PCA observation space

**Role:** Descriptive result figure; proposed one-column width.

**Caption:** Two-component PCA projection of the 25 standardized Matrix-C observations. Circles denote project-labelled source observations, squares denote project-labelled blank-sky observations, and open diamonds identify the four fixed Isolation Forest candidates. PC1 and PC2 account for 38.74% and 22.51% of standardized variance, respectively. The projection is a descriptive view of archive geometry; it neither determines nor independently validates candidate status.

**What the reader should learn:** The four fixed candidates occupy visibly separated parts of the two-dimensional projection, but the plot preserves only 61.25% of standardized variance.

**What the figure must not imply:** Anomaly ground truth, astrophysical classes, full information preservation or prospective separation.

### Fig. 3 — Fixed Isolation Forest ranking and seed frequency

**Role:** Primary machine-learning result figure; proposed two-column width.

**Caption:** Fixed Isolation Forest anomaly-score ranking for all 25 observations. Bar colour and label shape encode project observation role; hatched outlines identify the four candidates returned by the frozen model. The annotation beside each bar reports the number of selections across 100 tested Isolation Forest seeds at contamination 0.16. Blank Sky-13, Sco X-1 and Her X-1 were selected in 100/100 runs, whereas fixed candidate Blank Sky-5 was selected in 29/100. These are algorithmic selection frequencies, not anomaly probabilities or confidence levels.

**What the reader should learn:** The fixed four and tested-seed persistence are different results. Blank Sky-15 is a fixed-Normal boundary competitor selected in 68/100 runs.

**What the figure must not imply:** Probability, predictive accuracy, a statistically calibrated threshold or confirmed anomalies.

### Fig. 4 — Fractional harmonic diagnostic space

**Role:** Primary independent-diagnostic result figure; proposed two-column width.

**Caption:** Fractional second-harmonic coordinates \(q=Q/C\) and \(u=U/C\) for the 25 WeightedRoll fits. Circles denote source observations; filled squares denote the 13 blank-sky fits satisfying the declared reduced-chi-square rule \(\chi^2_\mathrm{red}\le2\); open squares denote the two blank-sky fits excluded by that rule; and open diamonds identify the four fixed Matrix-C candidates. The cross shows the component-wise sample mean plus or minus one sample standard deviation of the 13-fit reference. It is a descriptive summary, not a confidence region, detection contour or official background model.

**What the reader should learn:** Fixed candidates and harmonic coordinates do not agree one-to-one. Sco X-1 and the two blank-sky candidates provide visible examples, while Crab P01_0005 is fixed Normal despite a comparatively large raw harmonic amplitude.

**What the figure must not imply:** Calibrated Stokes parameters, polarization detection, statistical significance, covariance-aware confidence coverage or official background subtraction.

## Result versus explanation classification

| Figure | Classification | Evidence role |
|---|---|---|
| Fig. 1 | Explanatory diagram | Communicates the verified implementation and branch separation |
| Fig. 2 | Descriptive result | Shows the frozen Matrix-C PCA geometry |
| Fig. 3 | Primary ML result | Reports fixed scores, labels and tested-seed frequencies |
| Fig. 4 | Primary physical-diagnostic result | Reports saved fractional harmonic coordinates and the selected empirical reference |

## Supplementary-only candidates

These are reserved for later guide selection and were not generated in this phase:

1. Representative WeightedRoll curve with saved second-harmonic fit and residuals.
2. Compact local-XAI component view for Sco X-1 using the accepted deployed-function output.
3. Full seed, contamination, jackknife and feature-tier plots.
4. All-observation harmonic-fit panels.

No supplementary figure should be generated merely to increase figure count.

