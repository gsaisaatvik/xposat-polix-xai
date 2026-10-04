# Research Paper Highlights for Students

This guide explains the content candidate in study-ready language. It does not replace the evidence ledger, POLIX handbook, code, or faculty review.

## 1. The paper in one sentence

The paper shows how 25 archived POLIX Level-2 observations can be summarized with 15 traceable features, screened without anomaly labels, explained with a project-specific local ranking, and compared independently with raw WeightedRoll harmonic behaviour.

## 2. The problem in simple language

One POLIX observation is not a single spreadsheet row. It contains different products about exposure, detector channels, roll angle, light curves, detectors, and WeightedRoll modulation. The project needed a consistent observation-level summary so researchers could compare observations without pretending that trusted “normal/anomaly” labels existed. It also needed to avoid treating an ML flag as proof of polarization.

## 3. Why the exact title is appropriate

“An Explainable AI Framework for Analysis of X-Ray Polarimetry Data from XPoSat” is the college project title. It is broad enough to include feature engineering, unsupervised screening, explanations, physical diagnostics, and the Flask interface. The paper must immediately narrow its scope: it analyses 25 POLIX Level-2 observations in the project archive and does not claim calibrated polarimetry or discovery.

## 4. How the project evolved

The initial proposal considered supervised or general post-hoc approaches such as SHAP and LIME. Inspection of the released data showed that no trusted anomaly labels were available, so supervised classification was not justified. The completed pipeline instead uses StandardScaler, PCA, KMeans, Isolation Forest, and a custom four-component ranking. SHAP and LIME were not deployed or benchmarked. This is normal project evolution: the final method followed the evidence and data constraints.

## 5. Literature gap in simple language

Existing sources explain POLIX, harmonic/Stokes analysis, astronomical anomaly detection, or explainable anomaly detection. The review found limited published work combining all four for POLIX Level-2 observation screening while keeping the physical modulation check separate. The paper says “limited published work was identified,” not “this is the first.”

## 6. Exact dataset scope

- 25 POLIX Level-2 observations included in the project archive.
- 10 project-labelled source observations.
- 15 project-labelled blank-sky observations.
- 15 Matrix-C features per observation.
- 15 WeightedRoll fits for blank sky; 13 pass the project’s acceptable-fit rule of reduced chi-square \(\le2\).
- The archive is not claimed to contain all public POLIX observations.

## 7. What each project stage did

1. **Archive organization:** matched observation identifiers and product files.
2. **Feature engineering:** converted heterogeneous products into Matrix A, B, and C summaries.
3. **Frozen screening:** standardized Matrix C and applied PCA, KMeans, and Isolation Forest.
4. **Local explanation:** ranked features by four within-observation evidence components.
5. **Sanity check:** neutralized leading features in six exploratory cases.
6. **Independent physical branch:** fitted WeightedRoll with a second-harmonic model.
7. **Blank-sky comparison:** compared fractional harmonic coordinates with a 13-fit empirical reference.
8. **Interface:** exposed saved outputs in a Flask research prototype.
9. **Paper audit:** checked versioning, stability, claim boundaries, references, and reproducibility without retraining the project.

## 8. All 15 Matrix-C features by product family

### Roll exposure

1. `t1A_exp_uniformity_cv`: coefficient of variation of exposure across roll bins. A larger value means less uniform exposure.
2. `t1A_exp_max_to_min_roll`: maximum-to-minimum exposure ratio. It describes exposure imbalance and is not a source property.

### Channel distribution

3. `t1A_energy_peak_channel`: channel index with the largest summarized response. It is not a calibrated energy peak.
4. `t1A_energy_weighted_mean_channel`: response-weighted average channel. It is not a spectral centroid in keV.
5. `t1A_energy_weighted_std_channel`: response-weighted channel spread. It is not calibrated spectral width.
6. `t1A_energy_high_channel_fraction`: fraction above the project’s channel-index threshold of 4000. Say “high-channel,” not “high-energy.”
7. `t1A_energy_channel_entropy`: spread/disorder of the channel distribution.
8. `t1A_energy_anode_balance_cv`: relative variation among anode summaries.

### Source azimuth

9. `t1B_src_peak_to_median_roll`: ratio between the peak and median source-azimuth values across roll.
10. `t1B_src_roll_entropy`: spread/disorder across source-roll bins.
11. `t1B_src_roll_smoothness_norm`: normalized mean absolute first difference in stored order. The safe name is “order-dependent roughness proxy” because the circular closing difference is omitted.

