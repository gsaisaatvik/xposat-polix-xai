# Agent 11 — Manuscript Reconstruction Architecture

**Role:** Manuscript Reconstruction Architect  
**Audit date:** 2026-07-28  
**Source manuscript:** `research_paper_ieee/06_IEEE_Conference_Manuscript_Draft.md` (frozen Draft 1)  
**Decision vocabulary:** `RETAIN`, `REWRITE`, `REMOVE`, `MOVE TO SUPPLEMENT`, `NEED GUIDE APPROVAL`, `NEED DOMAIN APPROVAL`  
**Execution boundary:** This document is a reconstruction plan. Draft 1, the reviewed report, project code, notebooks, matrices, result CSVs, saved model, and figures were not modified. No model was fitted, no experiment was run, no Draft 2 or PDF was generated.

## 1. Executive reconstruction decision

### Draft-2 gate: PASS WITH MANDATORY QUALIFICATIONS

Draft-2 reconstruction may proceed. Agent 8 rates the primary applied-methodology contribution **MODERATE**, and Agent 9 found **no numerical or provenance contradiction that invalidates the central archive-screening result**. The controlling evidence supports all of the following:

- the frozen archive contains 25 identifier-matched observations, mapped by the project as 10 source and 15 blank sky;
- Matrix C contains exactly 15 deployed features and excludes WeightedRoll;
- the saved artifact reproduces 21 `Normal` outputs and four anomaly candidates;
- the four deployed candidates and six exploratory explanation/perturbation cases are separate stages;
- three Matrix-C candidates were flagged in all 100 tested Isolation Forest seeds, while Blank Sky-5 was flagged in 29/100;
- the current Sco X-1 ranking is peak channel, weighted mean channel, and entropy;
- WeightedRoll supplies a separate source-plus-background harmonic diagnostic;
- 13 of 15 blank-sky fits satisfy the project-defined acceptable-fit rule, reduced chi-square no greater than 2;
- the saved archive supports a bounded descriptive finding that Matrix-C unusualness and modulation-like harmonic evidence do not identify the same property.

The gate would fail only if Draft 2 restored broad claims rejected by Agents 1–9: validated anomalies, future-data generalization, Matrix-C superiority, general XAI faithfulness, exact label attribution, official background subtraction, calibrated polarization degree, official sky polarization angle, polarization detection, or priority/superiority claims.

### Required paper position

**Exact title**

> An Explainable AI Framework for Analysis of X-Ray Polarimetry Data from XPoSat

**Primary contribution**

> A traceable, product-aware Explainable Artificial Intelligence framework for archive-relative screening of heterogeneous POLIX Level-2 observations.

**Secondary contributions**

1. A 15-feature observation representation preserving provenance to selected POLIX Level-2 product families.
2. A deterministic, project-specific, model-informed local feature-ranking method connecting composite unusualness evidence to Matrix-C features and deterministic product-family labels.
3. A scientifically separate WeightedRoll harmonic and empirical blank-sky diagnostic branch that prevents direct circular confirmation.

**Principal empirical finding**

> Statistical unusualness and modulation-like harmonic evidence are non-equivalent within the frozen project archive.

This means the branches identify different diagnostic properties in the recorded cases. It does not assert statistical independence, physical causation, or correctness of either branch.

## 2. Controlling evidence and approval rules

### 2.1 Evidence order

1. Original archive and observation identifiers.
2. Numerical CSV plus exact generating notebook or code.
3. Saved deployed PKL plus versioned deployed code.
4. Existing reproduction and robustness scripts plus saved outputs.
5. POLIX handbook and current ISRO/ISSDC guidance.
6. Verified primary literature.
7. Reviewed report plus errata.
8. Drafts, summaries, and learning material.

Draft-1 prose is never allowed to override C001–C041, the disagreement register, the exact XAI audit, or Agents 1–9.

### 2.2 Citation identifiers used below

- `R01–R17` refer to the 17 sources classified `VERIFIED AND RETAIN` in `literature/Verified_Reference_Library.md`.
- `R18–R22` are `CONTEXT ONLY` and may not enter Draft 2 unless the exact claim needs them and the recorded follow-up is completed.
- Internal numerical claims cite claim-ledger IDs `C001–C041` in this plan; the final manuscript will cite data/method sources through its reproducibility and evidence statements rather than presenting the internal IDs as scholarly citations.

### 2.3 Approval states

- **No further approval:** computation or boundary is controlled by existing evidence.
- **Guide approval:** framing, placement, venue strategy, author order, or contribution emphasis.
- **Domain approval:** POLIX product semantics, physical terminology, fit adequacy, archive role mapping, or representative-case interpretation.
- **Reference follow-up:** a context-only source would have to be promoted through full inspection, or the claim must be removed/replaced.

## 3. Exhaustive Draft-1 reconstruction map

Line references identify the frozen Markdown Draft 1. Each prose block, heading, list claim, table, and reference block is mapped below. Draft 1 contains no embedded figure object; planned figures are handled separately in Section 5.

### 3.1 Front matter

| Draft-1 item | Action | Reason and mandatory change | Controlling claim/evidence | Draft-2 location | Citation requirement | Approval |
|---|---|---|---|---|---|---|
| Title, line 1 | **REWRITE** | Replace the working title with the exact final title. The product-aware/blank-sky phrase may appear only as scope language. | Final-title instruction; Agent 8 gate | Title | None | No further approval unless guide later changes title |
| Authors/affiliation, lines 3–5 | **REWRITE** | Use four student-author placeholders and a guide/affiliation placeholder without deciding order. Preserve corresponding-author placeholder. | Agent 9; guide questions | Author block | None | **NEED GUIDE APPROVAL** for order and affiliation text |
| Abstract, line 9 | **REWRITE** | Rebuild as exactly 200 words. Name XPoSat and POLIX; state 25/10/15, 15 features, unsupervised screening, project-specific local ranking, separate harmonic/blank-sky branch, fixed four plus qualified three-case stability, non-equivalence, and principal limits. Remove headline “faithfulness” grading, unqualified `Q/U`, “polarization-like” if not immediately bounded, and all uncertainty values. | C001–C003, C012–C015, C017–C024, C035–C040; A8; A9 M1–M10 | Abstract | No citations allowed | Guide approval of final emphasis; domain approval of physical wording |
| Index Terms, line 11 | **RETAIN** with typographic repair | Keep XPoSat, POLIX, X-ray polarimetry, unsupervised anomaly detection, explainable artificial intelligence, scientific machine learning. Repair mojibake dash. | Paper brief | Index Terms | None | No further approval |

### 3.2 I. Introduction

