# Agent 5 — Explainable-AI Method Audit

**Audit date:** 2026-07-28  
**Scope:** Research Paper OS V2, Phase 4B  
**Method:** read-only inspection of the frozen deployment source, saved model metadata, Notebook 10 source, existing XAI tables, the accepted version-mismatch audit, and the existing six-case neutralization results. No model was refitted, no prediction or explanation was regenerated, and no new experiment was run.

## 1. Executive verdict

The deployed explanation layer is a **deterministic, project-specific, model-informed local feature-ranking heuristic**. It ranks the 15 Matrix-C features for one observation by adding four within-observation normalized terms:

1. a two-component principal component analysis (PCA) separation term;
2. a KMeans assigned-centroid distance term;
3. a positive Isolation Forest single-feature occlusion term; and
4. an absolute standardized-value term.

The method is useful for answering a restrained question:

> Which Matrix-C features provide the largest combined local evidence under the project's chosen PCA, KMeans, Isolation Forest, and standardized-abnormality views?

It does **not** provide a formally additive attribution of the deployed anomaly label. In `model_service.py`, the `Anomaly`/`Normal` prediction is produced solely by `IsolationForest.predict`; PCA and KMeans do not vote on that label. Therefore, the combined score should not be described without qualification as identifying the features that “caused,” “determined,” or uniquely “drove” the classifier's decision.

The phrase **feature attribution** is defensible only when qualified as a *project-specific heuristic attribution of composite anomaly evidence*. The safer paper term is **local feature-importance ranking** or **four-component explanation score**. “Model-specific feature attribution method” is too strong unless the text immediately explains that the combined score is not an exact decomposition of one model output and has no Shapley, completeness, causal, or probabilistic guarantee.

The existing neutralization analysis is a useful **in-sample perturbation sanity check**. For the six exploratory cases, simultaneously replacing the three highest-ranked standardized features with zero reduced both the two-dimensional PCA distance and the Isolation Forest anomaly score in five cases; it reduced only the PCA distance in one case. This reproduces the project-defined count of five `Strong`, one `Moderate`, and zero `Weak`. These labels are internal verdict categories, not statistical significance levels or literature-standard grades.

The six cases are sufficient to demonstrate that the authors attempted a local functional check. They are not sufficient to establish general faithfulness, scientific correctness, explanation stability, or future-data validity. Faithfulness should remain a secondary proof-of-concept evaluation rather than an independently validated principal contribution.

## 2. Controlling evidence

| Evidence | Audit use | Status |
|---|---|---|
| `D:\polix_xai_webapp\model_service.py` | Exact deployed functions `product_family`, `normalize_score`, `PolixXAIPredictor.explain_one`, and `make_explanation_sentence` | Primary implementation evidence |
| `D:\polix_xai_webapp\model\polix_v2_matrixC_unsupervised_xai_model.pkl` | Frozen feature order and fitted estimator metadata | Primary model evidence |
| `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\01_notebooks\10_Unsupervised_XAI_Model_Explanations.ipynb` | Offline XAI construction and neutralization-verdict definitions | Primary analysis-code evidence |
| `...\03_ml_xai_results\v2_final_primary_unsupervised_xai_explanations.csv` | Six exploratory Matrix-C explanation summaries | Primary result table |
| `...\03_ml_xai_results\v2_unsupervised_xai_faithfulness_test.csv` | Exact before/after perturbation measurements | Primary result table |
| `...\03_ml_xai_results\v2_unsupervised_xai_faithfulness_verdict.csv` | Project-defined `Strong`/`Moderate` verdicts | Primary result table |
| `research_paper_ieee\supplementary_experiments\faithfulness_reproduction.csv` and `faithfulness_verdict_reproduction.csv` | Existing exact numerical reproduction of the six-case files | Verified supplementary evidence |
| `research_paper_ieee\XAI_Version_Mismatch_Audit.md` and `...\deployed_xai_exact_from_model_service.csv` | Accepted current Sco X-1 ordering and version identifiers | Controlling version audit |

The accepted version identifiers are:

- Git commit: `15628ee7cc434de9ba03caaae5dd115d8cd09f9a`;
- `model_service.py` SHA-256: `f749ffd0e79a951f42555f5083d2056567de9ccaaf721772601ea0a79856c877`;
- saved model SHA-256: `d8efd73c9744ed1ca1098a4599da91acdedc250bb2b6639728364aef6b8c180d`;
- frozen Matrix-C SHA-256: `3936e1b0aaf44acff39597befec1b466a26511123655946f8829a4e6263db0fa`.

