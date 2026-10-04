# Draft 0 to Draft 1 Changelog

## Scope

Draft 1 accepts `XAI_Version_Mismatch_Audit.md` as the controlling evidence for the frozen current Sco X-1 explanation. No original project artifact was rerun or regenerated, no experiment was added, and no result other than the local Sco X-1 explanation ordering was changed.

The authoritative order is:

1. `t1A_energy_peak_channel` — 2.454499
2. `t1A_energy_weighted_mean_channel` — 2.207369
3. `t1A_energy_channel_entropy` — 1.813968

The historical entropy-first narrative is superseded and is not used in Draft 1.

## Markdown manuscript changes

File: `06_IEEE_Conference_Manuscript_Draft.md`

### Experimental Protocol

Changed the artifact-reproduction paragraph by adding this sentence:

> For Sco X-1, an exact imported-function audit was adopted as the controlling versioned evidence after it agreed with Notebook 10 and the supplementary reproduction.

Purpose: identifies the evidence version used by Draft 1.

### Table IV title

- Draft 0: `Fixed-model candidates and top local drivers`
- Draft 1: `Fixed-model candidates and leading local XAI evidence`

Purpose: permits the ordered top-three Sco X-1 evidence to be shown without implying that every row must contain only one feature.

### Table IV column heading

- Draft 0: `Top combined XAI driver`
- Draft 1: `Leading deployed XAI evidence`

Purpose: makes the Sco X-1 row explicitly versioned and ordered.

### Table IV Sco X-1 row

- Draft 0: `G01_0006 | Sco X-1 | 0.593516 | Energy peak channel | 100/100`
- Draft 1: `G01_0006 | Sco X-1 | 0.593516 | Peak channel 2.454499; weighted mean 2.207369; entropy 1.813968 | 100/100`

The Isolation Forest score and seed frequency did not change.

### Discussion paragraph on Sco X-1

Draft-0 text:

> Sco X-1 is also a stable Matrix-C candidate, driven primarily by its energy peak channel in the deployed explanation. Its physical vector distance is only 0.3005 and its raw modulation lies within empirical blank-sky scatter. This is the clearest example that a multivariate product anomaly can arise without unusual blank-sky-relative modulation.

Draft-1 text:

> Sco X-1 is also a stable Matrix-C candidate. Its accepted deployed XAI ranking is energy peak channel (2.454499), energy weighted mean channel (2.207369), and energy channel entropy (1.813968). The historical entropy-first narrative was not reproducible from a located versioned artifact and is superseded by the exact imported-function audit. The three leading features all arise from the energy-resolved product family; they identify local model evidence and do not establish a physical cause. Sco X-1’s physical vector distance is only 0.3005, and its raw modulation lies within empirical blank-sky scatter. This is the clearest example that a multivariate product anomaly can arise without unusual blank-sky-relative modulation.

Purpose: records all three accepted ranks, supersedes the historical narrative, and preserves the cautious interpretation. The physical values and non-equivalence conclusion did not change.

## LaTeX manuscript changes

File: `07_IEEE_Conference_Manuscript.tex`

### Experimental Protocol

Added the LaTeX-equivalent sentence:

> For Sco X-1, an exact imported-function audit was adopted as the controlling versioned evidence after it agreed with Notebook 10 and the supplementary reproduction.

### Candidate-table caption

- Draft 0: `Fixed-Model Candidates`
- Draft 1: `Fixed-Model Candidates and Leading Local XAI Evidence`

### Candidate-table column heading

- Draft 0: `Top driver`
- Draft 1: `Leading XAI evidence`

### Candidate-table Sco X-1 row

- Draft 0: `G01_0006 & Sco X-1 & .593516 & Peak channel & 100`
- Draft 1: `G01_0006 & Sco X-1 & .593516 & Peak 2.454499; weighted mean 2.207369; entropy 1.813968 & 100`

The table was changed from a one-column `table` float to a `table*` float, and the evidence column received a fixed width, solely to accommodate the accepted ordered ranking without clipping.

### Discussion paragraph

The previous single Sco X-1 clause—

> Sco X-1 is a stable candidate driven by energy peak channel, yet its vector distance is only 0.3005 and its raw modulation is within blank-sky scatter.

—was replaced by:

> Sco X-1 is a stable candidate whose accepted deployed XAI order is energy peak channel (2.454499), energy weighted mean channel (2.207369), and energy channel entropy (1.813968). The historical entropy-first narrative was not reproducible from a located versioned artifact and is superseded by the exact imported-function audit. These three features are local model evidence from the energy-resolved product family and do not establish a physical cause. Sco X-1's vector distance is only 0.3005 and its raw modulation is within blank-sky scatter.

The surrounding Her X-1 finding and the main statistical/physical non-equivalence claim were not changed.

## Evidence-control file changes

### `00_Paper_Status.md`

- Status changed from an evidence-audited working draft to `Draft 1 — evidence-audited working draft`.
- Added completion of the accepted exact-function audit and stated that no project rerun or new experiment occurred.
- Replaced the brief Sco X-1 report correction with the exact three-feature order and supersession statement.
- Updated the Markdown word count from 4,435 to 4,518 total and from 4,009 to 4,092 before references. The 219-word abstract did not change.

### `01_Evidence_Inventory.md`

- Replaced the single Sco X-1 top-driver row with three accepted ordered score rows at six-decimal manuscript precision.
- Added a separate row marking the historical entropy-first narrative as superseded.

### `02_Claim_and_Novelty_Matrix.md`

- Added a Draft-1 evidence-control paragraph with the accepted Sco X-1 order.
- Added a safe-wording row for the Sco X-1 local explanation.
- No novelty-strength claim changed.

### `04_Experiment_and_Robustness_Audit.md`

- Expanded the Sco X-1 candidate row to include ranks 1–3 and their scores.
- Added an accepted-version-audit subsection.
- Replaced the earlier two-feature discrepancy note with the exact ordered result and supersession statement.
- Explicitly recorded that predictions, anomaly scores, physical results, robustness results, and faithfulness verdicts did not change.

### `09_Reviewer_Risk_Checklist.md`

- Added checks for the exact three-feature order and exclusion of the historical entropy-first narrative.
- Strengthened the evidence check from the top feature alone to all three reported ranks and scores.

### `11_Reproducibility_Checklist.md`

- Added completed checks for exact-function import/execution, capture of all 15 scores, the accepted top-three order, evidence hashes, and supersession of the historical narrative.

## Protected records

The following were intentionally not changed:

- `XAI_Version_Mismatch_Audit.md`
- `POLIX_XAI_Final_Report_Errata.md`
- `POLIX_XAI_Final_Report_Reviewed.md`

## Numerical-change statement

No numerical project result other than adding and fixing the local Sco X-1 XAI ordering was changed. In particular, the 25-observation composition, 21/4 deployed predictions, anomaly scores, seed frequencies, contamination results, jackknife results, matrix ablation, faithfulness verdicts, blank-sky baseline, WeightedRoll fits, and all source physical diagnostics are unchanged.