| Draft-1 item | Action | Reason and mandatory change | Controlling claim/evidence | Draft-2 location | Citation requirement | Approval |
|---|---|---|---|---|---|---|
| Section heading, line 13 | **RETAIN** | Required final structure. | Final structure | I. Introduction | None | No further approval |
| Paragraph I-P1, line 15 | **REWRITE** | Retain mission and heterogeneous-product motivation, but remove any wording implying that every feature has an established physical role. Use “selected archive products” and distinguish exposure, channel-distribution, source-azimuth, delivered-light-curve, detector, and roll-resolved products. | C005–C010; Agent 3 | I, context/problem | `R01`, `R02`; `R05` only for instrument lineage | **NEED DOMAIN APPROVAL** for product names/semantics |
| Paragraph I-P2, line 17 | **REWRITE** | Convert the B.Tech narrative into the completed-method story. State that SHAP/LIME were considered initially but not deployed; the final unlabeled design uses the custom local ranking. Preserve branch separation and source-plus-background limitation. | C010, C018–C020, C028, C034; A8 | I, completed design and scope | `R02`; no SHAP citation is necessary for project-history wording. If SHAP is technically described, `R19` needs reference follow-up. | Guide approval of project-evolution wording |
| Paragraph I-P3, line 19 | **REWRITE** | Replace five-way integration/faithfulness gap with the audited limited-gap statement. Avoid “directly comparable framework” as an exhaustive claim and do not present established algorithms as novelty. | C025–C026; A8-D01–D07; A9 M10 | I, literature gap | `R12–R17` as applicable; no context-only multi-view reference unless followed up | **NEED GUIDE APPROVAL** after venue selection |
| Research question, line 21 | **RETAIN** with terminology update | Keep the mandated central question, using “products,” “product-aware features,” “project-specific explainable unsupervised learning,” and “blank-sky-referenced harmonic modulation behaviour.” | Final story; C024 | I, research question | None | Domain approval of “harmonic” formulation |
| Contribution lead, line 23 | **REWRITE** | Replace “five bounded contributions” with one primary and up to three secondary contributions. | A8 contribution hierarchy | I, contribution lead | None | **NEED GUIDE APPROVAL** |
| Contribution item 1, line 25 | **REWRITE** | Retain as secondary contribution 1; explicitly say provenance-preserving engineered representation, not calibrated physical feature set or multi-view learning. | C003, C005–C009, C026 | I, secondary contribution 1 | No citation required for project contribution; method provenance later | Domain approval of feature-family names |
| Contribution item 2, line 26 | **REWRITE** | Fold into the single primary integration contribution. PCA/KMeans/Isolation Forest are established components, not a separate algorithmic contribution. | C011–C012; A8 Section 4 | I, primary contribution | Cite `R08`, `R09`, `R11` later in Methods, not necessarily here | Guide approval |
| Contribution item 3, line 27 | **REWRITE** | Replace “feature-attribution score” with “project-specific, model-informed local feature-ranking method.” State that product grouping is deterministic. | C018, C034, C036; D027–D037 | I, secondary contribution 2 | `R15` for XAD distinction; `R19` only if followed up | Guide approval of XAI terminology |
| Contribution item 4, line 28 | **MOVE TO SUPPLEMENT** | Seed, contamination, included-observation jackknife, tier comparison, ranking correlation, and six-case neutralization are supporting evidence, not co-equal contributions. Summarize only the principal robustness and sanity-check outcomes in Results/Limitations. | C017, C030–C035; A8 Section 4; A9 M4/M7 | Supplement; concise Results references | `R16`, `R17` for evaluation context | Guide decides perturbation visibility |
| Contribution item 5, line 29 | **REWRITE** | Retain as secondary contribution 3. Replace unqualified `Q/U` with harmonic coefficients/fractional harmonic coordinates; say branch separation prevents direct feature leakage and permits comparison, not that it proves independence. | C010, C019–C024, C039–C041 | I, secondary contribution 3 | `R02`, `R06`, `R07` | **NEED DOMAIN APPROVAL** |
| Scope-boundary paragraph, line 31 | **REWRITE** | Keep the explicit nonclaims. Describe Flask as proof-of-concept supporting implementation, not a contribution headline. Add no future-generalization or official-background claim. | C022–C023, C027–C028; A8 | I, final scope paragraph | `R02` for release boundary | Guide approval of disclosure density |

### 3.3 II. Literature Review / Related Work

| Draft-1 item | Action | Reason and mandatory change | Controlling claim/evidence | Draft-2 location | Citation requirement | Approval |
|---|---|---|---|---|---|---|
| Section heading, line 33 | **REWRITE** | Rename to “Literature Review and Related Work” if venue permits; otherwise “Related Work.” | Final structure | II | None | Guide/venue |
| Subsection II-A heading, line 35 | **RETAIN** | Covers required XPoSat/POLIX and polarimetry foundations. | Final structure | II-A | None | No further approval |
| Paragraph II-A-P1, line 37 | **REWRITE** | Separate official mission/product facts from general polarimetry foundations. Use harmonic-response language and explain that calibrated inference requires response, background, and coordinate treatment. Avoid implying the fitted project coefficients are official Stokes parameters. | C019–C023, C027; Agent 2/6 | II-A, two shorter paragraphs | `R01`, `R02`, `R05–R07` | **NEED DOMAIN APPROVAL** |
| Paragraph II-A-P2, line 39 | **REWRITE** | Preserve the handbook-controlled release limitation. Replace `Q/U`-style output language with raw modulation, fitted phase, fit category, fractional harmonic coordinates, and empirical comparison. | C019–C023, C027, C040 | II-A, released-product boundary | `R02` exact handbook location | Domain approval; printed page/section check |
| Subsection II-B heading, line 41 | **RETAIN** | Required astronomy anomaly-screening context. | Final structure | II-B | None | No further approval |
| Paragraph II-B-P1, line 43 | **REWRITE** | Expand to use the verified astronomy anomaly literature and emphasize prioritization for expert inspection, not physical classification. Avoid implying direct dataset comparability. | C025; Agent 7 | II-B | `R12–R14` | No further approval |
| Paragraph II-B-P2, line 45 | **REWRITE** | Keep the small, unlabeled archive distinction. Add that same-archive sensitivity analyses do not provide held-out validation and that threshold count is contamination-defined. | C029–C031; A9 M1–M4 | II-B closing gap | `R17` for unlabeled evaluation | No further approval |
| Subsection II-C heading, line 47 | **REWRITE** | Rename “Explainable Anomaly Detection” and avoid “faithfulness” in the heading unless the limited test is immediately qualified. | A9 M7 | II-C | None | Guide |
| Paragraph II-C-P1, line 49 | **REWRITE** | State that general post-hoc methods were considered initially but the final pipeline implemented neither SHAP nor LIME. Replace the context-only Yepmo source with verified `R15`. Describe perturbation as a general evaluation concept only. | C018, C034–C036; Agent 5/7 | II-C | `R15`, `R16`; `R19` only after follow-up if SHAP’s formal method is described | No further approval for nondeployment fact; reference follow-up if `R19` retained |
| Paragraph II-C-P2, line 51 | **REWRITE** | Replace “faithfulness” claim with “six-case in-sample top-three-to-zero perturbation sanity check.” State that Strong/Moderate are project-defined sign rules, KMeans is excluded from verdict, and no causal/scientific validity follows. | C035; D029–D033; A9 M7 | II-C closing comparison; protocol detail in V | `R16` | Guide decides main-paper versus supplement |
| Subsection II-D heading, line 53 | **REWRITE** | Rename “Product-Aware Engineered Representation” to prevent multi-view-learning implication. | C026 | II-D | None | Guide |
| Paragraph II-D-P1, line 55 | **REWRITE** | Remove the direct `R22` reliance and describe Matrix C as traceable engineered early fusion. If a multi-view comparison remains, label it conceptually adjacent and require follow-up for `R21/R22`. | C026; A8-D07; Agent 7 | II-D | Prefer no context-only citation; `R21/R22` only after reference follow-up | Guide approval of gap wording |

### 3.4 III. Dataset, Scope and Problem Formulation

