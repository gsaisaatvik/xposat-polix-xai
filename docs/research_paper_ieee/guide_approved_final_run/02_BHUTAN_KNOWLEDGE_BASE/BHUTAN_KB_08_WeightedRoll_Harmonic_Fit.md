# BHUTAN Knowledge Card 08 — WeightedRoll and Second-Harmonic Fitting

## Beginner explanation

WeightedRoll supplies a 360-bin curve of delivered exposure-weighted total count rate versus roll angle. It is kept outside the machine-learning feature matrix. A repeating second-harmonic curve summarizes its mean level, cosine and sine terms, raw modulation and fitted phase. These are diagnostic summaries, not calibrated polarization measurements.

## Technical theory

For roll angle \(\phi\),

\[
y(\phi)=C+Q\cos(2\phi)+U\sin(2\phi).
\]

Here \(C\) is the fitted mean level, and \(Q\) and \(U\) are cosine and sine second-harmonic coefficients. The project derives

\[
A=\sqrt{Q^2+U^2},\qquad
m_{\mathrm{raw}}=100\frac{A}{C},
\]

\[
\psi_{\mathrm{fit}}=\tfrac12\operatorname{atan2}(U,Q)\pmod{180^\circ},
\qquad q=Q/C,\quad u=U/C.
\]

The letters \(Q\) and \(U\) are coefficient names in the code. The manuscript uses “cosine/sine second-harmonic coefficients” and “fractional harmonic coordinates,” not unqualified calibrated Stokes terminology.

## Exact project implementation and parameters

Notebook 11 reads finite angle, total-count-rate and positive-error values; forms `[1, cos(2phi), sin(2phi)]`; applies weights \(w_i=1/\sigma_i^2\); solves the weighted normal equations; and derives residuals, chi-square, reduced chi-square, amplitude, raw modulation, phase, \(q\) and \(u\). All saved fits use 360 bins and 357 degrees of freedom.

Project fit categories are:

- acceptable: reduced chi-square \(\le2\);
- caution: \(2<\) reduced chi-square \(\le5\);
- poor simple-harmonic fit: reduced chi-square \(>5\).

They are descriptive project rules, not p-values or polarization-detection thresholds. WeightedRoll is not an input to Matrix C or the fixed Isolation Forest label.

## Controlling sources and cells

- `D:\ISROtrial\Polix_L2_full_archive\11_POLIX_Polarization_Parameter_Analysis.ipynb`: labelled Cell 7 / JSON index 6 for `fit_weightedroll_modulation`; labelled Cell 8 / index 7 for all-observation execution and CSV save.
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\04_polarimetry_results\polix_weightedroll_raw_modulation_fits.csv`: controlling result.
- `D:\polix_xai_webapp\polarization_service.py`: later `_fit_modulation_curve` implementation and fit categories; supporting, not controlling, for reported uncertainty values.
- `D:\polix_xai_webapp\config\polarimetry_config.json`: project settings.

## Verified numerical results

- Successful fits: 25.
- Acceptable: 19; caution: 3; poor: 3.
- All saved fits: 357 degrees of freedom.

Notebook-11 CSVs control manuscript uncertainty values. Notebook 11 uses relative-quadrature propagation for \(A/C\), omitting amplitude–mean covariance. The later Flask service uses a full three-parameter gradient with covariance terms. The implementations are not numerically identical and must not be merged.

## Safe inference

The branch descriptively summarizes how well a weighted second harmonic represents each delivered WeightedRoll curve. Raw modulation, fitted phase and fit category may be compared among archived observations with the stated limitations.

## Unsupported inference

Do not infer calibrated polarization degree, official sky polarization angle, polarization significance, official background subtraction, physical cause, or exact source/background composition.

## Paper-ready wording

> The independent diagnostic branch fitted the delivered 360-bin exposure-weighted WeightedRoll total-count-rate curve with \(C+Q\cos(2\phi)+U\sin(2\phi)\) using inverse-variance weighted least squares. We report cosine and sine second-harmonic coefficients, raw modulation \(100\sqrt{Q^2+U^2}/C\), fitted modulation phase and a project-defined fit-quality category. These quantities are descriptive harmonic summaries and are not calibrated polarization degree or official sky polarization angle.

## Likely reviewer challenge and safe answer

**Question:** Why use a simple second harmonic when some curves fit poorly?

**Safe answer:** It is a common descriptive summary, not an assumed adequate physical model for every curve. Reduced chi-square is reported, and a poor category means only that this summary is inadequate for that delivered curve.

