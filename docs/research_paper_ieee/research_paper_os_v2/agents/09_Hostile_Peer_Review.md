# Agent 9 — Hostile IEEE Peer Review

**Review date:** 2026-07-28  
**Recommended decision:** **WEAK REJECT in its present state**  
**Evidence-contradiction decision:** **No located contradiction invalidates the central archive-screening result.** The fixed saved pipeline reproducibly assigns 21 Normal labels and four archive-relative anomaly-candidate labels to the frozen 25-observation Matrix-C table. The weakness is the limited scientific validation and contribution strength, not a failure to reproduce that result.

## 1. Review scope and standard

This review treats the work as an IEEE conference methodology and applied scientific-computing paper, not as an astrophysical-discovery paper. Draft 1 and the reviewed college report were used only to identify proposed statements. Numerical and methodological judgments follow the frozen matrices, result CSVs, notebooks and code, saved model, supplementary experiment outputs, the POLIX handbook, verified literature, and Agents 1–7.

The paper asks whether heterogeneous POLIX Level-2 products can be compressed into interpretable features, screened without anomaly labels, explained locally, and compared with a scientifically separate blank-sky-referenced harmonic diagnostic. This is a legitimate case-study question. It is not equivalent to showing that the selected observations are scientifically anomalous, that the custom explanations are generally faithful, or that the fitted harmonic quantities are calibrated polarimetry.

## 2. Summary judgment

The project is technically traceable and unusually candid about its boundaries. The fixed candidate output is reproducible, WeightedRoll is excluded from Matrix C, and several retrospective sensitivity checks have been preserved rather than hidden. The representative cases do support a bounded statement that multivariate feature unusualness and raw second-harmonic behavior answer different questions within this archive.

Nevertheless, a skeptical reviewer can reject the paper on contribution and evaluation grounds:

1. the primary analysis uses only 25 observations, with no anomaly ground truth and no independent evaluation archive;
2. the same observations define scaling, PCA, KMeans, Isolation Forest structure, explanation rankings, and retrospective evaluation;
3. contamination 0.16 imposes approximately four candidates rather than estimating a scientifically meaningful rate;
4. exact candidate membership is sensitive to feature tier and random seed near the threshold;
5. the proposed XAI method is an unbenchmarked, correlated, within-observation scoring heuristic rather than a validated attribution method;
6. several feature names have stronger physical connotations than their verified channel-space or delivered-array computations justify;
7. the harmonic branch uses source-plus-background WeightedRoll products and a small selected empirical reference, without official background subtraction, response calibration, or sky-angle conversion; and
8. the integrated framework is a useful implementation, but the literature audit establishes only a limited gap, not methodological novelty or superiority.

These issues do not require invalidating or reworking the completed project. They require a narrower paper: an evidence-first archive case study and reproducible screening framework, not a generally validated anomaly detector, XAI method, or polarimetry procedure.

## 3. Major concerns

### M1 — No ground truth and no independent test set

There are no trusted observation-level anomaly labels. Consequently, the paper cannot estimate accuracy, precision, recall, false-positive rate, scientific utility, or superiority. It can report only archive-relative rankings and candidate flags.

All 25 rows participate in fitting the scaler and the unsupervised structure. PCA, KMeans, Isolation Forest, feature explanations, and most sensitivity summaries are evaluated retrospectively on the same archive. Exact replay establishes software reproducibility, not predictive performance. The leave-one-out summaries mainly assess how the ranking of the 24 retained training rows changes when another row is omitted; they are not a conventional independent validation. Sco X-1 is not flagged in its one held-out refit.

**Required manuscript action:** call the work a same-archive retrospective screening case study. Do not use “validation,” “prediction performance,” or “generalization” for the 25-row results.

### M2 — Sample size is structurally limiting

Matrix C has 15 features for 25 rows. Two-dimensional PCA explains 61.2486% of standardized variance, leaving substantial variation outside the displayed plane. KMeans selects \(k=5\) on the same data and produces cluster sizes 1, 9, 10, 1, and 4. Two singleton clusters give Sco X-1 and Blank Sky-13 exactly zero assigned-centroid distance. This makes the clustering component difficult to interpret as evidence of local normality or anomaly.

The rows are not documented as independent random draws from a population, and the archive includes repeated target classes. Nominal rank-correlation \(p\)-values therefore do not rescue the small sample. Their inferential interpretation would be misleading.

