# V3 Scientific Content Audit

## Audit scope and controlling evidence

This package is a factual input to Version 3, not manuscript prose. No model was retrained, no feature matrix was regenerated, and no new scientific experiment was run. Read-only calculations were limited to applying the saved scaler, PCA, KMeans, Isolation Forest, and deployed explanation function to already frozen Matrix-C rows.

Evidence was controlled in this order: observation identifiers and archive roles; numerical CSVs and their generating notebooks or code; saved model plus deployed service code; existing robustness outputs; verified primary literature for general context; and prior reports or drafts only for orientation. The 2025 handbook and uploaded architecture image are not evidence for V3 and should not be cited.

The detailed feature definitions, observation case packs, contradictions, figure values, and claim-level evidence are in the five companion files:

- `v3_feature_dictionary.csv`
- `v3_candidate_case_studies.md`
- `v3_contradiction_audit.md`
- `v3_figure_interpretation.md`
- `v3_claim_evidence_matrix.csv`

## Part 1 — Actual research contribution

### 1.1 Problem actually solved

The project converts several heterogeneous POLIX Level-2 product families into one traceable, observation-level table and uses that table to prioritize observations for inspection relative to the 25-observation project archive. For a flagged observation, the system reports which engineered features and originating product families provide the strongest local evidence. A separate analysis examines the delivered WeightedRoll curve with a second-harmonic fit and an empirical blank-sky reference. Thus, a researcher can move from an archive-level screening result back to specific products requiring inspection without treating the screening label as a physical diagnosis.

The system does **not** determine whether an observation is astrophysically anomalous, instrumentally faulty, or polarized. It prioritizes archive-relative unusualness under a frozen feature representation and screening rule.

### 1.2 Contribution hierarchy

| Category | Defensible contribution | Strength and boundary |
|---|---|---|
| Primary scientific/computational | A traceable, product-aware framework for archive-relative screening of heterogeneous POLIX Level-2 observations. | Moderate applied-method contribution. It is demonstrated on 25 project observations, not prospectively validated. |
| Secondary methodological | A 15-feature Matrix-C representation retaining feature-to-product provenance across exposure, energy-resolved azimuth, source azimuth, delivered light curve, and detector-context products. | Useful representation design; it is hand-engineered and not proven optimal. |
| Secondary explainability | A deterministic, model-informed local feature-ranking heuristic combining four normalized evidence components and mapping ranked features back to POLIX product families. | Local evidence ranking, not SHAP, a causal explanation, a probability, or an exact decomposition of the Isolation Forest score. |
| Secondary scientific-method | Deliberate separation of Matrix-C screening from WeightedRoll second-harmonic and empirical blank-sky diagnostics. | Prevents circular confirmation and supports the non-equivalence result; it is not calibrated polarimetry. |
| Implementation/tool | A Flask research interface for upload, feature extraction, analysis, visualization, and export. | Supporting implementation and reproducibility contribution, not a standalone research contribution. |

Seed, contamination, jackknife, feature-tier, and six-case perturbation results support or qualify these contributions; they are not separate main contributions.

### 1.3 What is genuinely POLIX-specific

The machine-learning algorithms are generic. POLIX specificity lies in the input representation and provenance:

- exposure-versus-roll summaries from the exposure–azimuth product;
- channel-space distribution summaries and the 48-anode balance statistic from the energy-resolved source-azimuth product;
- peak-to-median, entropy, and order-dependent adjacent-bin roughness from the source-azimuth product;
- delivered source-light-curve summaries and cross-detector rate/centroid dispersion;
- explicit feature-to-product-family mapping in the explanation output; and
- independent treatment of the delivered WeightedRoll curve rather than including it in Matrix C.

These elements define what the framework asks of POLIX Level-2 products. StandardScaler, PCA, KMeans, and Isolation Forest alone are not POLIX-specific.

### 1.4 Concrete researcher utility