Read-only model-metadata inspection found:

- 15 ordered input features;
- PCA with `n_components=2` and explained-variance ratios 0.387435 and 0.225051;
- KMeans with \(k=5\), `random_state=42`, and cluster sizes 1, 9, 10, 1, and 4;
- Isolation Forest with 100 trees, `contamination=0.16`, and `random_state=42`.

## 3. What the deployed score computes

Let \(x_j\) be the standardized value of feature \(j\), fitted on the 25-observation archive. Let \(v_{1j}\) and \(v_{2j}\) be the first two PCA loading coefficients, \(r_1\) and \(r_2\) their explained-variance ratios, \(c_{gj}\) the assigned KMeans centroid coordinate, and

\[
a(x)=-\operatorname{IsolationForest.score\_samples}(x)
\]

so that a larger value is treated as more anomalous.

For feature \(j\), the deployed function computes:

\[
P_j=|x_jv_{1j}|r_1+|x_jv_{2j}|r_2,
\]

\[
K_j=(x_j-c_{gj})^2,
\]

\[
I_j=a(x)-a(x^{(j\leftarrow0)}),
\]

and

\[
Z_j=|x_j|.
\]

The normalization function is applied separately to each 15-feature component vector:

\[
N(s)_j=
\begin{cases}
|s_j|/\max_k|s_k|,&\max_k|s_k|>0\text{ and finite},\\
0,&\text{otherwise}.
\end{cases}
\]

The final score is:

\[
S_j=N(P)_j+N(K)_j+N(\max(I,0))_j+N(Z)_j.
\]

The function sorts \(S_j\) in descending order and returns the top five features.

### Consequences of this definition

1. **The score is a rank-oriented composite, not a probability.** With finite inputs its nominal range is 0–4, but it has no calibrated interpretation.
2. **Normalization is local to one observation and one component.** A score of 3 for one observation is not commensurate with a score of 3 for another.
3. **Equal component weighting is an implementation choice.** The four normalized vectors are added with weight 1; no empirical or theoretical weighting study is present.
4. **Magnitude information is discarded across components.** Any nonzero component assigns its within-vector maximum a normalized value of 1, whether its raw effect is large or very small.
5. **A zero component silently disappears.** This occurs for KMeans when an observation is its cluster's sole member and therefore equals its fitted centroid.
6. **The score explains a composite evidence construction.** It is not an exact decomposition of `IsolationForest.predict`, which alone sets the deployed label.

## 4. Component-level review

### 4.1 PCA separation contribution

**What it measures:** the absolute magnitude of each feature's term in PC1 and PC2, with each term multiplied by that component's explained-variance ratio.

**What is reasonable:** it identifies features with large standardized values and large loadings in the two displayed PCA directions. The saved PCA contains exactly these two components, together explaining approximately 61.25% of archive variance.

**Limitations:**

- \(P_j\) is not an additive decomposition of radial distance in the PC1–PC2 plane.
- Taking absolute values removes whether a feature increases or cancels another feature's signed PC coordinate.
- Multiplying each feature term by the explained-variance ratio is a project choice, not the standard unique definition of “PCA contribution.”
- Variation outside PC1 and PC2 is absent by design.
- Because PCA was fitted on the same 25 observations being explained, these are in-sample geometric descriptions, not held-out explanation evidence.

**Safe name:** “PC1/PC2 loading-weighted separation term.”

**Unsafe name:** “the feature's exact contribution to PCA distance” or “the causal contribution to anomaly status.”

### 4.2 KMeans centroid-distance contribution

**What it measures:** feature \(j\)'s exact additive term in the squared Euclidean distance from the observation to its assigned centroid.

**What is reasonable:** unlike the PCA term, the \(K_j\) values exactly sum to the squared distance from the fixed assigned centroid.

**Limitations:**

- The contribution is relative to the assigned cluster only.
- It does not measure distance to the second-nearest cluster or uncertainty in cluster assignment.
- The training set has two singleton clusters. Sco X-1 and C24_0018 each equal their own fitted centroids, so every KMeans contribution is zero for those observations.
- Because normalization returns an all-zero vector in those cases, their combined score effectively has three active components, while other observations may have four. Cross-observation score comparisons are therefore especially unsafe.
- In the faithfulness test, distance after neutralization is measured to the **original** cluster rather than after reassignment.

**Safe name:** “assigned-centroid squared-distance term.”

