# Agent 8 — Novelty and Contribution Audit

**Audit date:** 2026-07-28  
**Role:** Novelty and Contribution Reviewer  
**Scope:** Completed project and Research Paper OS evidence through Agent 7  
**Decision vocabulary:** STRONG / MODERATE / WEAK / NOT DEFENSIBLE  
**Execution boundary:** No model fitting, feature generation, result regeneration, or new experiment was performed.

## 1. Executive decision

The project supports a **MODERATE applied-methodology contribution**:

> A traceable, product-aware Explainable Artificial Intelligence framework for archive-relative screening of heterogeneous POLIX Level-2 observations.

The contribution is the disciplined integration of product-derived representation, archive-relative unsupervised screening, inspectable local feature ranking, and a scientifically separate harmonic diagnostic. It is not a new machine-learning algorithm, a general theory of explainable anomaly detection, or a calibrated polarimetry method.

Three secondary contributions are defensible at **MODERATE** strength when their archive-specific and implementation-specific limits are stated:

1. a 15-feature observation representation that preserves provenance to selected POLIX Level-2 product families;
2. a deterministic, project-specific, model-informed local feature-ranking method that connects composite unusualness evidence to Matrix-C features and deterministic product-family labels;
3. a separate WeightedRoll and empirical blank-sky harmonic diagnostic branch that prevents the physical curve from being used both as an anomaly input and as its confirmation.

No contribution qualifies as STRONG under the present evidence. The archive has only 25 observations, no anomaly ground truth, no prospective release validation, no comparison against a directly competing end-to-end framework, and several feature and physical interpretations still require POLIX-aware approval.

The principal empirical finding is **MODERATE as a bounded descriptive finding**:

> Statistical unusualness and modulation-like harmonic evidence are non-equivalent within the frozen project archive.

Discordant source and blank-sky cases support this conclusion. They do not establish a universal relationship, an astrophysical cause, a polarization detection, or the correctness of either diagnostic branch.

## 2. Evidence and literature examined

### 2.1 Project and audit evidence

The audit examined:

- Agent 1, project provenance and evidence hierarchy;
- Agent 2, POLIX product and calibration boundaries;
- Agent 3, all 15 Matrix-C feature definitions and semantic risks;
- Agent 4, fixed results and existing stability, sensitivity, jackknife, ablation, and ranking evidence;
- Agent 5, the exact four-component XAI implementation and six-case neutralization test;
- Agent 6, the WeightedRoll harmonic fit and empirical blank-sky diagnostic;
- Agent 7, the controlled reference library, claim map, and literature-gap assessment;
- the Phase-4 dashboard, truth map, disagreement register, claim ledger, contribution decision, and guide questions;
- the frozen Matrix-C, model, prediction, XAI, faithfulness, and physical-result provenance reported by Agents 1–6.

Draft 1 and the reviewed report were treated as narrative aids. Machine-readable outputs, generating code, saved artifacts, accepted audits, and official product guidance controlled whenever wording differed.

### 2.2 Verified literature baseline

The controlled library contains 17 references classified `VERIFIED AND RETAIN` and five classified `CONTEXT ONLY`. The following comparisons control the contribution decision:

| Literature area | What the verified literature supplies | What it does not establish for this project |
|---|---|---|
| Official XPoSat/POLIX sources, including the Level-2 handbook | Mission context, instrument and released-product semantics, WeightedRoll source-plus-background status, and calibration limitations | An archive-level XAI screening method or validity of the project’s engineered features |
| PCA, KMeans, Isolation Forest, and scikit-learn sources | Established algorithms and software provenance | Algorithmic novelty, project parameter validity, or correctness of the four candidates |
| Astronomical anomaly-detection studies | Precedent for unsupervised ranking and expert inspection of unusual archive objects | A directly comparable POLIX Level-2 representation, product-linked explanation layer, or independent WeightedRoll branch |
| Explainable-anomaly literature | Distinction between detection and explanation and a taxonomy for local explanation methods | Formal guarantees, novelty, or scientific correctness of the project’s combined heuristic |
| Perturbation and explanation-faithfulness literature | Motivation for functional checks under a specified intervention | The project’s `Strong` and `Moderate` labels as standard metrics or proof of general faithfulness |
| X-ray polarimetry and Stokes literature | Harmonic/modulation foundations, additive background treatment, and calibration requirements | Calibrated Stokes quantities, polarization degree, or sky angle from the project’s WeightedRoll fits |
| Multi-view literature | General language for complementary representations | Evidence that Matrix C implements a multi-view learning objective |

