# INDIA Part 04 - Active Decisions and Exclusions

## Active decisions

1. The exact paper title is **An Explainable AI Framework for Analysis of X-Ray Polarimetry Data from XPoSat**.
2. The model, parameters, feature definitions, matrices and project results are frozen.
3. The intended paper is a bounded applied scientific-computing case study.
4. The dataset wording is “25 POLIX Level-2 observations included in the project archive.”
5. Observation roles use the project mapping: 10 source and 15 blank sky.
6. Matrix C contains 15 features and is the deployed anomaly-screening input.
7. WeightedRoll is scientifically separate and must not be used to confirm the model circularly.
8. Only `IsolationForest.predict` defines the fixed Normal/candidate label.
9. PCA and KMeans are complementary descriptive/model components, not independent anomaly validators.
10. The four-component XAI output is a project-specific, model-informed local feature-ranking heuristic.
11. Main-paper Sco X-1 values are rounded to 2.454, 2.207 and 1.814 in the accepted order.
12. The blank-sky reference comprises 13 qualifying fits under the declared reduced-chi-square rule of at most 2.
13. The main paper may report raw modulation, fitted modulation phase and fractional harmonic coordinates only with explicit diagnostic boundaries.
14. The manuscript will be produced in Word and LaTeX using a generic IEEE conference layout with a 6–8-page target.
15. No final PDF will be delivered before venue selection.

## Excluded manuscript claims

- astrophysical discovery;
- confirmed anomaly or official anomaly ground truth;
- polarization detection;
- calibrated polarization degree;
- official sky polarization angle;
- official background subtraction;
- official modulation factor;
- SHAP or LIME deployment;
- supervised prediction accuracy;
- causal feature attribution;
- Matrix-C superiority;
- benchmark superiority;
- future-release generalization;
- analysis of all publicly available POLIX data;
- independent validation from PCA, KMeans and Isolation Forest;
- statistical confidence contours for the empirical blank-sky reference.

## Source exclusions

### Excluded from scientific evidence

- `C:\Users\Saatvik\Downloads\WhatsApp Image 2026-08-01 at 10.58.20.jpeg`: communication architecture only. It contains elements that require correction and will not be inserted unchanged.
- `C:\Users\Saatvik\Downloads\WhatsApp Image 2026-07-10 at 20.42.37.jpeg`: screenshot supplied as context only. It will not be cited or used as proof.

### Excluded from the manuscript and final BibTeX

- The 2025 POLIX handbook, including its title, edition and handbook-specific statements.

Physical wording previously dependent on the handbook must be supported by an inspected primary source or reduced to what the project code and outputs directly establish. If neither is possible, the wording is removed.

### Historical but frozen

- Reviewed final report: narrative understanding only.
- Draft 1 Markdown and LaTeX: no evidence role.
- Existing final-content candidate: later omission comparison only.
- Prior reconstruction plan: historical planning record only.

## Model-change decision

No model change is authorized. Known weaknesses will be disclosed. Suggested alternative models, parameters, covariance-aware baselines or prospective validation belong only in Future Work.

## Architecture corrections reserved for Phase 4

The eventual paper diagram must:

- remove median imputation;
- show the scaler feeding PCA, KMeans and Isolation Forest without implying an unsupported sequential chain;
- show that only Isolation Forest produces the fixed label;
- show the XAI score as local evidence ranking, not label generation;
- keep WeightedRoll separate;
- remove generalized scalability, confidence-fusion and PD-oriented claims;
- avoid third-party logos and presentation decoration.

