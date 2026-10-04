# Guide Review Package

## Exact title

**An Explainable AI Framework for Analysis of X-Ray Polarimetry Data from XPoSat**

## Abstract — 200 words

The Polarimeter Instrument in X-rays (POLIX) aboard XPoSat produces heterogeneous Level-2 products that require observation-level synthesis before archive screening. This work examines 25 POLIX observations included in a frozen project archive, comprising 10 project-labelled source observations and 15 project-labelled blank-sky observations. Exposure, channel-distribution, source-azimuth, delivered-light-curve, and cross-detector summaries are compressed into a traceable 15-feature Matrix-C representation. Standardization, principal component analysis, KMeans clustering, and Isolation Forest provide complementary views of this archive, with the fixed model artifact flagging four observations as anomaly candidates. A deterministic, project-specific local feature-ranking heuristic connects composite unusualness evidence to Matrix-C features and their product families. Seed, contamination, jackknife, feature-tier, and six-case neutralization analyses are treated as sensitivity or sanity checks rather than external validation. WeightedRoll is excluded from Matrix C and analysed independently through a weighted second-harmonic fit and an empirical reference formed from 13 qualifying blank-sky fits. Representative observations show that Matrix-C unusualness and modulation-like harmonic behaviour do not identify the same property within the project archive. The Flask interface exposes the saved workflow as a researcher-facing inspection prototype. The study is limited by the small unlabeled sample, archive-specific fitting, proxy feature semantics, source-plus-background WeightedRoll products, and absence of official background, polarization-degree, and sky-angle calibration.

## Problem

POLIX Level-2 observations contain heterogeneous products with different scientific meanings and dimensions. The paper asks whether selected products can be compressed into interpretable observation-level features for label-free screening within the project archive while preserving a scientifically independent comparison with raw WeightedRoll harmonic behaviour. The objective is researcher triage, not anomaly confirmation or calibrated polarimetry.

## Proposed contribution framing

**Primary contribution:** A traceable, product-aware XAI framework for screening heterogeneous POLIX Level-2 observations within the project archive.

**Secondary contributions:**

1. A 15-feature observation representation preserving provenance to exposure, channel-distribution, source-azimuth, delivered-light-curve, and cross-detector products.
2. A deterministic, project-specific, model-informed local feature-ranking method linking composite unusualness evidence to original product families.
3. A separate WeightedRoll and empirical blank-sky harmonic diagnostic branch that avoids circular confirmation.

Agent 8 rated this hierarchy Moderate. Seed, contamination, jackknife, ablation, six-case neutralization, and Flask deployment are supporting evidence/implementation rather than standalone major contributions.

## Dataset and methodology

- 25 POLIX Level-2 observations included in the project archive.
- 10 project-labelled source and 15 project-labelled blank-sky observations.
- Final Matrix C: 15 features with no missing values; no deployed imputer.
- Saved stack: StandardScaler, two-component PCA, \(k=5\) KMeans, and Isolation Forest with 100 trees, contamination 0.16, and random state 42.
- Fixed candidate labels come only from saved `IsolationForest.predict`.
- Local evidence ranks four normalized components: PCA separation, KMeans centroid displacement, positive Isolation Forest occlusion, and absolute standardized abnormality.
- WeightedRoll is excluded from Matrix C and fitted separately with \(C+Q\cos2\phi+U\sin2\phi\).
- Thirteen blank-sky fits with reduced chi-square \(\le2\) form an empirical fractional-harmonic reference.

## Four principal results

1. **Fixed result:** 21 Normal outputs and four candidates—Blank Sky-13, Sco X-1, Her X-1, and Blank Sky-5.
2. **Tested-procedure stability:** Blank Sky-13, Sco X-1, and Her X-1 were selected in 100/100 seeds; Blank Sky-5 was selected in 29/100. The paper calls this a three-candidate Matrix-C core stable under the tested procedures.
3. **Versioned local explanation:** Sco X-1 ranks energy peak channel 2.454, weighted mean channel 2.207, and channel entropy 1.814. The historical entropy-first narrative is superseded.
4. **Scientific diagnostic:** Statistical unusualness and modulation-like harmonic behaviour are non-equivalent within the project archive. All ten source raw-modulation values lie within the declared empirical blank-sky scalar range, but this is not a polarization conclusion.

## Six important limitations

1. \(n=25\), no anomaly ground truth, and no prospective validation.
2. Contamination-defined threshold, seed-sensitive boundary, feature-tier dependence, and singleton KMeans clusters.
3. Channel, source-roll, and delivered-light-curve quantities are diagnostic proxies requiring POLIX-aware interpretation.
4. The XAI score is a project-specific within-observation heuristic with a six-case in-sample neutralization check.
5. WeightedRoll contains source and background; the selected 13-fit reference is empirical and not official subtraction or a confidence region.
6. No official background procedure, official \(\mu_{100}\), calibrated PD, or verified PA conversion; Notebook 11 and the later service also differ in \(A/C\) uncertainty propagation.

## Proposed main-paper figures

1. Framework flow with separate Matrix-C ML and WeightedRoll harmonic branches.
2. Matrix-C PCA observation space using the saved transform.
3. Saved anomaly-score ranking with 100-seed frequency annotation.
4. Empirical blank-sky/source fractional-harmonic diagnostic space without confidence contours.

## Decisions required

- Approve or revise the one-primary/three-secondary contribution framing.
- Confirm author order, corresponding author, affiliation, and acknowledgment additions.
- Select IEEE venue and page limit.
- Approve POLIX feature semantics and candidate interpretation.
- Approve “harmonic coefficients/fractional harmonic coordinates” terminology and the 13-fit empirical blank-sky treatment.
- Select final main-paper figures and decide whether the limitations table fits the page budget.
- Decide whether PD sensitivity scenarios should remain supplement-only or be omitted.
- Confirm venue-specific AI-assisted-writing disclosure requirements.

## Current readiness

Draft 2 content, LaTeX, controlled references, evidence ledger, figure assets, supplementary plan, limitations disclosure, hostile-review response, and student-learning package are complete as a guide-review candidate. No evidence contradiction invalidates the narrow archive-screening result, and Agent 9 identified no mandatory new experiment for that framing. Submission readiness remains **No** pending guide/POLIX-domain approval, author order, venue/page limit, final figure selection, final human revision, citation recheck, and venue-specific formatting/disclosure. No PDF has been generated.