The reviewed search identified **limited published work** combining all project elements for POLIX, and it did not identify a directly comparable integrated framework. This is a finite, publication-focused search result, not proof of priority or uniqueness. It cannot support “first,” “novel,” “unique,” or “never attempted.”

## 3. Contribution taxonomy and ranking

### 3.1 Primary contribution

| Proposed contribution | Category | Rank | Why it is defensible | Why it is not stronger |
|---|---|---|---|---|
| A traceable, product-aware XAI framework for archive-relative screening of heterogeneous POLIX Level-2 observations | Applied methodology and systems integration | **MODERATE** | The frozen archive, 15-feature schema, saved pipeline, versioned explanation function, independent WeightedRoll branch, and researcher-facing implementation form a coherent and inspectable workflow. The literature review did not locate a directly comparable POLIX framework. | Its components are established or project-specific heuristics; \(n=25\); there is no anomaly ground truth, prospective validation, end-to-end benchmark, or domain-expert confirmation of all feature semantics. |

**Permitted manuscript formulation**

> This work investigates a traceable, product-aware framework that represents selected heterogeneous POLIX Level-2 products at observation level, screens the frozen archive using unsupervised learning, ranks local feature evidence, and retains WeightedRoll harmonic analysis as a separate empirical diagnostic.

**Do not call this:** a novel algorithm, the first POLIX anomaly framework, a general POLIX anomaly detector, a validated polarimetry pipeline, or a superior method.

### 3.2 Secondary contribution 1 — product-aware observation representation

| Category | Rank | Evidence | Literature comparison | Boundary |
|---|---|---|---|---|
| Applied representation and scientific data engineering | **MODERATE** | Matrix C has 25 rows, one identifier, exactly 15 traceable features, and zero missing cells. Notebook 08 and Agent 3 map each feature to a product field and computation. WeightedRoll is excluded. | Official product documents define the inputs but do not supply this observation-level representation. Multi-view sources are only conceptually adjacent. | This is engineered early fusion, not multi-view learning. Nine features are descriptive proxies whose scientific semantics require restraint and, in some cases, domain approval. |

The contribution is provenance-preserving compression for screening. It is not a calibrated physical feature set. Safe descriptions include “channel-space summary,” “high-channel fraction,” “order-dependent roughness proxy,” and “delivered-light-curve diagnostic proxy.”

### 3.3 Secondary contribution 2 — local feature-ranking method

| Category | Rank | Evidence | Literature comparison | Boundary |
|---|---|---|---|---|
| Project-specific XAI case-study method | **MODERATE** | The deployed function deterministically combines normalized PCA separation, assigned-centroid distance, positive Isolation Forest occlusion sensitivity, and absolute standardized abnormality; it then maps ranked features to fixed product-family labels. | Explainable-anomaly literature supports separating detection from explanation. SHAP provides a different formal framework and was not deployed. No located source validates this exact composite. | It is not an exact decomposition of the Isolation Forest label, a Shapley value, a causal attribution, a calibrated score, or a cross-observation metric. |

The strongest value is practical traceability from an observation to ranked engineered features and their input-product provenance. “Project-specific, model-informed local feature ranking” is preferred. “Feature attribution” is safe only with an immediate heuristic qualification.

The six-case top-three-to-zero experiment is supporting evidence, not an independent contribution. Five project-defined `Strong` and one `Moderate` verdict show that the selected perturbation changed two method-aligned signals in the expected direction for five cases. This does not establish general faithfulness, explanation stability, scientific correctness, or performance relative to another explainer.

