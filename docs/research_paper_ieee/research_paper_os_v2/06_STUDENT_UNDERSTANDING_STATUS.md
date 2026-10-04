# Student Understanding Status

**Completed teaching scope:** Modules 1-18.

## Competency status

| Competency | Learning evidence | Status |
|---|---|---|
| Explain why X-ray astronomy requires space instruments | Module 1 and self-test | TAUGHT; STUDENT SELF-CHECK REQUIRED |
| Separate counts, rate, channel, energy, spectrum, and calibration | Module 1 | TAUGHT; STUDENT SELF-CHECK REQUIRED |
| Explain linear polarization and two-fold azimuthal modulation | Module 2 | TAUGHT; STUDENT SELF-CHECK REQUIRED |
| Distinguish raw modulation, PD, fitted phase, and PA | Module 2 | TAUGHT; STUDENT SELF-CHECK REQUIRED |
| State separate roles/bands of POLIX and XSPECT | Module 3 | TAUGHT; STUDENT SELF-CHECK REQUIRED |
| Explain that the project uses POLIX only and a fixed 25-observation archive | Module 3 | TAUGHT; STUDENT SELF-CHECK REQUIRED |
| Name and distinguish relevant POLIX Level-2 product families | Module 4 | TAUGHT; STUDENT SELF-CHECK REQUIRED |
| State WeightedRoll source-plus-background and release limitations | Module 4 | TAUGHT; STUDENT SELF-CHECK REQUIRED |
| Defend all 15 features and their semantic boundaries | Module 6 | TAUGHT; STUDENT SELF-CHECK REQUIRED |
| Defend PCA/KMeans/Isolation Forest | Modules 7-9 | TAUGHT; STUDENT SELF-CHECK REQUIRED |
| Defend XAI and faithfulness | Modules 10-11 | TAUGHT; STUDENT SELF-CHECK REQUIRED |
| Defend physical fits and empirical baseline | Modules 12-13 | TAUGHT; STUDENT SELF-CHECK REQUIRED |
| Explain the Agent-4 robustness boundaries | Agent 4 audit plus Modules 7-9 | AUDIT INTEGRATED; STUDENT SELF-CHECK REQUIRED |
| Explain the Agent-5 XAI claim boundaries | Agent 5 audit plus Modules 10-11 | AUDIT INTEGRATED; STUDENT SELF-CHECK REQUIRED |
| Explain the Agent-6 physical-diagnostic boundaries | Agent 6 audit plus Modules 12-13 | AUDIT INTEGRATED; STUDENT SELF-CHECK REQUIRED |
| Distinguish all result sets and threshold-neighborhood cases | Module 14 | TAUGHT; STUDENT SELF-CHECK REQUIRED |
| Defend the Moderate primary and secondary contributions | Module 15 and Agent 8 | AUDIT INTEGRATED; STUDENT SELF-CHECK REQUIRED |
| Explain every major threat to validity and safe claim boundary | Module 16 and Agent 9 | AUDIT INTEGRATED; STUDENT SELF-CHECK REQUIRED |
| Map evidence correctly into an IEEE conference-paper structure | Module 17 | TAUGHT; STUDENT SELF-CHECK REQUIRED |
| Answer hostile viva and reviewer questions without overclaiming | Module 18 and Viva Questions 71-100 | TAUGHT; STUDENT SELF-CHECK REQUIRED |

## Required student demonstration before final manuscript synthesis is used

Without reading the answers, the student should explain aloud:

1. why channel is not keV;
2. why a two-fold curve appears in linear polarimetry;
3. why raw modulation is not PD;
4. why fitted phase is not official PA;
5. why POLIX and XSPECT cannot be conflated;
6. what WeightedRoll contains;
7. why Matrix C excludes WeightedRoll;
8. why an anomaly candidate is not a physical discovery.
9. all fifteen feature formulas and the difference between a verified calculation and a calibrated physical quantity;
10. why PCA distance, KMeans centroid distance, and Isolation Forest score answer different geometric questions;
11. why contamination fixes a decision boundary and does not estimate anomaly prevalence;
12. why 100/100 seed stability is not anomaly probability;
13. all four XAI components and their per-observation normalization;
14. the exact Strong/Moderate faithfulness rules and at least three limitations;
15. the weighted harmonic model, raw-modulation formula, and fit-quality thresholds;
16. why the thirteen-fit blank-sky reference is descriptive and archive-specific; and
17. the safe meaning of statistical/physical non-equivalence;
18. why the fixed four, the three-candidate Matrix-C procedure-stability core, and the two cross-tier persistent candidates are different statements;
19. why the contamination check varies a threshold over one score ordering rather than independently replicating the result;
20. why included-observation jackknife persistence is not held-out or future-data validation;
21. why singleton KMeans clusters make zero centroid distance ambiguous;
22. why the deployed label comes only from Isolation Forest although the explanation score has four components;
23. why the combined explanation scores are only within-observation rankings; and
24. why five Strong and one Moderate verdict do not establish general faithfulness;
25. why the frozen notebook and current Flask service must not be said to use one identical \(A/C\) uncertainty formula;
26. why reduced-chi-square classes and vector-distance cutoffs are project rules rather than p-values or detection thresholds; and
27. why Crab P01_0005, Sco X-1, Her X-1, and anomalous blank skies support only archive-bounded non-equivalence.
28. the exact identities and roles of the fixed four, Matrix-C tested-procedure three, cross-tier pair, seed-sensitive Blank Sky-5, and competing `C24_0020`;
29. why the six exploratory XAI cases are not a second deployed candidate result;
30. Agent 8's primary contribution and three secondary contributions, including their Moderate rating;
31. why established algorithms, supplementary robustness checks, the perturbation test, and Flask interface are not separate major contributions;
32. the difference between “limited directly comparable published work was identified” and a priority claim;
33. Agent 9's Weak Reject reasoning and its conditional path to Weak Accept;
34. why no new experiment is mandatory only under the narrow archive-bounded case-study framing;
35. which broader claims would make external validation, expert benchmarks, or official calibration essential;
36. how each manuscript section differs in purpose, especially Results versus Discussion;
37. the safe six-step pattern for a hostile reviewer response; and
38. every remaining guide, domain, authorship, venue, figure, reference, and AI-disclosure decision before submission.

## Human-development record for the complete learning scope

Each of Modules 1-18 includes:

- what the paper may say;
- what it means in simple language;
- how the project implemented the relevant idea;
- what evidence supports it;
- a likely reviewer question;
- a student-safe answer; and
- what must not be claimed.

## Viva material status

- Questions 1-20: created with answers for Modules 1-4.
- Questions 21-70: created with answers for Modules 5-13.
- Questions 71-100: created with answers for Modules 14-18 and Agents 8-9.
- Full viva readiness: **NOT YET ASSESSED.**

## Specialist synthesis integrated

- Agent 8: one Moderate primary contribution and three Moderate secondary contributions; no Strong contribution and no priority or superiority claim.
- Agent 9: current Weak Reject for a broad methodology reading, with a plausible Weak Accept at a suitable applied or student venue after bounded reconstruction and guide/domain review.
- Agent 9 found no fatal numerical contradiction for the central archive-screening result and required no new experiment for the explicitly narrow case-study framing.
- Any broader generalization, accuracy, standalone-XAI, or calibrated-physical claim would require evidence outside the accepted completed-project workflow and must therefore remain excluded or future work.

## Honest current conclusion

The learning material now covers the scientific context, data, features, deployed ML, custom XAI, faithfulness test, harmonic fitting, blank-sky comparison, exact result-set distinctions, contribution framing, limitations, IEEE paper logic, and hostile-review defense. The cautions from Agents 4-9 have been integrated. This completion records teaching material, not student mastery. Mastery requires answering all self-tests and viva questions without notes, deriving the key equations, distinguishing every candidate/result set, explaining every claim boundary in the student's own words, and accepting guide or POLIX-aware correction where the audits identify ambiguity.

## Final student package

`final_content_candidate/13_RESEARCH_PAPER_HIGHLIGHTS_FOR_STUDENT.md` now supplies all 25 requested learning elements: a plain-language story, project evolution, all 15 features, ML/XAI/harmonic explanations, fixed and tested-procedure results, contribution/non-claim boundaries, all limitations, a six-part explanation of Sections I–X, 20 reviewer questions with answers, ten-minute and two-minute scripts, and equations/terms.

Modules 1–18 and Viva Questions 1–100 are complete. Student mastery remains **NOT ASSESSED** until the students can answer without notes and revise the manuscript in their own academic voice.