**Required manuscript action:** retain exact descriptive correlations if useful, omit their \(p\)-values from headline claims, and disclose the singleton clusters prominently.

### M3 — Contamination determines the candidate count

Isolation Forest contamination is fixed at 0.16. With \(n=25\), this setting yields approximately four candidates. The value is not learned from labels, an expected instrumental failure rate, or an astrophysical prevalence. It is a screening choice.

The contamination sensitivity experiment changes the decision threshold over the same score ordering. Persistence at 0.12–0.24 is therefore not four independent replications. The paper must not imply that the experiment validates 0.16 or estimates a true anomaly fraction.

**Required manuscript action:** report the fixed four as the output under the declared screening assumption and describe contamination sensitivity as threshold persistence only.

### M4 — “Stable core” is narrower than it sounds

Blank Sky-13, Sco X-1, and Her X-1 are flagged in 100/100 tested Matrix-C Isolation Forest seeds and in all included-observation jackknife fits. However:

- Blank Sky-5, the fourth fixed candidate, is flagged in only 29/100 seeds;
- Blank Sky-15, which is Normal in the fixed model, is flagged in 68/100 seeds;
- only Blank Sky-13 and Sco X-1 persist across Matrices A, B, and C;
- Her X-1 is specific to Matrix C; and
- Sco X-1 is not flagged in its held-out jackknife fit.

The phrase “robust core” would overstate the evidence. Even “stable core” must carry Matrix-C and tested-procedure qualifications.

**Required manuscript action:** use exactly “three-candidate Matrix-C core stable under the tested procedures” and separately report feature-tier and held-out caveats.

### M5 — Feature validity is engineering traceability, not physical validation

The 15 features are reproducibly computed, but several scientific labels remain proxies:

- channel summaries are not calibrated energies or spectra;
- the channel-4000 split is a high-channel fraction, not a verified high-energy band;
- source-roll “smoothness” omits the circular closing difference and angle sorting, so it is an order-dependent roughness proxy;
- light-curve ratios summarize delivered `RATE` arrays without demonstrated GTI, quality, fractional-exposure, background, error, or binning controls;
- detector summaries do not establish calibrated detector efficiency, gain offsets, or hardware health; and
- no feature-level measurement uncertainty enters the ML pipeline.

This is not data leakage in the conventional supervised sense, because no outcome label enters the features. It is, however, a semantic-validity and deployment-contract problem. The current Flask extractor can accept incomplete detector products and is not proven to reproduce all frozen Notebook-08 Matrix-C rows.

**Required manuscript action:** describe channel-space, exposure-pattern, stored-roll-profile, delivered-light-curve, and cross-detector summaries exactly. Limit the end-to-end claim to a proof-of-concept interface unless extractor-to-matrix equivalence is later established.

### M6 — The XAI score is a heuristic ranking, not exact attribution

The deployed label is supplied solely by `IsolationForest.predict`. The four-component explanation score combines:

1. a PC1/PC2 loading-weighted separation term;
2. assigned-centroid squared distance;
3. positive single-feature Isolation Forest occlusion sensitivity; and
4. absolute standardized abnormality.

These terms are max-normalized within each observation and summed with equal weights. Their original scales, uncertainty, redundancy, and reliability are not calibrated. PCA and absolute standardized value are mathematically related; KMeans often reflects the same standardized extremeness; negative Isolation Forest occlusion effects are clipped. The components are not independent confirmations, and the combined score does not decompose the anomaly label.

Scores are ordinal within an observation only. They are not comparable across observations, and a score of 3 is not three times a score of 1. Product-family mapping is a deterministic prefix lookup, not a learned product attribution. The accepted Sco X-1 order is peak channel, weighted mean channel, and entropy; all three remain channel-space distribution summaries, not physical causes.

**Required manuscript action:** use “project-specific, model-informed local feature-ranking heuristic.” Avoid “model-specific attribution,” “decision explanation,” “driver,” causal language, and SHAP-like guarantees.

### M7 — The faithfulness evidence is method-aligned and underpowered

The six-case experiment neutralizes the top three features simultaneously by setting their standardized values to zero. “Strong” means that PCA radial distance and Isolation Forest score both decrease; “Moderate” means that one decreases. KMeans is computed but ignored in the overall verdict. There is no minimum effect size, uncertainty interval, random-feature comparator, bottom-feature comparator, alternate replacement baseline, or test of explanation-rank stability.