### 3.4 Secondary contribution 3 — separate harmonic diagnostic branch

| Category | Rank | Evidence | Literature comparison | Boundary |
|---|---|---|---|---|
| Applied scientific-computing design | **MODERATE** | WeightedRoll is excluded from Matrix C, fit with a declared second-harmonic model, and compared with an empirical reference formed from 13 of 15 blank-sky fits meeting the project rule \(\chi_\nu^2\leq2\). | Polarimetry literature supplies harmonic and Stokes foundations, while the POLIX handbook controls the source-plus-background and calibration limits. The literature does not validate this small archive reference as a background or detection model. | Report harmonic coefficients, fractional harmonic coordinates, raw modulation, fitted phase, fit quality, and archive-relative position only. Do not report calibrated PD, official PA, official background subtraction, or polarization significance. |

The scientifically useful design choice is branch independence. It avoids direct circular confirmation because WeightedRoll is not part of the primary Matrix-C model. The empirical reference remains selected, small, diagonal, and archive-specific.

## 4. Other project elements and their status

| Element | Classification | Rank as a standalone research contribution | Permitted role |
|---|---|---|---|
| StandardScaler, PCA, KMeans, and Isolation Forest | Established algorithms | **NOT DEFENSIBLE** | Components of the integrated screening workflow |
| Fixed four-candidate result | Archive-specific result | **WEAK as a contribution** | Reproducible descriptive result: 21 Normal and four candidates under the frozen artifact |
| 100-seed stability | Supporting robustness evidence | **WEAK** | Shows three Matrix-C candidates in all tested seeds and Blank Sky-5 in 29/100; frequencies are not probabilities |
| Contamination sensitivity | Supporting sensitivity evidence | **WEAK** | Shows threshold sensitivity under the tested contamination values; it is not independent validation |
| Included-observation leave-one-out analysis | Supporting sensitivity evidence | **WEAK** | Describes ranking sensitivity; it is not out-of-sample or target-level validation |
| Matrix A/B/C comparison | Supporting design evidence | **WEAK** | Discloses feature-tier dependence; it does not prove Matrix-C superiority |
| Ranking correlations | Descriptive diagnostic | **NOT DEFENSIBLE as a contribution** | Optional descriptive comparison; nominal p-values do not validate the model |
| Six-case feature neutralization | Supporting XAI sanity check | **WEAK** | Limited in-sample functional check with project-defined verdicts |
| Deterministic explanation sentences | Interface behavior | **NOT DEFENSIBLE as a research contribution** | Reproducible presentation of ranked evidence; the sentences are templates, not LLM outputs |
| Flask research interface and export | Supporting implementation/reproducibility | **WEAK as a research contribution** | Demonstrates an end-to-end prototype; not the principal scientific contribution |
| Versioned scripts, hashes, manifests, and audits | Reproducibility support | **WEAK as a research contribution** | Evidence control and implementation transparency |
| Empirical non-equivalence examples | Bounded empirical finding | **MODERATE** | Supports methodological separation within the frozen archive |

The screening pipeline should not be promoted as a separate algorithmic contribution in addition to the primary framework. Doing so would count the same integration twice.

## 5. Principal empirical finding

**Rank:** **MODERATE as a bounded descriptive finding**

The evidence supports:

> Within the frozen 25-observation archive, statistical unusualness under Matrix C and modulation-like harmonic behaviour under the separate WeightedRoll analysis do not identify the same property.

The representative evidence is intentionally discordant:

- Sco X-1 is a fixed Matrix-C candidate, but its raw modulation and empirical fractional-harmonic position are within the declared blank-sky rules; its harmonic fit is `caution`.
- Her X-1 is a fixed Matrix-C candidate with a moderate project vector distance, but its simple harmonic fit is poor, preventing physical confirmation.
- Crab `P01_0005` has the largest source raw modulation but is not a fixed Matrix-C candidate and remains within the declared empirical blank-sky rules.
- Matrix-C candidates occur among project-labelled blank-sky observations.