| Draft-1 item | Action | Reason and mandatory change | Controlling claim/evidence | Draft-2 location | Citation requirement | Approval |
|---|---|---|---|---|---|---|
| Section/subsection headings, lines 57 and 59 | **REWRITE** | Use final title “Dataset, Scope and Problem Formulation”; retain data-freeze subsection. | Final structure | III / III-A | None | No further approval |
| Paragraph III-A-P1, line 61 | **REWRITE** | Retain date, 25/10/15, target list, and duplicate Blank Sky-2 warning. State that source/blank-sky roles are project mappings, and observation IDs are controlling keys. | C001–C002; D005 | III-A | `R03` for archive context; internal role metadata for counts | **NEED DOMAIN APPROVAL** for role mapping/friendly names |
| Table I, lines 63–69 | **REWRITE** | Keep 10/15/25 but split “screening use” from harmonic-reference use. Do not imply all 15 blank skies define the baseline; exactly 13 acceptable fits do. Merge product-family summary here only if page pressure requires. | C001–C002, C021 | Final Table I | `R02/R03` only in caption or surrounding text | Domain approval of roles |
| Paragraph III-A-P2, line 71 | **RETAIN** with qualification | Preserve label absence and archive-relative meaning. Replace quoted “Anomaly” with “anomaly candidate”; add no probability, accuracy, or population interpretation. | C012, C029; A9 M1/M3 | III-A, problem formulation | `R17` optional | No further approval |
| Subsection III-B heading, line 73 | **REWRITE** | Rename “Level-2 Product Families and Branch Scope.” | Final structure | III-B | None | No further approval |
| Paragraph III-B-P1, line 75 | **REWRITE** | Use exact product-family/proxy labels. Do not call WR a matrix tier; it is a separate product branch. Explicitly state source-plus-background and exclusion from Matrix C. | C005, C010, C019; Agent 3/6 | III-B | `R02` | **NEED DOMAIN APPROVAL** |
| Paragraph III-B-P2, line 77 | **REWRITE** | Say separation prevents direct use of WR in both screening and comparison. It does not establish statistical independence and does not make the empirical mean an official background. | C024, C039; A8/A9 | III-B closing scope | `R02`, `R07` | Domain approval |

### 3.5 IV. Product-Aware Feature Engineering

| Draft-1 item | Action | Reason and mandatory change | Controlling claim/evidence | Draft-2 location | Citation requirement | Approval |
|---|---|---|---|---|---|---|
| Section/subsection headings, lines 79 and 81 | **RETAIN** | Required final structure; subsection can become “Matrix Development and Final Representation.” | Final structure | IV / IV-A | None | No further approval |
| Paragraph IV-A-P1, line 83 | **REWRITE** | Preserve A=8, B=11, C=15 and WR=6 development history, but do not present WR as another ML tier. State Matrix C is the frozen deployed representation, not an optimum. | C003, C010, C026, C033 | IV-A | Internal matrix files/Notebook 08 | No further approval |
| Table II, lines 85–103 | **REWRITE** | Main paper should group features by family and concise exact computation; complete formulas move to supplement. Apply row-specific terminology below. | C003, C005–C009; Agent 3 | Final Table II plus supplement | `R02` for product semantics; internal code for formulas | Domain approval for nine proxy interpretations |
| Table II, exposure rows 89–90 | **REWRITE** | Use “recorded roll-exposure coefficient of variation” and “recorded maximum/minimum roll-exposure ratio”; avoid source/detector causal interpretations. | C005; Agent 3 | Table II | `R02` | Domain approval |
| Table II, channel rows 91–96 | **REWRITE** | Use raw channel-space terms. Feature 6 is “fraction above channel index 4000,” not high energy. Entropy is descriptive. Anode balance is a relative array-count spread, not health/efficiency. | C006, C009; Agent 3 | Table II | `R02` | **NEED DOMAIN APPROVAL** |
| Table II, source-azimuth rows 97–99 | **REWRITE** | Keep peak/median and entropy as delivered roll-profile summaries. Replace “smoothness” interpretation with exact normalized mean absolute first difference in stored order, excluding the circular closing difference, or “order-dependent roughness proxy.” | C007; D008 | Table II | Internal code; `R02` product context | **NEED DOMAIN APPROVAL** |
| Table II, light-curve rows 100–101 | **REWRITE** | Use “delivered-light-curve RATE-array coefficient of variation/peak-to-median proxy.” Do not claim intrinsic variability, flare, or quality-filtered timing analysis. | C008; D010 | Table II | `R02` p. 25 limitation | **NEED DOMAIN APPROVAL** |
| Table II, detector rows 102–103 | **REWRITE** | Use cross-detector delivered-rate spread and raw-channel PHA-centroid spread. Do not claim detector health, gain shift, or calibrated energy disagreement. | C005, C009; Agent 3 | Table II | `R02` | **NEED DOMAIN APPROVAL** |
| Paragraph IV-A-P2, line 105 | **REWRITE** | Keep zero missing values and no deployed imputer. Remove historical report discussion from main prose; put correction/provenance in changelog or reproducibility note. State future missing values are outside frozen results. | C004 | IV-A or reproducibility supplement | None | No further approval |
| Subsection IV-B heading, line 107 | **REWRITE** | Rename “Selection and Leakage Controls.” | Final structure | IV-B | None | No further approval |
| Paragraph IV-B-P1, line 109 | **REWRITE** | Retain traceability and deployed-selection history. Add that A/B/C comparison reveals feature-tier dependence; only Sco X-1 and Blank Sky-13 persist across A/B/C. No optimality or superiority claim. | C026, C033; D024 | IV-B | Internal ablation output | No further approval |

### 3.6 V. Explainable Unsupervised Methodology

| Draft-1 item | Action | Reason and mandatory change | Controlling claim/evidence | Draft-2 location | Citation requirement | Approval |
|---|---|---|---|---|---|---|
| Section/subsection headings, lines 111 and 113 | **REWRITE** | Use required title “Explainable Unsupervised Methodology.” Retain preprocessing/components subsection. | Final structure | V / V-A | None | No further approval |
| Paragraph V-A-P1, line 115 | **REWRITE** | Preserve scaler, two-component PCA values, KMeans \(k=5\), and Isolation Forest settings. State only `IsolationForest.predict` supplies the fixed label. Add that two Matrix-C KMeans clusters are singletons, producing zero assigned-centroid distance for Sco X-1 and Blank Sky-13. | C011, C029, C032, C034 | V-A | `R08`, `R09`, `R10`, `R11` | Guide decides whether singleton detail is main text or limitations |
| Paragraph V-A-P2, line 117 | **REWRITE** | Replace “complementary evidence” with precise roles. Contamination is a fixed screening assumption imposing four candidates in this sample, not prevalence. KMeans is descriptive geometry, not independent confirmation. | C029, C032; D023 | V-A | `R11`, `R17` | No further approval |
| Subsection V-B heading, line 119 | **REWRITE** | Rename “Project-Specific Four-Component Local Feature Ranking.” | C018, C034 | V-B | None | Guide approval of final terminology |
| PCA equation block, lines 121–127 | **RETAIN** with notation check | Formula matches deployed implementation. Explicitly say it describes absolute weighted separation in the retained two-component PCA view, not the full-space decision. | C018, C034; Agent 5 | V-B | Internal `model_service.py`; `R08` | No further approval |
| KMeans equation block, lines 127–131 | **RETAIN** with caveat | Formula is correct. Add singleton-cluster behavior and say it is assigned-centroid displacement, not anomaly proof. | C032; Agent 5 | V-B | Internal code; `R09` | No further approval |
| Isolation Forest occlusion block, lines 133–137 | **REWRITE** | Preserve zero-in-standardized-space intervention, but state negative deltas are clipped to zero before combination and zero is the training mean for a feature. Do not call it causal occlusion or exact attribution. | C018, C034; Agent 5 | V-B | Internal code; `R11` | No further approval |
| Abnormality/normalization/equation block, lines 139–145 | **REWRITE** | State that each nonzero component is max-normalized within one observation, the four normalized vectors are summed with equal implicit weight, and combined values are valid only for within-observation ordering. Product families are prefix-mapped labels, not learned attributions. | C018, C034, C036; D031–D036 | V-B | `R15` for XAD context; internal code for exact method | Guide approval |
| Deterministic sentence paragraph, line 147 | **REWRITE** | Retain template fact but remove language such as “mainly because” or causal “driver.” Use “highest-ranked feature under the local explanation score.” State explicitly that no large language model generates the deployed sentence. | D034, C018 | V-B or implementation note | None | No further approval |
| Subsection V-C heading, line 149 | **REWRITE** | Rename “Six-Case Feature-Neutralization Sanity Check.” Do not headline general faithfulness. | C035; A9 M7 | V-C | None | Guide decides main text versus supplement |
| Paragraph V-C-P1, line 151 | **REWRITE** | Preserve separation from fixed four. Specify simultaneous top-three-to-zero intervention; Strong means PCA and Isolation Forest decrease, Moderate means exactly one decreases, Weak neither; KMeans does not enter the verdict. State sign-only, no effect threshold, no comparator, in-sample, method-aligned. | C014, C035; D029–D033 | V-C concise protocol; detail supplement | `R16` for perturbation concept | Guide approval |

