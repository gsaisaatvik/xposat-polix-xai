# Reproducibility Checklist

## Data and freeze

- [x] Freeze date recorded: 2026-07-27.
- [x] Scope stated as 25 observations included in the project archive.
- [x] Source/blank-sky roles recorded.
- [x] Observation IDs retained as stable keys.
- [x] Target labels recorded separately from observation IDs.
- [x] Primary evidence paths recorded.
- [x] SHA-256 hashes generated for key inputs.
- [ ] Data redistribution rights checked before public release.

## Feature engineering

- [x] Matrix A/B/C/WR paths recorded.
- [x] Row and feature counts verified.
- [x] Matrix-C ordered feature list recorded.
- [x] Missing-value count verified as zero.
- [x] WR excluded from primary Matrix-C input.
- [ ] Domain expert approves each feature’s physical wording.
- [ ] Duplicate Blank Sky-2 display label resolved.

## Model

- [x] Saved artifact path and hash recorded.
- [x] StandardScaler, PCA, KMeans, and Isolation Forest parameters recorded.
- [x] Fixed-model predictions reproduced exactly.
- [x] Candidate IDs and scores exported.
- [x] Top deployed XAI drivers reproduced.
- [x] Exact current `model_service.py` function imported and executed for the Sco X-1 Matrix-C row.
- [x] All 15 Sco X-1 feature scores captured in `deployed_xai_exact_from_model_service.csv`.
- [x] Sco X-1 order fixed as peak channel, weighted mean channel, then entropy.
- [x] Current code, model, Matrix-C, and Notebook-10 evidence hashes recorded in `XAI_Version_Mismatch_Audit.md`.
- [x] Historical entropy-first narrative marked superseded for Draft 1.
- [x] Current software versions exported.
- [ ] Original training environment/lockfile recovered.
- [ ] Independent future-data validation completed.

## Robustness

- [x] 100-seed Isolation Forest stability.
- [x] Contamination 0.12–0.24 sensitivity.
- [x] Leave-one-out jackknife.
- [x] Matrix A/B/C ablation.
- [x] WR retained as separate diagnostic.
- [x] PCA/KMeans/Isolation ranking agreement.
- [x] Faithfulness neutralization reproduced.
- [ ] Alternative neutralization baselines tested.
- [ ] Stability evaluated on a larger archive.

## Physical diagnostics

- [x] WeightedRoll model and weighted least-squares implementation inspected.
- [x] 25 fit rows verified.
- [x] Fit-quality thresholds verified from code.
- [x] 15 blank-sky observations verified.
- [x] 13-fit acceptable baseline verified.
- [x] Mean/scatter Q/U values verified.
- [x] All ten source rows verified.
- [x] No calibrated PD/PA claim.
- [ ] Official background procedure available and applied.
- [ ] Official \(\mu_{100}\) and response calibration available.
- [ ] Mission-approved sky-PA conversion available.

## Software implementation

- [x] Flask route and services inspected.
- [x] Feature extraction, model/XAI, physical branch, plotting, and export modules identified.
- [x] Deterministic template explanation confirmed.
- [ ] Browser-level result-download test completed.
- [ ] Automated unit/integration test suite added.
- [ ] Deployment environment and security review completed.

## Literature and claims

- [x] Review-I documents read.
- [x] Publication-focused search performed.
- [x] Official acknowledgment wording verified.
- [x] XPoSat and POLIX named in abstract.
- [x] BibTeX file created.
- [x] Legacy references [3], [4], [14], and [18] addressed.
- [ ] Full text of Saini *et al.* inspected.
- [ ] Full text of Yepmo *et al.* inspected.
- [ ] Search rerun immediately before submission.

## Manuscript and figures

- [x] Markdown draft created.
- [x] LaTeX draft created.
- [x] Figure/table manifest created before insertion.
- [ ] Author/affiliation fields completed.
- [ ] Venue and page limit selected.
- [ ] Figures regenerated from verified CSVs.
- [ ] Figure captions independently checked.
- [ ] LaTeX compiled in target IEEE environment.
- [ ] Final PDF visually inspected.
- [ ] No final PDF created before review.

## Supplementary experiment command

```powershell
& 'D:\polix_xai_webapp\venv\Scripts\python.exe' `
  'D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\robustness_audit.py'
```

Expected machine summary: `supplementary_experiments/audit_summary.json`.
