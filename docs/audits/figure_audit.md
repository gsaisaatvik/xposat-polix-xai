# Scientific Figure Audit — XPoSat/POLIX Explainable Unsupervised Study

## Audit conclusion

The current four figures are individually defensible, but the set has two evidentiary gaps:

1. no main-paper figure shows a delivered POLIX Level-2 measurement before it is reduced to features or harmonic coordinates; and
2. no figure demonstrates the paper's central explainability claim by showing why a specific observation was sent for inspection.

Both gaps can be filled from frozen project artifacts without retraining, refitting, manual data entry, or calibrated-polarization interpretation. Two figures were therefore generated. If page space is constrained, the descriptive PCA plot is the first existing figure to move to the supplement.

## Files and evidence audited

- Application code: `D:\polix_xai_webapp\feature_extractor.py`, `model_service.py`, and `polarization_service.py`.
- Saved model: `D:\polix_xai_webapp\model\polix_v2_matrixC_unsupervised_xai_model.pkl`.
- Notebooks 01–11 under `D:\ISROtrial\Polix_L2_full_archive`; all notebook JSON structures and code cells were scanned, with relevant cell indices recorded in `figure_audit_support\notebook_audit_summary.csv`.
- All 28 CSV files under `final_project_outputs`: six feature-engineering files, nine ML/XAI result files, and thirteen polarimetry-result files. Paths, hashes, dimensions, and columns are recorded in `figure_audit_support\final_outputs_csv_inventory.csv`.
- Matrix A, B, C, and WR files. Each contains 25 observation rows. Matrix C contains the 15 deployed features; WR remains separate.
- All 25 delivered `WeightedRoll_L2.fits` files. Each inspected figure case contains 360 finite rows with `ROLL_AZ_ANG`, `TOTAL_COUNTRATE`, and `ERROR` columns.
- Existing four paper figures, their generation code, figure-source manifest, and captions.
- The canonical manuscript and the reviewed friend-modified manuscript copy, to determine which scientific sentences each figure is intended to support.

The saved PKL contains a 15-feature scaler, a two-component PCA model, KMeans with five clusters, and Isolation Forest with 100 trees, contamination 0.16, and random state 42. No model fitting is performed by the new plotting script.

## Candidate-figure decision table