The supported workflow is: process an observation into the same 15 summaries; obtain its archive-relative Isolation Forest score and label; inspect its PCA/KMeans context descriptively; inspect the local feature and product-family ranking; return to the implicated source products; inspect the separate WeightedRoll harmonic result; and decide whether domain, instrument, calibration, or data-quality review is warranted. The framework can reduce unstructured manual browsing by providing a consistent triage order and product-level pointers. No measured time saving or automated scientific-discovery claim is supported.

## Part 2 — Research gap and novelty boundary

### 2.1 Related pieces already exist

Existing work provides XPoSat/POLIX mission and instrument context, harmonic or Stokes-based polarimetric foundations, general astronomical anomaly detection, standard PCA/KMeans/Isolation Forest methods, explainable-anomaly approaches, and perturbation-based explanation evaluation. The contribution is not any one of those components in isolation.

### 2.2 Useful combination in this project

Within the finite verified literature set, no directly comparable workflow was identified that combines a POLIX Level-2 product-aware observation representation, archive-relative unsupervised screening, deterministic feature/product-family evidence ranking, and an intentionally independent WeightedRoll/blank-sky harmonic branch. This is a bounded literature finding, not proof of first use.

### SAFE NOVELTY CLAIMS

- “This work investigates an integrated, product-aware workflow for unsupervised screening of POLIX Level-2 observations.”
- “Limited published work was identified that directly combines these four elements for POLIX.”
- “The reviewed literature did not provide a directly comparable POLIX workflow.”
- “The contribution is the traceable integration and POLIX-specific representation, evaluated on the project archive.”

### UNSAFE NOVELTY CLAIMS

- “The first explainable AI system for POLIX.”
- “A novel or unique method” without a comprehensive systematic review.
- “Superior to existing methods” without a quantitative benchmark.
- “A breakthrough, discovery, or confirmed anomaly detector.”

## Part 3 — Feature semantics

The exact 15-feature dictionary is in `v3_feature_dictionary.csv`. None of the 15 features is a calibrated physical measurement. They are descriptive statistics or engineering proxies whose values become archive-relative diagnostics after standardization. Channel positions are channel indices, not calibrated energies. Delivered-light-curve variation is a property of the delivered product under the implemented calculation, not intrinsic source variability. Source-azimuth roughness is the mean absolute difference between adjacent stored bins divided by the mean; the implementation does not add a final-to-first wraparound difference. High-channel fraction refers to the implemented channel-index threshold, not a calibrated high-energy fraction.

## Part 4 — Matrix A/B/C story

| Matrix | Included features | Fixed candidates |
|---|---|---|
| A | Eight Tier-1A exposure and energy/anode summaries | C24_0018, C24_0020, G01_0006, P01_0005 |
| B | Matrix A plus three source-azimuth summaries | C24_0010, C24_0018, C24_0020, G01_0006 |
| C | Matrix B plus four delivered-light-curve and detector-context summaries | C24_0010, C24_0018, G01_0003, G01_0006 |

Sco X-1 (G01_0006) and Blank Sky-13 (C24_0018) persist across A, B, and C, showing that their selection is not dependent on only the four Matrix-C additions under these frozen tier configurations. Her X-1 (G01_0003) appears only in Matrix C, consistent with its leading delivered-light-curve features. Crab P01_0005 appears only in Matrix A, showing that candidate status can change when the representation changes. These results demonstrate feature-tier dependence; they do not establish that Matrix C is objectively better or that persistent cases are physically more important.

## Part 5 — Candidate case studies

The exact five case packs are in `v3_candidate_case_studies.md`. Their framework roles are:

- **Sco X-1:** fixed candidate, selected in 100/100 seed runs and across A/B/C; local evidence is led by energy/channel-space summaries. This supports inspection of the corresponding product, not an energy-spectrum or physical-cause claim.
- **Her X-1:** fixed candidate, selected in 100/100 seeds, Matrix-C-only, with delivered-light-curve summaries leading its local evidence; its simple second-harmonic fit is very poor. It demonstrates that local statistical unusualness and fit adequacy are separate questions.
- **Blank Sky-13:** highest fixed score, selected in 100/100 seeds and across A/B/C, but excluded from the 13-fit blank-sky reference because reduced chi-square exceeds 2. Its selection shows that the model is not a source or polarization classifier.
- **Blank Sky-5:** fixed candidate under seed 42 but selected in only 29/100 seed runs. It is a boundary-sensitive case, not part of the three-candidate tested-procedure core.
- **Crab P01_0005:** fixed Normal in Matrix C, selected in only 3/100 seed runs, A-only across tiers, and acceptably represented by the simple harmonic model. It is a useful comparison showing that scientific prominence or visible modulation does not imply Matrix-C candidate status.