### Delivered light curve

12. `t2_lc_rate_cv`: coefficient of variation of the delivered RATE array.
13. `t2_lc_peak_to_median_rate`: peak-to-median ratio in the delivered RATE array.

These two are diagnostic proxies. They do not prove intrinsic source variability, flares, or a physical timing state.

### Cross-detector

14. `t2_det_lc_rate_balance_cv`: relative imbalance of delivered detector-rate summaries.
15. `t2_det_pha_centroid_spread`: spread of detector pulse-height channel centroids. It is not a calibrated energy spread.

## 9. PCA in simple language

Principal component analysis rotates the standardized 15-dimensional feature space to show directions with large variance. The two-component plot is a map for geometric inspection. A far-away observation is unusual in that projection, but PCA does not decide the deployed candidate label and does not explain a physical cause.

## 10. KMeans in simple language

KMeans divides standardized observations into five clusters and gives each observation a nearest fitted centroid. Feature-wise squared differences from that centroid contribute to the local explanation. In this small archive, two clusters contain only one observation. Sco X-1 and Blank Sky-13 therefore have zero distance from their own singleton centroids. That does not mean they are normal.

## 11. Isolation Forest in simple language

Isolation Forest repeatedly splits feature space. Observations isolated with fewer splits tend to receive more unusual scores. In the saved model, contamination 0.16 sets an approximate candidate fraction and produces four candidates. Contamination is a threshold assumption, not the true percentage of anomalous POLIX observations.

## 12. The custom four-component XAI method

For each feature within one observation, the method combines:

1. **PCA separation contribution:** how strongly the standardized feature contributes to the first two PCA coordinates.
2. **KMeans centroid contribution:** squared displacement from the assigned centroid in that feature.
3. **Isolation Forest occlusion contribution:** change in anomaly score when that standardized feature is replaced by zero; only positive changes enter.
4. **Standardized abnormality:** absolute z-score of the feature.

Each component is normalized within the observation, then summed. Therefore the result is a local ranking of composite evidence. It is model-informed, deterministic, and product-mappable. It is not SHAP, a Shapley value, causal explanation, exact Isolation Forest label attribution, or a score that can be compared absolutely across different observations.

## 13. WeightedRoll and harmonic fitting

WeightedRoll is an exposure-weighted roll-modulation product containing source and background contributions. The project fits:

\[
y(\phi)=C+Q\cos(2\phi)+U\sin(2\phi).
\]

\(C\) is the fitted constant term. \(Q\) and \(U\) are cosine and sine harmonic coefficients. The fractional coordinates are \(q=Q/C\) and \(u=U/C\). Raw modulation is

\[
m_{\mathrm{raw}}=\frac{\sqrt{Q^2+U^2}}{C},
\]

and fitted phase is

\[
\psi_{\mathrm{fit}}=\tfrac12\operatorname{atan2}(U,Q).
\]

These equations summarize the curve. In this project, \(Q/U\) are not claimed as calibrated sky Stokes quantities, raw modulation is not PD, and fitted phase is not official PA.

## 14. Why blank sky was used

Blank-sky observations provide an empirical view of raw modulation and harmonic-coordinate scatter in the same project archive. Thirteen of 15 blank-sky fits pass the project’s reduced-chi-square \(\le2\) rule and define the reference centre/scatter. The reference is useful for archive diagnostics, but it is not official background subtraction, a matched-background model, or a confidence/detection region.

## 15. The four fixed candidates

| Fixed candidate | Saved score | Leading evidence summary |
|---|---:|---|
| Blank Sky-13 (C24_0018) | 0.615964 | Energy weighted standard channel |
| Sco X-1 (G01_0006) | 0.593516 | Peak channel 2.454499; weighted mean 2.207369; entropy 1.813968 |
| Her X-1 (G01_0003) | 0.572308 | Delivered-light-curve rate coefficient of variation |
| Blank Sky-5 (C24_0010) | 0.517611 | Source-roll order-dependent roughness proxy |

The fixed model result is 21 Normal and four anomaly candidates. “Candidate” means statistically unusual relative to this archive, not confirmed anomaly.

## 16. The three-candidate tested-procedure result

Across 100 recorded Isolation Forest seeds, Blank Sky-13, Sco X-1, and Her X-1 were flagged 100/100 times. Blank Sky-5 was flagged 29/100 times. A fixed-Normal case, Blank Sky-15, appeared 68/100 times. The safe wording is:

