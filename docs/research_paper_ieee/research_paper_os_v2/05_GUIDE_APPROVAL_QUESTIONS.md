# Guide and Domain-Expert Approval Questions

## Highest priority

1. Is “product-aware 15-feature representation” the correct central contribution, or should the paper be framed primarily as archive-screening systems integration?
2. Are “harmonic coefficients” and “empirical Stokes-like q/u coordinates” safer than calling the fitted quantities \(Q/U\)?
3. Should any PD sensitivity-proxy table remain in the paper, move to a supplement, or be removed?
4. Is fitted modulation phase useful enough to retain when no official sky-PA conversion is verified?
5. Is the 13-fit acceptable blank-sky baseline scientifically defensible as an empirical reference, and should it use mean/standard deviation or robust summaries?

## Feature semantics

6. May channel `>=4000` be associated with a physical high-energy region? If yes, what official calibration file and valid channel range support it?
7. How should the delivered source light-curve RATE features be described under the handbook's quick-diagnosis and scientific-use cautions?
8. Are the 48-anode balance and four-detector summaries comparable across observation dates and known detector changes?
9. Is the non-circular first-difference source-roll statistic acceptable as a screening proxy, or must it be renamed or recomputed in a later authorized phase?
10. Does a `Source` product include any official background treatment relevant to the wording, or must every feature remain source-associated rather than source-only?

## Observation metadata and cases

11. Please confirm the 10/15 role mapping and resolve why two IDs are both labelled “Blank Sky-2” while “Blank Sky-12” is absent.
12. Which representative cases are scientifically appropriate for discussion: Her X-1, Sco X-1, Crab P01_0005, Blank Sky-13, and/or Blank Sky-5?
13. May the three observations stable in all 100 tested seeds be described as a “three-candidate Matrix-C core stable under the tested procedures,” while Blank Sky-5 is described as seed-sensitive? Agent 4 rejects the unqualified phrase “robust core.”

## ML and XAI framing after Agents 4 and 5

14. Is the chosen contamination value 0.16 acceptable as a fixed screening threshold that yields four candidates, given that it is not an estimated anomaly prevalence?
15. Should the paper explicitly discuss the two singleton KMeans clusters, which give zero assigned-centroid distance for Sco X-1 and Blank Sky-13?
16. Is the Matrix-C feature-tier dependence acceptable for the proposed archive-specific methodology framing, especially because Her X-1 is Matrix-C-specific and only Sco X-1 and Blank Sky-13 persist across A/B/C?
17. Should nominal rank-correlation p-values be omitted entirely, given the small reused archive and lack of a pre-specified inferential design?
18. Approve “project-specific, model-informed local feature ranking” in place of unqualified “model-specific feature attribution.”
19. Should the deterministic web sentence replace “mainly because” and “strongest driver” with “highest-ranked under the explanation score” in any later authorized implementation revision?
20. Is the six-case neutralization result sufficient as a supporting sanity check, or should it be moved to supplementary material until matched baselines and explanation-stability tests are available?
21. Should the project-defined Strong/Moderate/Weak labels be retained with their sign-only definitions, renamed, or replaced by direct before/after values?

## Physical-diagnostic framing after Agent 6

22. Approve “fractional harmonic coordinates” and “empirical \(q/u\) diagnostic space,” or specify whether explicitly qualified “Stokes-like” terminology is acceptable.
23. Should the notebook-versus-Flask \(A/C\) uncertainty mismatch be resolved before submission, or is explicit notebook/CSV provenance sufficient for the paper?
24. Should the project-defined reduced-chi-square classes and diagonal-distance categories remain in the main paper, move to the supplement, or be replaced by direct numerical values?
25. Is the bounded non-equivalence discussion scientifically appropriate using Sco X-1, Her X-1, Crab P01_0005, and anomalous blank-sky observations without assigning physical causes?
26. Should the assumed-\(\mu_{100}\) PD sensitivity scenarios be placed only in supplementary material or removed entirely?
27. Does the 13-fit empirical blank-sky reference require observation matching, covariance-aware estimation, or additional blank-sky data before it may support more than a descriptive archive diagnostic?

## Paper strategy

28. Approve or revise the provisional five-contribution framing.
29. Confirm author order and affiliations.
30. Select the IEEE venue and page limit before figure selection or Draft 2.
31. Decide which figures are essential and which results belong only in supplementary material.
32. Confirm the official acknowledgment and any institute-specific acknowledgment requirements immediately before submission.

## Approvals that require a POLIX-aware reviewer

- official product names, axis meanings, units, GTI/exposure treatment, and background status;
- detector/channel comparability across the observation dates;
- use of \(Q/U\), raw modulation, fitted phase, and blank-sky terminology;
- any interpretation connecting a feature driver to instrument or source behavior;
- any comparison with published physical PD/PA results.

## Additional final-candidate decisions

33. Approve the Agent-8 hierarchy of one Moderate primary and three Moderate secondary contributions.
34. Confirm that the exact college project title should remain despite the paper’s narrower archive-screening scope.
35. Confirm whether the paper should target an applied/student IEEE conference where an archive-specific case study is in scope.
36. Approve the term “three-candidate Matrix-C core stable under the tested procedures.”
37. Decide whether the fixed-Normal but 68/100 seed-selected Blank Sky-15 should remain in main-text discussion or only the supplement.
38. Approve omitting uncertainty columns from the main harmonic table while preserving Notebook-11 CSV provenance and the supplement mismatch disclosure.
39. Approve the Fig. 4 empirical centre/scatter display without confidence or detection contours.
40. Confirm whether the limitations/claim-boundaries table should enter the main paper after the page limit is known.
41. Recheck the official ISSDC acknowledgment wording and abstract-identification rule immediately before submission.
42. Approve the venue-specific AI-assisted-writing disclosure after all four authors have manually verified and revised the manuscript.
