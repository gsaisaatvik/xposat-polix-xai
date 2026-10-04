# Final Submission Readiness

**Assessment date:** 2026-07-28  
**Content status:** **GUIDE-READY**  
**Submission status:** **NO — approvals, venue adaptation, and final human verification remain**

## 1. Draft-2 execution gate

| Gate | Result | Evidence |
|---|---|---|
| Fixed result remains 21 Normal and four candidates | PASS | Saved PKL and deployed reproduction CSV |
| Four fixed candidates remain separate from six exploratory XAI cases | PASS | Agent 1/5 audits; manuscript Sections V and VII |
| Three-candidate tested-procedure stability remains supported | PASS | 100-seed summary: three at 100/100; Blank Sky-5 at 29/100 |
| Matrix-C/WeightedRoll separation remains intact | PASS | Matrix-C header, Notebook 08, feature script, framework figure |
| Representative non-equivalence cases remain supported | PASS | Fixed predictions, XAI CSV, harmonic-fit and source-comparison CSVs |
| Primary contribution at least Moderate | PASS | Agent 8: Moderate |
| No contradiction invalidates the bounded archive-screening result | PASS | Agents 9 and 11 |
| New experiment essential for narrow case study | NONE IDENTIFIED | Agent 9; broader validation remains future work |

## 2. Protected-artifact integrity

Rechecked SHA-256 values:

| Protected artifact | SHA-256 | Result |
|---|---|---|
| Draft-1 Markdown | `6E110EF5FE6570ABB138337BEC53C12D8A89A02C048B2582AE6D9613D90F5305` | UNCHANGED |
| Draft-1 LaTeX | `C849C8340CE41A08767579BDC0C565F9FB7693C2FBC17023D46C6E1714F5511A` | UNCHANGED |
| Reviewed report | `5D37B4A43901C86C697F83E31F138384CE320470ECB6BE2E887861E3A2C3229F` | UNCHANGED |
| Matrix C | `3936E1B0AAF44ACFF39597BEFEC1B466A26511123655946F8829A4E6263DB0FA` | UNCHANGED |
| Saved model PKL | `D8EFD73C9744ED1CA1098A4599DA91ACDEDC250BB2B6639728364AEF6B8C180D` | UNCHANGED |
| `model_service.py` | `F749FFD0E79A951F42555F5083D2056567DE9CCAAF721772601EA0A79856C877` | UNCHANGED |
| `feature_extractor.py` | `45A9AE59E9822528C1E6D64AC107A121BB7291D7C352BF744E6FC9D06F0569CB` | UNCHANGED |
| `polarization_service.py` | `9F93886080C9D6378C670D6365C17A12FE4DDDAECAE145EEFED34A6718C5D738` | UNCHANGED |
| Harmonic-fit CSV | `0904F151095CBBBE30B2F9CB163E38B6E0B97788627964461C1D707F0A3CEC86` | UNCHANGED |
| Blank-sky baseline CSV | `67CD737FA57545AA75B731121222B53A77F1413774DEA67C91B67FDB5A72E964` | UNCHANGED |
| Fractional-coordinate CSV | `115811A3170B29774F3172093489530E2CBA75A4339CBB0475B535CCD859E28E` | UNCHANGED |
| Deployed-model reproduction CSV | `3E6B88BC77917C07DB7BEF8021B7E3B10741314657A12E654F919D1B2923BAD1` | UNCHANGED |
| Seed-stability summary CSV | `5125A5D60491FF8DA656CFC83A4D995BC380E737A0D65290FE2730C3B4654DF2` | UNCHANGED |

No original notebook, model, matrix, result CSV, report, Draft 1, or application source was edited.

## 3. Prohibited-action check

- Model retraining: **NOT PERFORMED**.
- Original matrix or feature regeneration: **NOT PERFORMED**.
- New scientific experiment or threshold: **NOT PERFORMED**.
- SHAP/LIME implementation: **NOT PERFORMED**.
- Original project recomputation: **NOT PERFORMED**.
- Original artifact overwrite: **NOT PERFORMED**.
- Final PDF generation: **NOT PERFORMED**.
- Scientific figures generated from artificial data: **NO**.