## Part 6 — Sco X-1 XAI figure interpretation

| Ranked feature | Raw value | Matrix-C z value | Local ranking score |
|---|---:|---:|---:|
| Energy peak channel | 465 | +4.894106 | 2.454499 |
| Energy weighted mean channel | 1648.3309997 | -3.432505 | 2.207369 |
| Energy channel entropy | 11.9933947 | -2.855662 | 1.813968 |

The three features rank highest because the deployed heuristic aggregates their normalized PCA, KMeans, Isolation Forest occlusion, and absolute standardized-magnitude evidence. Sco X-1 forms a singleton KMeans cluster in the frozen model, so KMeans feature contributions are zero for that observation; its ordering comes from the other components. The combined scores are ordinal within Sco X-1 and are not calibrated magnitudes or reliably comparable across observations. The z values express position relative to the 25-row Matrix-C scaling distribution. The peak and weighted-mean values are channel indices and entropy is a distribution-shape statistic; none directly establishes a calibrated energy or astrophysical mechanism.

Legitimate conclusion: under the deployed project heuristic, Sco X-1’s archive-relative unusualness is most strongly associated with three summaries derived from the energy-resolved product, which identifies that product family for inspection.

## Part 7 — WeightedRoll figure interpretation

| Observation | C | Q | U | Amplitude | Raw modulation (%) | Fitted phase (deg) | Reduced chi-square | dof | Bins | Error use | Category | Fixed ML label |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| Sco X-1 | 170.932232 | 1.704594 | -0.942709 | 1.947907 | 1.139578 | 165.527814 | 2.030761 | 357 | 360 | supplied errors | caution | Candidate |
| Crab P01_0005 | 174.050062 | 2.468975 | -1.622235 | 2.954232 | 1.697346 | 163.346589 | 1.062540 | 357 | 360 | supplied errors | acceptable | Normal |
| Her X-1 | 154.613107 | -0.326388 | -0.862800 | 0.922471 | 0.596632 | 124.639464 | 57.433514 | 357 | 360 | supplied errors | poor | Candidate |

The coefficients belong to the project model (y(\phi)=C+Q\cos(2\phi)+U\sin(2\phi)). Here Q and U are fitted harmonic coefficients, not unqualified calibrated Stokes parameters. Raw modulation is (100\sqrt{Q^2+U^2}/C), and fitted phase is not official sky polarization angle.

Crab is useful because it has the largest raw modulation of the three displayed cases but is Matrix-C Normal and has an acceptable simple fit. Sco X-1 is an ML candidate with lower raw modulation and a caution-category fit. Her X-1 is an ML candidate with low raw modulation but an extremely poor simple fit; the delivered curve contains prominent localized structure and residual excursions that a single second harmonic cannot summarize. The high reduced chi-square records model inadequacy under the supplied errors; it does not identify the cause. Together, these cases support non-equivalence between Matrix-C unusualness, raw harmonic magnitude, and second-harmonic fit adequacy.

## Part 8 — The XAI claim

For a standardized row (x), the deployed function calculates:

1. **PCA component:** absolute per-feature products of the standardized value and each of the first two PCA loading vectors, weighted by the respective explained-variance ratios and summed.
2. **KMeans component:** squared per-feature difference from the assigned centroid.
3. **Isolation Forest component:** the change in negative `score_samples` after replacing one standardized feature with zero, retaining only positive changes before normalization.
4. **Standardized-magnitude component:** absolute standardized feature value.

Each component vector is divided by its maximum absolute finite value; a non-finite or zero maximum yields an all-zero component. The four normalized vectors are then added with equal implicit weight. The implementation performs no probability calibration and no cross-observation normalization. Negative occlusion changes are clipped to zero. For a singleton cluster, the row equals its centroid and all KMeans contributions are zero.