| Candidate Figure | Available underlying data/code | Exact source file(s) | Scientific question answered | Recommended? YES/NO | Reason | Risk of overclaiming | Suggested paper section | Suggested caption |
|---|---|---|---|---|---|---|---|---|
| Current architecture diagram | Verified method structure and existing author-drawn diagram | `04_SRI_LANKA_FIGURES/figure_generation/generate_phase4_figures.py`; saved PKL; `model_service.py`; `polarization_service.py` | How do the Matrix-C screening, local-ranking, and separate WeightedRoll branches relate? | YES — KEEP | It prevents the common but incorrect reading that PCA, KMeans, and Isolation Forest form a sequential prediction chain. It also shows that only Isolation Forest sets the fixed label. | Calling the branches statistically “independent” would be too strong. Use “separate”; do not imply confidence fusion or calibrated output. | Methodology | “Product-aware screening and separate harmonic-diagnostic architecture. PCA, KMeans, and Isolation Forest receive the standardized Matrix-C representation; only Isolation Forest sets the fixed label. WeightedRoll is excluded from Matrix C and analysed separately.” |
| Current two-dimensional PCA projection | Frozen Matrix C and transform-only use of saved scaler/PCA | `polix_matrix_v2_C_primary_plus_supporting.csv`; saved PKL; `phase4_pca_coordinates.csv` | What does the first-two-component archive geometry look like, and where are the fixed candidates in that projection? | YES — MOVE TO SUPPLEMENT if page-limited | It is correct and useful for descriptive geometry, but it explains only 61.25% of standardized variance and neither sets nor validates the label. It is the least claim-essential current result figure. | Readers may mistake visual separation in two dimensions for validation of candidate status. | Supplementary robustness/geometry | Existing caption is suitable if it continues to state that the view is descriptive and does not determine or validate the label. |
| Current Isolation Forest score ranking with seed counts | Exact saved-model reproduction and 100-seed summary | `deployed_model_reproduction.csv`; `isolation_seed_stability_summary.csv`; verified observation truth table | Which four observations did the frozen model flag, how are all 25 ranked, and which memberships are seed-sensitive? | YES — KEEP | This is the primary deployed ML result and visibly distinguishes the fixed four from selection frequency under the tested seeds. | Seed counts must not be called probabilities, confidence, or anomaly truth. The four-candidate count is contamination-defined. | Results: fixed screening and stability | Existing caption is scientifically bounded and should be retained. |
| Current fractional harmonic-coordinate plot | Saved `q=Q/C`, `u=U/C`, fit-quality membership, and candidate labels | `path2_all_observations_fractional_qu_vectors.csv`; `deployed_model_reproduction.csv`; `phase4_harmonic_plot_data.csv` | Do Matrix-C candidate labels and fractional second-harmonic coordinates agree one-to-one, and where is the selected 13-fit blank-sky reference? | YES — KEEP | It supports the central non-equivalence discussion and shows sources, selected/excluded blank skies, and fixed candidates together. | `q/u` must remain fractional harmonic coordinates, not calibrated Stokes parameters. The cross is not a confidence or detection region. | Results: harmonic/blank-sky comparison | Existing caption is suitable if it states that the cross is component-wise sample mean ± sample SD, not a confidence or detection contour. |
| **New Fig. A: representative delivered WeightedRoll curves and saved fits** | Three raw 360-row FITS tables, supplied errors, saved `C,Q,U`, fixed labels, and saved reduced chi-square values | Three `WeightedRoll_L2.fits` files for Sco X-1, Crab P01_0005, and Her X-1; `polix_weightedroll_raw_modulation_fits.csv`; `deployed_model_reproduction.csv` | What does a delivered POLIX product look like before summary, and is Her X-1's poor second-harmonic fit visually evident relative to useful comparison cases? | **YES — ADD** | This is the missing near-original measurement figure. Sco X-1 shows a stable candidate with a caution-category fit; Crab P01_0005 shows a fixed-Normal source with an acceptable fit and larger raw modulation; Her X-1 makes the severe model inadequacy visible. The lower residual panels prevent a smooth fitted line from hiding lack of fit. | Count rate is delivered and not verified background-subtracted. The orange curve is a descriptive saved harmonic fit. It is not a polarization model, PD estimate, PA curve, or detection. Reduced-chi-square categories are project-defined. | Independent harmonic diagnostic / Results | “Delivered 360-bin WeightedRoll total-count-rate curves with supplied uncertainties and the saved weighted second-harmonic summaries for (a) Sco X-1, a fixed candidate with a caution-category fit; (b) Crab P01_0005, fixed Normal with an acceptable fit; and (c) Her X-1, a fixed candidate for which the simple second harmonic is inadequate. Lower panels show residuals divided by supplied errors. These are raw delivered and harmonic diagnostics, not calibrated polarization measurements.” |
| **New Fig. B: archive-relative explanation of Sco X-1** | Matrix C, saved scaler, exact deployed-function XAI CSV, and product-family mapping | `polix_matrix_v2_C_primary_plus_supporting.csv`; saved PKL; `deployed_xai_exact_from_model_service.csv`; `model_service.py` | Why did the framework ask the researcher to inspect Sco X-1, and how do feature deviation and explanation score differ? | **YES — ADD** | It directly demonstrates the paper's XAI contribution. Panel (a) shows the 25-row standardized archive distribution and Sco X-1's actual position. Panel (b) separately shows the heuristic ranking. The three accepted top features all trace to the EnergyRes product family. | The score is ordinal and within-observation. It is not probability, causal attribution, SHAP, physical effect size, or evidence that the energy product contains a physical anomaly. | Explainable methodology / Local explanations in Results | “Archive-relative local explanation for Sco X-1. (a) Standardized values of the three leading Matrix-C features across all 25 observations; the diamond marks Sco X-1 and the dashed line is the archive mean after scaling. (b) Exact project-specific local-ranking scores from the versioned deployed function. All three features originate from the Tier-1A EnergyRes product family. Scores rank local evidence and are not probabilities, causal effects, or physical interpretations.” |
| Raw energy-channel spectrum for Sco X-1 | Energy-resolved Level-2 FITS product and extraction code exist | `EnergyRes_Src_Azimuth_Roll_L2.fits`; `feature_extractor.py`; Notebook 08 | What channel-space distribution produced the peak, weighted mean, and entropy summaries? | NO for the current main paper | It could be useful supplementary evidence, but it would consume space while the new XAI case figure already displays the archive context of these features. A raw spectrum would also require more careful discussion of dimensional reduction and instrument channel semantics. | High risk of calling channel index calibrated energy or treating raw count structure as a physical spectrum. | Optional supplement only | If ever retained: “Collapsed channel-count distribution used only to derive channel-space summaries; channel index is not calibrated photon energy in this study.” |