**Unsafe claim:** that a large term establishes a scientifically meaningful cluster distinction.

### 4.3 Isolation Forest occlusion contribution

**What it measures:** the change in the negated `score_samples` value after replacing one standardized feature with zero, the archive mean for that feature. A positive \(I_j\) means this intervention lowers the anomaly score. Negative values are retained in the returned diagnostic row but clipped to zero before combination.

**What is reasonable:** this is a direct local sensitivity test of the exact fitted Isolation Forest score under a stated intervention. Because `decision_function` differs from `score_samples` by an observation-independent offset, score differences are meaningful for this fitted estimator.

**Limitations:**

- Zero is a marginal mean, not necessarily a physically valid or jointly plausible conditional value.
- One-feature replacement can create an off-distribution combination when features are correlated.
- Isolation Forest is nonlinear; individual occlusion deltas do not sum to the total score and do not allocate interactions.
- Clipping negative deltas discards features whose neutralization makes the observation more anomalous.
- There is no completeness, efficiency, local-accuracy, or consistency guarantee.
- The direction and magnitude can depend on the baseline, fitted forest seed, contamination setting, and correlated feature representation.

**Safe name:** “positive single-feature Isolation Forest occlusion sensitivity.”

**Unsafe name:** “Isolation Forest SHAP value” or “the feature's share of the Isolation Forest prediction.”

### 4.4 Absolute standardized-value contribution

**What it measures:** absolute distance in standard-deviation units from the archive mean, as represented by the fitted `StandardScaler`.

**What is reasonable:** it is an interpretable, model-independent indicator of marginal archive-relative unusualness.

**Limitations:**

- It is not a model attribution.
- The fitted archive includes the observation being explained.
- A large marginal z-score need not influence the Isolation Forest decision strongly.
- It ignores feature dependence and distribution shape.

**Safe name:** “absolute standardized abnormality term.”

**Unsafe name:** “fourth model” or “classifier contribution.”

## 5. Component normalization and combined-score validity

The normalization code is internally deterministic and includes an all-zero/nonfinite-maximum guard. It does not, however, make component values scientifically equivalent. The equal-weight sum treats “largest PCA term,” “largest centroid-distance term,” “largest positive occlusion,” and “largest absolute z-score” as equally important within each observation, regardless of their original units, raw magnitudes, reliability, or redundancy.

PCA and absolute-z components are mathematically related because both grow with \(|x_j|\). KMeans distance also often grows with archive-relative extremeness. The sum can therefore reward the same marginal departure several times. This is not an implementation error, but it means “four independent sources of evidence” would be inaccurate. “Four complementary components” is acceptable only with acknowledgment that they are correlated views of the same standardized row.

The score is best treated as an **ordinal prioritization device within one observation**. It should not be averaged across observations, assigned thresholds, interpreted as an effect size, or used to claim that a feature with score 3.0 is three times as important as a feature with score 1.0.

## 6. Top-feature ordering and accepted Sco X-1 result

The deployed implementation sorts the combined score descending and returns the first five rows. Python's stable sort preserves model feature order for exact ties; there is no explicit scientific tie-breaking rule.

For the frozen current implementation, model, and Matrix-C row, the accepted Sco X-1 top three are:

1. `t1A_energy_peak_channel` — 2.454499;
2. `t1A_energy_weighted_mean_channel` — 2.207369;
3. `t1A_energy_channel_entropy` — 1.813968.

All three map to `Tier1A EnergyRes`. Their scientifically safe interpretation is limited to unusual channel-distribution summaries relative to this 25-observation archive. The peak and weighted-mean values are channel-space quantities, not calibrated energies; entropy is a binning-dependent distribution summary, not a physical disorder measure.

The historical entropy-first narrative is superseded by the accepted exact versioned-function audit. No located versioned artifact reproduces it. This discrepancy is a provenance warning about historical output, not evidence against the current ranking.

The current exact ranking is reproducible for the frozen artifacts. **Explanation-rank stability under model seeds, contamination values, jackknife samples, alternate normalizations, or future observations has not been tested.** Candidate-label stability does not establish feature-ranking stability.

## 7. Product-family mapping

`product_family(feature)` is a deterministic prefix lookup. It is not inferred by a model and is not an additional attribution method.

| Prefix | Returned label |
|---|---|
| `t1A_exp` | Tier1A Exposure |
| `t1A_energy` | Tier1A EnergyRes |
| `t1B_src` | Tier1B Source Azimuth |
| `t2_lc` | Tier2 Light Curve |
| `t2_det` | Tier2 Detector Balance |
| `t2_pha` | Tier2 Spectrum |
| `t3_wr` | Tier3 WeightedRoll |