The result measures a composite of local archive deviation, two-dimensional PCA geometry, assigned-centroid separation, and one-feature occlusion sensitivity. It does not measure causality, probability, physical importance, prediction accuracy, or an additive decomposition of the Isolation Forest decision. “Project-specific, model-informed local feature-ranking heuristic” remains accurate. “Composite archive-relative local evidence ranking” is a more literal alternative, but the existing phrase more clearly signals use of model components while retaining the heuristic boundary.

## Part 9 — Neutralization/explanation check

The existing experiment neutralized the top three ranked standardized features for six cases by setting them to zero, then recomputed three evidence measures.

| Observation | Neutralized features (abbreviated) | PCA before→after | IF before→after | KMeans before→after | Project verdict |
|---|---|---:|---:|---:|---|
| Sco X-1 | peak, weighted mean, entropy | 3.435667→1.402399 | 0.593516→0.429706 | 0.000000→6.624890 | Strong |
| Blank Sky-13 | weighted spread, high-channel fraction, entropy | 4.598621→1.087332 | 0.615964→0.474996 | 0.000000→5.488487 | Strong |
| Her X-1 | light-curve CV, light-curve peak/median, source entropy | 4.999296→2.173506 | 0.572308→0.454444 | 4.418462→2.247871 | Strong |
| Blank Sky-5 | roughness, source peak/median, exposure max/min | 4.257909→1.453484 | 0.517611→0.437459 | 3.430534→2.994384 | Strong |
| Blank Sky-15 | detector-rate balance, entropy, light-curve CV | 3.830147→2.795604 | 0.513010→0.454567 | 2.944649→2.142905 | Strong |
| Blank Sky-6 | anode balance, exposure max/min, detector-rate balance | 1.897808→1.267127 | 0.396280→0.405040 | 1.234989→1.508996 | Moderate |

The stored verdict is Strong when PCA distance and Isolation Forest evidence both decrease, and Moderate when exactly one decreases; KMeans change is recorded but does not determine the verdict. This demonstrates local sensitivity of selected in-sample cases to neutralization of their top-ranked features. It does not prove unique attribution, causal faithfulness, general explanation validity, or performance on new observations. The most accurate name is **six-case feature-neutralization perturbation sanity check**.

## Part 10 — Stability evidence

### A. Random-seed test

- **Question:** Does Isolation Forest seed variation alter candidate selection while other assumptions remain fixed?
- **Procedure:** Matrix C, seeds 0–99, 100 trees, contamination 0.16.
- **Result:** Blank Sky-13, Sco X-1, and Her X-1 were selected 100/100 times; Blank Sky-5 29/100; Blank Sky-15 68/100; Crab P01_0005 3/100.
- **Interpretation:** A three-candidate Matrix-C core is stable under the tested seeds; Blank Sky-5 is seed-sensitive.
- **Limitation:** Same small archive and representation; this is not future-data validation.

### B. Contamination-value test

- **Question:** How does the candidate set change under nearby assumed candidate fractions?
- **Procedure:** contamination 0.12, 0.16, 0.20, and 0.24; corresponding candidate counts 3, 4, 5, and 6.
- **Result:** The three core cases persist at all settings; Blank Sky-5 enters at 0.16, Blank Sky-15 at 0.20, and Crab P01_0005 at 0.24.
- **Interpretation:** The top three are insensitive to the tested contamination settings; boundary cases are definition-dependent.
- **Limitation:** The values are selected sensitivity settings, not estimates of true anomaly prevalence.

### C. Included-observation jackknife/refit test

- **Question:** Does leaving one archive row out strongly change the fitted screening ordering?
- **Procedure:** Existing leave-one-out refits; each included observation receives 24 opportunities, with rank agreement evaluated on common rows.
- **Result:** The three core cases were flagged 24/24 times; Blank Sky-5 19/24, Blank Sky-15 7/24, and Crab 2/24. Common-row Spearman rank correlation had median 0.989565 and minimum 0.968696. Held-out prediction results differ for some cases, including Sco X-1 not flagged when held out.
- **Interpretation:** Rankings of included observations are stable under the tested deletion procedure, while extrapolation to a held-out row is less secure.
- **Limitation:** This is still resampling within the same 25 observations and does not constitute an independent evaluation set.