The PCA figure calls only saved scaler/PCA `transform` operations. The figure script contains no `.fit(` call.

## 4. Manuscript lint

| Check | Result |
|---|---|
| Exact fixed title in Markdown and LaTeX | PASS |
| Abstract length | PASS — exactly 200 words |
| Abstract names XPoSat and POLIX | PASS |
| Sections I–X present | PASS |
| Four author/affiliation placeholders retained | PASS |
| Four figures and four main tables present in both formats | PASS |
| Key numerical values/equations agree between formats | PASS |
| Sco X-1 order is peak, weighted mean, entropy | PASS |
| 13-fit blank-sky rule is reduced chi-square \(\le2\) | PASS |
| No imputation method asserted | PASS |
| No SHAP/LIME deployment claim | PASS |
| No calibrated PD/official PA/background-subtraction claim | PASS |
| Notebook/service uncertainty mismatch disclosed | PASS |
| Generic IEEE conference LaTeX; no venue header | PASS |
| Manuscript word count, including tables | Approximately 3,650 |
| Estimated two-column length | Approximately 7–9 pages with four figures and four tables; venue compilation pending |

## 5. Evidence and citation lint

- Final claim ledger carries C001–C041 forward and adds C042–C064.
- Section-to-claim control is recorded.
- All numerical project claims in Draft 2 trace to controlling CSV/code evidence.
- The BibTeX library contains 18 retained entries.
- All 18 entries are cited in both Markdown and LaTeX.
- No citation key is missing from the BibTeX library.
- Every reference has an inspected-source claim map and limitation.
- Current ISSDC wording was rechecked on 2026-07-28; it must be checked again immediately before submission.
- Chandra and XSPEC are not presented as analysed project data.

## 6. Figure lint

| Check | Result |
|---|---|
| SVG and 300-dpi PNG for Figs. 1–4 | PASS |
| Input and output SHA-256 values recorded | PASS |
| PNG dimensions and 300-dpi metadata checked | PASS |
| Axes, labels, legends, candidate identities, and captions inspected | PASS |
| Fixed candidates distinguished in PCA/ranking views | PASS |
| Fig. 4 uses empirical centre/scatter without confidence contour | PASS |
| No fitting, retraining, thresholding, or feature regeneration in plotting code | PASS |

## 7. Learning lint

- Modules 1–18: **COMPLETE**.
- Required teaching sections and five self-tests plus separate answers per module: **PASS**.
- Viva Questions 1–100: **CONTINUOUS AND COMPLETE**.
- Student highlights contain all 25 requested elements, all-section six-part explanations, 20 reviewer questions, two oral scripts, and key equations.
- Student mastery: **NOT ASSESSED**; students must verify and revise every manuscript sentence.

## 8. Remaining approvals and submission blockers

The following prevent submission but do not invalidate guide review:

1. Faculty approval of contribution framing and exact title use.
2. Author order, corresponding author, affiliation, and any institute acknowledgment.
3. IEEE venue and page limit.
4. POLIX-aware approval of feature semantics, candidate interpretation, harmonic terminology, and the 13-fit empirical reference.
5. Final figure/table selection and page compression.
6. Decision on supplement inclusion of PD sensitivity scenarios.
7. Final reference and official-guidance recheck.
8. Venue-specific AI-assisted-writing disclosure.
9. Manual verification and academic rewriting by all authors.
10. Venue-specific LaTeX adaptation and final PDF inspection.

No unresolved evidence contradiction prevents the bounded paper. No new experiment is a submission blocker for the narrow applied case-study framing accepted in this workflow. A venue or reviewer demanding generalization, accuracy, standalone-XAI validation, or calibrated physical inference would require work outside the completed-project scope.

## 9. Final readiness decision

- **Guide-ready:** YES.
- **Domain-approved:** NO — pending POLIX-aware review.
- **Venue-formatted:** NO.
- **Submission-ready:** NO.
- **Issue preventing guide review:** NONE.
- **Issue preventing submission:** Outstanding approvals, venue adaptation, official-guidance recheck, and final human verification; not a contradiction in the frozen central result.