### 3.7 VI. Independent Harmonic Diagnostic

| Draft-1 item | Action | Reason and mandatory change | Controlling claim/evidence | Draft-2 location | Citation requirement | Approval |
|---|---|---|---|---|---|---|
| Section/subsection headings, lines 153 and 155 | **REWRITE** | Use “Independent Harmonic Diagnostic” and “WeightedRoll Semantics and Fit.” | Final structure | VI / VI-A | None | **NEED DOMAIN APPROVAL** |
| Fit model paragraph/equation, lines 157–161 | **REWRITE** | Keep inverse-variance weighted second-harmonic model, but use neutral coefficient symbols \(C,H_c,H_s\), or explicitly define project \(Q,U\) as mathematical harmonic coefficients. Avoid unqualified Stokes notation. | C019–C020; D038 | VI-A | `R02`, `R06`, `R07` | **NEED DOMAIN APPROVAL** for notation and fit suitability |
| Raw-modulation block, lines 163–167 | **REWRITE** | Replace \(Q,U\) if notation changes; call \(A/C\) raw modulation. Main paper should report central values without uncertainty unless needed. Notebook-11 CSV controls any displayed uncertainty. | C022, C037 | VI-A | `R02`, `R06`, `R07` | Domain approval |
| Phase block, lines 169–173 | **REWRITE** | Call this fitted modulation phase only. Consider omitting the equation/value from the main paper if it does not serve the non-equivalence argument. It is not sky PA. | C023 | VI-A or supplement | `R02`, `R07` | **NEED DOMAIN APPROVAL** |
| Boundary/fit-class paragraph, line 175 | **REWRITE** | Preserve coefficient and PA boundaries. State fit bands are project-defined descriptive screening categories, not p-values, detection thresholds, or proof of adequacy. | C020, C023, C040 | VI-A | `R02` | **NEED DOMAIN APPROVAL** for retaining categories |
| Subsection VI-B heading, line 177 | **REWRITE** | Rename “Empirical Blank-Sky Reference.” | C021 | VI-B | None | No further approval |
| Normalized-coordinate/reference block, lines 179–186 | **REWRITE** | Use “fractional harmonic coordinates” \(h_c=H_c/C\), \(h_s=H_s/C\), or explicitly empirical \(q,u\). Keep 13/15 and exact mean/sample SD only if needed. Describe the distance as diagonal and descriptive; it ignores coordinate covariance, fit uncertainty, baseline-estimation uncertainty, and observing-condition matching. Never call it sigma/confidence. | C021, C039, C040 | VI-B; detailed equations/statistics supplement | `R02`, `R07` | **NEED DOMAIN APPROVAL** for baseline suitability and notation |
| PD-sensitivity paragraph, line 188 | **MOVE TO SUPPLEMENT** | Remove from the main paper. Retain only as optional sensitivity scenarios if guide requests; no official \(\mu_{100}\), PD, or measurement claim. | C022, C041; A9 M8 | Supplementary plan at most | `R02`, `R06`, `R07` | **NEED GUIDE APPROVAL** and **NEED DOMAIN APPROVAL** |

### 3.8 Draft-1 VII. Experimental Protocol

The final structure has no standalone Experimental Protocol section. Its verified content must be distributed across Sections V–VI, Results, Limitations, and the supplement.

| Draft-1 item | Action | Reason and mandatory change | Controlling claim/evidence | Draft-2 location | Citation requirement | Approval |
|---|---|---|---|---|---|---|
| Section heading, line 190 | **REMOVE** as a standalone section | Integrate reproducible method settings in V–VI and move audit mechanics to supplement. | Final structure; page discipline | No standalone section | None | Guide/venue |
| Paragraph VII-P1, line 192 | **REWRITE** | Keep exact replay and accepted Sco X-1 audit provenance in the reproducibility supplement/changelog. Do not burden main Results with historical mismatch beyond using the controlling order. | C012, C015–C016 | Short Results provenance sentence; detailed supplement | None | No further approval |
| Paragraph VII-P2, line 194 | **MOVE TO SUPPLEMENT** | Preserve exact seed, contamination, included-observation jackknife, A/B/C, separate WR, rank-correlation, and neutralization protocols. State contamination changes thresholds over one ordering; jackknife is retrospective, not held-out validation; WR is not an ablation tier. | C017, C030–C035; Agent 4/5 | Supplementary robustness protocol | `R16`, `R17` for evaluation context | No further approval |
| Paragraph VII-P3, line 196 | **MOVE TO SUPPLEMENT** | Record audit environment as the successful reproduction environment, not original training environment. Put unpinned-environment limitation in Section IX. Do not claim portable raw-data-to-result reproduction. | D004; A9 M11 | Reproducibility supplement and IX | `R10` for software | Guide decides how much version detail appears in main paper |

### 3.9 Draft-1 VIII. Results → Draft-2 VII. Results