## Evaluation of the current four figures

### 1. Architecture diagram — KEEP

**Sentence made stronger:** the two diagnostic branches are deliberately separated, and only Isolation Forest determines the fixed candidate label.

The diagram carries methodological information that would otherwise require several paragraphs. It should use “separate harmonic branch,” not “statistically independent branch.”

### 2. PCA projection — MOVE TO SUPPLEMENT under a page limit

**Sentence made stronger:** the first two components provide a partial, descriptive view of the 25-row Matrix-C geometry.

It is reproducible and honest but not decisive. It does not establish anomaly status, and it is less important than direct evidence of XAI behaviour or the delivered WeightedRoll measurement.

### 3. Isolation Forest ranking — KEEP

**Sentence made stronger:** the frozen configuration produces exactly four candidates, with three selected in all tested seeds and Blank Sky-5 showing seed sensitivity.

This is the strongest result figure because it reports the deployed label source and the procedure-qualified stability result without conflating them.

### 4. Fractional harmonic-coordinate plot — KEEP

**Sentence made stronger:** statistical unusualness in Matrix C and raw second-harmonic coordinates do not agree one-to-one within the archive.

This plot should not be asked to show the original curve or fit quality by itself. The proposed WeightedRoll figure supplies that missing evidence.

## Representative WeightedRoll case selection

Four types of case were evaluated: Sco X-1, Her X-1, Crab P01_0005, and acceptable-fit blank skies. The strongest three-panel scientific story is:

1. **Sco X-1:** fixed candidate; selected in all 100 tested seeds; raw modulation 1.139578%; reduced chi-square 2.030761, project category “caution.”
2. **Crab P01_0005:** fixed Normal; selected in 3/100 seeds; raw modulation 1.697346%, larger than Sco X-1 and Her X-1; reduced chi-square 1.062540, project category “acceptable.”
3. **Her X-1:** fixed candidate; selected in all 100 tested seeds; raw modulation 0.596632%; reduced chi-square 57.433514, making failure of the simple harmonic summary directly visible.

An acceptable blank sky was reproducible—for example `C24_0008` has reduced chi-square 0.681650—but was not selected for the three-panel main figure. The existing all-observation harmonic-coordinate figure already displays the 13-fit blank-sky reference. Replacing Crab with a blank sky would weaken the visually demonstrable candidate-versus-raw-modulation non-equivalence result.

## XAI figure assessment

The XAI figure adds information not present in the score ranking, PCA projection, or harmonic plot:

- feature values and explanation scores are displayed in separate panels;
- all 25 standardized archive values are shown rather than only a generic importance bar;
- Sco X-1 is visibly extreme in opposite directions across the three accepted features;
- raw feature values are annotated;
- product-family provenance is stated;
- the heuristic score is explicitly separated from physical interpretation.