Five Strong and one Moderate are reproducible project-defined outcomes. They do not prove explanation correctness. The evaluation reuses PCA and Isolation Forest measures that are already components of the explainer, making it a method-aligned sanity check rather than independent validation. Two of the six cases are not fixed deployed candidates.

**Required manuscript action:** report the six cases as a separate exploratory, in-sample perturbation sanity check. This is supporting evidence, not a standalone faithfulness contribution.

### M8 — Physical branch is descriptive and background-limited

The POLIX handbook states that WeightedRoll contains source and background modulation contributions. The fitted \(C,Q,U\) are mathematical second-harmonic coefficients, not verified calibrated sky Stokes parameters. \(A/C\) is raw modulation, not polarization degree; the half-angle phase is not official sky position angle.

The empirical baseline uses 13 of 15 project-labelled blank-sky fits selected by a project-defined reduced-\(\chi^2\leq2\) rule. The mean and sample scatter are a description of this selected archive subset, not an official background model or detection region. The standardized fractional-harmonic distance ignores \(q/u\) covariance, per-observation fit uncertainty, uncertainty in the estimated baseline, observing-condition matching, and selection sensitivity. Its cutoffs are not sigma levels.

Her X-1 illustrates the danger: it has a larger empirical vector displacement, but its simple harmonic fit is very poor. That result cannot confirm a physical modulation effect. All ten source raw-modulation values lie within the declared scalar blank-sky range, but this does not prove that they are unpolarized.

**Required manuscript action:** keep the branch as a separate archive diagnostic supporting non-equivalence. Remove calibrated Stokes, background-subtraction, detection-significance, PD, and PA implications.

### M9 — Notebook/service uncertainty mismatch

Notebook 11 and the current Flask service propagate \(A/C\) uncertainty differently. The notebook result CSV must control reported project uncertainty values. Claiming one identical end-to-end numerical implementation would be false.

**Required manuscript action:** disclose the mismatch, report notebook/CSV provenance, avoid unnecessary uncertainty columns in the main table, and move the formula comparison to supplementary material. Do not silently select whichever uncertainty is more favorable.

### M10 — Contribution and novelty remain modest

StandardScaler, PCA, KMeans, Isolation Forest, harmonic fitting, and Flask are established components. The product-aware feature table and separated diagnostic branches are useful engineering decisions, but no comparative benchmark demonstrates that the integrated system performs better than a simpler ranking, a single detector, an alternative feature set, or a published explainer.

The literature audit supports only: “limited published work was identified on the integrated combination studied here.” It does not establish “first,” “novel,” “unique,” “superior,” or priority. Matrix C is engineered early feature integration, not a learned multi-view method.

**Required manuscript action:** frame one primary applied contribution—traceable archive-relative screening of heterogeneous POLIX Level-2 products—and at most three secondary design contributions. Present sensitivity tests and the Flask interface as support.

### M11 — Reproducibility is partial

The frozen model and result files are well identified, but full reproduction remains fragile:

- the model pickle embeds scikit-learn 1.9.0 while the system environment differs;
- `requirements.txt` is unpinned;
- notebooks and research evidence are outside the application’s one-commit Git repository;
- the organized output folder omits some controlling root-level files;
- official archive URLs, acquisition date, release notice, and source checksums are incomplete;
- upload-time extractor equivalence with the frozen Matrix-C CSV has not been demonstrated; and
- observation friendly-name provenance includes two IDs mapped to “Blank Sky-2.”

**Required manuscript action:** use hashes and absolute provenance paths in the reproducibility supplement, specify the known compatible environment, use observation IDs as primary keys, and avoid claiming a fully portable or raw-data-to-result reproducibility package.

### M12 — AI-assisted writing creates a governance risk, not scientific evidence

AI assistance is not itself a reason for rejection. The risk arises if generated prose smooths over unresolved evidence boundaries, creates unsupported citations, or produces language the authors cannot defend. The manuscript must not cite an AI system as scientific evidence or imply that deterministic application sentences were generated by a large language model.

**Required manuscript action:** follow the selected venue’s disclosure policy, identify the assisted tasks, manually verify every reference and numerical statement, and require all authors to revise and defend the final prose. Automated “humanizer” rewriting would increase rather than reduce scientific risk.