The Matrix-C detector-PHA centroid-spread feature begins `t2_det_pha` and is therefore mapped to `Tier2 Detector Balance`, not `Tier2 Spectrum`. That label is consistent with its cross-detector construction but should be described as an engineering taxonomy. The mapping does not prove that a product family physically caused an unusual observation.

Product-level explanation is supportable in the limited sense that feature labels are grouped by their source-product family. It is not a separate learned product attribution, and no family-level aggregation uncertainty or statistical significance is computed.

## 8. Deterministic explanation sentence

`make_explanation_sentence` is a fixed Python template. It uses:

- prediction label;
- anomaly score;
- the top three feature names;
- prefix-mapped product-family labels;
- z-score signs and values; and
- combined XAI scores.

No large language model is used to generate the sentence.

The sentence is reproducible, but two phrases require caution:

- “flagged as anomalous mainly because” can be read as a faithful decomposition of the Isolation Forest decision, which the combined score is not;
- “strongest driver” suggests causal or decision-specific influence.

Safer generated prose would say “the highest-ranked feature under the four-component explanation score” and “the next-ranked feature.” For a zero z-score, the present implementation uses the `else` branch and would say “lower than usual”; this is a general edge-case defect, although no material frozen result was identified here from it.

The direction text means only above or below the fitted scaler mean. It does not identify an astrophysical or instrumental cause.

## 9. Six-case feature-neutralization audit

### 9.1 Exact protocol

Notebook 10 refits the same configured StandardScaler, two-component PCA, five-cluster KMeans, and Isolation Forest on Matrix C. For each of six exploratory consensus cases, it:

1. selects the three highest combined-XAI Matrix-C features;
2. simultaneously sets their standardized values to zero;
3. recomputes radial distance in the two-dimensional PCA plane;
4. recomputes Euclidean distance to the original KMeans centroid; and
5. recomputes the negated Isolation Forest `score_samples` value.

The six cases are:

- G01_0006, Sco X-1;
- C24_0018, Blank Sky-13;
- G01_0003, Her X-1;
- C24_0010, Blank Sky-5;
- C24_0020, Blank Sky-15; and
- C24_0023, Blank Sky-6.

Only the first four are anomaly candidates under the frozen deployed Matrix-C Isolation Forest. C24_0020 and C24_0023 belong to the earlier six-case exploratory consensus stage. The sets must not be conflated.

### 9.2 Verdict definitions

The code defines:

- `pca_pass`: PCA distance reduction \(>0\);
- `isolation_pass`: Isolation Forest anomaly-score reduction \(>0\);
- `kmeans_pass`: original-centroid distance reduction \(>0\).

It then assigns:

- **Strong:** both `pca_pass` and `isolation_pass`;
- **Moderate:** either `pca_pass` or `isolation_pass`, but not both;
- **Weak:** neither passes.

`kmeans_pass` is recorded but **does not affect the overall verdict**. There is no minimum effect-size threshold beyond strict positivity, no uncertainty interval, and no statistical test.

### 9.3 Verified result

| Scope | Result |
|---|---|
| Six exploratory cases | 5 Strong, 1 Moderate, 0 Weak |
| Strong meaning | The selected top three jointly reduced both PCA radial distance and Isolation Forest anomaly score under zero neutralization |
| Moderate case | C24_0023: PCA distance reduced; Isolation Forest anomaly score did not reduce |
| KMeans behavior | Two singleton-cluster cases increased distance from their original centroid after neutralization; this did not change their Strong verdict |
| Reproduction status | Existing supplementary reproduction matches every stored verdict |

### 9.4 What the test supports

The result supports this restrained statement:

> Under the project's zero-neutralization intervention, the three highest-ranked Matrix-C features collectively tracked reductions in two selected anomaly-evidence measures for five of six exploratory cases and one measure for the remaining case.

It demonstrates local functional concordance for these rows, this fitted archive, this top-three intervention, and these metrics.

### 9.5 What the test does not support

It does not establish:

- that each of the three features is individually necessary or sufficient;
- that their internal rank order is correct;
- that the intervention is physically realizable;
- that the same result holds for bottom-ranked or randomly selected feature sets;
- that the result exceeds a chance or matched-baseline expectation;
- that the explanation remains stable across seeds, contamination values, resampled archives, or future data;
- that KMeans behavior is faithfully summarized by the overall verdict;
- that the neutralized sample changes its deployed anomaly label;
- that explanations correspond to anomaly ground truth;
- that the features identify an astrophysical or instrumental cause;
- that the method is more faithful than SHAP or another explainer;
- that the score has a formal faithfulness guarantee.

