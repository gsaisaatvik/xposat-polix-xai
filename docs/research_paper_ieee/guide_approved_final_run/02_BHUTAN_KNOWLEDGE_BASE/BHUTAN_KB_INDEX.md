# BHUTAN Knowledge-Base Index

## Purpose

This Phase-2 knowledge base converts the approved Phase-1 evidence into focused, reusable cards. It is the technical interpretation layer for the next Results and Discussion phase. It does not use old report or manuscript prose as evidence, does not use the 2025 POLIX handbook, and introduces no new experiment or result.

## Central teaching summary

The study maps each of 25 heterogeneous POLIX Level-2 observations to a traceable 15-feature Matrix-C row. Standardization provides a common numerical scale. PCA and KMeans describe two aspects of archive geometry, while Isolation Forest alone sets the fixed label. A deterministic four-component local heuristic then ranks which product-derived features provide the strongest evidence within a single observation; it does not cause or redefine the label.

WeightedRoll is deliberately kept outside Matrix C. Its 360-bin delivered total-count-rate curve is fitted separately with a weighted second harmonic. Thirteen acceptably fitted project-labelled blank skies define a descriptive empirical reference. The saved results show that Matrix-C unusualness and modulation-like harmonic behaviour do not agree one-to-one. This is the main defensible scientific interpretation within the project archive; it is not a polarization detection, calibrated polarimetry result or astrophysical discovery.

## Card routing

| Need | Read this card | Main question answered |
|---|---|---|
| Dataset scope and inputs | [Card 01](BHUTAN_KB_01_Dataset_and_Products.md) | What are the 25 observations and heterogeneous products? |
| Feature formulas | [Card 02](BHUTAN_KB_02_Matrix_C_15_Features.md) | What exactly are the 15 Matrix-C features? |
| Scaling and projection | [Card 03](BHUTAN_KB_03_StandardScaler_and_PCA.md) | What do standardization and the PCA plot mean? |
| Cluster evidence | [Card 04](BHUTAN_KB_04_KMeans.md) | What does KMeans contribute, and why do singletons matter? |
| Fixed label | [Card 05](BHUTAN_KB_05_Isolation_Forest.md) | How are the fixed four candidates produced? |
| Local explanation | [Card 06](BHUTAN_KB_06_Local_XAI_Heuristic.md) | What does the four-component ranking actually measure? |
| Sensitivity evidence | [Card 07](BHUTAN_KB_07_Robustness_Evidence.md) | Which results persist, and under which tested procedures? |
| Harmonic method | [Card 08](BHUTAN_KB_08_WeightedRoll_Harmonic_Fit.md) | How is WeightedRoll fitted and bounded scientifically? |
| Blank-sky comparison | [Card 09](BHUTAN_KB_09_Empirical_Blank_Sky_Reference.md) | How is the 13-fit empirical rule constructed? |
| Case interpretation | [Card 10](BHUTAN_KB_10_Representative_Cases.md) | How do representative observations demonstrate non-equivalence? |
| Claims and future work | [Card 11](BHUTAN_KB_11_Claim_Boundaries_and_Future_Work.md) | What may the paper claim, exclude or defer? |

## Result-set vocabulary that must remain distinct

| Term | Exact membership or meaning |
|---|---|
| Fixed four candidates | Blank Sky-13, Sco X-1, Her X-1 and Blank Sky-5 under the saved Matrix-C model |
| Tested-procedure stable three | Blank Sky-13, Sco X-1 and Her X-1 under the existing seed, contamination and included-observation checks |
| Cross-tier persistent two | Blank Sky-13 and Sco X-1 across Matrix A/B/C |
| Six exploratory XAI cases | Sco X-1, Blank Sky-13, Her X-1, Blank Sky-5, Blank Sky-15 and Blank Sky-6 |

The tested-procedure frequencies are not probabilities, the cross-tier result does not prove Matrix-C superiority, and the six exploratory cases do not replace the fixed four.

## Controlling terminology

- Use **anomaly candidate** or **statistically unusual relative to the project archive**, not confirmed anomaly.
- Use **high-channel fraction**, not high-energy fraction.
- Use **weighted channel spread**, not energy weighted standard channel.
- Use **order-dependent roughness proxy**, not unrestricted circular smoothness.
- Use **delivered-light-curve diagnostic proxy**, not intrinsic source variability.
- Use **project-specific, model-informed local feature-ranking heuristic**, not SHAP or causal attribution.
- Use **cosine/sine second-harmonic coefficients**, **fractional harmonic coordinates**, **raw modulation**, and **fitted modulation phase**.
- Use **within the declared empirical blank-sky reference rule**, not within statistically validated scatter.
- Use **three-candidate Matrix-C core stable under the tested procedures**, not robust anomalies or robust core.

## Frozen values for Phase 3

- Dataset: 25 observations; 10 source; 15 blank sky.
- Matrix C: 15 features; zero missing; no imputation; WeightedRoll excluded.
- Fixed model: 21 Normal and four candidates.
- Sco X-1 main-paper local ranking: peak channel 2.454; weighted mean channel 2.207; channel entropy 1.814.
- Seed results: stable three 100/100; Blank Sky-5 29/100; Blank Sky-15 68/100 but fixed Normal.
- Harmonic fits: 25 total; 19 acceptable, 3 caution, 3 poor.
- Blank-sky reference: 13 of 15 at reduced chi-square \(\le2\).
- Main interpretation: statistical unusualness and modulation-like harmonic behaviour answer different diagnostic questions within the project archive.

## Phase-2 gate status

- Focused cards 01–11: complete.
- Old reports and manuscript drafts consulted as evidence: No.
- 2025 handbook consulted or cited: No.
- New experiment, model fit, parameter change or matrix generation: No.
- Original artifact modified: No.
- Ready for student/guide interpretation confirmation: Yes.
- Phase 3 started: No.