| Draft-1 item | Action | Reason and mandatory change | Controlling claim/evidence | Draft-2 location | Citation requirement | Approval |
|---|---|---|---|---|---|---|
| Section heading, line 198 | **RETAIN** and renumber | Results becomes Draft-2 Section VII. Required subsections are fixed deployed result, tested-procedure stability, cross-tier persistence, local ranking examples, and harmonic results. | Final structure | VII | None | No further approval |
| Subsection VIII-A heading, line 200 | **REWRITE** | Rename “Cross-Feature-Tier Persistence” and keep separate from fixed four and seed-stable three. | C033 | VII-C | None | No further approval |
| Table III, lines 202–209 | **MOVE TO SUPPLEMENT** | Full A/B/C/WR table is too easily read as a four-way model contest. WR is not an ML tier; \(k\) differs by matrix; no superiority is supported. Main paper should report only the bounded cross-tier persistence statement, optionally in final candidate table. | C010, C026, C033; D024/D026 | Supplement; two-column summary in final Table III | Internal ablation output | Guide page-limit decision |
| Paragraph VIII-A-P1, line 211 | **REWRITE** | Retain descriptive A/B/C rank and threshold sensitivity only if space permits. Separate WR entirely. State only Sco X-1 and Blank Sky-13 persist across A/B/C; no optimality. | C033; Agent 4 | VII-C | Internal ablation output | No further approval |
| Paragraph VIII-A-P2, line 213 | **MOVE TO SUPPLEMENT** | Rank correlations are descriptive. Remove nominal p-values from main paper. Explain singleton KMeans clusters before interpreting its distances; do not say “independent.” | C032; D023/D025 | Supplementary ranking agreement | `R08`, `R09`, `R11`; internal CSV | Guide decides omission |
| Subsection VIII-B heading, line 215 | **REWRITE** | Split into “Fixed Deployed Result” and “Procedure-Qualified Stability.” | Final structure | VII-A and VII-B | None | No further approval |
| Paragraph VIII-B-P1, line 217 | **RETAIN** | Exact controlling result: 21 Normal and four anomaly candidates under the frozen artifact. | C012 | VII-A | Internal PKL/reproduction CSV | No further approval |
| Table IV, lines 219–226 | **REWRITE** | Retain IDs, project labels, fixed score, 100-seed frequency, cross-tier persistence, and leading local evidence. Use current Sco order. Rename Blank Sky-5 evidence “order-dependent source-roll roughness proxy.” Label scores as within-observation ranking values where applicable. Do not imply equal robustness or causal drivers. | C013, C015, C017, C032–C036 | Final Table III | Internal reproduction/XAI/seed/ablation CSVs | Domain approval of friendly labels and feature wording |
| Paragraph VIII-B-P2, line 228 | **REWRITE** | Use exact phrase “three-candidate Matrix-C core stable under the tested procedures.” Explain Blank Sky-5 at 29/100 and Blank Sky-15 (`C24_0020`) as a boundary competitor at 68/100 without adding it to the fixed four. Contamination is threshold persistence; included-row jackknife is retrospective. Cross-tier two is separate. | C017, C030–C033 | VII-B and VII-C | Internal robustness outputs | Guide approval of prominence |
| Paragraph VIII-B-P3, line 230 | **MOVE TO SUPPLEMENT** | The median/minimum jackknife rank correlations are valid descriptive values but not central. Include only if page space remains, with no generalization wording. | C031; Agent 4 | Supplementary jackknife results | Internal CSV | No further approval |
| Subsection VIII-C heading, line 232 | **REWRITE** | Rename “Six-Case Perturbation Sanity Check.” | C035 | VII-D or supplement | None | Guide placement |
| Paragraph VIII-C-P1, line 234 | **REWRITE** | Keep exact reproduction tolerance and 5 Strong/1 Moderate/0 Weak only if criteria and six-case exploratory scope are adjacent. Say this supports internal behavioral consistency under the chosen intervention only. | C014, C035 | VII-D concise result or supplement | `R16` for evaluation concept | Guide approval |
| Subsection VIII-D heading, line 236 | **REWRITE** | Rename “Harmonic and Empirical Blank-Sky Results.” | C020–C024 | VII-E | None | Domain approval |
| Paragraph VIII-D-P1, line 238 | **REWRITE** | Retain 25 fitted, 19/3/3 overall fit categories, 15 blank skies and 13/1/1 breakdown only if useful. The main central baseline statement is 13 acceptable fits under the declared rule. Raw-modulation summary values may move to supplement. | C021, C040 | VII-E; detailed statistics supplement | Internal physical CSVs | **NEED DOMAIN APPROVAL** |
| Table V, lines 240–253 | **REWRITE** and compress | Main paper should retain representative central values and fit-quality categories, not all propagated uncertainties. Use IDs as keys. Keep Sco X-1, Her X-1, Crab `P01_0005`, and selected blank skies if they serve the non-equivalence finding. All ten source rows and uncertainty details move to supplement. Notebook-11 CSV controls any retained error. Replace `Q/U` distance with descriptive fractional-harmonic-coordinate distance and remove “within empirical scatter” unless the declared rule is named. | C037–C040; A9 M8/M9 | Final Table IV; full table supplement | Internal Notebook-11 result CSVs | **NEED DOMAIN APPROVAL** for cases, baseline, categories |
| Paragraph VIII-D-P2, line 255 | **REWRITE** | Say “All ten source raw-modulation values lie within the empirical blank-sky mean ± two sample standard deviations under the declared scalar rule.” Do not imply zero polarization or a calibrated interval. | C038 | VII-E | Internal source-comparison CSV | Domain approval |
| Subsection VIII-E heading, line 257 | **REMOVE** from Results | Implementation is supporting evidence, not a result subsection. | C028; A8 | Reproducibility note/supplement | None | Guide |
| Paragraph VIII-E-P1, line 259 | **MOVE TO SUPPLEMENT** | Retain proof-of-concept integration and known pending checks. Do not claim production validation or exact Notebook-11/service uncertainty equivalence. | C028, C037; A9 M9/M11 | Reproducibility supplement; one sentence in Conclusion if space | None | Guide |

### 3.10 Draft-1 IX. Discussion → Draft-2 VIII. Discussion

| Draft-1 item | Action | Reason and mandatory change | Controlling claim/evidence | Draft-2 location | Citation requirement | Approval |
|---|---|---|---|---|---|---|
| Heading and thesis, lines 261–263 | **REWRITE** | Renumber as VIII. State “within the frozen archive” and use “modulation-like harmonic evidence.” Do not call the branches statistically independent. | C024; A8 Section 5 | VIII opening | None | Guide and domain approval |
| Her X-1 paragraph, line 265 | **REWRITE** | Retain stable Matrix-C status, leading delivered-light-curve RATE-array proxy, descriptive coordinate distance, and project-defined poor fit. Do not conclude a physical cause or formal inadequacy beyond “not well summarized under the project fit category.” | C008, C017, C039–C040 | VIII, case 1 | Internal CSVs | **NEED DOMAIN APPROVAL** |
| Sco X-1 paragraph, line 267 | **REWRITE** | Retain exact order and values: peak 2.454499, weighted mean 2.207369, entropy 1.813968. Historical mismatch belongs in changelog/audit, not the scientific narrative. Say these are highest-ranked energy-product features under the local heuristic. Its harmonic result is within the declared empirical rules and does not confirm or refute polarization. | C015–C016, C017–C018, C036, C038–C040 | VIII, case 2 | Internal XAI/physical CSVs | Domain approval |
| Crab `P01_0005` paragraph, line 269 | **REWRITE** | Retain the converse descriptive comparison: largest source raw modulation, acceptable project fit, not fixed candidate, 3/100 seed flags, and within declared empirical blank-sky rule. Do not call it polarization evidence. | C017, C022, C024, C038–C040 | VIII, case 3 | Internal CSVs | Domain approval |
| Blank-sky paragraph, line 271 | **REWRITE** | Retain Blank Sky-13 stable and Blank Sky-5 seed-sensitive. Use exact proxy names. Their presence supports archive-quality triage, not a source-physics classifier. List possible causes only as untested categories, not explanations. | C013, C017, C024; Agent 3/4 | VIII, case 4 | Internal CSVs | Domain approval of labels/interpretation |
| Synthesis paragraph, line 273 | **REWRITE** | Preserve the triage concept but remove categorical four-quadrant language unless the criteria are displayed. Say branch disagreement is an inspectable diagnostic comparison; neither branch validates the other. | C024, C039; A8/A9 | VIII closing synthesis | None | Guide/domain approval |

### 3.11 Draft-1 X. Limitations → Draft-2 IX. Limitations and Threats to Validity