### D. Feature-tier A/B/C comparison

- **Question:** Is candidate selection dependent on which product-family tiers are represented?
- **Procedure:** Existing fixed Matrix A, B, and C fits.
- **Result:** Sco X-1 and Blank Sky-13 persist across all tiers; Her X-1 is C-only; Crab is A-only; Blank Sky-15 is A/B; Blank Sky-5 is B/C.
- **Interpretation:** Two cases persist, but other selections are representation-dependent.
- **Limitation:** There is no anomaly ground truth with which to declare one tier superior.

PCA–Isolation Forest rank correlation is high in the frozen archive (Spearman 0.894615), whereas PCA–KMeans (0.155799) and KMeans–Isolation Forest (0.186574) are low. These values are descriptive agreement measures. Nominal p-values, if present in exploratory outputs, must not be used as confirmatory population inference for this small, same-archive analysis.

## Part 11 — Empirical blank-sky reference

All 15 project-labelled blank-sky observations were fitted. The declared rule retained 13 with reduced chi-square at or below 2: C24_0020, C24_0010, C24_0021, C24_0007, C24_0015, C24_0009, C24_0019, C24_0022, C24_0002, C24_0001, C24_0024, C24_0014, and C24_0008. C24_0023 and C24_0018 were excluded because their reduced chi-square values were 6.920304 and 2.565811, respectively.

For the 13 retained fits, mean raw modulation is 1.147820%, with sample standard deviation 0.565960 percentage points. Mean fractional harmonic coordinates are q=0.009092 and u=-0.006478; sample standard deviations are 0.004857 and 0.004019. All ten source observations fall within the scalar mean ± two sample-standard-deviation raw-modulation rule.

This reference is an empirical description of selected delivered blank-sky fits in the project archive. It is not official background subtraction, a calibrated null distribution, a confidence region, or a significance test. The safest name for the mean ± two-standard-deviation comparison is **declared empirical blank-sky reference rule**; “descriptive threshold” is also acceptable. A stale boolean column in one combined fractional-coordinate file marks all 15 blank skies for use; V3 must instead apply the controlling reduced-chi-square rule and use 13.

## Part 12 — What the results actually show

1. **Astrophysical anomaly?** No. There are no trusted anomaly labels or causal follow-up data.
2. **Instrumental problem?** No. Screening and poor fit may motivate inspection but do not identify a cause.
3. **Polarization detection?** No. The reported harmonic quantities are uncalibrated diagnostics.
4. **Scientifically interesting observations?** The system identifies inspection priorities, which may be interesting for methodological or data-quality follow-up; scientific importance itself is not established.
5. **What is identified?** Observations statistically unusual relative to the 15-feature project archive under the frozen Isolation Forest rule, plus local feature/product-family evidence and independent harmonic-fit descriptors.
6. **Why are flagged blank skies not necessarily failure?** The model has no source/blank-sky target and screens product-feature unusualness. Blank-sky variation can legitimately be unusual within that representation.
7. **Why can a Normal source remain interesting?** Normal means not selected by this archive-relative threshold; it says nothing about astrophysical importance or polarization.
8. **Why does high raw harmonic amplitude not imply candidate status?** WeightedRoll is excluded from Matrix C, and raw harmonic magnitude measures a different delivered-curve property. Crab demonstrates this separation.
9. **Why does poor harmonic fit not invalidate an ML candidate?** Fit adequacy tests whether one simple harmonic summarizes a delivered curve; ML screening evaluates Matrix-C features. Her X-1 demonstrates the distinction.
10. **Strongest empirical conclusion:** Within the 25-observation project archive, statistical unusualness in Matrix C and modulation-like harmonic behavior are non-equivalent diagnostics.

## Part 13 — Practical POLIX usefulness