This finding demonstrates diagnostic non-equivalence, not independence in a statistical sense. It does not mean that the two branches are unrelated, that one validates the other, or that any observation has a particular physical or instrumental cause.

## 6. Claims that are not defensible

### 6.1 Priority, novelty, and superiority

The following are **NOT DEFENSIBLE**:

- “the first,” “novel,” “unique,” “breakthrough,” “never attempted,” or “discovery”;
- superiority over existing screening, explanation, or polarimetry methods;
- a comprehensive or systematic literature-review claim;
- a claim that the combined use of established components is algorithmic novelty;
- a claim that Matrix C is a new multi-view learning algorithm.

### 6.2 Machine-learning validity

The following are **NOT DEFENSIBLE**:

- four confirmed or robust anomalies;
- anomaly ground truth, anomaly probabilities, statistical significance, or population inference;
- future-POLIX generalization from the 25-row same-archive analysis;
- Matrix-C superiority;
- independence of PCA, KMeans, Isolation Forest, and standardized abnormality;
- “robust core” without the full tested-procedure and Matrix-C qualification;
- treating seed flag frequency as posterior confidence;
- treating nominal correlation p-values as evidence of detector validity or independence.

### 6.3 XAI validity

The following are **NOT DEFENSIBLE**:

- SHAP or LIME was deployed;
- the explanation score exactly decomposes the Isolation Forest label;
- the four components are four models;
- the ranking is causal, physically explanatory, probabilistic, calibrated, or comparable across observations;
- product-family labels are learned attributions;
- `Strong` faithfulness proves scientific correctness or general explanation faithfulness;
- the custom method outperforms a generic explainer;
- deterministic explanation prose was generated by a large language model.

### 6.4 Physical interpretation

The following are **NOT DEFENSIBLE**:

- calibrated or measured Stokes parameters from the project fits;
- official POLIX background subtraction;
- polarization detection or significance;
- calibrated polarization degree;
- official sky polarization angle;
- an official or observation-specific \(\mu_{100}\);
- a Gaussian confidence region or sigma interpretation for the empirical vector-distance cutoffs;
- a physical or instrumental cause assigned to any candidate;
- any implication that Chandra or XSPECT data were analysed in this project.

### 6.5 Dataset and implementation scope

The following are **NOT DEFENSIBLE**:

- “all available POLIX observations”;
- externally verified source/blank-sky friendly names without archive confirmation;
- exact equivalence of the frozen Notebook-08 Matrix C and every future Flask extraction;
- identical Notebook-11 and Flask uncertainty implementations;
- production validation, environment-independent PKL portability, or fully reproducible raw-archive-to-result execution under an unpinned environment.

## 7. Contribution language approved for reconstruction

### 7.1 Primary contribution

> A traceable, product-aware Explainable Artificial Intelligence framework for archive-relative screening of heterogeneous POLIX Level-2 observations.

### 7.2 Secondary contributions

1. A 15-feature observation representation that preserves provenance to selected exposure, channel-distribution, source-azimuth, delivered-light-curve, and cross-detector product summaries.
2. A deterministic, project-specific, model-informed local ranking that connects composite archive-relative unusualness evidence to Matrix-C features and deterministic product-family labels.
3. A scientifically separate WeightedRoll harmonic and empirical blank-sky diagnostic branch that avoids using the same modulation product for both primary screening and confirmation.

### 7.3 Supporting evidence statement

> Existing seed, contamination, included-observation jackknife, feature-tier, and six-case perturbation analyses are sensitivity and sanity checks supporting the case study; the Flask application is a proof-of-concept research interface.

## 8. Disagreements added by Agent 8

Prior disagreements remain in force. The entries below refine contribution framing rather than silently resolving domain or statistical questions.

