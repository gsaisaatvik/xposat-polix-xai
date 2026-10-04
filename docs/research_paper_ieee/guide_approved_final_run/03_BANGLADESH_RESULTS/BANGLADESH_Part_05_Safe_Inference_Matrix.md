# BANGLADESH Part 05 — Safe Inference Matrix and Phase-3 Claim Gate

## Central result story proposed for the paper

The project represents heterogeneous POLIX Level-2 products using a traceable 15-feature observation-level Matrix C. A frozen Isolation Forest model screens the 25-observation project archive and returns four inspection candidates. A deterministic local heuristic maps unusualness back to features and product families. WeightedRoll is excluded from Matrix C and analysed independently through a weighted second harmonic and a selected empirical blank-sky reference. The saved outputs show that archive-relative statistical unusualness and modulation-like harmonic behaviour do not agree one-to-one.

## Claim approval matrix

| ID | Proposed claim | Evidence strength | Safe inference | Excluded extension | Proposed location |
|---|---|---|---|---|---|
| BD-C01 | The archive contains 25 observations: 10 source and 15 blank sky by project mapping. | High | Exact dataset scope | All available POLIX data | Dataset/Results |
| BD-C02 | Matrix C contains 15 features, zero missing values and no WeightedRoll input. | High | Traceable final representation | Complete physical representation | Methods |
| BD-C03 | The fixed model returns 21 Normal and four candidates. | High | Reproducible archive-relative result | Confirmed anomalies or accuracy | Results |
| BD-C04 | Blank Sky-13, Sco X-1 and Her X-1 form a Matrix-C core stable under the tested procedures. | Moderate–High, procedure-qualified | Retrospective persistence | Robust anomalies or future generalization | Results/Discussion |
| BD-C05 | Blank Sky-5 is seed-sensitive. | High within tested seeds | Boundary sensitivity | 29% anomaly probability | Results |
| BD-C06 | Blank Sky-15 is fixed Normal but selected in 68/100 seeds. | High within tested seeds | Competing boundary row | Mislabelled ground truth | Results/Limitations |
| BD-C07 | Only Blank Sky-13 and Sco X-1 persist across A/B/C. | High | Cross-tier persistence | Matrix-C superiority | Results |
| BD-C08 | Sco X-1’s current top three local features are peak channel, weighted mean channel and entropy, with main-paper scores 2.454, 2.207 and 1.814. | High | Exact local ordering under versioned function | Physical or causal mechanism | Results |
| BD-C09 | Five Strong and one Moderate verdict occur in six exploratory neutralization cases. | High for saved check | Bounded in-sample sensitivity | General explanation faithfulness | Results/Limitations |
| BD-C10 | Weighted second-harmonic fits exist for all 25 observations. | High | Complete archive processing | Calibrated polarimetry | Results |
| BD-C11 | Nineteen fits are acceptable, three caution and three poor under declared rules. | High | Project fit-category counts | Statistical significance | Results |
| BD-C12 | Thirteen of 15 blank skies define the empirical reference at reduced chi-square \(\le2\). | High | Selected archive reference | Official background or null distribution | Results |
| BD-C13 | All ten source raw-modulation values are within the declared empirical reference rule. | High | Descriptive scalar comparison | No polarization | Results/Discussion |
| BD-C14 | Sco X-1 is a stable ML candidate with a bounded raw harmonic result. | Moderate–High | Branch non-equivalence example | Physical cause | Discussion |
| BD-C15 | Crab P01_0005 is fixed Normal despite larger raw modulation than several candidates. | High | Harmonic amplitude does not determine ML label | Polarization detection | Discussion |
| BD-C16 | Blank-sky candidates show that screening is not a source/polarization classifier. | Moderate–High | Role-aware diagnostic boundary | Official background anomaly | Discussion |
| BD-C17 | Statistical unusualness and modulation-like harmonic behaviour answer different questions within the project archive. | Moderate–High | Central archive-specific conclusion | Independence theorem or astrophysical discovery | Abstract/Discussion/Conclusion |
| BD-C18 | Notebook-11 CSV controls uncertainty values; the later service uses different propagation. | High | Provenance disclosure | Identical numerical implementations | Limitations/Supplement |

## Exact proposed Results paragraph claims

The following claims are approved for wording review, not yet inserted into a manuscript:

> The frozen Matrix-C configuration labelled 21 of the 25 observations Normal and flagged four as archive-relative anomaly candidates: Blank Sky-13, Sco X-1, Her X-1 and Blank Sky-5. Blank Sky-13, Sco X-1 and Her X-1 were selected under all 100 tested Isolation Forest seeds, all four tested contamination settings and all eligible included-observation jackknife refits. We therefore describe them as a three-candidate Matrix-C core stable under the tested procedures. Blank Sky-5 was selected in 29 of 100 seed runs and is treated as a seed-sensitive boundary case. The fixed-Normal Blank Sky-15 was selected in 68 seed runs, illustrating competition near the contamination-defined threshold.

> Feature-tier comparison addressed a separate question. Blank Sky-13 and Sco X-1 were the only observations flagged using Matrix A, Matrix B and Matrix C. Her X-1 appeared only in Matrix C. This persistence analysis demonstrates dependence on the chosen feature tier and does not establish that Matrix C is superior.

> For Sco X-1, the accepted versioned local-ranking function placed energy peak channel first (2.454), energy weighted mean channel second (2.207) and energy-channel entropy third (1.814). These values order local evidence within the observation and do not identify a physical cause. In the separate six-case perturbation check, joint neutralization of the three highest-ranked features reduced both PCA distance and Isolation Forest score in five cases and one of the two quantities in the sixth.

> Weighted second-harmonic fits were saved for all 25 WeightedRoll curves. Nineteen met the declared acceptable rule, three were caution and three were poor simple-harmonic fits. Thirteen of 15 project-labelled blank-sky fits met reduced chi-square \(\le2\) and formed the empirical reference, with mean raw modulation 1.147820% and sample standard deviation 0.565960%. All ten source raw-modulation values remained within the declared empirical blank-sky reference rule.

## Exact proposed Discussion paragraph claims

> The principal finding is that statistical unusualness and modulation-like harmonic behaviour are non-equivalent within the project archive. Sco X-1 was persistently selected in Matrix-C sensitivity checks, while its raw modulation remained within the declared empirical reference rule. Crab P01_0005 was Normal in the fixed Matrix-C result despite a larger raw-modulation value than several candidates. Blank Sky-13 and Blank Sky-5 were fixed candidates, showing that the screening label is neither a source classification nor a polarization classification.

> The branches answer different questions by construction. Matrix C summarizes exposure, channel-space, source-azimuth, delivered-light-curve and detector-balance products. WeightedRoll is excluded from that input and is fitted separately. Agreement between the outputs is therefore not circularly imposed, but disagreement does not establish statistical independence or a physical explanation.

> Her X-1 illustrates the importance of fit quality. Its reduced chi-square of 57.433514 indicates that the selected second harmonic provides a poor summary of the delivered curve. The corresponding raw modulation and fitted phase must not be interpreted as calibrated polarization quantities or used to infer an astrophysical cause.

> The custom local score improves computational traceability by connecting archive-relative unusualness to explicit features and their product families. Its equal component weighting, within-observation normalization and six-case in-sample perturbation check limit the claim to a project-specific local feature-ranking heuristic rather than causal attribution or generally validated explanation faithfulness.

## Claims rejected from the paper

- Confirmed anomaly, anomaly ground truth or model accuracy.
- Robust anomaly, robust core or future-data generalization.
- Polarization detection, calibrated polarization degree or official sky polarization angle.
- Official background subtraction or a statistically validated blank-sky confidence region.
- Calibrated Stokes parameters; use harmonic-coefficient terminology.
- Causal XAI, SHAP attribution or cross-observation calibrated XAI values.
- Matrix-C superiority or quantitative superiority over alternative models.
- Physical causes for Sco X-1, Her X-1, Crab or blank-sky behaviour.

## Questions for the Phase-3 approval gate

1. Does the guide accept the central wording that the two branches answer different diagnostic questions within the project archive?
2. May the paper retain all five representative cases, or should the main text use Sco X-1, Her X-1 and Crab P01_0005 while moving blank-sky detail to a table?
3. Is “three-candidate Matrix-C core stable under the tested procedures” acceptable, provided the small-sample and retrospective limitations appear alongside it?
4. Should all ten source harmonic rows appear in the main paper, or should the main table be compressed to representative cases with the complete table in supplementary material?
5. Does the guide approve the neutral wording “fractional harmonic coordinates” for \(q=Q/C\) and \(u=U/C\)?

## Phase-3 status

- Results and Discussion claims constructed from approved evidence: Yes.
- Historical draft/report language used as evidence: No.
- New model execution or experiment: No.
- Manuscript drafting begun: No.
- Awaiting guide/student claim approval before Phase 4: Yes.

