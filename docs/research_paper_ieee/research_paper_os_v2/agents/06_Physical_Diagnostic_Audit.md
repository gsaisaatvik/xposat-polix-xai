# Agent 6 - Physical-Diagnostic Audit

**Role:** Independent physical-diagnostic reviewer  
**Audit date:** 2026-07-28  
**Scope:** Existing WeightedRoll fit, empirical blank-sky reference, source comparison, and calibration boundaries  
**Execution boundary:** Existing code, notebook, handbook, configuration, and result files were inspected. No experiment was run. No original project file or Draft 1 file was modified.

## 1. Executive verdict

The physical branch is defensible as an **archive-specific, empirical modulation diagnostic**, provided that its terminology and uncertainty limits are stated more carefully than in some project-generated labels. It is not a calibrated polarimetry analysis.

The strongest supported physical result is not a polarization measurement. It is that the second-harmonic summaries derived from WeightedRoll do not reproduce the Matrix-C anomaly decisions in a one-to-one manner. This supports the cautious conclusion:

> Within the 25 observations in the frozen project archive, statistical unusualness under Matrix C and second-harmonic behaviour relative to the empirical blank-sky sample are related diagnostic questions but are not equivalent.

This is a descriptive conclusion about the frozen archive and the implemented procedures. It does not establish a universal property of future POLIX data, an astrophysical cause, or a polarization detection.

## 2. Controlling evidence

| Evidence | What it controls |
|---|---|
| `C:\Users\Saatvik\Downloads\POLIX_User_Handbook.pdf`, Version 1.0, October 2025, pp. 26, 35, 57, and 67 | WeightedRoll meaning, input construction, columns, background limitation, and release-specific polarimetry boundary |
| `D:\ISROtrial\Polix_L2_full_archive\11_POLIX_Polarization_Parameter_Analysis.ipynb`, Cells 7, 14, and 16 | Frozen fit, uncertainty propagation, fit-quality labels, baseline construction, and source comparison |
| `D:\ISROtrial\Polix_L2_full_archive\polix_weightedroll_raw_modulation_fits.csv` | Primary numerical fit results for 25 observations |
| `D:\ISROtrial\Polix_L2_full_archive\path2_blank_sky_modulation_baseline.csv` | Fifteen-observation and thirteen-fit blank-sky summaries |
| `D:\ISROtrial\Polix_L2_full_archive\path2_all_observations_fractional_qu_vectors.csv` | Fractional harmonic coefficients and observation roles |
| `D:\ISROtrial\Polix_L2_full_archive\path2_source_vs_blank_sky_modulation_comparison.csv` | Scalar source-versus-blank comparison |
| `D:\ISROtrial\Polix_L2_full_archive\path2_final_source_only_pd_pa_candidate_table.csv` | Source vector-distance diagnostics and their project labels |
| `D:\polix_xai_webapp\polarization_service.py` and `config\polarimetry_config.json` | Current researcher-facing implementation and saved empirical constants |

## 3. WeightedRoll semantics

The handbook describes `WeightedRoll_L2.fits` as the final intensity modulation with azimuthal angle and explicitly states that it includes modulation from both source and background count rates (p. 26). Its weighted-exposure module forms azimuthal count-rate distributions using count and exposure values, applies configured energy-dependent azimuthal shifts, and combines the selected energy and detector channels (p. 35). The product contains `ROLL_AZ_ANG`, `TOTAL_COUNTRATE`, and `ERROR` columns (p. 67).

Accordingly:

- "WeightedRoll azimuthal count-rate curve" is safe.
- "Exposure-weighted" is acceptable only when defined by the pipeline construction; it should not imply that the paper independently designed the weighting.
- "Source modulation curve" is unsafe because the product contains both source and background contributions.
- "Background-subtracted WeightedRoll" and "official POLIX background subtraction" are prohibited.

The handbook also reports variable two-fold blank-sky modulation, including narrow spikes in some observations, and states that X-ray polarization measurement is not possible with the currently released data and observing strategy (p. 57). This is the controlling limitation.

## 4. Exact harmonic method

The frozen notebook reads 360 angle bins and fits

\[
y(\phi)=C+Q\cos(2\phi)+U\sin(2\phi)
\]

by weighted linear least squares, with weights \(w_i=1/\sigma_i^2\) from the FITS `ERROR` column. The design matrix contains a constant, cosine, and sine term. The notebook solves

\[
\hat{\beta}=(X^\mathsf{T}WX)^{-1}X^\mathsf{T}Wy,
\]