> A three-candidate Matrix-C core was stable under the tested procedures, while the threshold neighbourhood was seed-sensitive.

Do not shorten this to “robust anomalies.”

## 17. Main non-equivalence finding

Statistical unusualness and modulation-like harmonic behaviour are different questions within the archive. Examples:

- Sco X-1 is ML-stable, but its harmonic coordinates are close to the empirical blank-sky centre.
- Her X-1 is ML-stable, but its simple harmonic fit is poor, limiting physical interpretation.
- Crab P01_0005 is not a fixed Matrix-C candidate even though its raw harmonic summary is visible and its fit is acceptable.
- Blank Sky-13 is ML-stable with a caution fit.
- Blank Sky-5 has an acceptable fit but a seed-sensitive ML flag.

This pattern supports separate inspection branches. It does not prove or disprove polarization.

## 18. What the paper contributes

**Primary:** a traceable, product-aware XAI framework for archive-relative screening of heterogeneous POLIX Level-2 observations.

**Secondary:**

1. a 15-feature provenance-preserving observation representation;
2. a deterministic, project-specific local feature-ranking method; and
3. a separate WeightedRoll/empirical blank-sky harmonic diagnostic.

Stability checks, feature neutralization, and Flask deployment support the framework. They are not separate major contributions.

## 19. What the paper does not prove

- No astrophysical discovery.
- No confirmed anomaly or official anomaly ground truth.
- No polarization detection.
- No calibrated polarization degree.
- No official sky polarization angle.
- No official background subtraction or \(\mu_{100}\).
- No causal cause for any candidate.
- No superiority over other methods.
- No generalization to future POLIX releases.
- No SHAP or LIME deployment.

## 20. Important limitations

1. Only 25 observations.
2. No trusted anomaly labels.
3. Same-archive retrospective model description.
4. Contamination fixes the four-candidate threshold.
5. Seed-sensitive boundary cases.
6. Candidate membership depends on feature tier.
7. Two singleton KMeans clusters.
8. Channel-space and other proxy semantics.
9. Project-specific XAI heuristic.
10. Only six in-sample neutralization cases.
11. WeightedRoll contains source plus background.
12. The 13-fit empirical reference is selected and archive-specific.
13. Fit-quality bands are project-defined, not p-values.
14. Diagonal harmonic distance ignores covariance and uncertainty.
15. No official background/calibration chain.
16. Notebook 11 and Flask propagate \(A/C\) uncertainty differently.
17. The original environment was not fully pinned.
18. No future-release validation or domain-expert confirmation.

## 21. Section-by-section paper explanation

### I. Introduction

- **What the paper says:** POLIX products are heterogeneous, the archive is unlabeled, and the project links traceable screening to a separate physical diagnostic.
- **What it means simply:** We need one careful workflow to compare observations without pretending an ML flag is physics.
- **What evidence supports it:** Official mission/handbook sources, feature inventory, saved model, and literature audit.
- **What a reviewer may ask:** Why is this a research contribution rather than an application of standard algorithms?
- **Safe student answer:** The contribution is the traceable product-aware integration and evidence separation for POLIX; the algorithms themselves are standard.
- **What must not be claimed:** First, novel, superior, or generally validated.

### II. Literature Review

- **What the paper says:** Prior work covers instrumentation, polarimetric analysis, anomaly screening, and XAI, but limited directly comparable integration was identified.
- **What it means simply:** Relevant pieces exist, but the review did not find the same complete POLIX workflow.
- **What evidence supports it:** Verified 18-source library and reference–claim map.
- **What a reviewer may ask:** Was the search comprehensive enough for a priority claim?
- **Safe student answer:** No priority claim is made; the statement is deliberately scoped to reviewed sources.
- **What must not be claimed:** “The first” or “never attempted.”

### III. Dataset, Scope, and Problem

- **What the paper says:** The frozen project archive has 25 observations, mapped as 10 source and 15 blank sky, with no trusted anomaly labels.
- **What it means simply:** This is a small, unlabeled case study.
- **What evidence supports it:** Identifier inventory and role metadata.
- **What a reviewer may ask:** Are these all public POLIX observations?
- **Safe student answer:** No. They are the 25 observations included in the project archive.
- **What must not be claimed:** Complete coverage or official labels.

### IV. Feature Engineering

