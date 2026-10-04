# BANGLADESH Part 03 — Independent Harmonic Results

## Branch definition

The WeightedRoll branch is scientifically and computationally separate from Matrix C. It fits the delivered 360-bin exposure-weighted total-count-rate curve with

\[
y(\phi)=C+Q\cos(2\phi)+U\sin(2\phi)
\]

using inverse-variance weighted least squares. The reported quantities are cosine and sine second-harmonic coefficients, fractional harmonic coordinates \(q=Q/C\) and \(u=U/C\), raw modulation \(100\sqrt{Q^2+U^2}/C\), fitted modulation phase and a project-defined fit category. They are not calibrated polarization degree, official sky polarization angle or polarization significance.

## All-observation fit status

- Saved fits: 25/25 observations.
- Bins per fit: 360; degrees of freedom: 357.
- Acceptable, reduced chi-square \(\le2\): 19.
- Caution, \(2<\) reduced chi-square \(\le5\): 3.
- Poor simple-harmonic fit, reduced chi-square \(>5\): 3.

The category boundaries are declared project rules, not p-values or calibrated goodness-of-fit decisions.

## Blank-sky empirical reference

Fifteen project-labelled blank-sky observations were fitted. Thirteen satisfied reduced chi-square \(\le2\) and formed the declared empirical reference. Blank Sky-13 (`C24_0018`, reduced chi-square 2.565811) and Blank Sky-6 (`C24_0023`, 6.920304) were excluded by that rule.

| Reference quantity | Verified value |
|---|---:|
| Accepted blank-sky fits | 13 |
| Mean raw modulation | 1.147820% |
| Sample SD of raw modulation | 0.565960% |
| Median raw modulation | 1.492835% |
| Minimum raw modulation | 0.294127% |
| Maximum raw modulation | 1.778927% |
| Mean \(q\) | 0.009092005 |
| Sample SD of \(q\) | 0.004856906 |
| Mean \(u\) | -0.006478172 |
| Sample SD of \(u\) | 0.004019024 |

The scalar rule compares a source raw-modulation value with the blank-sky mean plus/minus two sample standard deviations. It is a descriptive archive rule, not a confidence interval, detection region or null distribution. The component-wise \(q/u\) summary is not covariance-aware.

## All ten source observations

| ID | Target | Fixed ML label | Raw modulation (%) | Reduced chi-square | Fit category | \(q\) | \(u\) |
|---|---|---|---:|---:|---|---:|---:|
| C24_0026 | Cas-A SNR | Normal | 0.692664 | 1.702988 | Acceptable | 0.0050391 | -0.0047525 |
| G01_0002 | Cen X-3 | Normal | 0.928623 | 1.897200 | Acceptable | 0.0086469 | -0.0033860 |
| G01_0003 | Her X-1 | Candidate | 0.596632 | 57.433514 | Poor | -0.0021110 | -0.0055804 |
| G01_0004 | GX 301-2 | Normal | 0.722337 | 4.374479 | Caution | 0.0030149 | -0.0065641 |
| G01_0005 | 4U 1700-37 | Normal | 1.080606 | 1.229127 | Acceptable | 0.0069412 | -0.0082820 |
| G01_0006 | Sco X-1 | Candidate | 1.139578 | 2.030761 | Caution | 0.0099723 | -0.0055151 |
| P01_0005 | Crab | Normal | 1.697346 | 1.062540 | Acceptable | 0.0141854 | -0.0093205 |
| T24_0001 | Crab | Normal | 1.395515 | 0.814632 | Acceptable | 0.0134580 | -0.0036916 |
| T24_0002 | Crab | Normal | 1.200778 | 1.367146 | Acceptable | 0.0084931 | -0.0084884 |
| T24_0007 | Cyg X-1 | Normal | 0.681147 | 5.408023 | Poor | 0.0035773 | -0.0057964 |

All ten source raw-modulation values remain within the declared empirical blank-sky reference rule. This does not imply absence of polarization, equivalence to blank sky or successful background subtraction.

## Uncertainty provenance

Any manuscript uncertainty values must come from the frozen Notebook-11 CSV. Notebook 11 propagates \(A/C\) uncertainty through relative quadrature and omits amplitude–mean covariance. The later Flask implementation uses a full three-parameter gradient containing covariance terms. The two implementations are not numerically identical; their detailed comparison belongs in supplementary material and their values must not be merged.

## Exact proposed Results claims

**H-R1.** Weighted second-harmonic fits were saved for all 25 observations; 19 met the declared acceptable rule, three were caution and three were poor simple-harmonic fits.

**H-R2.** Thirteen of 15 project-labelled blank-sky observations met reduced chi-square \(\le2\) and formed the empirical reference.

**H-R3.** The 13-fit reference had mean raw modulation 1.147820% and sample standard deviation 0.565960%.

**H-R4.** All ten source raw-modulation values remained within the declared empirical blank-sky reference rule.

**H-R5.** The source fits included six acceptable, two caution and two poor fits; fit category must accompany interpretation of the corresponding harmonic values.

## Exact proposed Discussion claims

**H-D1.** The blank-sky comparison is an archive-specific descriptive diagnostic, not official background subtraction, a confidence region or a polarization null test.

**H-D2.** A raw-modulation value within the declared reference rule does not establish zero polarization.

**H-D3.** A poor reduced-chi-square category indicates that the chosen second harmonic does not summarize the delivered curve well; it does not establish a physical cause.

**H-D4.** Because WeightedRoll is excluded from Matrix C, the harmonic branch provides a non-circular comparison with the fixed screening result.

## Controlling evidence

- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\04_polarimetry_results\polix_weightedroll_raw_modulation_fits.csv`
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\04_polarimetry_results\path2_blank_sky_modulation_baseline.csv`
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\04_polarimetry_results\path2_source_vs_blank_sky_modulation_comparison.csv`
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\04_polarimetry_results\path2_all_observations_fractional_qu_vectors.csv`
- `D:\ISROtrial\Polix_L2_full_archive\11_POLIX_Polarization_Parameter_Analysis.ipynb`, labelled Cells 7, 8, 14 and 15.
