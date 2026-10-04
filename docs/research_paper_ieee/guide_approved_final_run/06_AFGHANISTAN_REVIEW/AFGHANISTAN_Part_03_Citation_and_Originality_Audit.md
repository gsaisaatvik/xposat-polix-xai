# AFGHANISTAN Part 03 — Citation and Originality Audit

## Verdict

**PASS with normal pre-submission follow-up.** The Phase-5 manuscript cites 17 retained sources, and the BibTeX file contains the same 17 keys with no uncited entry. The excluded 2025 handbook does not appear in the manuscript or BibTeX. No citation is used as evidence for a project-specific numerical result.

## Reference-set audit

| Reference role | Retained sources | Audit result |
|---|---:|---|
| Official mission/archive/acknowledgment context | 3 | Retained for bounded official context only |
| POLIX/X-ray polarimetry foundations | 3 | Retained; not used to validate project-specific features or calibration |
| Astronomy anomaly screening | 3 | Retained for motivation and positioning, not as quantitative baselines |
| Explainable anomaly detection and perturbation evaluation | 3 | Retained with method-boundary language |
| Unsupervised-outlier evaluation | 1 | Retained for limitations of label-free evaluation |
| PCA, KMeans, Isolation Forest, and scikit-learn | 4 | Retained for algorithm/software provenance |
| Total | 17 | Citation keys and BibTeX keys match one-to-one |

The reference identity, claim, full-text or authoritative-page status, and limitation are recorded in `research_paper_os_v2/literature/Verified_Reference_Library.md` and `Reference_Claim_Map.csv`. The Phase-5 claim ledger narrows each citation to a specific manuscript claim.

## Citation-to-claim findings

- Mission and payload statements cite the official ISRO mission page.
- Instrument geometry and general polarimetry statements cite instrument-development or peer-reviewed polarimetry sources.
- Project dataset size, feature definitions, model parameters, XAI ordering, stability, and harmonic values cite no literature as proof; they are controlled by local artifacts.
- SHAP appears only as a Related Work comparator and is explicitly not deployed.
- The perturbation paper supports the general evaluation motivation; the manuscript explicitly states that it does not reproduce the published metric or inherit its guarantees.
- The literature-gap paragraph uses “limited published work was identified” and explicitly rejects priority, novelty, and superiority claims.
- The prescribed acknowledgment appears as a separate exact sentence, with the webpage citation placed in the preceding sentence.

## Originality and close-paraphrase review

The manuscript was written as an original account of the implemented study rather than by copying another paper’s structure or prose. Most Results, Methods, Discussion, and Limitations text is project-specific and linked to the project artifacts.

Three distinctive Related Work and gap sentences were searched as exact phrases on 2026-08-03. No meaningful exact match to a published source was identified. This is a screening check, not a plagiarism certificate. A final institutional similarity check should still be run after the four authors revise the prose in their own academic voice.

The exact official acknowledgment is intentionally reproduced because the data-use page prescribes that wording. It should not be paraphrased.

## Risks and required follow-up

1. Recheck URLs, access dates, and official acknowledgment wording immediately before submission.
2. Confirm that every reference remains necessary after venue-driven page compression.
3. Run the institution’s approved similarity checker on the final human-revised manuscript.
4. Ensure the authors can explain each literature statement and have inspected the cited source or authoritative page.
5. Do not introduce references solely to increase citation count.

## References requiring follow-up

No current BibTeX entry is unresolved. All 17 should nevertheless receive a final metadata and access-date check immediately before submission.