- **What the paper says:** Matrix C contains 15 traceable summaries from five product families; WeightedRoll is separate.
- **What it means simply:** Each complex observation becomes one row, but every number can be traced back to a product.
- **What evidence supports it:** Matrix-C CSV, Notebook 08, extractor, and PKL feature list.
- **What a reviewer may ask:** Are the channel features calibrated energy measurements?
- **Safe student answer:** No. They are channel-space diagnostic summaries.
- **What must not be claimed:** Spectral peaks in keV, intrinsic variability, or circular smoothness.

### V. Explainable Unsupervised Methodology

- **What the paper says:** StandardScaler, PCA, KMeans, and Isolation Forest screen the archive; a custom four-component score ranks local evidence.
- **What it means simply:** The model finds unusual rows, then the explanation points to which product summaries made each row stand out.
- **What evidence supports it:** Saved PKL, exact `model_service.py`, reproduction CSV, and Agent-5 audit.
- **What a reviewer may ask:** Does the explanation exactly explain the Isolation Forest decision?
- **Safe student answer:** No. It is a model-informed composite local heuristic; the label comes only from `IsolationForest.predict`.
- **What must not be claimed:** SHAP, causal attribution, or exact label decomposition.

### VI. Independent Harmonic Diagnostic

- **What the paper says:** WeightedRoll is fitted separately with a second harmonic and compared with a 13-fit empirical blank-sky reference.
- **What it means simply:** The project checks the raw modulation curve without feeding it into the anomaly model.
- **What evidence supports it:** Notebook 11, harmonic-result CSVs, blank-sky baseline, and handbook.
- **What a reviewer may ask:** Are \(Q,U\) calibrated Stokes parameters?
- **Safe student answer:** No. They are fitted harmonic coefficients; the paper uses fractional harmonic coordinates.
- **What must not be claimed:** Official subtraction, PD, PA, or detection.

### VII. Results

- **What the paper says:** The fixed model has four candidates, three are seed-stable in the tested procedure, feature tiers differ, and physical evidence does not mirror ML evidence.
- **What it means simply:** Some cases repeatedly look unusual, but what looks unusual depends partly on representation and is different from raw modulation.
- **What evidence supports it:** Prediction, seed, ablation, XAI, harmonic, and source-comparison CSVs.
- **What a reviewer may ask:** Why is Blank Sky-5 still listed if unstable?
- **Safe student answer:** It is part of the authoritative fixed saved model result, but its seed sensitivity is disclosed.
- **What must not be claimed:** Four equally robust anomalies or statistical significance from the threshold.

### VIII. Discussion

- **What the paper says:** Sco X-1, Her X-1, Crab P01_0005, and blank-sky cases demonstrate non-equivalence.
- **What it means simply:** The two branches are complementary, not confirmation tests.
- **What evidence supports it:** Candidate/XAI tables and representative harmonic CSV rows.
- **What a reviewer may ask:** What physical cause explains the disagreement?
- **Safe student answer:** The project does not establish a cause; POLIX-aware inspection and calibration are required.
- **What must not be claimed:** Source physics, instrument malfunction, or background cause.

### IX. Limitations

- **What the paper says:** Small sample, no labels, threshold/tier dependence, proxy semantics, heuristic XAI, physical calibration boundaries, and reproducibility gaps restrict the claims.
- **What it means simply:** The project is useful for triage but not a final scientific decision.
- **What evidence supports it:** Agents 2–6 and 9, code audits, and handbook.
- **What a reviewer may ask:** Why submit without future-data validation?
- **Safe student answer:** The paper is framed as an archive-specific applied case study and openly states that prospective validation is future work.
- **What must not be claimed:** Production readiness or future performance.

### X. Conclusion

- **What the paper says:** The integrated workflow was implemented, four candidates were observed, three were stable under tested seeds, and the branches were non-equivalent.
- **What it means simply:** The project helps researchers know where to inspect, without claiming a discovery.
- **What evidence supports it:** Frozen model, sensitivity outputs, XAI audit, and harmonic comparison.
- **What a reviewer may ask:** What is the next scientifically valid step?
- **Safe student answer:** Apply official background/calibration guidance, pin the environment, and validate prospectively on later expert-reviewed releases.
- **What must not be claimed:** The framework proved polarization or anomaly truth.

## 22. Twenty likely guide/reviewer questions with safe answers

