# BHUTAN Knowledge Card 10 — Representative Observation Cases

## Beginner explanation

These examples show why the machine-learning and harmonic branches must remain separate. An observation can be unusual in Matrix-C space while having an ordinary raw harmonic value, and a fixed-Normal observation can have a larger raw modulation than some candidates.

## Technical explanation

The cases compare two non-identical mappings of the same observation: a 15-dimensional archive-relative Isolation Forest label and a fit to a separate delivered WeightedRoll curve. Because WeightedRoll is excluded from Matrix C, agreement is neither engineered nor guaranteed. Case comparisons are illustrative summaries of the full 25-row truth table, not causal case studies.

## Exact project implementation

The table joins the authoritative fixed prediction output and saved harmonic outputs by full observation identifier. It ignores the older physical-table `is_xai_consensus_anomaly` and priority fields, which describe six exploratory cases rather than the fixed four.

## Exact implementation, parameters and verified results

| Observation | Fixed ML result | Raw modulation (%) | Fitted phase (deg) | Reduced chi-square | Fit category | \(q\) | \(u\) |
|---|---|---:|---:|---:|---|---:|---:|
| Sco X-1 | Candidate | 1.139578 | 165.527814 | 2.030761 | Caution | 0.0099723 | -0.0055151 |
| Her X-1 | Candidate | 0.596632 | 124.639464 | 57.433514 | Poor | -0.0021110 | -0.0055804 |
| Crab P01_0005 | Normal | 1.697346 | 163.346589 | 1.062540 | Acceptable | 0.0141854 | -0.0093205 |
| Blank Sky-13 | Candidate | 0.853951 | 158.783354 | 2.565811 | Caution | 0.0063027 | -0.0057619 |
| Blank Sky-5 | Candidate | 1.518535 | 158.002153 | 0.713428 | Acceptable | 0.0109242 | -0.0105478 |

- **Sco X-1:** fixed candidate, 100/100 seeds and A/B/C persistent. Raw modulation remains within the declared empirical reference rule; the fit is caution. Its local ranking begins with energy peak channel, weighted mean channel and channel entropy. This points to energy-product summaries under the heuristic, not a physical cause.
- **Her X-1:** fixed candidate and 100/100 seeds, but Matrix-C-specific. Reduced chi-square 57.433514 means the chosen second harmonic summarizes the curve poorly; it is not evidence for or against polarization.
- **Crab P01_0005:** fixed Normal and 3/100 seeds, yet raw modulation 1.697346% exceeds that of several candidates with an acceptable fit. Raw harmonic amplitude therefore does not set the ML label.
- **Blank Sky-13:** fixed candidate, 100/100 seeds and A/B/C persistent, with a caution harmonic fit. Its role shows the model is not a source-physics or polarization classifier.
- **Blank Sky-5:** fixed candidate but 29/100 seeds; present in Matrix B/C but not A; acceptable harmonic fit. It is a seed-sensitive screening boundary case.

## Controlling sources

- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\deployed_model_reproduction.csv`.
- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\isolation_seed_stability_summary.csv`.
- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\matrix_ablation_summary.csv`.
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\04_polarimetry_results\polix_weightedroll_raw_modulation_fits.csv`.
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\04_polarimetry_results\path2_all_observations_fractional_qu_vectors.csv`.
- `D:\polix_xai_webapp\research_paper_ieee\guide_approved_final_run\01_NEPAL_EVIDENCE\NEPAL_Part_03_All_25_Observation_Truth_Table.csv`.

## Safe inference

Together, these observations show that Matrix-C statistical unusualness and WeightedRoll modulation-like harmonic behaviour do not agree one-to-one within the project archive.

## Unsupported inference

Do not assign instrumental or astrophysical causes, identify polarization, call candidates confirmed anomalies, or treat poor/acceptable harmonic fit as a physical class.

## Paper-ready wording

> The representative observations demonstrate non-equivalence between the diagnostic branches. Sco X-1 was a stable Matrix-C screening candidate, yet its raw modulation remained within the declared empirical blank-sky reference rule. Conversely, Crab P01_0005 was Normal in the fixed result despite a larger raw modulation than several candidates. The blank-sky candidates further show that screening is not source-physics classification. Her X-1’s high reduced chi-square indicates only that the selected second harmonic provides a poor summary of its delivered WeightedRoll curve.

## Likely reviewer challenge and safe answer

**Question:** Were these cases cherry-picked?

**Safe answer:** They are representative illustrations, not the sole evidence. The controlling truth table contains all 25 observations, and the conclusion is based on the complete fixed-label and harmonic outputs. The cases make the observed non-equivalence easier to inspect.
