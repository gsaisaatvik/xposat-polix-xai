# Figure and Table Manifest

No figure has been inserted into the manuscript draft. This manifest must be reviewed after the venue and page limit are selected.

## Recommended compact figure set

| Figure | Purpose | Primary source | Status | Page-limit decision |
|---|---|---|---|---|
| Fig. 1 | End-to-end architecture and independence of ML/physical branches | Code architecture and manuscript methods | AUTHOR-DRAWN VECTOR DIAGRAM REQUIRED | Keep if space permits |
| Fig. 2 | Product families, Matrix A/B/C construction, and WR exclusion | Matrix definitions and feature CSVs | AUTHOR-DRAWN VECTOR DIAGRAM REQUIRED | Merge with Fig. 1 for ≤8 pages |
| Fig. 3 | Matrix-C PCA observation space | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\05_figures\v2_plots\pca_scatter_C_primary_plus_supporting.png` | EXISTING REAL PROJECT FIGURE; labels require review | Keep |
| Fig. 4 | Deployed Isolation Forest score ranking and seed-frequency annotation | `supplementary_experiments/deployed_model_reproduction.csv`; `isolation_seed_stability_summary.csv` | PAPER-SPECIFIC REGENERATION REQUIRED | Keep; replaces exploratory consensus plot |
| Fig. 5 | Representative deployed XAI explanations (Her X-1, Sco X-1, two blank skies) | `supplementary_experiments/deployed_xai_reproduction.csv` | PAPER-SPECIFIC REGENERATION REQUIRED | Optional composite |
| Fig. 6 | Faithfulness reductions and verdicts | original/reproduced faithfulness CSVs | PAPER-SPECIFIC REGENERATION REQUIRED | Optional; table may suffice |
| Fig. 7 | Representative WeightedRoll fit | `...\05_figures\polarization_modulation_fits\X01_PLX_P01_0005_000000_weightedroll_modulation_fit.png` | EXISTING REAL PROJECT FIGURE | Keep only with raw-diagnostic caption |
| Fig. 8 | Source and blank-sky normalized Q/U space | `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\05_figures\path2_source_blank_vector_plots\blank_sky_source_qu_vector_space.png` | EXISTING REAL PROJECT FIGURE; baseline ellipse/status requires verification | Keep |

## Existing figures not suitable without qualification

| File | Reason |
|---|---|
| `v2_consensus_anomaly_ranking.png` | Represents exploratory multi-matrix consensus, not the deployed four-candidate model |
| `v2_anomaly_evidence_by_method.png` | Exploratory evidence; can be supplementary but should not headline deployed results |
| `pca_scatter_WR_weightedroll_diagnostic.png` | WR is a separate physical diagnostic and must not be presented as primary anomaly confirmation |
| `raw_modulation_percent_ranking.png` | Raw modulation alone is not calibrated polarization |
| `modulation_phase_vs_percent.png` | Fitted phase is not official sky PA |
| PD-proxy plots | Assumed \(\mu_{100}\) sensitivity only; likely omit from conference paper |

## Recommended tables

| Table | Contents | Evidence | Status |
|---|---|---|---|
| Table I | Dataset composition | role table | Drafted |
| Table II | Product families and Matrix-C features | matrix CSV + extractor + handbook | Drafted |
| Table III | Matrix A/B/C and separate WR comparison | ablation CSV | Drafted |
| Table IV | Four deployed candidates, top XAI driver, seed frequency | reproduction CSVs | Drafted |
| Table V | Faithfulness verdict summary | original/reproduced verdict CSV | Drafted |
| Table VI | Ten source physical diagnostics and blank-sky-relative status | source-only CSV | Drafted; compress for page limit |
| Table VII | Limitations and claim boundaries | audits/config/handbook | Drafted |

## Caption boundaries

- Use “anomaly candidate,” never “confirmed anomaly.”
- Describe PCA and Isolation Forest values as archive-relative.
- State that WR is exposure-weighted and contains source and background contributions.
- Label phase as “fitted modulation phase (not official PA).”
- State that source/blank-sky Q/U differences are empirical diagnostics, not official subtraction.
- Do not plot PD sensitivity proxies as calibrated measurements.
- Scientific plots must be regenerated from real CSV values, not created through image generation.

## Tentative ≤8-page selection

Use four figures: merged architecture/feature pipeline, Matrix-C PCA, deployed score/seed ranking, and source/blank-sky Q/U space. Use four main tables: composition/features combined, matrix/robustness, candidates/XAI/faithfulness combined, and compressed source diagnostics. Move detailed features, 10-row physical table, and faithfulness metrics to supplementary material.
