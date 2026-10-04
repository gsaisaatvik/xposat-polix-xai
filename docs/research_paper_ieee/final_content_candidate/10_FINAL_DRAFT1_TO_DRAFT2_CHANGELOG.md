# Draft 1 to Draft 2 Changelog

**Protected source:** `06_IEEE_Conference_Manuscript_Draft.md` and `07_IEEE_Conference_Manuscript.tex` remain unchanged.  
**Reconstruction authority:** Agent 11 section/paragraph map, Agents 1–10 audits, C001–C064, and controlling machine-readable evidence.

## Global changes

| Draft-1 element | Draft-2 action | Reason |
|---|---|---|
| Working title | REWRITE | Replaced by the exact college project title required by the completion gate. |
| Four-author line | RETAIN AS PLACEHOLDERS | Author order and affiliation await guide approval. |
| Abstract | REWRITE | Exactly 200 words; removes over-detailed faithfulness and physical numbers; states archive size, method, bounded result, and limitations. |
| Five contribution bullets | REWRITE | Reduced to one primary and three secondary Moderate contributions per Agent 8. Robustness, faithfulness, and Flask are supporting evidence. |
| “Feature-attribution score” terminology | REWRITE | Changed to “project-specific, model-informed local feature-ranking heuristic.” |
| \(Q/U\) terminology | REWRITE | Uses harmonic coefficients and fractional harmonic coordinates rather than unqualified Stokes quantities. |
| Broad “polarization-like evidence” statements | REWRITE | Limited to modulation-like harmonic behaviour within the frozen archive. |
| Result precision | REWRITE | Keeps exact values only where necessary; representative physical table uses compressed central values and fit categories. |
| Uncertainty columns | MOVE TO SUPPLEMENT | Notebook 11 and Flask service use different \(A/C\) propagation. |

## Front matter and Section I

| Draft-1 sentence/claim | Draft-2 change |
|---|---|
| Title “Product-Aware Explainable Anomaly Screening…” | Replaced with “An Explainable AI Framework for Analysis of X-Ray Polarimetry Data from XPoSat.” The former phrase is retained only as an internal scope description. |
| Abstract statement of “model-specific explanation score” | Recast as deterministic, project-specific local feature ranking. |
| Abstract faithfulness verdict counts | Removed from abstract and retained in Section V. |
| “All ten source raw-modulation values were within the empirical blank-sky range” | Retained in Results with the exact declared mean \(\pm2\) sample-SD scalar-rule qualification. |
| Five equal contributions | Reorganized into one primary, three secondary, and supporting evidence/implementation. |
| Direct research-gap claim | Narrowed to “limited published work was identified” and explicitly denies priority/superiority. |
| Project history | Added the verified evolution from initial SHAP/LIME consideration to the deployed project-specific method; explicitly states neither was deployed or benchmarked. |

## Section II

| Draft-1 element | Draft-2 change |
|---|---|
| XPoSat/POLIX discussion | Retained with verified official and primary references. |
| Stokes terminology | Qualified so project \(Q,U\) are harmonic coefficients, not calibrated sky Stokes parameters. |
| Astronomy anomaly examples | Retained as motivation only; no transfer of validation claims. |
| SHAP discussion | Retained only as a comparator defining what was not deployed. |
| “Product-aware representation” subsection | Compressed into the scoped gap; removed any implication of multi-view representation learning. |

## Section III

| Draft-1 sentence/table row/claim | Draft-2 change |
|---|---|
| 25 observations, 10 source, 15 blank sky | Retained exactly, with “project mapping” and archive-scope qualification. |
| Target list | Retained in prose; “Cas-A SNR” normalized to “Cassiopeia A” while identifiers remain controlling. |
| Table I | Rewritten to distinguish the 15 blank-sky observations from the 13 qualifying reference fits. |
| “All processed by both branches” | Retained only as frozen-output status, not public-archive completeness. |
| Problem formulation | Rewritten to distinguish archive-relative screening from calibrated polarimetry. |

## Section IV

| Draft-1 sentence/table row/claim | Draft-2 change |
|---|---|
| Matrix A/B/C/WR history | Retained and compressed. |
| Fifteen one-feature table rows | Grouped into five product-family rows while retaining all 15 exact feature names. |
| “Energy-resolved” wording | Replaced where necessary by channel-distribution/channel-space wording. |
| `t1A_energy_high_channel_fraction` | Explicitly called high-channel fraction, not high-energy fraction. |
| `t1B_src_roll_smoothness_norm` | Recast as an order-dependent roughness proxy with exact limitation. |
| Light-curve variability language | Recast as delivered-light-curve diagnostic proxy, not intrinsic variability. |
| Median-imputation narrative | Removed; frozen Matrix C has zero missing values and deployed code has no imputer. |
| Matrix-C rationale | Narrowed from implicit optimization to completed-project choice with tier sensitivity. |

## Section V

| Draft-1 sentence/equation/claim | Draft-2 change |
|---|---|
| Scaler/PCA/KMeans/Isolation Forest description | Retained with saved parameters and clarified component roles. |
| PCA variance percentages | Removed from main paper as unnecessary to the central claim; available in supplement/evidence. |
| KMeans interpretation | Added singleton-cluster limitation and statement that zero centroid distance does not mean ordinary. |
| Four-component equations | Retained with notation cleaned and `IsolationForest.predict` separated from the explanation score. |
| “Model-specific local attribution” | Renamed project-specific local feature ranking; denies label decomposition, causality, Shapley guarantees, and cross-observation calibration. |
| Deterministic sentence | Retained; explicitly not generated by a large language model. |
| Faithfulness verdict | Retained as a six-case in-sample feature-neutralization sanity check; KMeans excluded from verdict. |