| Draft-1 item | Action | Reason and mandatory change | Controlling claim/evidence | Draft-2 location | Citation requirement | Approval |
|---|---|---|---|---|---|---|
| Heading, line 275 | **RETAIN** and renumber | Required final structure. | Final structure | IX | None | No further approval |
| Paragraph X-P1, line 277 | **REWRITE** | Retain \(n=25\), no labels/holdout, same-archive fitting, contamination assumption, feature-tier and seed sensitivity. Add distinction among fixed four, seed-stable three, and cross-tier two. State no inferential performance or population claim. | C012, C017, C029–C033 | IX, statistical validity | `R17` | No further approval |
| Paragraph X-P2, line 279 | **REWRITE** | Add feature-proxy limits, raw-channel semantics, no intrinsic-variability claim, singleton KMeans clusters, no feature-uncertainty propagation, future-data drift, and unpinned original environment. | C006–C009, C032; A9 disclosures | IX, representation/reproducibility | `R02`; internal audits | Domain approval of feature language |
| Paragraph X-P3, line 281 | **REWRITE** | Retain source-plus-background, 13 selected fits, lack of official subtraction/\(\mu_{100}\)/PA conversion, poor-fit limits. Add project-defined fit classes, diagonal distance limitations, and Notebook-11/service uncertainty mismatch. State Notebook CSV controls reported errors. | C019–C023, C027, C037–C041 | IX, physical validity | `R02`, `R06`, `R07` | **NEED DOMAIN APPROVAL** |
| Paragraph X-P4, line 283 | **REWRITE** | Retain no expert adjudication/no causal follow-up/proof-of-concept. Add no prospective release validation, partial Git coverage, and authors’ manual verification obligation. Remove access-control detail unless deployment is discussed. | C028; A9 M11/M12 | IX, external/implementation validity | None | Guide approval |
| Optional limitations table | **NEED GUIDE APPROVAL** | A compact claim-boundary table may replace repetitive prose only if venue page limit permits. It must not be used to hide limitations outside the narrative. | A9 | Final Table V, optional | `R02` for physical boundaries | Guide/venue |

### 3.12 Draft-1 XI. Conclusion → Draft-2 X. Conclusion

| Draft-1 item | Action | Reason and mandatory change | Controlling claim/evidence | Draft-2 location | Citation requirement | Approval |
|---|---|---|---|---|---|---|
| Heading, line 285 | **REWRITE** | Renumber as X. Conclusion. | Final structure | X | None | No further approval |
| Paragraph XI-P1, line 287 | **REWRITE** | Replace “demonstrates” with bounded implementation wording. Replace “local attribution” with project-specific local ranking and “perturbation tests” with six-case sanity check. Say exactly three candidates form a Matrix-C core stable under tested procedures; do not say all contamination values unless the exact candidate-level evidence is adjacent. | C003, C011–C018, C029–C036 | X, implemented workflow/results | None | Guide approval |
| Paragraph XI-P2, line 289 | **REWRITE** | Use harmonic coefficients/fractional coordinates. Preserve 13-fit reference, scalar-rule result, and bounded non-equivalence. Avoid `Q/U` and any implication that modulation amplitude itself is polarization evidence. | C020–C024, C038–C040 | X, empirical finding | None | Domain approval |
| Paragraph XI-P3, line 291 | **REWRITE** | Keep all nonclaims. Future work is restricted to prospective POLIX releases, domain review, official background/response/calibration information, environment freezing, and optional independent validation. Do not prescribe model rework in this completed-project run. | C022–C023, C027; A9 Section 9 | X, limitations/future work | `R02` if release limitation restated | Guide/domain approval |

### 3.13 Acknowledgment and references

| Draft-1 item | Action | Reason and mandatory change | Controlling claim/evidence | Draft-2 location | Citation requirement | Approval |
|---|---|---|---|---|---|---|
| Acknowledgment heading, line 293 | **RETAIN** | Required structure. | Final structure | Acknowledgment | None | No further approval |
| Data acknowledgment, line 295 | **REWRITE** | Use the current official ISSDC wording exactly as verified immediately before submission. Do not paraphrase if the official page prescribes text. | `R04`; C025 reference governance | Acknowledgment | `R04` authoritative page; access date recorded | **NEED DOMAIN/ADMINISTRATIVE APPROVAL** and final web recheck |
| College/guide placeholder, line 297 | **RETAIN** as placeholder | Complete only after names, laboratory, funding, and permissions are approved. | Guide decision | Acknowledgment | None | **NEED GUIDE APPROVAL** |
| References heading, line 299 | **RETAIN** | Required structure; renumber after reconstruction. | Final structure | References | None | No further approval |
| Draft [1] official mission page, line 301 | **RETAIN** | Maps to `R01`, verified. | L001/L002 | References | Verify current page title/access date | Final bibliographic check |
| Draft [2] POLIX handbook, line 303 | **RETAIN** | Maps to `R02`; controls product and calibration boundaries. | L001–L005, L007 | References | Check printed page/section convention | Domain/reference check |
| Draft [3] archive page, line 305 | **RETAIN** | Maps to `R03`; use only for archive identity/provenance. | L016 | References | Record access date | Final bibliographic check |
| Draft [4] acknowledgment page, line 307 | **RETAIN** | Maps to `R04`; controls acknowledgment wording. | L016 | References | Recheck immediately before submission | Administrative/domain check |
| Draft [5] Saini et al., line 309 | **REMOVE** unless followed up | Maps to context-only `R18`; full text was not inspected. Mission context is already supported by `R01/R02`. | Agent 7 warning 1 | References only if promoted | Full-text inspection required | Reference follow-up |
| Draft [6] Rishin et al., line 311 | **RETAIN** with warning | Maps to `R05`; use for development lineage, not current flight calibration. | L002 | References | Confirm arXiv/DOI metadata | Final bibliographic check |
| Draft [7] Fabiani, line 313 | **RETAIN** | Maps to `R06`; general instrumentation/modulation only. | L007 | References | DOI/metadata verified | Final bibliographic check |
| Draft [8] Kislat et al., line 315 | **RETAIN** | Maps to `R07`; general Stokes/background foundation, not certification of project coefficients. | L006/L007 | References | DOI/metadata verified | Final bibliographic check |
| Draft [9] Pearson, line 317 | **RETAIN** | Maps to `R08`; PCA foundation. | L013 | References | Metadata verified | No further approval |
| Draft [10] MacQueen, line 319 | **RETAIN** | Maps to `R09`; KMeans foundation. | L013 | References | Metadata verified | No further approval |
| Draft [11] Liu et al., line 321 | **RETAIN** | Maps to `R11`; Isolation Forest method. | L009 | References | DOI verified | No further approval |
| Draft [12] Baron and Poznanski, line 323 | **RETAIN** | Maps to `R12`; astronomy outlier ranking. | L008 | References | DOI verified | No further approval |
| Draft [13] Lochner and Bassett, line 325 | **RETAIN** | Maps to `R14`; human-in-the-loop astronomical anomaly detection. | L008 | References | DOI verified | No further approval |
| Draft [14] Lundberg and Lee, line 327 | **REMOVE** unless needed and promoted | Maps to context-only `R19`. SHAP was not deployed. Initial-design history can be documented without making SHAP a scientific dependency. | L015; Agent 7 warning 3 | Related Work only if retained | Full inspected support/reference promotion required | Reference follow-up |
| Draft [15] Yepmo et al., line 329 | **REMOVE/REPLACE** | Maps to context-only `R20`. Use verified `R15` explainable-anomaly taxonomy instead. | L010; Agent 7 warning 2 | References | Add valid BibTeX for `R15` | No further approval after verification |
| Draft [16] Yeh et al., line 331 | **RETAIN** | Maps to `R16`; perturbation evaluation concept only. | L011 | References | Metadata verified | No further approval |
| Draft [17] Pedregosa et al., line 333 | **RETAIN** | Maps to `R10`; software provenance. | L013 | References | Metadata verified | No further approval |
| Draft [18] Hwang et al., line 335 | **REMOVE** unless followed up | Maps to context-only `R22`; Matrix C is not the method described by this paper. Prefer no multi-view algorithm claim. | L014; C026 | References only if comparison retained | Full-text support and explicit limitation required | Reference follow-up |
| Missing retained sources | **REWRITE** bibliography | Consider adding `R13` for anomaly-ranking evaluation and `R17` for unlabeled outlier-evaluation limits because Draft 2 makes those exact claims. Do not add references to increase count. | L008/L012 | Related Work/Limitations | Existing verified BibTeX entries required | Final claim-to-reference check |

## 4. Draft-2 section-by-section reconstruction

