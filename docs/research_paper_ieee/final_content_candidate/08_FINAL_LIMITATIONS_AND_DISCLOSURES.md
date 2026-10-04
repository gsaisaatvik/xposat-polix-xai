# Final Limitations and Disclosures

## Scientific and statistical limitations

1. The frozen archive contains 25 observations and 15 Matrix-C variables.
2. No trusted anomaly labels or independent test archive are available.
3. Standardization, representation, model fitting, screening, and retrospective checks use the same archive.
4. Isolation Forest contamination 0.16 defines the four-candidate threshold; it is not an estimated anomaly prevalence.
5. Three candidates persist in all 100 tested seeds, but that frequency is not a probability of physical validity.
6. Candidate identity depends on feature tier. Only Sco X-1 and Blank Sky-13 persist across Matrix A/B/C candidate sets.
7. Matrix-C KMeans has two singleton clusters, making assigned-centroid distance zero for Sco X-1 and Blank Sky-13.
8. Included-observation jackknife persistence is influence sensitivity, not held-out or future-release validation.
9. The original software environment was not fully pinned; the saved scikit-learn artifact records version 1.9.0.

## Feature and explanation limitations

1. Several Matrix-C variables are engineering proxies rather than calibrated physical quantities.
2. Channel quantities are not calibrated energy values.
3. The channel-4000 threshold is a high-channel boundary without a verified energy conversion.
4. Source-roll roughness omits the circular closing difference and assumes stored order.
5. Delivered light-curve and detector summaries do not establish intrinsic variability, detector health, or physical cause.
6. The four-component explanation score is a deterministic, project-specific, model-informed local ranking.
7. Only Isolation Forest sets the deployed Normal/Anomaly label.
8. Component normalization is within observation; combined scores are not calibrated or comparable across observations.
9. The six-case neutralization analysis is an in-sample, method-aligned sanity check without matched random or bottom-feature baselines.

## Physical-diagnostic limitations

1. WeightedRoll contains source and background modulation contributions.
2. The second-harmonic coefficients are mathematical fit coefficients, not verified calibrated Stokes parameters.
3. Raw modulation is not polarization degree, and fitted phase is not official sky polarization angle.
4. The 13-fit blank-sky reference is selected, small, archive-specific, and not an official background model.
5. The diagonal fractional-coordinate distance ignores \(q/u\) covariance, fit uncertainty, baseline uncertainty, and observing-condition matching.
6. Reduced-chi-square classes and vector-distance cutoffs are project-defined descriptive rules.
7. No official background strategy, observation-specific \(\mu_{100}\), response calibration, or sky-angle conversion was available.
8. Notebook 11 and the later Flask service propagate \(A/C\) uncertainty differently. Manuscript values retain frozen notebook/CSV provenance.

## Claims explicitly excluded

- Astrophysical discovery or confirmed anomaly.
- Predictive accuracy, anomaly probability, statistical significance, or future-data generalization.
- Algorithmic novelty, priority, uniqueness, or superiority.
- SHAP/LIME deployment or formal Shapley guarantees.
- Causal or physical interpretation of leading local features.
- Official background subtraction, calibrated polarization degree, official sky angle, or polarization detection.
- Analysis of Chandra or XSPECT data.

## AI-assisted writing disclosure draft

OpenAI Codex assisted with evidence organization, source-code review, literature organization, specialist-audit drafting, figure scripting, manuscript drafting, BibTeX preparation, and language editing. The original POLIX data, notebooks, matrices, trained model, project results, and web application predate the final-paper workspace and were not modified during this workflow. Existing supplementary robustness scripts and outputs were used; no new scientific experiment was added.

All numerical statements must be checked by the authors against the cited CSV or model artifact. All bibliographic entries and scientific interpretations must be manually checked. The authors must revise and approve every manuscript sentence, follow the selected venue’s AI-disclosure policy, and obtain POLIX-aware review where marked. AI output is not scientific evidence. The application’s deterministic explanation sentences are Python templates, not large-language-model output.

## Human approval record required before submission

- All four authors understand and approve every claim.
- Faculty guide approves contribution framing, author order, venue, and figure selection.
- POLIX-aware reviewer approves feature and physical terminology.
- Authors verify the current acknowledgment wording and reference details.
- Authors apply the selected venue’s AI, ethics, conflict-of-interest, funding, and data-use requirements.