| ID | Existing or proposed position | Agent 8 decision | Resolution owner |
|---|---|---|---|
| A8-D01 | Draft material can present five co-equal contributions. | Use one primary and no more than three secondary contributions. Treat robustness, faithfulness, and deployment as supporting evidence. | Manuscript architect and guide |
| A8-D02 | The unsupervised PCA/KMeans/Isolation-Forest stack is a separate methodological innovation. | It is an established-method integration contained within the primary framework, not algorithmic novelty. | Manuscript architect |
| A8-D03 | “Model-specific feature attribution” is an adequate standalone contribution label. | Prefer “project-specific, model-informed local feature ranking”; formal label attribution is not supported. | Manuscript architect and guide |
| A8-D04 | The six-case faithfulness result is a major independent contribution. | It is a WEAK standalone claim and a useful supporting sanity check only. | Guide |
| A8-D05 | The Flask implementation is a major research contribution. | It is supporting proof-of-concept implementation and reproducibility evidence, not principal novelty. | Guide |
| A8-D06 | The physical branch provides confirmation of ML candidates. | Its contribution is scientific separation and demonstration of archive-bounded non-equivalence; it does not confirm candidates. | Guide and POLIX-domain reviewer |
| A8-D07 | The 15-feature matrix is a scientifically validated representation. | Its construction is traceable, but its contribution rank remains MODERATE because multiple feature semantics are descriptive proxies pending domain review. | POLIX-domain reviewer |
| A8-D08 | Absence of a directly comparable paper establishes novelty. | It supports only “limited published work was identified”; it does not prove priority, uniqueness, or novelty. | Literature owner and guide |
| A8-D09 | The non-equivalence result establishes statistical independence. | It establishes descriptive discordance within the frozen archive only. | Statistical reviewer |
| A8-D10 | The paper can use broad “explainable anomaly detection method” language. | The scope must remain archive-relative and project-specific; general method validity is untested. | Manuscript architect |

## 9. Guide and domain decisions still required

1. Approve the single-primary/three-secondary contribution hierarchy.
2. Confirm that “product-aware” is acceptable for engineered early fusion without implying multi-view learning.
3. Approve domain-safe names for all 15 features, particularly the channel-4000 fraction, roll roughness, light-curve proxies, and detector summaries.
4. Approve “harmonic coefficients” and “fractional harmonic coordinates” as the default terminology.
5. Decide whether the empirical blank-sky diagnostic and representative cases receive main-paper or supplementary emphasis.
6. Decide whether the six-case perturbation check belongs in the main paper or supplement.
7. Confirm that the non-equivalence finding is described as archive-specific diagnostic discordance, not statistical independence.
8. Approve the final literature-gap wording after venue selection.
9. Recheck current official XPoSat/POLIX acknowledgment wording before submission.
10. Approve author order, venue, page limit, and final figure selection.

## 10. Final gate recommendation

**Contribution gate for Draft-2 reconstruction:** **PASS WITH MANDATORY QUALIFICATIONS**

The primary contribution is rated **MODERATE**, satisfying the reconstruction gate. No evidence contradiction found in Agents 1–7 invalidates the central archive-screening result. The fixed saved artifact reproducibly returns 21 Normal observations and four anomaly candidates, the exploratory six-case XAI stage remains separately identified, the tested procedures support a three-candidate Matrix-C stability core, and WeightedRoll remains outside the primary input.

Draft-2 reconstruction may proceed if it:

- uses the exact fixed title required by the project;
- uses the one-primary/three-secondary hierarchy in Section 7;
- avoids all claims classified NOT DEFENSIBLE;
- presents the fixed four, the three-candidate tested-procedure result, and cross-tier persistence as different findings;
- treats the XAI method as a local ranking heuristic and its neutralization test as supporting evidence;
- treats WeightedRoll as a source-plus-background empirical harmonic diagnostic;
- records unresolved feature semantics and physical interpretation as guide/domain-approval items;
- leaves prospective validation, domain adjudication, improved blank-sky statistics, and explanation benchmarking as limitations or future work rather than executing new experiments.

This is a contribution-framing approval, not a statement that the manuscript is submission-ready. Agent 9 hostile review, Agent 11 reconstruction mapping, faculty/domain approval, venue selection, and final author verification remain required.
