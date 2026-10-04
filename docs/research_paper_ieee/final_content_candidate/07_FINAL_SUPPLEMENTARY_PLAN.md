# Final Supplementary-Material Plan

No new analysis is authorized. The supplement will organize existing evidence and expose implementation differences that are too detailed for the main paper.

## S1. Data and feature specification

- Archive identifier and role table for all 25 observations.
- Exact Matrix A/B/C/WR schemas.
- All 15 Matrix-C formulas, source products, units/status, edge handling, and approved proxy wording.
- Explicit statement that Matrix C has zero missing cells and the deployed path contains no imputer.

## S2. Frozen model and sensitivity evidence

- Saved-model metadata and SHA-256 values.
- Complete 100-seed flag-frequency table.
- Contamination-threshold sensitivity table, described as threshold persistence over one ordering.
- Included-observation jackknife and held-out rows, explicitly not external validation.
- Matrix A/B/C comparison and separate WR diagnostic results.
- Descriptive ranking correlations without inferential use of nominal p-values.

## S3. Local explanation method

- Exact four-component equations and within-observation normalization.
- All 15 Sco X-1 feature scores from the accepted exact-function audit.
- Historical entropy-first result recorded only as superseded provenance.
- Six exploratory feature-neutralization rows, direct before/after values, and project-defined verdict rules.
- Explicit note that KMeans reduction is not used in the overall Strong/Moderate/Weak verdict.

## S4. Harmonic analysis

- All 25 weighted second-harmonic fit rows.
- Coefficient, raw-modulation, fitted-phase, and project fit-quality fields.
- All 15 blank-sky rows and the 13-fit selection.
- Complete source-versus-blank-sky comparison.
- No official Stokes, polarization-degree, polarization-angle, background-subtraction, or detection claim.

## S5. Uncertainty implementation comparison

- Frozen Notebook-11 formula and the saved CSV provenance.
- Later Flask three-parameter gradient formula.
- Explanation that the two \(A/C\) uncertainty implementations are not numerically identical.
- No corrected or regenerated result is introduced; the difference is disclosed as versioned implementation history.

## S6. Optional sensitivity proxies

Assumed-\(\mu_{100}\) scenarios may be included only after guide approval and only as sensitivity diagnostics. They must not be described as calibrated measurements. The preferred default is omission from the submitted supplement because they are unnecessary for the central methodology argument.

## Deferred future work—not supplement results

- Prospective evaluation on a later POLIX release.
- Expert adjudication of candidate relevance.
- Matched/random explanation perturbation baselines.
- Target-grouped validation.
- KMeans stability analysis.
- Covariance-aware or matched blank-sky analysis.
- Official background, response, \(\mu_{100}\), and sky-angle calibration.

These items are not executed and must not be written as completed work.
