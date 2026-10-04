# Final Guide Decision Sheet

**Fixed title:** *An Explainable AI Framework for Analysis of X-Ray Polarimetry Data from XPoSat*

## Decisions requested

| # | Decision | Recommended default | Approval |
|---:|---|---|---|
| 1 | Primary contribution | Traceable, product-aware XAI framework for screening POLIX Level-2 observations within the project archive | [ ] Approve [ ] Revise |
| 2 | Secondary contributions | 15-feature provenance; project-specific local ranking; separate harmonic/blank-sky branch | [ ] Approve [ ] Revise |
| 3 | Paper type | Applied scientific-computing/archive case study, not a general anomaly-method paper | [ ] Approve [ ] Revise |
| 4 | Author order and corresponding author | To be supplied by the guide and four authors | [ ] Complete |
| 5 | Affiliations and email addresses | Replace all placeholders before submission | [ ] Complete |
| 6 | Venue and page limit | Select before final compression or PDF generation | [ ] Complete |
| 7 | Main figures | Retain framework, PCA, ranking/stability, and fractional-harmonic space | [ ] Approve [ ] Revise |
| 8 | Main tables | Retain Tables I–IV; Table V only if page space permits | [ ] Approve [ ] Revise |
| 9 | Matrix-C terminology | Approve product-aware early-fusion wording without implying multi-view learning | [ ] Approve [ ] Revise |
| 10 | Feature proxy terminology | Approve high-channel, order-dependent roughness, delivered-light-curve, and detector-balance wording | [ ] Approve [ ] Domain review |
| 11 | Stability wording | “Three-candidate Matrix-C core stable under the tested procedures” | [ ] Approve [ ] Revise |
| 12 | XAI terminology | “Project-specific, model-informed local feature ranking” | [ ] Approve [ ] Revise |
| 13 | Six-case sanity check | Keep as supporting evidence; move detailed values to supplement | [ ] Approve [ ] Remove |
| 14 | Harmonic terminology | Harmonic coefficients/fractional harmonic coordinates; no calibrated Stokes claim | [ ] Approve [ ] Domain review |
| 15 | Blank-sky treatment | Descriptive 13-fit empirical archive reference only | [ ] Approve [ ] Domain review |
| 16 | Representative cases | Sco X-1, Her X-1, Crab P01_0005, Blank Sky-13/5 | [ ] Approve [ ] Revise |
| 17 | PD sensitivity scenarios | Omit by default; supplement only if explicitly requested | [ ] Omit [ ] Supplement |
| 18 | Fitted phase | Retain as an implementation definition only or omit for space | [ ] Retain [ ] Omit |
| 19 | Uncertainty mismatch | Report notebook/CSV provenance; place formula comparison in supplement | [ ] Approve [ ] Require reconciliation |
| 20 | AI disclosure | Adapt the supplied disclosure to the chosen venue | [ ] Approve [ ] Revise |

## Domain-review checklist

- Product names, axes, units, and release-specific meaning.
- Source/blank-sky project role mapping and duplicated friendly-label issue.
- Scientific suitability of all 15 features as screening proxies.
- Channel-space comparability and channel-4000 boundary.
- Light-curve and detector-product use.
- Harmonic notation, fit-quality rules, and blank-sky reference construction.
- Captions and discussion of representative observations.

## Submission blockers not requiring new experiments

- Author order and affiliations.
- Venue and page limit.
- Guide approval of contribution framing.
- POLIX-aware review of marked terminology.
- Final human citation, number, and prose verification.
- Venue-specific AI-use disclosure and final acknowledgment check.
