# BHUTAN Knowledge Card 11 — Claim Boundaries and Future Work

## Beginner explanation

The study provides an archive-screening and inspection framework. It identifies observations that look unusual relative to the project archive and separately summarizes raw harmonic behaviour. It does not establish why an observation is unusual or report a calibrated astrophysical polarization measurement.

## Technical explanation

The ML result is conditional on \(X_C\in\mathbb{R}^{25\times15}\), the fitted scaler, the frozen Isolation Forest parameters and its contamination-defined threshold. The physical branch is conditional on a second-harmonic model and a selected 13-fit blank-sky reference. Neither branch contains anomaly ground truth, a formal polarization null distribution or prospective validation. Their non-equivalence is an archive-specific empirical observation, not a claim of statistical independence.

## Exact project implementation and parameters

- 25 observations; 10 project-labelled source and 15 blank sky.
- Matrix C: 15 features; WeightedRoll excluded.
- Fixed model: 100 Isolation Forest trees, contamination 0.16, random state 42; 21 Normal and four candidates.
- Procedure-qualified result: three candidates stable under the tested seed, contamination and included-observation procedures; Blank Sky-5 seed-sensitive.
- Harmonic branch: weighted \(C+Q\cos2\phi+U\sin2\phi\) fit.
- Empirical reference: 13 of 15 blank skies selected at reduced chi-square \(\le2\).
- Reported physical quantities remain raw modulation, fitted phase and fractional harmonic coordinates.

## Controlling sources

- All Phase-1 controls listed in Cards 01–10.
- `D:\polix_xai_webapp\research_paper_ieee\guide_approved_final_run\01_NEPAL_EVIDENCE\NEPAL_Part_04_Controlling_Numerical_Results.md`.
- `D:\polix_xai_webapp\research_paper_ieee\guide_approved_final_run\01_NEPAL_EVIDENCE\NEPAL_Part_05_Evidence_Contradictions.md`.

## Verified results and safe claims

The paper may state that the project processed the defined 25-observation archive; created a 15-feature product-aware Matrix C; produced four fixed archive-relative candidates; identified a tested-procedure stable three and a seed-sensitive fourth; ranked local feature evidence with a deterministic four-component heuristic; fitted all 25 WeightedRoll curves; formed a descriptive 13-fit blank-sky reference; and observed that ML unusualness and modulation-like harmonic behaviour do not agree one-to-one.

## Safe inference

The safe conclusion is methodological and archive-specific: traceable product summaries can support explainable unsupervised screening, while a scientifically separate harmonic branch shows that feature-space unusualness and modulation-like behaviour answer different diagnostic questions in the project archive.

## Unsupported inference

The paper must not claim astrophysical discovery, confirmed anomaly, anomaly ground truth, polarization detection/significance, calibrated polarization degree, official sky polarization angle, official background subtraction, calibrated Stokes parameters, a validated confidence region, causal XAI, predictive accuracy, superiority, future-data generalization, all available POLIX data, or numerical identity between Notebook-11 and the later service uncertainty implementation.

## Future work — not executed in this run

- Prospective validation on later observations.
- Domain-expert adjudication of candidates and feature semantics.
- An officially supported background and calibration workflow when available to the authors.
- Covariance-aware modelling of blank-sky harmonic coordinates with a larger archive.
- Reconciliation and explicit testing of notebook/service uncertainty propagation.
- Environment pinning and containerized reproduction.
- Comparative evaluation on an independent dataset with defensible labels or expert adjudication.
- Any expanded representation as a separately versioned future study.

No current evidence requires retraining, tuning or replacement of the completed model.

## Paper-ready wording

> This study treats the task as an applied scientific-computing problem. Its outputs identify inspection priorities within the 25-observation project archive and provide separate raw harmonic summaries. They do not establish anomaly ground truth, a physical cause, calibrated polarization degree, official sky polarization angle, polarization significance or an official background-subtraction result. Prospective validation, expert interpretation and supported calibration analysis remain future work.

## Likely reviewer challenge and safe answer

**Question:** Without labels or calibrated polarization quantities, what scientific conclusion remains?

**Safe answer:** The contribution is methodological and diagnostic: heterogeneous Level-2 products are represented through traceable observation-level features, screened with a frozen unsupervised pipeline, linked to local evidence and compared with an intentionally separate harmonic branch. The archive shows that statistical feature-space unusualness and modulation-like harmonic behaviour answer different questions; neither output is elevated to a calibrated astrophysical conclusion.