The figure does not show a probability or a causal decomposition. A perturbation-reduction inset was rejected because it would compress a six-case, joint-top-three, sign-based sanity check into a visually stronger claim than the evidence supports. Those values remain better suited to a supplementary table.

## Direct-product overclaim controls

The following wording controls apply to all retained or proposed figures:

- use **channel index**, **peak channel**, and **weighted mean channel**, not calibrated photon energy;
- use **delivered total count rate** and **supplied error** for WeightedRoll axes;
- use **raw modulation** only for `100*sqrt(Q^2+U^2)/C`, never polarization degree;
- use **fitted modulation phase**, never official polarization angle;
- use **fractional cosine/sine harmonic coordinates**, not unqualified calibrated Stokes parameters;
- do not call delivered-light-curve diagnostics intrinsic source variability;
- do not label any curve or coordinate as background-subtracted;
- use **candidate** or **inspection priority**, not confirmed anomaly;
- use **separate branch**, not statistical independence.

## Generated files and numerical verification

### New publication-quality figures

- `D:\polix_xai_webapp\figure_audit_figures\FigA_representative_weightedroll_fits.png`
- `D:\polix_xai_webapp\figure_audit_figures\FigA_representative_weightedroll_fits.pdf`
- `D:\polix_xai_webapp\figure_audit_figures\FigA_representative_weightedroll_fits.svg`
- `D:\polix_xai_webapp\figure_audit_figures\FigB_sco_x1_archive_relative_xai.png`
- `D:\polix_xai_webapp\figure_audit_figures\FigB_sco_x1_archive_relative_xai.pdf`
- `D:\polix_xai_webapp\figure_audit_figures\FigB_sco_x1_archive_relative_xai.svg`

### Verification and provenance

- `figure_audit_support\weightedroll_figure_verification.csv` records the exact FITS file and SHA-256 for each case, all saved coefficients, the 360 plotted rows, stored reduced chi-square, and direct reduced chi-square reconstructed from the FITS values and saved coefficients.
- `figure_audit_support\xai_figure_verification.csv` records each plotted raw value, saved-scaler standardized value, exact deployed XAI score, and product family.
- `figure_audit_support\figure_provenance.csv` records SHA-256 hashes for every figure source and output.
- `figure_audit_support\generate_audit_figures.py` contains no model `.fit()` call. It reads the raw FITS rows, evaluates the already-saved harmonic coefficients, transforms Matrix C with the saved scaler, and plots the accepted deployed XAI values.

Direct reconstruction checks passed:

| Case | Stored reduced chi-square | Direct value from 360 FITS rows and saved coefficients |
|---|---:|---:|
| Sco X-1 | 2.0307608047722137 | 2.0307608047722128 |
| Crab P01_0005 | 1.0625397079395509 | 1.0625397079395507 |
| Her X-1 | 57.43351375364045 | 57.43351375364045 |

The three Sco X-1 standardized values reproduced the exact deployed XAI CSV values to numerical precision: +4.894106 for peak channel, -3.432505 for weighted mean channel, and -2.855662 for channel entropy. The plotted ranking scores are 2.454499, 2.207369, and 1.813968, displayed to three decimals in the figure.

## Page-priority ranking

If the venue imposes a strict limit, allocate main-paper space in this order:

1. Isolation Forest ranking and seed annotation — primary fixed ML result.
2. Sco X-1 archive-relative XAI case — evidence for the explainability contribution.
3. Representative WeightedRoll curves/fits — delivered-product evidence and visible fit adequacy.
4. Fractional harmonic-coordinate plot — empirical blank-sky/non-equivalence context.
5. Architecture diagram — compact method explanation.
6. PCA projection — descriptive and first to move to the supplement.

## Final recommendation

**D. Add both, and move the two-dimensional PCA projection to the supplement to control paper length.**

This recommendation is evidence-based: the new WeightedRoll figure adds the missing original/near-original Level-2 measurement, and the new Sco X-1 figure visibly demonstrates the XAI contribution. The PCA projection is valid but carries the least indispensable main-paper claim.