## 4. Fatal concerns under broader claim framings

No fatal numerical contradiction was located. The following become fatal if the manuscript retains the corresponding broad claim:

| Broad claim | Why it would be fatal | Non-experimental remedy |
|---|---|---|
| The four cases are validated or confirmed anomalies | No anomaly ground truth or expert adjudication exists | Call them fixed archive-relative candidates |
| The method generalizes to future POLIX observations | No external or prospective release was evaluated | Remove the claim and state future validation is required |
| The custom XAI method is generally faithful or superior | Six in-sample, method-aligned cases have no comparator | Reframe as a project-specific heuristic with a limited sanity check |
| Matrix C is optimal or superior | Existing A/B/C results show feature-tier sensitivity and no benchmark | Call it the frozen deployed representation |
| The physical branch detects polarization | WeightedRoll is source-plus-background and official calibration is absent | Retain only raw harmonic diagnostics |
| The blank-sky reference is official subtraction or a calibrated significance region | It is a selected 13-fit empirical summary with a diagonal distance | Use archive-specific descriptive language |
| The integrated framework is the first or novel | The literature audit is finite and does not establish priority | Use the limited-gap statement |
| The current Flask service exactly reproduces the notebook uncertainty pipeline | The two \(A/C\) uncertainty formulas differ | Disclose versioned implementations and notebook provenance |

If these claims are removed, the remaining applied archive-screening story is internally coherent.

## 5. Fixable writing and presentation concerns

1. Replace the Draft-1 working title with the exact required project title.
2. Reduce the contribution list from five co-equal items to one primary and at most three secondary contributions.
3. Replace unqualified “model-specific attribution” with the accepted heuristic-ranking terminology.
4. Replace “faithfulness evaluation” in headline positions with “six-case feature-neutralization sanity check,” unless the exact project-defined criteria immediately follow.
5. Separate fixed four, seed-stable three, cross-tier two, and exploratory six in both prose and tables.
6. State that contamination sensitivity varies the threshold over one ordering.
7. State that included-observation jackknife frequency is not held-out validation.
8. Remove inferential wording around Spearman \(p\)-values; report rank correlations descriptively if space permits.
9. Do not interpret zero KMeans distance as ordinariness; explain the two singleton clusters.
10. Replace calibrated-energy, circular-smoothness, intrinsic-variability, and detector-health wording with exact proxy definitions.
11. Use observation IDs in result tables and project labels only as secondary readable annotations.
12. Replace unqualified \(Q/U\) or “Stokes space” with harmonic coefficients or fractional harmonic coordinates.
13. Compress uncertainty values from the main harmonic table unless they are essential to an explicit argument.
14. Keep PD sensitivity scenarios out of the main paper and preferably out of the submission unless the guide requests them.
15. Use “within the empirical blank-sky scalar range under the declared rule,” not “consistent with zero polarization.”
16. Avoid saying that branch separation “confirms” non-equivalence. It prevents direct feature leakage and permits a descriptive comparison.
17. Limit representative cases to observations that make one clear methodological point each.
18. Avoid excessive audit prose in the main paper; put complete formulas, 25-row results, robustness tables, and implementation discrepancies in supplementary material.
19. Recheck every citation number after reconstruction; Draft 1 contains references that Agent 7 classifies as context-only.
20. Make the final abstract state the sample size, archive-relative scope, independent branch, principal bounded finding, and absence of calibrated PD/PA.

## 6. Domain-review concerns

The following require guide or POLIX-aware review before submission but do not invalidate the central archive-screening computation:

1. exact product names, axes, columns, units, and release-specific semantics;
2. archive provenance and the project’s 10-source/15-blank-sky role mapping;
3. duplicated “Blank Sky-2” friendly label and missing “Blank Sky-12” label;
4. whether every Matrix-C feature is defensible as an archive-screening proxy;
5. channel-4000 terminology and comparability of channel distributions;
6. light-curve and detector-product suitability for the implemented summaries;
7. preferred notation for harmonic coefficients and fractional coordinates;
8. scientific adequacy of inverse-variance second-harmonic fitting for these products;
9. the project-defined reduced-chi-square categories;
10. the 13-fit blank-sky selection and mean/standard-deviation summary;
11. whether fitted phase and PD sensitivity proxies should be omitted entirely;
12. selection and wording of Sco X-1, Her X-1, Crab P01_0005, and blank-sky examples; and
13. current official XPoSat/POLIX acknowledgment and identification wording.

