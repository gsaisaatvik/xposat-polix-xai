# INDIA Part 01 - Run Charter

**Run:** Guide-approved final research-paper workflow  
**Control date:** 2026-08-03  
**Workspace:** `D:\polix_xai_webapp\research_paper_ieee\guide_approved_final_run`  
**Current gate:** Phase 0 only; Phase 1 has not started.

## Fixed title

**An Explainable AI Framework for Analysis of X-Ray Polarimetry Data from XPoSat**

## Objective

Prepare an evidence-controlled, venue-neutral IEEE conference manuscript describing the research already completed on 25 POLIX Level-2 observations in the project archive. The paper is an applied scientific-computing case study. It is not an astrophysical-discovery paper and does not report calibrated polarization degree or official sky polarization angle.

## Frozen project scope

- 25 POLIX Level-2 observations included in the project archive.
- 10 project-labelled source observations and 15 project-labelled blank-sky observations.
- A 15-feature Matrix-C representation.
- `StandardScaler`, principal component analysis, KMeans and Isolation Forest.
- A project-specific four-component local feature-ranking heuristic.
- A six-case feature-neutralization sanity check.
- A separate WeightedRoll second-harmonic diagnostic and empirical blank-sky reference.
- A Flask researcher-facing implementation.

## Frozen result statements carried into verification

These are control expectations, not newly verified Phase-0 findings:

- Fixed deployed output: 21 Normal observations and four anomaly candidates.
- Candidate identities: Blank Sky-13, Sco X-1, Her X-1 and Blank Sky-5.
- Seed result: the first three were selected in 100/100 tested seeds; Blank Sky-5 was selected in 29/100.
- Sco X-1 local order: energy peak channel, energy weighted mean channel, energy channel entropy.
- Six exploratory XAI/neutralization cases remain distinct from the four fixed candidates.
- WeightedRoll remains outside Matrix C.
- Fifteen blank-sky fits were analysed; 13 qualifying fits use the declared reduced-chi-square rule of at most 2.

Phase 1 must verify each statement from controlling machine-readable evidence before it becomes manuscript text.

## Model freeze

The completed model is frozen. This run will not retrain, tune contamination, change KMeans or PCA settings, alter feature definitions, regenerate matrices, introduce SHAP or LIME, or run result-seeking experiments. Existing reproducibility and robustness outputs may be inspected. A parameter or model alternative may appear only as Future Work.

If a genuine contradiction invalidates the central archive-screening result, work stops for user approval. It will not be repaired through silent recomputation.

## Reading firewall

1. Latest guide-approved instructions control scope and wording.
2. Original CSVs plus their generating notebook/code control numbers.
3. The saved PKL plus deployed code control model and XAI behaviour.
4. Existing supplementary audits control robustness wording.
5. Verified primary literature controls general theory.
6. The reviewed report is narrative support only.
7. Draft 1 and the existing final-content candidate are historical comparison material, not evidence.
8. Uploaded images are non-evidentiary communication references.

Old drafts will not be bulk-read during evidence construction. They may be consulted only for an explicitly logged omission check after the new evidence-controlled manuscript exists.

## Paper-level exclusions

The manuscript will not claim an astrophysical discovery, confirmed anomaly, polarization detection, calibrated polarization degree, official sky polarization angle, official background subtraction, official modulation factor, causal XAI, predictive accuracy, superiority, future-data generalization or use of all available POLIX data.

The 2025 POLIX handbook will not be mentioned or cited in the manuscript or final BibTeX. Any handbook-dependent sentence must be replaced by verified primary literature, narrowed to a code-supported operational statement, or removed.

## Phase approval rule

Each country-named phase ends with a user-facing gate. Work must stop after the phase report until the user explicitly approves continuation. Creating this control set does not authorize Phase 1.