1. Load a POLIX Level-2 observation archive through the implemented interface.
2. Extract the same product-aware 15-feature row using the deployed feature extractor.
3. Apply the saved scaler and model to obtain an archive-relative Isolation Forest score and fixed screening label; view PCA and KMeans only as descriptive geometry.
4. For archive cases, consult the saved seed, contamination, jackknife, and tier analyses. The current interface does not automatically establish prospective stability for a new release.
5. Inspect the local ranked features and their mapped POLIX product families.
6. Return to the implicated original products and examine the underlying distributions or light curves.
7. Separately inspect the WeightedRoll second-harmonic coefficients, raw modulation, phase, residuals, fit category, and declared empirical blank-sky comparison.
8. Escalate selected cases for domain, instrument, calibration, or data-quality review rather than treating the software output as a scientific diagnosis.

The practical saving is organizational: the framework converts multi-product inspection into a repeatable prioritization and trace-back workflow. It may reduce undirected manual examination, but no timing or workload benchmark was performed.

## Part 14 — Ranked limitations and placement

| Rank | Limitation | Placement |
|---:|---|---|
| 1 | Only 25 observations and no trusted anomaly ground truth | Main paper |
| 2 | Same archive used for representation development and retrospective evaluation; no independent or future-release validation | Main paper |
| 3 | Contamination 0.16 defines four fixed candidates and is not estimated prevalence | Main paper |
| 4 | Hand-designed features and feature-tier dependence; channel indices are not calibrated energies | Main paper |
| 5 | Future-distribution behavior is unknown | Main paper |
| 6 | KMeans has singleton clusters, producing zero local centroid contribution for those rows | Main paper |
| 7 | XAI is a project-specific heuristic evaluated by only a six-case in-sample perturbation sanity check | Main paper; detailed values in supplement |
| 8 | WeightedRoll includes delivered source-plus-background behavior; the 13-fit reference is empirical, selected by a project rule, and not official subtraction | Main paper |
| 9 | No calibrated modulation factor or verified official sky-angle conversion is applied; no PD or PA is reported | Main paper |
| 10 | Notebook 11 and later Flask code use different A/C uncertainty propagation | Main-paper provenance sentence; details in supplement |
| 11 | Original environment is not fully pinned/containerized | Supplement and reproducibility statement |
| 12 | Detailed seed, contamination, jackknife, tier, harmonic, and perturbation tables are too large for the main story | Supplement |

Historical draft wording, superseded Sco X-1 ranking, old candidate lists, and obsolete imputation claims belong in the audit trail, not the scientific narrative. The excluded 2025 handbook and uploaded design image need not be discussed in V3.

## Part 15 — Future work

| Direction | Why it matters | Current limitation addressed |
|---|---|---|
| Prospective validation on later POLIX observations | Tests behavior under archive growth and distribution change | Same-archive retrospective evidence and future-distribution uncertainty |
| Domain-expert adjudication | Determines whether inspection priorities correspond to meaningful data-quality or scientific cases | No anomaly ground truth or verified causes |
| Calibrated channel-to-energy mapping where officially supported | Permits physically grounded energy interpretation | Current channel-index summaries |
| Integration of an officially supported background/calibration workflow | Enables calibrated polarimetric analysis separate from this screening system | Empirical blank-sky treatment and uncalibrated harmonic quantities |
| Larger blank-sky reference | Better characterizes background variability | Only 13 selected acceptable blank-sky fits |
| Covariance-aware blank-sky modelling | Treats joint q/u structure without pretending the present descriptive rule is a confidence region | Scalar and marginal empirical summaries |
| Independent evaluation set | Supports performance and generalization assessment | No trusted external test set |
| Comparative anomaly-detector evaluation | Tests whether findings depend on Isolation Forest | No quantitative model benchmark |
| Broader explanation evaluation | Tests stability, completeness, and usefulness beyond six in-sample cases | Limited perturbation sanity check |
| Pinned environment or container | Improves exact replay across systems | Unpinned original environment |

These are recommendations only. None was executed in this audit.

## Part 16 — Contradiction audit summary

