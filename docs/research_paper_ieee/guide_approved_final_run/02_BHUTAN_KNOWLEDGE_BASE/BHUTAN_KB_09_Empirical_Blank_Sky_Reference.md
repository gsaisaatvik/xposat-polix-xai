# BHUTAN Knowledge Card 09 — Empirical Blank-Sky Reference

## Beginner explanation

The project-labelled blank-sky observations show the raw harmonic behaviour present in this archive. Acceptably fitted blank-sky curves form a descriptive comparison rule for source observations. The result is not an official background correction or a statistically calibrated detection region.

## Technical theory

The reference uses 13 of 15 blank-sky observations whose fits satisfy reduced chi-square \(\le2\). It summarizes scalar raw modulation and fractional harmonic coordinates \(q=Q/C\) and \(u=U/C\). The scalar diagnostic is

\[
z_m=\frac{m_{\mathrm{raw}}-\bar m_{\mathrm{blank}}}{s_{\mathrm{blank}}},
\]

with the declared rule \(-2<z_m<2\). Separate sample means and standard deviations summarize \(q\) and \(u\). No covariance-aware confidence ellipse or probability coverage is estimated.

## Exact project implementation and parameters

- Total project-labelled blank skies: 15.
- Selected reference: 13 fits satisfying the declared acceptable rule.
- Scalar comparison: mean plus/minus two sample standard deviations.
- Coordinate comparison: component-wise sample mean and sample standard deviation.
- A historical diagonal standardized-distance diagnostic ignores \(q/u\) covariance, fit uncertainty and baseline-estimation uncertainty; it is not a sigma significance.

## Controlling sources and cells

- `D:\ISROtrial\Polix_L2_full_archive\11_POLIX_Polarization_Parameter_Analysis.ipynb`: labelled Cell 14 / JSON index 13 for blank-sky selection and scalar comparison; labelled Cell 15 / index 14 for fractional coordinates.
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\04_polarimetry_results\path2_blank_sky_modulation_baseline.csv`.
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\04_polarimetry_results\path2_source_vs_blank_sky_modulation_comparison.csv`.
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\04_polarimetry_results\path2_all_observations_fractional_qu_vectors.csv`.

## Verified numerical results

For the 13-fit reference:

- mean raw modulation: 1.147820%; sample SD: 0.565960%;
- median: 1.492835%; minimum: 0.294127%; maximum: 1.778927%;
- mean \(q\): 0.009092005; sample SD: 0.004856906;
- mean \(u\): -0.006478172; sample SD: 0.004019024.

All ten source raw-modulation values fall within the declared empirical mean-plus/minus-two-sample-SD rule. This does not imply zero polarization or statistical identity with blank sky.

## Safe inference

The 13 accepted blank-sky fits provide an archive-specific empirical reference for raw harmonic summaries. The ten source values do not cross the declared scalar rule in this archive.

## Unsupported inference

Do not call the reference official background subtraction, a background model, a confidence interval, a detection region, a polarization null distribution, or proof of no polarization.

## Paper-ready wording

> Thirteen of the 15 project-labelled blank-sky observations satisfied the declared acceptable-fit rule of reduced chi-square \(\le2\) and formed a descriptive empirical reference. Their mean raw modulation was 1.147820%, with sample standard deviation 0.565960%. All ten source values remained within the declared empirical blank-sky reference rule. This archive-specific comparison is neither an official background-subtraction procedure nor a calibrated confidence region.

## Likely reviewer challenge and safe answer

**Question:** Does selecting only 13 blank skies bias the reference?

**Safe answer:** Selection is conditioned on a predeclared fit-quality rule because the scalar summary is difficult to interpret for poorly fitted curves. This creates a selected, archive-specific reference and is disclosed as a limitation; it is not presented as a population model or formal null distribution.

