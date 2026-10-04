# BANGLADESH Part 04 — Representative Case Studies

## Selection principle

These cases illustrate relationships visible in the full 25-row truth table. They are not the sole evidence for the conclusions and are not selected to assign astrophysical or instrumental causes.

## Case 1 — Sco X-1: persistent ML candidate with bounded harmonic result

### Verified evidence

- Fixed rank 2; Isolation Forest score 0.593516133.
- Selected in 100/100 tested seeds and every eligible included-observation jackknife refit.
- Candidate under Matrix A, B and C.
- Top local features: energy peak channel 2.454, energy weighted mean channel 2.207 and energy-channel entropy 1.814.
- Raw modulation 1.139578%; fitted phase 165.527814 degrees.
- Reduced chi-square 2.030761, caution category.
- Fractional harmonic coordinates \(q=0.0099723\), \(u=-0.0055151\).
- Raw modulation remains within the declared empirical blank-sky reference rule.

### Safe interpretation

Sco X-1 is persistently unusual in the product-aware Matrix-C representation under the procedures tested. Its local ranking directs attention to energy-resolved channel summaries. The independent harmonic result does not cross the declared empirical rule, and its caution fit category limits interpretation. No physical cause or polarization conclusion follows.

## Case 2 — Her X-1: stable Matrix-C candidate with an inadequate simple harmonic summary

### Verified evidence

- Fixed rank 3; score 0.572308197.
- Selected in 100/100 tested seeds and 24/24 eligible jackknife refits.
- Candidate in Matrix C but not Matrix A or B.
- Raw modulation 0.596632%; fitted phase 124.639464 degrees.
- Reduced chi-square 57.433514, poor simple-harmonic fit.
- \(q=-0.0021110\), \(u=-0.0055804\).

### Safe interpretation

Her X-1 belongs to the tested-procedure stable Matrix-C core but is feature-tier dependent. Its high reduced chi-square means the selected second harmonic is a poor description of its delivered WeightedRoll curve. The fitted phase and raw modulation must therefore not be elevated to a physical interpretation.

## Case 3 — Crab P01_0005: fixed Normal with comparatively larger raw modulation

### Verified evidence

- Fixed Normal; Isolation Forest score 0.504655628.
- Selected in 3/100 seed runs.
- Candidate in Matrix A but not Matrix B or C.
- Raw modulation 1.697346%; fitted phase 163.346589 degrees.
- Reduced chi-square 1.062540, acceptable category.
- \(q=0.0141854\), \(u=-0.0093205\).

### Safe interpretation

Crab P01_0005 has a larger raw-modulation value than Sco X-1, Her X-1 and Blank Sky-13 while remaining Normal under the fixed Matrix-C model. This directly shows that the scalar harmonic amplitude does not determine the archive-relative ML label. It is not a polarization detection.

## Case 4 — Blank Sky-13: strongest fixed candidate with a caution harmonic fit

### Verified evidence

- Fixed rank 1; score 0.615963875.
- Selected in 100/100 seeds and 24/24 eligible jackknife refits.
- Candidate across Matrix A/B/C.
- Raw modulation 0.853951%; fitted phase 158.783354 degrees.
- Reduced chi-square 2.565811, caution category.
- \(q=0.0063027\), \(u=-0.0057619\).
- Excluded from the 13-fit blank-sky reference by the declared fit rule.

### Safe interpretation

A project-labelled blank-sky observation can be statistically unusual in Matrix-C space. This confirms that the screening output is neither a source classifier nor a polarization classifier. Its fit category does not reveal a cause.

## Case 5 — Blank Sky-5: fixed candidate near a seed-sensitive boundary

### Verified evidence

- Fixed rank 4; score 0.517611306.
- Selected in 29/100 seeds and 19/24 eligible jackknife refits.
- Candidate in Matrix B and C but not A.
- Raw modulation 1.518535%; fitted phase 158.002153 degrees.
- Reduced chi-square 0.713428, acceptable category.
- \(q=0.0109242\), \(u=-0.0105478\).

### Safe interpretation

Blank Sky-5 is an archive-relative candidate only for the frozen configuration and is explicitly seed-sensitive. Its acceptable harmonic fit neither confirms nor invalidates the ML result.

## Cross-case synthesis

| Contrast | What it shows | What it does not show |
|---|---|---|
| Sco X-1 vs its harmonic reference status | Stable feature-space unusualness can coexist with a bounded raw harmonic result | A contradiction, physical cause or absence of polarization |
| Her X-1 high reduced chi-square | The second harmonic can be an inadequate summary | Polarization, non-polarization or anomaly cause |
| Crab P01_0005 vs fixed candidates | Larger raw modulation does not imply Matrix-C candidate status | A calibrated detection |
| Blank Sky-13 and Blank Sky-5 | Candidate labels are not source/polarization labels | Official background behaviour |
| Blank Sky-5 vs stable three | The contamination boundary is seed-sensitive for some rows | A 29% anomaly probability |

## Exact proposed Discussion claims

**CASE-D1.** Sco X-1 demonstrates persistent Matrix-C unusualness linked locally to channel-space summaries, while its raw harmonic result remains within the declared empirical reference rule.

**CASE-D2.** Her X-1 demonstrates that a stable ML candidate can have a poorly represented second-harmonic curve; the poor fit prevents physical interpretation of the fitted harmonic quantities.

**CASE-D3.** Crab P01_0005 demonstrates that a fixed-Normal observation can have larger raw modulation than several ML candidates.

**CASE-D4.** The blank-sky candidates demonstrate that Isolation Forest screens feature-space unusualness rather than source identity or polarization.

**CASE-D5.** Taken together, the representative cases support non-equivalence between statistical unusualness and modulation-like harmonic behaviour within the project archive, without identifying an astrophysical or instrumental cause.

## Controlling evidence

- `D:\polix_xai_webapp\research_paper_ieee\guide_approved_final_run\01_NEPAL_EVIDENCE\NEPAL_Part_03_All_25_Observation_Truth_Table.csv`
- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\deployed_xai_exact_from_model_service.csv`
- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\isolation_seed_stability_summary.csv`
- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\matrix_ablation_summary.csv`
- Saved harmonic CSVs listed in `BANGLADESH_Part_03_Harmonic_Results.md`.

