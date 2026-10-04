# AFGHANISTAN Part 02 — Hostile IEEE Review

## Recommendation

**Major revision before submission.** The archive-screening result is internally reproducible, and no fatal evidence contradiction was found. However, a general machine-learning or astrophysics venue could reject the paper because the sample is small, labels are absent, the explanation score is project-specific, and the harmonic branch is an empirical diagnostic without calibrated physical interpretation. The work is more defensible as an applied scientific-computing case study, student research paper, or domain-workflow contribution.

## Fatal evidence concerns

No current evidence contradiction invalidates the central result that the fixed saved implementation returns four archive-relative candidates from Matrix C.

The following would become fatal only if the paper made stronger claims than it currently does:

- treating the four candidates as true anomalies;
- claiming calibrated polarization degree or sky polarization angle;
- presenting the 13-fit blank-sky reference as an official background or detection region;
- calling the local score a SHAP attribution, causal explanation, or exact decomposition of the deployed label;
- claiming future-data generalisation or quantitative superiority.

The Phase-5 manuscript excludes these claims.

## Major scientific concerns

### 1. Small, same-archive analysis

All representation design, model fitting, explanation, neutralization, and robustness checks use the same 25 observations. The stability analyses measure procedural persistence within this archive, not predictive validity. This must remain central in the abstract, Results, Discussion, and Limitations.

### 2. Contamination-defined candidate count

Contamination 0.16 mechanically creates a four-row screening result for 25 observations. The manuscript correctly calls this a frozen screening assumption rather than an estimated anomaly prevalence. A reviewer may still ask why 0.16 was chosen. The answer must remain historical and procedural; it cannot be defended as statistically estimated from these data.

### 3. No anomaly ground truth

No accuracy, recall, false-positive rate, or scientific anomaly rate can be estimated. Candidate stability is not a substitute for labels. The paper is defensible only if it consistently presents a triage framework.

### 4. Project-specific XAI heuristic

The equal-weight sum combines evidence from PCA, KMeans, Isolation Forest occlusion, and absolute standardized abnormality. Two components do not explain the Isolation Forest label directly, normalization is observation-specific, and six joint-neutralization cases do not establish completeness or uniqueness. The bounded term “model-informed local feature-ranking heuristic” is defensible; broad “validated feature attribution” wording is not.

### 5. Harmonic branch is descriptive

The 13-fit blank-sky set is small and selected by a project fit rule. The scalar ±2-standard-deviation rule and component-wise scatter are not calibrated confidence or detection regions. Weighted least squares uses delivered point errors without a demonstrated covariance or systematic-error model. The paper must preserve its diagnostic-only interpretation.

### 6. Representation dependence and singleton clusters

Only two observations persist across Matrix A/B/C. KMeans has two singleton clusters, giving zero assigned-centroid distance for Sco X-1 and Blank Sky-13. This substantially limits the clustering component’s interpretation and should not be hidden behind the combined score.

## Fixable writing and presentation concerns

1. Replace the rough plain-text equations in the DOCX with real Word equations; the current strings are not guide-facing publication quality.
2. Move the DOCX into the official venue template after the venue is selected. The current file approximates IEEE geometry but is not proof of template compliance.
3. Reduce the current nine-page Word draft only after the venue page limit and final figure set are approved.
4. Keep “separate harmonic branch” more common than “independent branch” so readers do not infer statistical independence.
5. Where “stable under the tested procedures” appears, keep the tested procedures and retrospective scope nearby.
6. Preserve the distinction among fixed four, seed-stable three, cross-tier two, and exploratory six in every table and caption.
7. Add one explicit limitation that weighted least squares uses the delivered per-bin uncertainties without a covariance/systematic-error model.
8. Retain the finite-review qualifier on the literature-gap statement; do not convert it into a priority claim.

## Domain-review concerns

- Whether the 15 features have acceptable POLIX-aware operational interpretations.
- Whether “fractional second-harmonic coordinates” is the preferred neutral terminology.
- Whether the WeightedRoll delivered total-count-rate semantics are described sufficiently without implying official background treatment.
- Whether the reduced-chi-square categories and 13-fit selection are acceptable as a project diagnostic.
- Whether Her X-1 should remain in the main table despite the poor simple-harmonic fit.
- Whether Fig. 4 belongs in the main paper or supplement.

## Limitations that must simply be disclosed

- (n=25) and no anomaly ground truth.
- Same-archive retrospective checks.
- No future-release or independent-dataset validation.
- Contamination-defined threshold and seed-sensitive boundary rows.
- Feature-tier dependence and singleton KMeans clusters.
- Six-case, in-sample, sign-only perturbation check.
- Empirical selected blank-sky reference.
- No calibrated polarization quantities or official background workflow.
- Notebook/service uncertainty mismatch.
- Original environment not fully pinned.

## Experiments truly essential before submission

No experiment is essential to preserve the manuscript’s present **bounded case-study claim**. The following becomes essential only if the selected venue or reviewers require general method validity:

- **NOT EXECUTED — prospective or independent-archive validation would be required for future-data or generalisation claims — SUBMISSION IMPORTANCE: HIGH for a general ML venue; not required for the current archive-specific claim.**
- **NOT EXECUTED — domain-expert adjudication would be required to claim scientific anomaly validity — SUBMISSION IMPORTANCE: HIGH for an astrophysics-results venue; the present paper claims inspection priority only.**

## Optional experiments

- **NOT EXECUTED — compare alternative detectors on an independent labelled or expert-adjudicated dataset — SUBMISSION IMPORTANCE: OPTIONAL for the current case study.**
- **NOT EXECUTED — covariance-aware blank-sky modelling with a larger sample — SUBMISSION IMPORTANCE: OPTIONAL/FUTURE WORK.**
- **NOT EXECUTED — evaluate individual-feature rather than joint top-three interventions across all observations — SUBMISSION IMPORTANCE: OPTIONAL/FUTURE WORK.**

## Hostile-review bottom line

The saved result can support an honest applied workflow paper. It cannot support a validated anomaly detector, a general XAI method, or a polarimetric measurement paper. Acceptance will depend heavily on venue choice, domain approval, and disciplined presentation.