### Front matter

- Use the exact title and four-author placeholders.
- Write one exactly 200-word abstract with no citation, equation, acronym ambiguity, or calibrated polarimetry claim.
- Keep six controlled index terms.

### I. Introduction

1. Establish XPoSat/POLIX and the computational challenge of heterogeneous Level-2 products.
2. Explain the completed-project evolution: SHAP/LIME were considered in the initial proposal, but lack of trusted labels and the final data structure led to an unsupervised, project-specific local ranking.
3. State the finite-search literature gap without priority language.
4. State the central research question.
5. Present one primary and three secondary contributions.
6. Close with archive, calibration, and deployment boundaries.

### II. Literature Review and Related Work

- Official XPoSat/POLIX and released-product semantics.
- Harmonic/Stokes foundations with explicit limits on applying calibrated terminology.
- Astronomy anomaly ranking and expert inspection.
- Explainable anomaly detection and perturbation concepts.
- Gap: limited published work identified on the complete bounded integration, not proof of priority.

### III. Dataset, Scope and Problem Formulation

- Define the 27 July 2026 freeze and identifier-controlled 25-row scope.
- State the project mapping: 10 source, 15 blank sky.
- Explain product families, label absence, archive-relative candidate definition, and physical/nonphysical branch distinction.
- Use IDs as primary keys and friendly names as project labels.

### IV. Product-Aware Feature Engineering

- Briefly explain Matrix A/B/C development, then define Matrix C as the frozen deployed representation.
- Group all 15 features by provenance; main table uses concise exact descriptions.
- Move full formulas and code/path provenance to supplement.
- State zero missing values and no deployed imputer.
- Explain WR exclusion and reject Matrix-C superiority.

### V. Explainable Unsupervised Methodology

- Give saved scaler/PCA/KMeans/Isolation Forest settings.
- State that only Isolation Forest sets the fixed label.
- Explain contamination as a fixed screening assumption.
- Define the four-component local ranking exactly, including positive occlusion clipping, within-observation max normalization, implicit equal sum, and deterministic family mapping.
- Describe deterministic explanation text.
- Describe six-case perturbation only as an in-sample sanity check with project-defined sign rules.

### VI. Independent Harmonic Diagnostic

- State exact WeightedRoll source-plus-background semantics.
- Define inverse-variance second-harmonic fitting using domain-approved coefficient notation.
- Define raw modulation and fitted phase with explicit non-PD/non-PA boundaries.
- State project fit classes and their descriptive status.
- Define the 13-fit empirical blank-sky reference and the limitations of the diagonal coordinate distance.
- Keep Notebook-11 CSV as uncertainty provenance and disclose later service divergence in supplement.

### VII. Results

- **A. Fixed deployed result:** 21 Normal and four candidates.
- **B. Procedure-qualified stability:** three fixed candidates 100/100; Blank Sky-5 29/100; boundary sensitivity stated.
- **C. Cross-feature-tier persistence:** only Sco X-1 and Blank Sky-13 across A/B/C; do not confuse with fixed four or seed-stable three.
- **D. Local feature-ranking examples:** accepted Sco X-1 order; optional concise six-case sanity-check result.
- **E. Harmonic/blank-sky results:** 15 blank-sky fits, 13 reference fits, bounded source findings, fit-quality limitations.

### VIII. Discussion

- Organize around archive-bounded diagnostic non-equivalence.
- Use Sco X-1, Her X-1, Crab `P01_0005`, and selected blank-sky cases for one methodological point each.
- Do not assign astrophysical or instrumental causes.
- Explain that branch separation prevents direct leakage and permits comparison; it does not prove statistical independence.

### IX. Limitations and Threats to Validity

Cover all of the following explicitly:

- \(n=25\), 15 features, no anomaly labels, no external holdout;
- same-archive retrospective fitting and description;
- contamination-defined count and seed-sensitive threshold neighborhood;
- feature-tier dependence and singleton KMeans clusters;
- channel-space and delivered-array proxies;
- no feature-uncertainty propagation or future-release validation;
- project-specific heuristic XAI and six in-sample perturbation cases;
- source-plus-background WeightedRoll;
- project-defined fit categories and selected 13-fit baseline;
- diagonal empirical distance without covariance/uncertainty/matching;
- no official background, \(\mu_{100}\), calibrated PD, or official PA;
- Notebook-11/service uncertainty mismatch;
- unpinned original environment, partial Git coverage, and prototype deployment;
- no POLIX-domain candidate adjudication.

### X. Conclusion

- State what was implemented and observed in the frozen archive.
- State how the framework supports expert triage and provenance inspection.
- Restate only the bounded non-equivalence finding.
- State what was not established.
- Limit future work to new releases, official calibration/background information, prospective validation, reproducibility hardening, and expert review.

## 5. Figure reconstruction map

Draft 1 contains no inserted figures. The frozen `05_Figure_and_Table_Manifest.md` lists candidates; their Draft-2 decisions are:

| Planned Draft-1 figure | Action | Draft-2 figure | Required construction and boundary | Evidence | Approval |
|---|---|---|---|---|---|
| Fig. 1 architecture | **REWRITE** | Fig. 1 | Author-drawn vector flow: Level-2 products → Matrix C → scaler/PCA/KMeans/Isolation Forest → local ranking; parallel WR → harmonic fit → empirical blank-sky comparison. Show no arrow from WR to anomaly input. | Code architecture; C003/C010/C018–C021 | Guide/domain caption approval |
| Fig. 2 feature/Matrix pipeline | **REWRITE** and merge | Fig. 1 | Merge with architecture to save space. Use product-family blocks and exact 15-feature count; no multi-view-learning label. | Matrix definitions; C003/C026 | Guide |
| Fig. 3 PCA scatter | **REWRITE** | Fig. 2 | Generate paper-specific PCA view from frozen Matrix-C rows and saved scaler/PCA only. Mark fixed four and use IDs. Caption as descriptive observation space, not validation. | Frozen matrix/model/reproduction | Guide |
| Fig. 4 IF ranking | **REWRITE** | Fig. 3 | Plot saved fixed anomaly-score ordering and annotate 100-seed frequencies. Separate fixed label from seed frequency; frequencies are not probabilities. | Reproduction and seed-summary CSVs; C012/C017 | Guide |
| Fig. 5 XAI examples | **MOVE TO SUPPLEMENT** | Supplementary figure | If retained, use accepted Sco order and within-observation scores only. No cross-observation bar-height comparison or causal “driver” caption. | Exact XAI CSV; C015/C036 | Guide |
| Fig. 6 perturbation | **MOVE TO SUPPLEMENT** | Supplementary figure/table | Show six exploratory cases and project-defined criteria. No general faithfulness headline. | Faithfulness CSV; C014/C035 | Guide |
| Fig. 7 representative WR fit | **MOVE TO SUPPLEMENT** | Supplementary figure | Retain only with source-plus-background, raw harmonic, fit-category, non-PD/non-PA caption. | WeightedRoll fit CSV/real project figure | Domain approval |
| Fig. 8 source/blank coordinates | **REWRITE** | Fig. 4 | Regenerate from verified fractional harmonic coordinates. Show 13-fit empirical center/sample scatter descriptively; no confidence ellipse, sigma region, or detection boundary. Distinguish project roles and outline fixed candidates. | Baseline/source CSVs; C021/C039 | Domain approval |
| Exploratory consensus/evidence figures | **REMOVE** from main paper | None | They do not represent the fixed deployed result. May appear in supplement only if clearly labeled exploratory. | Manifest warning | Guide |
| WR-PCA, raw-modulation ranking, phase/PD plots | **REMOVE** from main paper | None | Risk of circular confirmation or calibrated interpretation. PD sensitivity plots are supplementary at most. | C022/C023/C041 | Guide/domain |