The complete audit is in `v3_contradiction_audit.md`. V3 must use: four fixed Matrix-C candidates; three cases selected in 100/100 seeds; two cases persistent across A/B/C; six separate perturbation cases; the current Sco X-1 ordering of peak channel, weighted mean channel, then entropy; zero Matrix-C missing values and no imputation claim; 13 blank-sky reference fits chosen directly by reduced chi-square ≤2; Notebook-11 CSVs as the provenance for reported harmonic uncertainties; and WeightedRoll outside Matrix C. The stale all-15 reference boolean, historical entropy-first XAI narrative, old candidate sets, median-imputation wording, and any calibrated PD/PA or official-background wording must not enter V3.

## Part 17 — Claim-evidence matrix

`v3_claim_evidence_matrix.csv` contains 60 potential claims with YES/PARTIAL/NO status, exact evidence, source location, limitations, and safe/unsafe wording. Claims marked PARTIAL require the stated boundary; claims marked NO must be excluded.

## A. FIVE STRONGEST CLAIMS V3 SHOULD EMPHASIZE

1. The project represents 25 POLIX Level-2 observations through 15 traceable features drawn from five product families and preserves feature provenance.
2. The frozen Isolation Forest result selects four archive-relative inspection candidates, while three form a Matrix-C core stable across all 100 tested seeds.
3. The deployed local heuristic connects an observation’s unusualness to specific features and POLIX product families without claiming causal or SHAP attribution.
4. WeightedRoll is excluded from Matrix C and analyzed independently through a saved second-harmonic fit and a declared 13-fit empirical blank-sky reference.
5. The saved case results show that Matrix-C unusualness, raw harmonic magnitude, and simple-harmonic fit adequacy are non-equivalent diagnostics.

## B. FIVE CLAIMS V3 SHOULD AVOID

1. Any confirmed astrophysical anomaly, instrumental fault, polarization detection, calibrated polarization degree, or official sky polarization angle.
2. Any “first,” “novel,” “unique,” “superior,” “breakthrough,” or discovery claim.
3. Any claim that the four-component score is SHAP, causal feature importance, a probability, or an exact decomposition of the Isolation Forest label.
4. Any claim that the empirical blank-sky rule is official background subtraction, a confidence interval, a significance test, or a calibrated detection region.
5. Any claim of predictive accuracy, generalization to future observations, completeness of the public POLIX archive, or Matrix-C superiority.

## C. THREE MOST IMPORTANT POLIX-SPECIFIC CONTRIBUTIONS

1. A 15-feature observation representation tied explicitly to POLIX exposure, energy-resolved azimuth, source-azimuth, delivered-light-curve, and detector-context products.
2. A local evidence ranking that maps statistical unusualness back to those POLIX product families for targeted inspection.
3. A deliberately separate WeightedRoll second-harmonic and empirical blank-sky diagnostic branch that avoids using the same physical proxy both to flag and to confirm a case.

## D. ONE-SENTENCE CENTRAL RESEARCH RESULT

Within the 25-observation project archive, a product-aware unsupervised screen produced four inspection candidates, three of which were selected in all 100 tested seeds, while independent WeightedRoll results showed that statistical unusualness and modulation-like harmonic behavior are non-equivalent diagnostics.

## E. ONE-SENTENCE PRACTICAL VALUE TO A POLIX RESEARCHER

The framework gives a POLIX researcher a repeatable way to prioritize observations, trace each priority to specific Level-2 product summaries, and compare it with an independent harmonic diagnostic before deciding what requires expert review.

## F. WHAT A SKEPTICAL REVIEWER IS MOST LIKELY TO QUESTION

A skeptical reviewer is most likely to ask whether a four-candidate result from 25 unlabeled, retrospectively analyzed observations—and a project-specific explanation heuristic—supports any conclusion beyond archive-specific triage.

## G. WHAT EVIDENCE WE ALREADY HAVE TO ANSWER THAT REVIEWER

The project does not claim detection accuracy or future generalization: it provides exact model replay, 100-seed, contamination, jackknife, and feature-tier analyses; transparent feature and product provenance; a bounded six-case perturbation sanity check; and independent harmonic examples that explicitly constrain the conclusion to traceable, archive-relative screening and non-equivalent diagnostics.