The test is partly **method-aligned** rather than independent: the combined score already includes PCA and positive Isolation Forest terms, and the evaluation then asks whether the selected features reduce PCA and Isolation Forest evidence. This is a legitimate sanity check, but it should not be described as external validation.

## 10. Relationship to SHAP and explainable-anomaly literature

The verified explainable-anomaly survey by Li, Zhu, and van Leeuwen supports distinguishing an anomaly detector from a post-hoc explanation mechanism. The present method is most accurately placed as an archive-specific, post-hoc local ranking that has access to fitted model internals and standardized features.

Yeh *et al.* supports the general principle that explanation quality can be examined through functional perturbations. The project's zero-neutralization protocol is **not** the published infidelity metric, and its `Strong`/`Moderate` labels are not categories defined by that literature.

SHAP, as introduced by Lundberg and Lee, is an additive feature-attribution framework with a different formal basis. SHAP was not executed in this project. The combined POLIX score:

- is not a Shapley value;
- has no Shapley background distribution;
- does not satisfy or claim SHAP's additive-explanation guarantees;
- does not allocate interactions;
- must not be called “SHAP-like” without immediately stating these differences.

The small archive is a reasonable motivation for avoiding an unvalidated generic explainer, but it is not evidence that SHAP is inherently invalid for Isolation Forest or that the custom heuristic is superior. No quantitative explainer benchmark was performed.

## 11. Sufficiency for a paper contribution

The explanation layer can support a **methodology/case-study contribution** if framed as:

> a deterministic four-component local ranking that links archive-relative unusualness to named Matrix-C features and their source-product families, accompanied by a limited six-case perturbation check.

It is not yet sufficient for a strong standalone claim of a generally validated explainable-anomaly method. The six cases were selected from the same archive used for model fitting, two are not deployed anomalies, the verdict reuses two components present in the explanation score, and no matched perturbation baseline or explanation-stability study exists.

The method's value in the paper is practical traceability: researchers can see which engineered summaries rank highest for a candidate. Its limitation is that this traceability is not equivalent to causal explanation, physical interpretation, or formal attribution of the Isolation Forest prediction.

## 12. Safe and unsafe manuscript claims

### Safe claims

- “The implementation computes four explanation components, not four models.”
- “A deterministic, project-specific explanation score ranks Matrix-C features within each observation.”
- “The score combines PC1/PC2 loading-weighted separation, assigned-centroid squared distance, positive Isolation Forest occlusion sensitivity, and absolute standardized abnormality.”
- “The ranking is mapped deterministically to product-family labels.”
- “For the six exploratory cases, zero-neutralizing the top three features yielded five project-defined Strong and one Moderate verdict.”
- “The perturbation test evaluates local model behavior under one chosen baseline.”
- “For frozen Sco X-1, the accepted order is peak channel, weighted mean channel, then entropy.”
- “The historical entropy-first narrative was superseded by the exact versioned-function audit.”
- “The explanation identifies candidate features for expert inspection, not physical causes.”

### Claims requiring qualification

- **Feature attribution:** qualify as heuristic attribution of the composite explanation score; “feature ranking” is safer.
- **Model-specific:** prefer “model-informed and implementation-specific”; the absolute-z term is not model-specific.
- **Faithful:** use only as the name of the defined perturbation verdict and state its exact criterion.
- **Product-level explanation:** state that product families are deterministic group labels, not separately learned attributions.
- **Driver:** replace with “highest-ranked feature” unless referring specifically to a positive Isolation Forest occlusion under the stated baseline.

### Unsafe claims

- “The four components are four models.”
- “The combined score explains the Isolation Forest prediction exactly.”
- “The top features caused the anomaly.”
- “The method proves why the observation is physically unusual.”
- “The explanation is SHAP,” “SHAP-like,” or has Shapley guarantees.
- “The XAI score is calibrated, probabilistic, or comparable across observations.”
- “Strong faithfulness validates scientific correctness.”
- “The six cases establish generalization or robustness.”
- “The method outperforms existing explainers.”
- “The deterministic explanation sentence was generated by an LLM.”

## 13. Disagreements for the controlling register