where \(\hat{\beta}=(C,Q,U)\). It uses 357 degrees of freedom for 360 valid bins and three fitted coefficients. The current service uses the same model but obtains the inverse through a pseudoinverse. The saved CSV results are controlled by the notebook implementation.

The coefficient convention is:

\[
A=\sqrt{Q^2+U^2}, \qquad
m_{\rm raw}=A/C,
\]

\[
\phi_0=\frac{1}{2}\operatorname{atan2}(U,Q)\pmod{180^\circ}.
\]

Thus \(Q=A\cos(2\phi_0)\) and \(U=A\sin(2\phi_0)\) within the project's fitted model. These are mathematical harmonic coefficients. They are not verified calibrated Stokes parameters.

The term **raw modulation** is safe when explicitly defined as \(100A/C\) percent for this project fit. The paper should not silently equate this definition to a calibrated polarization fraction or to another convention that may include a different normalization.

## 5. Uncertainty and fit-quality review

The notebook uses \((X^\mathsf{T}WX)^{-1}\) as the coefficient covariance, without rescaling it by reduced chi-square. This is valid only if the per-bin errors are reliable, independent standard deviations and the model is adequate. Those assumptions were not independently validated.

Amplitude and phase errors include the fitted \(Q/U\) covariance. The notebook's error for \(A/C\), however, combines relative amplitude and mean-level errors in quadrature and omits the covariance between \(A\) and \(C\). The current Flask service instead uses a full three-parameter gradient and covariance matrix. This is a real method-version discrepancy. Published uncertainty values must be identified as notebook/CSV values unless the methods are reconciled; no silent substitution is acceptable.

The rules

- reduced chi-square \(\leq 2\): `acceptable`;
- \(2 <\) reduced chi-square \(\leq 5\): `caution`;
- reduced chi-square \(>5\): `poor_simple_sinusoid_fit`

are project-defined screening thresholds, not calibrated statistical decision limits. "Acceptable" therefore means acceptable under this declared rule, not proof that residuals are random or the physical model is correct. Reduced chi-square values and amplitude signal-to-error ratios must not be converted into detection significances or p-values.

## 6. Blank-sky reference

All 15 archive observations labelled blank sky were fitted. Thirteen met the project rule of reduced chi-square \(\leq 2.0\) and were used for the empirical baseline. The primary baseline CSV gives:

- mean raw modulation: 1.147820 percent;
- sample standard deviation: 0.565960 percent;
- mean fractional coefficients: \(q=Q/C=0.0090920\) and \(u=U/C=-0.0064782\);
- sample scatter: 0.0048569 in \(q\) and 0.0040190 in \(u\).

The baseline is suitable for describing the centre and spread of this selected archive sample under the same fitting procedure. It is not an official background model, a matched-background subtraction, or a calibrated detection region.

The two-dimensional "vector distance" standardizes \(q\) and \(u\) separately and combines them by Euclidean norm. It ignores covariance between the blank-sky axes, parameter-estimation uncertainty for each observation, and uncertainty in the estimated baseline mean and scatter. Its thresholds of 2 and 3 are descriptive project cutoffs. They are not Gaussian sigma levels or p-values.

The scalar statement that all ten source observations lie within the project's blank-sky mean plus or minus two sample standard deviations is verified. Safe wording is "within the empirical blank-sky scalar range under the declared rule." It must not be rewritten as "consistent with zero polarization" or "unpolarized."

## 7. Source cases and non-equivalence

The central non-equivalence conclusion is supported by discordant examples:

- Sco X-1 is a fixed Matrix-C anomaly candidate, while its raw modulation is 1.139578 percent, its scalar comparison lies within the empirical blank-sky range, and its vector distance is 0.3005. Its harmonic fit is only `caution` at reduced chi-square 2.0308.
- Her X-1 is a fixed Matrix-C anomaly candidate and has a moderate project vector distance of 2.3174, but the simple harmonic fit is poor at reduced chi-square 57.4335. The apparent vector displacement is therefore not reliable physical confirmation.
- Crab P01_0005 is not a fixed Matrix-C anomaly candidate, yet it has the highest source raw modulation, 1.697346 percent. It remains within both the scalar and vector blank-sky rules.
- Blank-sky observations themselves include Matrix-C anomaly candidates, demonstrating that statistical unusualness is not source-specific.

These cases support methodological separation, not astrophysical interpretation. WeightedRoll is outside Matrix C, which avoids using the same physical curve as both anomaly input and confirmation.

## 8. Terminology decision