1. **Why unsupervised learning?** No trusted anomaly labels existed, so supervised accuracy claims were not defensible.
2. **Why Matrix C?** It was the completed project’s deployed tier and includes five product families; ablation is reported as sensitivity, not proof of optimality.
3. **Why contamination 0.16?** It is the frozen project setting that yields four candidates; it is not an estimate of prevalence.
4. **Are four candidates confirmed anomalies?** No. They are archive-relative candidates requiring expert inspection.
5. **Why use PCA and KMeans if Isolation Forest sets the label?** They add complementary geometric and local-structure evidence and support inspection.
6. **Why does KMeans give zero distance to two candidates?** They form singleton clusters, so each equals its own centroid.
7. **Is the XAI score SHAP?** No. It is a project-specific normalized sum of four local evidence components.
8. **Can feature scores be compared across observations?** No. Normalization is within each observation.
9. **What happened to the historical Sco X-1 entropy-first result?** It was superseded because no located versioned artifact reproduced it; the exact current order is peak, weighted mean, entropy.
10. **What does the faithfulness test prove?** Only that neutralizing ranked features changed PCA/Isolation evidence in six in-sample cases under the project rule.
11. **Why keep WeightedRoll separate?** To avoid circular confirmation and because it has different physical semantics.
12. **Are \(Q,U\) Stokes parameters?** They are fit coefficients related to a second harmonic; without full calibration the paper calls them harmonic coefficients.
13. **Is raw modulation PD?** No. PD requires an official modulation factor and background/calibration treatment.
14. **Is fitted phase PA?** No. Official PA requires verified coordinate conversion and calibration.
15. **Why only 13 blank-sky fits?** Thirteen of 15 meet the project-defined acceptable rule \(\chi_\nu^2\le2\).
16. **Is that reference official background subtraction?** No. It is an empirical archive diagnostic.
17. **What is the strongest result?** The fixed model produces four candidates, with a three-candidate core stable under tested seeds, while the harmonic branch shows non-equivalent evidence.
18. **What is fragile?** Boundary membership, especially Blank Sky-5; representation choice; physical interpretation of poor fits; future-data generalization.
19. **Why no new experiments?** The accepted workflow freezes the completed project. Desired prospective validation is disclosed as future work.
20. **Is the content submission-ready?** No. It is guide-ready after final checks; author order, venue, figures, domain interpretation, disclosure policy, and human revision remain pending.

## 23. Ten-minute oral explanation script

“Our paper is titled *An Explainable AI Framework for Analysis of X-Ray Polarimetry Data from XPoSat*. It is an applied scientific-computing paper about how to inspect heterogeneous POLIX Level-2 observations. It is not an astrophysical-discovery or calibrated-polarimetry paper.

The project archive contains 25 observations: 10 project-labelled sources and 15 project-labelled blank skies. POLIX gives multiple product types rather than one uniform table. We therefore designed a traceable observation representation. Matrix A first summarized roll exposure and channel distributions. Matrix B added source-azimuth summaries. Matrix C added delivered-light-curve and detector summaries, giving 15 deployed features. WeightedRoll was excluded because it contains different physical information and includes source and background contributions.

The frozen screening stack uses StandardScaler, PCA, KMeans, and Isolation Forest. StandardScaler puts features on comparable scales. PCA gives a low-dimensional geometric view. KMeans describes assigned local clusters. Isolation Forest produces the saved candidate decision. Because no trusted anomaly labels exist, we call outputs anomaly candidates relative to the project archive, not confirmed anomalies.

The fixed saved model gives 21 Normal outputs and four candidates: Blank Sky-13, Sco X-1, Her X-1, and Blank Sky-5. In the recorded 100-seed test, the first three appeared 100 times, while Blank Sky-5 appeared 29 times. Therefore we describe a three-candidate Matrix-C core stable under the tested procedures and disclose an unstable threshold neighbourhood.

To explain each observation, the project combines four components: PCA separation, KMeans feature displacement, Isolation Forest occlusion, and absolute standardized abnormality. The components are normalized within the observation and summed to rank features. This is not SHAP and does not exactly decompose the Isolation Forest label. For Sco X-1, the authoritative order is energy peak channel, weighted mean channel, and channel entropy. These are channel-space proxies, not calibrated spectral measurements.

Six exploratory cases were used in a feature-neutralization sanity check. The top standardized features were set to zero, and PCA distance and Isolation Forest score were recomputed. Five cases received the project’s Strong verdict and one Moderate. This supports internal behavioural consistency only; it is not external validation.

The physical branch fits WeightedRoll independently with \(C+Q\cos2\phi+U\sin2\phi\). We report harmonic coefficients, fractional coordinates, raw modulation, fitted phase, and fit quality. We do not report calibrated PD or official PA. Thirteen blank-sky fits with reduced chi-square at most two form an empirical reference. This reference is not official background subtraction.

