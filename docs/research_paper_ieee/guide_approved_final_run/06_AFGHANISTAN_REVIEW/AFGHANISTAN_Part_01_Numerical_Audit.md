# AFGHANISTAN Part 01 — Numerical Audit

## Verdict

**PASS — no numerical contradiction was found in the Phase-5 manuscript.** A read-only audit checked 35 dataset, model, robustness, XAI, harmonic, cross-format, terminology, citation, and integrity conditions. All 35 passed after resolving observation display names through the Phase-1 truth table. No model was fitted, no matrix was regenerated, and no scientific result was recomputed.

## Dataset and representation

| Check | Verified result | Controlling evidence | Status |
|---|---|---|---|
| Matrix-C rows | 25 | `D:\ISROtrial\Polix_L2_full_archive\polix_matrix_v2_C_primary_plus_supporting.csv` | PASS |
| Matrix-C feature columns | 15, excluding `observation_id` | Same CSV | PASS |
| Missing feature values | 0 | Same CSV | PASS |
| WeightedRoll in Matrix C | Absent | Same CSV schema | PASS |
| Project mapping | 10 source; 15 blank sky | `01_NEPAL_EVIDENCE/NEPAL_Part_03_All_25_Observation_Truth_Table.csv` | PASS |

## Fixed model result

The exact reproduction contains 21 `Normal` rows and four `Anomaly` rows, with all stored and recomputed labels matching and maximum score difference equal to zero.

| Candidate | Full identifier | Recomputed score | Manuscript value | Status |
|---|---|---:|---:|---|
| Blank Sky-13 | `X01_PLX_C24_0018_000000` | 0.6159638749 | 0.615964 | PASS |
| Sco X-1 | `X01_PLX_G01_0006_000000` | 0.5935161327 | 0.593516 | PASS |
| Her X-1 | `X01_PLX_G01_0003_000000` | 0.5723081973 | 0.572308 | PASS |
| Blank Sky-5 | `X01_PLX_C24_0010_000000` | 0.5176113060 | 0.517611 | PASS |

Controlling file: `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\deployed_model_reproduction.csv`.

## Procedure-qualified stability

| Observation | Seeds | Contamination settings | Included-observation jackknife | Manuscript interpretation |
|---|---:|---:|---:|---|
| Blank Sky-13 | 100/100 | 4/4 | 24/24 | Stable under the tested procedures |
| Sco X-1 | 100/100 | 4/4 | 24/24 | Stable under the tested procedures; held-out result separately disclosed |
| Her X-1 | 100/100 | 4/4 | 24/24 | Stable under the tested procedures |
| Blank Sky-5 | 29/100 | 3/4 | 19/24 | Seed-sensitive boundary candidate |
| Blank Sky-15 | 68/100 | 2/4 | 7/24 | Fixed-Normal boundary competitor |
| Crab P01_0005 | 3/100 | 1/4 | 2/24 | Matrix-A-only candidate in the tier comparison |

The common-observation jackknife ranking has median Spearman correlation 0.9895652174 and minimum 0.9686956522, matching the manuscript’s six-decimal values. These are retrospective procedure checks, not probabilities or prospective validation.

Controlling files: `isolation_seed_stability_summary.csv`, `contamination_candidate_stability.csv`, `jackknife_observation_stability.csv`, and `jackknife_run_summary.csv` in `research_paper_ieee/supplementary_experiments`.

## Feature-tier and ranking results

- Matrix A candidates: Blank Sky-13, Blank Sky-15, Sco X-1, Crab P01_0005.
- Matrix B candidates: Blank Sky-5, Blank Sky-13, Blank Sky-15, Sco X-1.
- Matrix C candidates: Blank Sky-5, Blank Sky-13, Her X-1, Sco X-1.
- Cross-tier persistent pair: Blank Sky-13 and Sco X-1.
- Spearman correlations: PCA–Isolation Forest 0.894615; PCA–KMeans 0.155799; KMeans–Isolation Forest 0.186574.

All values match `matrix_ablation_summary.csv` and `ranking_agreement.csv`. The manuscript correctly does not use the nominal p-values to validate candidates.

## XAI and neutralization

The exact deployed-function audit verifies the Sco X-1 order:

1. `t1A_energy_peak_channel`: 2.4544990315, reported as 2.454;
2. `t1A_energy_weighted_mean_channel`: reported as 2.207;
3. `t1A_energy_channel_entropy`: reported as 1.814.

The six-case reproduction contains five Strong, one Moderate, and zero Weak project verdicts. The manuscript correctly treats these as in-sample perturbation outcomes rather than general faithfulness proof.

## Harmonic and empirical-reference results

| Check | Verified result | Status |
|---|---:|---|
| Saved fits | 25 | PASS |
| Fit categories | 19 acceptable; 3 caution; 3 poor | PASS |
| Blank-sky fits | 15 | PASS |
| Selected reference | 13 with reduced chi-square ≤ 2 | PASS |
| Mean raw modulation | 1.1478203388% | PASS |
| Sample standard deviation | 0.5659596729% | PASS |
| Source rows satisfying declared scalar rule | 10/10 | PASS |

Representative Sco X-1, Her X-1, Crab P01_0005, Blank Sky-13, and Blank Sky-5 values in Table IV match `path2_final_polarization_xai_result_table_with_roles.csv`. The scalar comparison matches `path2_source_vs_blank_sky_modulation_comparison.csv`. These checks validate the reported archive diagnostics only; they do not validate polarization degree, sky angle, background subtraction, or detection significance.

## Cross-format and integrity checks

- Exact title: present in Markdown, DOCX, and LaTeX.
- Required numerical tokens: consistent across all three formats.
- DOCX: four figures and four tables.
- Citation and BibTeX sets: 17 matching keys, with no uncited entry.
- Forbidden or superseded wording: absent from manuscript and BibTeX.
- Protected files: 43 checked; 0 missing or changed.

Machine-readable working record: `working/phase6_checks.json`.

## Experiments requested by this audit

None. All Phase-6 activity was verification of existing outputs.