**Preferred:** "cosine and sine second-harmonic coefficients," "fractional harmonic coordinates \(q=Q/C\) and \(u=U/C\)," and "empirical \(q/u\) diagnostic space."

**Conditionally safe:** "Stokes-like" only when immediately qualified as an empirical mathematical analogy, not calibrated Stokes quantities.

**Unsafe:** "measured Stokes \(Q/U\)," "source Stokes parameters," "background-corrected modulation," "polarization detection," "official PD," "official PA," and "polarization significance."

"Fitted modulation phase" is safe. It is not an official sky polarization angle because the coordinate transformation, sign convention, offset, response, and calibration chain are not established.

PD values calculated with assumed \(\mu_{100}=0.40,0.42,0.44\) are sensitivity proxies only. No observation-specific official \(\mu_{100}\) was located. They should not be presented as measurements.

## 9. Placement recommendation

**Main paper:** WeightedRoll semantics and separation from Matrix C; harmonic equation and raw-modulation definition; 15 blank skies and the 13-fit rule; concise empirical baseline; source/blank comparison; fit-quality caveat; two or three discordant examples; the non-equivalence conclusion.

**Supplement:** Full 25-row fit table; all fitted coefficients and phase values; complete source vector table; detailed propagation formulas; project vector-distance categories; PD sensitivity scenarios, if the guide retains them.

**Remove from the main results:** PD proxy values, phase-based physical interpretation, background-relative "candidate" labels, amplitude-SNR detection language, and any statement that the empirical vector subtraction is official background subtraction. Consider removing the PD proxy table entirely if it distracts from the methodology contribution.

## 10. Disagreements requiring preservation

| ID | Disagreement | Agent 6 position | Required decision |
|---|---|---|---|
| D6-01 | \(Q/U\) may be read as calibrated Stokes parameters | Use harmonic-coefficient terminology; "Stokes-like" only with an explicit disclaimer | POLIX domain expert and guide |
| D6-02 | Notebook and Flask service use different \(A/C\) uncertainty propagation | Treat saved CSV errors as notebook results; do not claim one exact deployed uncertainty method until reconciled | Code/method review |
| D6-03 | Reduced chi-square cutoffs are presented as quality classes | Retain as declared project rules, not statistical significance thresholds | Guide/statistical approval |
| D6-04 | Diagonal standardized \(q/u\) distance is labelled as vector evidence | Treat as descriptive; it is not a calibrated confidence ellipse or sigma significance | Statistical and domain approval |
| D6-05 | "Background-relative" can imply subtraction | Use "relative to the empirical blank-sky mean vector" and state that no official subtraction is performed | Guide approval |
| D6-06 | PD/PA candidate language appears in frozen CSVs | Do not reproduce that label as a paper claim | Guide approval |

## 11. Needed work not executed

- **NOT EXECUTED - REASON:** residual, spike, and higher-harmonic diagnostics were not run because Phase 4 authorizes review of existing experiments only. **PRIORITY: HIGH.**
- **NOT EXECUTED - REASON:** the notebook and service uncertainty formulas were not numerically reconciled because no new experiment or result regeneration was authorized. **PRIORITY: HIGH.**
- **NOT EXECUTED - REASON:** leave-one-out, bootstrap, robust-centre, matched-sky/time, and covariance-aware blank-sky baselines were not tested because they would be new experiments. **PRIORITY: HIGH.**
- **NOT EXECUTED - REASON:** sensitivity to the reduced chi-square selection cutoff was not tested because it would add a new analysis. **PRIORITY: MEDIUM.**
- **NOT EXECUTED - REASON:** amplitude positive-bias treatment and circular phase intervals were not evaluated because they are outside the completed analysis. **PRIORITY: MEDIUM.**
- **NOT EXECUTED - REASON:** calibrated PD and sky PA conversion were not attempted because the required official response, \(\mu_{100}\), background strategy, and coordinate convention are absent. **PRIORITY: BLOCKING FOR ANY PD/PA CLAIM.**

## 12. Final verdict

Retain the physical branch as an independent, descriptive archive diagnostic and as evidence for non-equivalence between ML unusualness and raw modulation behaviour. Keep its strongest numerical summaries and representative discordant cases in the main paper, with full tables in supplementary material. Do not present the blank-sky reference as a statistical detection framework, and do not present \(Q/U\), phase, or assumed-\(\mu_{100}\) outputs as official Stokes parameters, PA, or PD. The branch supports a cautious scientific-computing contribution, not an astrophysical result.
