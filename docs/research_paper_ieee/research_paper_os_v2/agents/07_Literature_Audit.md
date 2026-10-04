# Agent 7 - Publication-Focused Literature Audit

**Audit date:** 2026-07-27  
**Scope:** Research Paper OS V2, Phase 2 only  
**Independence rule:** Draft 1 and the reviewed project report were treated as leads, not as evidence.

## 1. Search method

Eight searches were conducted separately: XPoSat/POLIX instrumentation; POLIX data analysis; X-ray polarimetry and Stokes methods; astronomy anomaly detection; explainable anomaly detection; explanation faithfulness; evaluation of small-sample or unlabeled anomaly analysis; and multi-product/multi-view representation. Candidate references were admitted only after bibliographic identity and an abstract, full text, official page, or technical handbook section had been inspected.

The evidence preference was:

1. current official ISRO/ISSDC documentation;
2. the POLIX Level-2 User Handbook;
3. peer-reviewed primary methods and applied astronomy papers;
4. author manuscripts or official proceedings when the publisher page was inaccessible;
5. surveys only for taxonomy or positioning.

Blogs, AI summaries, Wikipedia, title-only search results, and tangential papers were excluded.

## 2. Audit result

| Category | Count | Meaning |
|---|---:|---|
| VERIFIED AND RETAIN | 17 | Suitable for a defined paper claim, subject to the claim limits in the reference card |
| CONTEXT ONLY | 5 | Bibliographically useful, but indirect, partially inspected, or not necessary for a core claim |
| REMOVE OR REPLACE | 6 | Unauthoritative, uninspected beyond metadata, duplicative, or outside the contribution |
| **Total screened** | **28** | |

The counts describe this controlled library, not the number of citations that must appear in a final paper.

## 3. Coverage by research question

| Search area | Retained evidence | Audit conclusion |
|---|---|---|
| XPoSat/POLIX instrumentation | ISRO mission page; handbook; Rishin *et al.* | Adequate for mission and instrument context. The handbook controls released-product semantics. |
| POLIX data analysis | Handbook; ISSDC archive and acknowledgment pages | Adequate for product limitations and data-use wording. No peer-reviewed source located that supersedes the handbook for the released Level-2 products used here. |
| X-ray polarimetry/Stokes | Fabiani; Kislat *et al.* | Adequate for modulation and Stokes foundations. These sources do not validate the project's fitted phase as official sky position angle. |
| Astronomy anomaly detection | Baron and Poznanski; Giles and Walkowicz; Lochner and Bassett | Adequate to motivate unsupervised ranking plus expert inspection. They do not establish physical interpretation of a POLIX candidate. |
| Explainable anomaly detection | Li *et al.*; Yepmo *et al.* as context | Adequate for taxonomy and the distinction between detector and explanation. The project's four-component method remains project-specific. |
| Explanation faithfulness | Yeh *et al.* | Supports perturbation-based evaluation as a concept, not the project's “Strong/Moderate” labels as a universal standard. |
| Unlabeled/small-sample evaluation | Campos *et al.* | Supports cautious treatment of unsupervised evaluation and parameter sensitivity. It does not validate generalization from 25 observations. |
| Multi-product/multi-view analysis | Xu *et al.* and Hwang *et al.* as context | Supports broad terminology only. Matrix C is an early-fusion, engineered feature representation, not a demonstrated multi-view learning algorithm. |

## 4. Literature gap assessment

The reviewed sources support the following cautious statement:

> Limited published work was identified on integrated, product-aware screening of heterogeneous POLIX Level-2 observation products with observation-level feature explanations and a scientifically separate, blank-sky-referenced modulation diagnostic.

The search did **not** establish priority, novelty, superiority, or completeness. No located publication supplied a directly comparable combination of all project elements, but absence from this finite search is not proof that none exists.

## 5. Safe literature claims

- XPoSat carries POLIX for medium-energy X-ray polarimetry and XSPECT for spectroscopy/timing; use current official energy bands.
- POLIX is a Thomson-scattering polarimeter whose azimuthal response can contain polarization information.
- Stokes-type quantities are additive, and background treatment is an essential part of physical polarimetry.
- Unsupervised astronomical anomaly methods are commonly used to rank unusual objects for follow-up, not to provide anomaly ground truth.
- Feature attribution and anomaly detection are distinct tasks.
- Perturbation can test whether an explanation tracks model behaviour under the chosen intervention.
- Evaluation without trustworthy labels is intrinsically limited and sensitive to data and parameter choices.

## 6. Claims the literature does not support

- that this is the first or a novel POLIX anomaly framework;
- that Matrix C is equivalent to a published multi-view learning method;
- that the archive's four fixed candidates are true anomalies;
- that the explanation score is SHAP or has SHAP guarantees;
- that “Strong” faithfulness proves causal or scientific correctness;
- that WeightedRoll in these released files is fully background-corrected;
- that raw modulation is calibrated polarization degree;
- that the fitted phase is official sky polarization angle;
- that the 25-observation archive supports future-data generalization.

## 7. Reference-level warnings

1. **Saini, Madhu, and Karidhal (2025):** bibliographic identity and abstract were verified, but the full article was not retained locally. Keep as context until full-text inspection.
2. **Yepmo, Smits, and Pivert (2022):** DOI and abstract/taxonomy were verified, but full-text access was incomplete. The newer ACM survey is the stronger retained taxonomy source.
3. **SHAP:** retained only as context for what the deployed method is not. Do not imply SHAP was executed.
4. **Multi-view literature:** conceptually adjacent only. The project concatenates product-derived features; it does not implement the objectives studied in the retained multi-view papers.
5. **Instrument development paper:** prototype-era quantities must not be presented as current flight or calibration values.

## 8. Search limitations

- The search was publication-focused rather than a formal systematic review.
- Subscription-only full texts were not treated as fully inspected.
- Current official handbook wording may change in a future data release.
- No domain expert validated whether every retained polarimetry citation is the preferred citation for a final venue.
- Citation selection must be revisited after the guide chooses the paper's exact contribution framing.

## 9. Outputs

- `literature/Verified_Reference_Library.md` contains 22 retained/context reference cards.
- `literature/Reference_Claim_Map.csv` maps admissible claims to references.
- `literature/Rejected_or_Unnecessary_References.md` records six excluded candidates and reasons.