The main finding is that statistical unusualness and modulation-like harmonic behaviour are non-equivalent within the archive. Sco X-1 is ML-stable but close to the blank-sky harmonic centre. Her X-1 is ML-stable, but its simple harmonic fit is poor. Crab P01_0005 is not a fixed ML candidate even though its harmonic fit is acceptable. Blank Sky-13 and Blank Sky-5 also show different ML-stability and fit-quality combinations.

The primary contribution is the traceable integrated framework. The secondary contributions are the 15-feature product-aware representation, the deterministic local ranking, and the independent harmonic branch. The Flask application supports reproducible inspection.

The main limitations are the sample of 25, no ground truth, retrospective archive fitting, fixed contamination, feature-tier dependence, singleton KMeans clusters, proxy feature semantics, heuristic XAI, six-case in-sample perturbation, source-plus-background WeightedRoll, empirical selected reference, no official calibration, and an uncertainty mismatch between Notebook 11 and the later Flask service. Our conclusion is therefore deliberately narrow: the workflow helps researchers inspect archived POLIX products, but it does not establish discoveries, confirmed anomalies, PD, or PA.”

## 24. Two-minute elevator explanation

“POLIX observations contain several different Level-2 products, so our completed project first converted each of 25 archived observations into 15 traceable summaries. We standardized those features and used PCA, KMeans, and Isolation Forest to screen the archive without anomaly labels. The fixed model flagged four candidates. Three were selected in all 100 tested Isolation Forest seeds, while Blank Sky-5 was seed-sensitive.

We then used a custom four-component local ranking to show which Matrix-C features contributed composite evidence for each observation. It combines PCA separation, KMeans displacement, Isolation Forest occlusion, and standardized abnormality. It is project-specific and is not SHAP or causal attribution.

WeightedRoll was intentionally kept out of Matrix C. We fitted it separately with a second harmonic and compared fractional harmonic coordinates with 13 acceptable blank-sky fits. This revealed the main bounded finding: statistical unusualness and modulation-like harmonic behaviour do not identify the same property within the frozen archive.

The contribution is a traceable product-aware inspection framework, not a discovery claim. We do not report confirmed anomalies, calibrated polarization degree, official polarization angle, or official background subtraction. The study is limited by 25 unlabeled observations and requires guide and POLIX-domain review.”

## 25. Terms and equations to remember

| Term | Safe meaning |
|---|---|
| Archive-relative | Defined with respect to these 25 observations |
| Candidate | Flagged by the fixed model; not confirmed |
| StandardScaler | Subtracts fitted mean and divides by fitted standard deviation |
| PCA | Variance-oriented linear projection |
| KMeans | Assigned-centroid clustering |
| Isolation Forest | Isolation-based anomaly ranking and saved label source |
| Contamination | Imposed candidate-fraction setting, not prevalence |
| Local XAI ranking | Within-observation composite heuristic |
| Occlusion | Replace one standardized feature by zero and recompute score |
| Feature neutralization | Replace selected standardized features by the reference value zero |
| WeightedRoll | Exposure-weighted source-plus-background roll modulation |
| Harmonic coefficients | Fitted \(C,Q,U\) in the second-harmonic model |
| Fractional coordinates | \(q=Q/C,\ u=U/C\) |
| Raw modulation | \(\sqrt{Q^2+U^2}/C\), not calibrated PD |
| Fitted phase | \(\frac12\operatorname{atan2}(U,Q)\), not official PA |
| Reduced chi-square | Fit-residual summary; project bands are not p-values |
| Empirical blank-sky reference | Archive diagnostic from 13 selected fits, not official subtraction |

Core equations:

\[
z_{ij}=\frac{x_{ij}-\mu_j}{\sigma_j},
\qquad
k_{ij}=(z_{ij}-c_{g(i)j})^2,
\]

\[
e_{ij}=N(p_{ij})+N(k_{ij})+N(\max(o_{ij},0))+N(|z_{ij}|),
\]

\[
y(\phi)=C+Q\cos(2\phi)+U\sin(2\phi),
\]

\[
q=\frac QC,\quad u=\frac UC,\quad
m_{\mathrm{raw}}=\frac{\sqrt{Q^2+U^2}}C,\quad
\psi_{\mathrm{fit}}=\frac12\operatorname{atan2}(U,Q).
\]

Final sentence to remember:

> The framework screens statistical unusualness relative to a frozen archive and compares it with a separate raw harmonic diagnostic; neither branch establishes calibrated polarization or astrophysical truth.