## 7. Disclosure-only limitations

These limitations can be disclosed; they do not by themselves demand rework of the completed project:

- \(n=25\) and 15 features;
- no anomaly labels;
- retrospective use of the same archive for fitting and description;
- contamination-defined candidate count;
- archive-specific scaling and future-data drift risk;
- feature-tier dependence;
- singleton KMeans clusters;
- seed-sensitive threshold neighborhood;
- no feature-uncertainty propagation;
- project-specific XAI normalization and weighting;
- six exploratory perturbation cases;
- no future-release validation;
- source-plus-background WeightedRoll;
- project-defined fit-quality categories;
- 13-fit empirical reference;
- no official background subtraction, \(\mu_{100}\), calibrated PD, or official PA;
- unpinned original environment;
- partial Git coverage;
- notebook/service uncertainty mismatch; and
- no recorded POLIX domain-expert adjudication of candidates.

Disclosure is sufficient only if the conclusions remain correspondingly narrow.

## 8. Claims that would cause rejection

The following statements should trigger rejection because they contradict or exceed the verified evidence:

- “all publicly available POLIX observations were analyzed”;
- “four confirmed anomalies were detected”;
- “the contamination value reflects a 16% anomaly prevalence”;
- “the three candidates are robust” without Matrix-C and tested-procedure qualification;
- “leave-one-out validation proves generalization”;
- “Matrix C outperforms or is superior to A and B”;
- “KMeans independently confirms the anomaly”;
- “the rank correlations statistically validate the models”;
- “the four XAI components are four models or independent explanations”;
- “the explanation score exactly attributes the Isolation Forest decision”;
- “the method is SHAP, SHAP-like, or superior to SHAP/LIME”;
- “Strong faithfulness validates scientific or causal correctness”;
- “the leading features identify an astrophysical or instrumental cause”;
- “channel 4000 is a calibrated energy threshold”;
- “the light-curve features measure intrinsic source variability”;
- “WeightedRoll is a background-subtracted source modulation curve”;
- “\(Q/U\) are calibrated source Stokes parameters”;
- “raw modulation is polarization degree”;
- “fitted phase is sky polarization angle”;
- “the empirical blank-sky distance is a sigma significance or detection threshold”;
- “the harmonic branch confirms or falsifies polarization”;
- “the current notebook and service uncertainty calculations are identical”;
- “this is the first, novel, unique, superior, or breakthrough framework”; or
- any astrophysical discovery claim.

## 9. Experiments actually required

### 9.1 Required for the bounded applied case-study submission

**No new computational experiment is strictly required** if the manuscript is explicitly limited to:

- the frozen 25-observation archive;
- reproducibility of the fixed saved output;
- procedure-qualified retrospective sensitivity;
- a project-specific local ranking with a limited in-sample sanity check; and
- a descriptive, uncalibrated harmonic comparison.

For this narrow submission, the essential remaining work is audit and review rather than experimentation: domain validation of terminology, citation verification, provenance disclosure, manuscript reconstruction, and author verification.

### 9.2 Required if broader claims are retained

The following become essential submission experiments only if the paper claims a generally validated method:

1. **Independent future-release or prospective evaluation** for any generalization claim.
2. **Expert adjudication or a defensible proxy benchmark** for any accuracy, relevance, or candidate-validity claim.
3. **Matched random/bottom-feature perturbation baselines and explanation-rank stability** for a standalone faithfulness or XAI-quality contribution.
4. **Grouped target-level validation** for claims of transfer across sources rather than rows.
5. **KMeans stability and \(k\)-sensitivity analysis** for a substantive clustering contribution.
6. **Matched-background, covariance-aware, selection-sensitive physical analysis** for any detection-region or source-background inference.
7. **Official response/background/coordinate calibration** for any PD, PA, Stokes, or polarization-detection claim.

The frozen-workflow rule prohibits these experiments. Therefore the manuscript must remove the corresponding broader claims rather than implying that the tests were performed.

## 10. Experiments that are unnecessary

The following are not required for the bounded paper and should not be added merely to strengthen appearance:

- retraining the frozen model;
- selecting a different contamination value after seeing the results;
- creating a new feature matrix or redefining Matrix C;
- adding Chandra or XSPECT data;
- adding a supervised classifier without labels;
- implementing SHAP or LIME simply because they appeared in the initial proposal;
- expanding the Isolation Forest seed count beyond the existing 100 runs;
- multiplying contamination values over the same fixed ordering;
- searching more models without a prespecified benchmark;
- calculating additional \(p\)-values for the same 25 rows;
- generating calibrated PD/PA without official calibration;
- forcing background subtraction from the 13-fit empirical reference;
- producing AI-generated scientific plots; or
- rewriting prose with automated “humanizer” tools.

## 11. Minor concerns

1. Define XPoSat, POLIX, PCA, XAI, PD, PA, and WR at first use where retained.
2. Use “KMeans” consistently with the cited software/method convention.
3. Report no more decimal places than the controlling CSV supports or the comparison needs.
4. Distinguish the Isolation Forest anomaly score from the combined XAI score.
5. State whether larger Isolation Forest scores mean greater isolation under the project’s sign convention.
6. Identify population versus sample standard deviations where relevant.
7. State that the fitted harmonic phase is modulo \(180^\circ\).
8. Avoid “acceptable fit” without “under the project-defined reduced-chi-square rule.”
9. Do not use visual confidence ellipses or “sigma” contours for the diagonal blank-sky distance.
10. Keep the complete 15-feature formulas and full 25-row harmonic table in supplementary material.
11. Use the exact current Sco X-1 rank and mark the entropy-first account as superseded provenance only.
12. Preserve the distinction between Notebook-08 frozen Matrix C and upload-time feature extraction.
13. Verify that every retained BibTeX entry is cited and every citation supports the adjacent sentence.
14. Do not let the title’s broad wording imply official XPoSat analysis or calibrated polarimetry.
15. Avoid treating the Flask interface as production deployment.

## 12. Decision rationale

### Current decision: WEAK REJECT

The paper is not rejected because its fixed result is irreproducible; the opposite is true. It is weakly rejected because a standard methodology-paper reading would expect stronger evidence that the proposed representation and explanation method generalize or improve analysis. The current evidence instead supports a small, same-archive, unlabeled case study with several proxy features, an unbenchmarked local ranking, and an uncalibrated physical diagnostic.

The decision can plausibly move to **Weak Accept** at an appropriate applied or student research venue without new experiments if the final manuscript:

- makes the archive-bounded scope explicit in the abstract and conclusion;
- presents one restrained integration contribution rather than algorithmic novelty;
- uses the mandatory terminology corrections;
- separates the fixed four, tested-procedure three, cross-tier two, and exploratory six;
- demotes the XAI test to a limited sanity check;
- treats the physical branch as source-plus-background harmonic diagnostics only;
- discloses all material implementation and reproducibility limitations;
- passes POLIX-aware domain review; and
- is manually verified and revised by all authors.

For a venue demanding a new general anomaly-detection or explainability method, the recommendation remains **Reject** unless external and comparative validation is added. Those experiments are outside the accepted completed-project workflow and should be listed as future work rather than silently approximated.

## 13. Final answers to the orchestrator

| Question | Agent 9 answer |
|---|---|
| Are there fatal concerns? | No fatal evidence contradiction for the bounded archive-screening result. Broad anomaly-validation, general-XAI, calibrated-polarimetry, or novelty claims would be fatal. |
| Are the fixed results reproducible? | Yes: 21 Normal and four fixed candidates are exactly replayed from the saved Matrix-C artifact and model. |
| Is the three-candidate result defensible? | Yes, only as a “three-candidate Matrix-C core stable under the tested procedures.” |
| Is the XAI contribution defensible? | Moderate as a project-specific case-study ranking; weak as a generally validated attribution method. |
| Is the physical branch defensible? | Yes as an independent descriptive archive diagnostic; no as calibrated polarimetry or official background treatment. |
| Is a new experiment mandatory? | No for a narrowly framed applied case study. Yes conditionally for any generalization, accuracy, standalone-XAI, or calibrated-physical claim. |
| Does any located contradiction invalidate the central result? | **No.** The remaining conflicts constrain terminology, interpretation, uncertainty provenance, and reproducibility claims. |
| Overall recommendation | **WEAK REJECT**, potentially **Weak Accept** after evidence-bounded reconstruction and guide/domain review. |