## Section VI

| Draft-1 sentence/equation/claim | Draft-2 change |
|---|---|
| WeightedRoll semantics | Retained and strengthened with source-plus-background boundary. |
| \(C+Q\cos2\phi+U\sin2\phi\) | Retained as weighted second-harmonic model. |
| Raw modulation and phase equations | Retained; explicitly not PD or official PA. |
| “13 acceptable” rule | Corrected and retained as reduced chi-square \(\le2\). |
| Blank-sky mean/scatter | Retained as empirical fractional-harmonic reference; diagonal distance limitations added. |
| PD sensitivity scenarios | Removed from main text and made supplement-only if the guide retains them. |
| Uncertainty implementation | Added controlling Notebook-11 CSV provenance and disclosed the later Flask mismatch. |

## Section VII

| Draft-1 sentence/table row/claim | Draft-2 change |
|---|---|
| Separate Experimental Protocol section | Merged into Methodology/Results and supplementary plan to reduce repetition. |
| Audit software version list | Removed from main text; retained in reproducibility/limitations because figure audit loaded artifact under a different version. |
| Matrix-comparison table with PCA variance/silhouette | Moved to supplement. Main text retains only cross-tier candidate persistence. |
| Rank correlations and p-values | Moved to supplement; p-values not used as central validation. |
| Fixed 21 Normal/four candidates | Retained as Results VII-A. |
| “Stable three-case core” | Reworded exactly as “three-candidate Matrix-C core stable under the tested procedures.” |
| Blank Sky-15 boundary behaviour | Added to the seed-sensitivity paragraph to expose the unstable threshold neighbourhood. |
| Contamination and jackknife claims | Weakened to threshold and retrospective influence sensitivity; added Sco X-1 held-out caveat. |
| Table IV candidate rows | Rebuilt as Table III with fixed score, seed frequency, A/B/C persistence, and current local evidence. |
| Sco X-1 order | Corrected to peak channel 2.454499, weighted mean 2.207369, entropy 1.813968. Historical entropy-first wording is superseded. |
| Full ten-source harmonic table | Moved to supplement and replaced by five representative cases. |
| Uncertainty values | Removed from main table because of notebook/service mismatch. |
| Flask implementation subsection | Removed as a Results contribution; retained briefly as supporting implementation in Introduction/Conclusion. |

## Sections VIII–X

| Draft-1 sentence/claim | Draft-2 change |
|---|---|
| Main discussion finding | Retained but bounded to “non-equivalent within the frozen archive.” |
| Sco X-1 discussion | Rewritten using the current versioned feature order and no physical cause. |
| Her X-1 discussion | Added Matrix-C specificity and poor-fit constraint. |
| Crab P01_0005 discussion | Retained as a discordant representative case without polarization interpretation. |
| Blank-sky discussion | Rewritten to compare Blank Sky-13 fit caution with Blank Sky-5 seed sensitivity; no cause assigned. |
| Limitations | Expanded to include same-archive analysis, contamination threshold, tier dependence, singleton KMeans clusters, heuristic XAI, six-case perturbation, selected reference, uncertainty mismatch, unpinned environment, and POLIX-aware review. |
| Conclusion | Rewritten to state only implementation, frozen-archive observations, researcher-triage value, non-claims, and future official-calibration needs. |

## Figures and tables

| Draft-1/planned item | Draft-2 disposition |
|---|---|
| Framework architecture | New paper-specific Fig. 1 generated from author-controlled diagram code. |
| Matrix-C PCA space | New Fig. 2 from frozen Matrix C and saved scaler/PCA transform. |
| Isolation score ranking | New Fig. 3 from saved scores with 100-seed frequency annotations. |
| Source/blank-sky diagnostic space | New Fig. 4 from saved fractional-coordinate CSV and 13-fit reference; no confidence contours. |
| Representative XAI/faithfulness plots | Moved to supplement to fit the main story. |
| Dataset table | Retained and compressed. |
| Fifteen-feature table | Grouped by product family; complete formulas moved to supplement. |
| Matrix A/B/C/WR comparison | Moved to supplement; qualitative persistence retained. |
| Candidate/XAI table | Reconstructed with versioned Sco X-1 order and stability/tier distinctions. |
| Physical results table | Compressed to representative central values and fit classes; full 25 rows moved to supplement. |

## Claims removed rather than rewritten

- Any implication that SHAP or LIME was deployed.
- “Feature attribution” language implying exact Isolation Forest label decomposition.
- “Robust core” without tested-procedure qualification.
- Calibrated-energy, intrinsic-variability, unrestricted circular-smoothness, calibrated Stokes, PD, PA, official-background, detection-region, or astrophysical-cause readings.
- Any inference that contamination equals true anomaly prevalence.
- Any interpretation of rank-correlation p-values as validation.
- Any assertion of novelty, priority, superiority, discovery, confirmed anomaly, or future-observation generalization.
