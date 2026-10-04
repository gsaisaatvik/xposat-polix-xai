# Final Figure and Table Plan

**Status:** Guide-review candidate; final venue and page limit remain unknown.  
**Scientific rule:** All plotted numerical values come from frozen project artifacts. No estimator was fitted and no scientific result was recomputed.

## Main-paper figures

| Figure | File | Purpose | Controlling source | Caption boundary | Page priority |
|---|---|---|---|---|---|
| Fig. 1 | `figures/fig1_framework_flow.*` | Show the two deliberately separate branches | Matrix-C schema, deployed service architecture, WeightedRoll exclusion | Architecture diagram, not an experimental result | Essential |
| Fig. 2 | `figures/fig2_matrix_c_pca.*` | Show the frozen two-component Matrix-C projection and four fixed candidates | Frozen Matrix C and saved scaler/PCA transform | PC1+PC2 contain 61.25% of standardized variance; separation is descriptive | Essential |
| Fig. 3 | `figures/fig3_fixed_candidate_ranking.*` | Show all 25 frozen Isolation Forest scores with seed frequencies for the fixed four | `deployed_model_reproduction.csv`; `isolation_seed_stability_summary.csv` | Frequencies are tested-procedure stability, not anomaly probabilities | Essential |
| Fig. 4 | `figures/fig4_fractional_harmonic_space.*` | Compare source and blank-sky fractional harmonic coordinates | Fractional-coordinate CSV and frozen polarimetry configuration | Error bars are axis-wise sample scatter of the selected 13-fit reference, not confidence limits | Essential |

Each figure is supplied as SVG and 300-dpi PNG. Source paths and SHA-256 values are recorded in `figure_generation/figure_source_manifest.csv`.

## Main-paper tables

| Table | Contents | Main evidence | Placement decision |
|---|---|---|---|
| I | Archive composition and Level-2 product families | Role metadata, archive IDs, handbook | Main paper |
| II | Matrix-C product families and 15 feature names | Matrix-C header, Notebook 08, Agent 3 | Main paper; formulas move to supplement |
| III | Fixed candidates, anomaly scores, 100-seed frequency, cross-tier persistence, and leading local evidence | Deployed reproduction, seed summary, matrix ablation, XAI audit | Main paper |
| IV | Empirical blank-sky summary and representative source/blank-sky cases | Harmonic fits, blank-sky baseline, fractional-coordinate CSV | Main paper; central values and fit class only |
| V | Limitations and claim boundaries | Agents 3–9 and final ledger | Keep only if venue space permits |

## Caption wording

- Use “archive-relative anomaly candidate,” not “confirmed anomaly.”
- Use “frozen PCA transform,” not a validation embedding.
- Use “fractional harmonic coordinates” and “raw modulation,” not calibrated Stokes parameters or polarization degree.
- Use “13-fit empirical blank-sky reference,” not official background subtraction.
- State that fixed candidates, seed-stable candidates, cross-tier persistence, and six exploratory XAI cases are different sets.

## Supplement-only material

- Complete feature formulas and edge cases.
- Full seed, contamination, jackknife, matrix-ablation, and ranking-agreement tables.
- Detailed six-case feature-neutralization values.
- All 25 harmonic-fit rows and coefficient uncertainties.
- Notebook-versus-Flask uncertainty implementation comparison.
- Assumed-\(\mu_{100}\) sensitivity scenarios, only if the guide retains them.

## Venue decision

For an eight-page limit, retain Figs. 1–4 and Tables I–IV; omit Table V and place all detailed formulas/results in supplementary material. Any stricter limit requires guide selection before deletion or merging.