| ID | Issue | Evidence | Agent 5 position |
|---|---|---|---|
| XAI-D01 | Some project prose describes the combined score as explaining the anomaly “decision.” | `model_service.py` sets the label only from `iso.predict`; PCA, KMeans, and z-score do not vote. | Describe a ranking of composite local evidence. Do not claim an exact attribution of the deployed label. |
| XAI-D02 | “Model-specific feature attribution” is used as an unqualified method label. | One term is model-independent; the composite does not decompose one model output. | Prefer “project-specific, model-informed local feature ranking.” Use “attribution” only with an explicit heuristic qualifier. |
| XAI-D03 | Report prose calls the approach “faithful to the deployed models.” | Five Strong/one Moderate result tests two signals on six in-sample cases; KMeans is excluded from the overall verdict. | Limit “faithfulness” to the defined zero-neutralization outcome; avoid a global guarantee. |
| XAI-D04 | `Strong` and `Moderate` may sound like external standards. | Notebook 10 defines them solely by the sign of PCA and Isolation Forest reductions. | Identify them as project-defined categories with no p-value or effect-size threshold. |
| XAI-D05 | Four components may be presented as independent confirmation. | PCA, z-score, and often KMeans terms are correlated functions of the same standardized row. | Call them complementary components, not independent evidence or four models. |
| XAI-D06 | Combined XAI scores may be compared across observations. | Every component is max-normalized within one observation; singleton-cluster KMeans vectors vanish. | Use scores only for within-observation ranking. |
| XAI-D07 | KMeans is presented as part of faithfulness verdict. | `kmeans_pass` is calculated but ignored when assigning Strong/Moderate/Weak. | Report KMeans separately or state explicitly that it does not affect the verdict. |
| XAI-D08 | The generated sentence uses “mainly because” and “driver.” | The combined ranking is not an exact decision decomposition or causal model. | Use “highest-ranked under the explanation score” and “next-ranked feature.” |
| XAI-D09 | Historical Sco X-1 prose ranks entropy first. | Current code, PKL, Notebook 10, and exact audit agree on peak/weighted-mean/entropy. | Preserve the accepted versioned order and record the historical result only as superseded provenance. |
| XAI-D10 | Product-family output may be described as learned product attribution. | It is a prefix-based lookup; `t2_det_pha` maps to Detector Balance. | Call it deterministic product-family labeling/grouping. |

## 14. Additional experiments not executed

No experiment below was run in Phase 4.

1. **NOT EXECUTED —** compare top-three neutralization against random three-feature and bottom-three matched baselines; existing files contain no comparator and new experiments were prohibited. **PRIORITY: HIGH.**
2. **NOT EXECUTED —** evaluate alternative references such as assigned-centroid values, conditional replacements, or nearest-neighbor values; zero may create off-distribution combinations. **PRIORITY: HIGH.**
3. **NOT EXECUTED —** measure explanation-rank stability across Isolation Forest seeds, contamination settings, and leave-one-out fits; existing candidate-stability results do not test explanation stability. **PRIORITY: HIGH.**
4. **NOT EXECUTED —** test whether neutralization changes the deployed anomaly label and decision-function margin, not only `score_samples`; not present in the frozen result files. **PRIORITY: MEDIUM.**
5. **NOT EXECUTED —** test individual top features and feature interactions rather than only simultaneous top-three replacement. **PRIORITY: MEDIUM.**
6. **NOT EXECUTED —** quantify sensitivity to component weighting and normalization; equal weights and local max normalization are currently unbenchmarked design choices. **PRIORITY: MEDIUM.**
7. **NOT EXECUTED —** benchmark against SHAP or another explainable-anomaly method; unnecessary unless the paper claims comparative quality or superiority. **PRIORITY: LOW unless such a claim is proposed.**
8. **NOT EXECUTED —** validate explanations on genuinely new POLIX observations or with expert judgments; neither future data nor expert labels are currently available. **PRIORITY: HIGH for future generalization, but externally blocked.**

## 15. Final audit decision

The frozen implementation is reproducible and transparent enough to be described in a methodology paper, provided its status is not overstated. Its strongest defensible contribution is not formal attribution; it is a deterministic, inspectable link from an archive-relative candidate to ranked engineered features and named Level-2 product families.

The existing six-case perturbation result strengthens the implementation as a sanity check but does not validate the method generally. The paper should retain the exact protocol and counts, label the verdict categories as project-defined, preserve the four-deployed-versus-six-exploratory distinction, and avoid causal, physical, SHAP, comparative-superiority, or future-generalization claims.