All scientific plots must be generated from frozen CSV/model transformations. Plotting code may transform coordinates already defined by the saved model but may not call `.fit`, retrain, change thresholds, regenerate features, or infer new scientific quantities.

## 6. Final table plan

| Draft-2 table | Content | Source and claim controls | Placement |
|---|---|---|---|
| Table I | Dataset composition and selected Level-2 product families | C001/C002/C005/C019; IDs and project roles | Main |
| Table II | Final Matrix-C feature groups and concise exact meanings | C003–C009; domain-safe names | Main |
| Table III | Four fixed candidates, scores, 100-seed counts, cross-tier persistence, and leading within-observation local evidence | C012–C017/C033/C036; distinguish four/three/two | Main |
| Table IV | Compressed representative harmonic/blank-sky results: central raw modulation, project fit class, descriptive fractional-coordinate distance/status | C021–C024/C037–C040; no calibrated uncertainty synthesis | Main |
| Table V | Limitations and claim boundaries | C022–C041; A9 disclosure list | Main only if page space permits |
| Supplement tables | All 15 formulas; full seed/contamination/jackknife/A-B-C; rank correlations; six perturbation cases; all 25 harmonic fits; Notebook/service uncertainty comparison; optional PD sensitivity scenarios | Controlling CSVs/code and exact caveats | Supplement |

## 7. Mandatory corrections checklist for the reconstructing writer

- [ ] Exact final title; working title removed from title position.
- [ ] Abstract exactly 200 words and citation-free.
- [ ] “25 observations included in the project archive,” never all available data.
- [ ] Project mapping of 10 source and 15 blank sky.
- [ ] No median-imputation claim; frozen Matrix C has zero missing values and deployed path has no imputer.
- [ ] Fifteen Matrix-C features; WR excluded.
- [ ] “High-channel fraction,” not calibrated high-energy fraction.
- [ ] Exact order-dependent first-difference roughness computation, not unrestricted circular smoothness.
- [ ] Delivered-light-curve diagnostic proxy, not intrinsic variability.
- [ ] Raw channel/PHA summaries, not calibrated energy or detector health.
- [ ] Fixed four candidates distinct from six exploratory perturbation cases.
- [ ] Sco X-1: peak channel 2.454499; weighted mean channel 2.207369; entropy 1.813968.
- [ ] Historical entropy-first narrative absent from scientific results; audit/changelog records supersession.
- [ ] “Three-candidate Matrix-C core stable under the tested procedures,” not robust core.
- [ ] Cross-tier persistence of two cases stated separately.
- [ ] Contamination sensitivity described as threshold persistence over one ordering.
- [ ] Jackknife described as retrospective included-observation influence sensitivity, not held-out validation.
- [ ] Singleton KMeans clusters disclosed; zero centroid distance not interpreted as ordinary.
- [ ] Nominal rank-correlation p-values omitted or explicitly descriptive in supplement.
- [ ] Project-specific, model-informed local feature ranking; not SHAP/LIME, causal attribution, or exact label decomposition.
- [ ] Four explanation components, not four models or independent evidence.
- [ ] XAI scores used only for within-observation ordering.
- [ ] Six-case perturbation described as an in-sample sanity check; project-defined Strong/Moderate criteria; KMeans excluded from verdict.
- [ ] Harmonic coefficients/fractional harmonic coordinates; unqualified calibrated Stokes language removed.
- [ ] WeightedRoll described as exposure-weighted and source-plus-background.
- [ ] Raw modulation, not PD; fitted modulation phase, not PA.
- [ ] Thirteen acceptable blank-sky fits at reduced chi-square no greater than 2 under a project-defined rule.
- [ ] Empirical blank-sky reference, not official subtraction/background model.
- [ ] Diagonal distance not described as sigma, confidence, or detection significance.
- [ ] Notebook-11 CSV controls reported uncertainty; later Flask propagation difference disclosed; no identical-implementation claim.
- [ ] PD sensitivity scenarios removed from main paper.
- [ ] No Chandra or XSPECT data-analysis implication.
- [ ] No first/novel/unique/superior/breakthrough/discovery/confirmed-anomaly/polarization-detection language.
- [ ] Flask described only as proof-of-concept supporting implementation and reproducibility.

## 8. Unresolved approvals and nonfatal gates

### Guide decisions

1. Approve one primary and three secondary contributions.
2. Select venue, page limit, and whether “Literature Review and Related Work” matches venue style.
3. Approve author order, affiliation, corresponding author, and acknowledgment additions.
4. Decide whether the six-case perturbation result remains in the main paper or supplement.
5. Approve the four-figure/four-table main-paper set and optional limitations table.
6. Decide whether any representative WR fit belongs in the supplement.
7. Approve the archive-bounded literature-gap wording.
8. Approve the final AI-use disclosure after venue policy is known.

### POLIX/domain decisions

1. Confirm product names, axes, columns, units, and project source/blank-sky mapping.
2. Approve “product-aware” for engineered early fusion.
3. Approve the restrained meanings of all 15 features, especially channel 4000, roughness, light-curve, and detector proxies.
4. Approve harmonic coefficient/fractional-coordinate notation.
5. Assess whether inverse-variance second-harmonic fitting and the project-defined fit categories are suitable archive diagnostics.
6. Assess the 13-fit blank-sky reference and diagonal distance as descriptive archive tools.
7. Approve or remove fitted phase and optional PD sensitivity material.
8. Approve Sco X-1, Her X-1, Crab `P01_0005`, and blank-sky case wording.
9. Confirm current official acknowledgment and paper-identification wording immediately before submission.

### Reference follow-up

- Remove context-only `R18`, `R19`, `R20`, and `R22` by default.
- If a specific Draft-2 claim genuinely needs one, inspect its authoritative/full text, update its reference card and claim map, then retain only the narrowly supported claim.
- Add verified `R13`, `R15`, and `R17` where the revised literature/evaluation argument requires them.

## 9. Reconstruction acceptance criteria

Draft 2 is acceptable for guide review only when:

1. every retained numerical statement is traceable to C001–C041 or a new claim-ledger entry tied to controlling evidence;
2. Markdown and LaTeX contain the same title, abstract, numbers, equations, citations, tables, and captions;
3. the fixed four, seed-stable three, cross-tier two, and exploratory six are never conflated;
4. no sentence upgrades a proxy to a calibrated physical quantity or a model score to scientific truth;
5. every retained scholarly citation has verified identity, inspected support, claim limitation, and valid BibTeX;
6. all figures use real frozen evidence and pass visual/data-source checks;
7. the notebook/service uncertainty divergence is disclosed and not numerically merged;
8. protected Draft-1/report/model/data hashes remain unchanged;
9. no new experiment, retraining, feature generation, SHAP/LIME implementation, or PDF generation occurs;
10. unresolved guide/domain questions are visible rather than silently resolved.

## 10. Final Agent-11 verdict

**Draft-2 gate: PASS WITH MANDATORY QUALIFICATIONS.**

The central archive-screening result is reproducible and internally coherent. The appropriate paper is a bounded applied scientific-computing case study, not a general anomaly-detection validation, a new XAI theory, or a calibrated polarimetry analysis. Agent 9’s current `WEAK REJECT` can plausibly move toward `Weak Accept` only at a suitable applied or student-research venue after this reconstruction, citation control, POLIX-aware review, guide approval, and full author verification.

No additional computational experiment is essential for that bounded submission. External evaluation, expert adjudication, explanation baselines, clustering sensitivity, covariance-aware matched-background analysis, and official calibration become essential only if broader claims are restored; under the accepted no-rework rule they must remain limitations or future work.
