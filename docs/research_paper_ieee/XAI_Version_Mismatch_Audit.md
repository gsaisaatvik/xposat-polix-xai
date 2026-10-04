# Sco X-1 Deployed-XAI Version Mismatch Audit

## Audit status

**Current deployed implementation: resolved. Historical website-output provenance: unresolved because the asserted saved output artifact was not found.**

The exact `PolixXAIPredictor.explain_one` function currently imported by the Flask application was executed against the frozen Sco X-1 Matrix-C row and the saved deployed PKL. The function was not manually reimplemented. A trace hook retained the function's complete sorted 15-row local result before its normal `rows[:5]` return.

The exact current result is:

1. `t1A_energy_peak_channel`: **2.4544990315347768**
2. `t1A_energy_weighted_mean_channel`: **2.2073686584810000**
3. `t1A_energy_channel_entropy`: **1.8139679863052869**

This ranking agrees with the original Notebook-10 Matrix-C output and with `deployed_xai_reproduction.csv`. It does not agree with the reviewed-report statement or the user-reported historical website output in which entropy was approximately 2.814 and peak channel was approximately 2.454.

## Frozen identifiers

| Item | Exact value |
|---|---|
| Git commit | `15628ee7cc434de9ba03caaae5dd115d8cd09f9a` |
| Git history for `model_service.py` | One committed version |
| Working-tree diff for `model_service.py` | Empty |
| `model_service.py` SHA-256 | `f749ffd0e79a951f42555f5083d2056567de9ccaaf721772601ea0a79856c877` |
| Web-app PKL SHA-256 | `d8efd73c9744ed1ca1098a4599da91acdedc250bb2b6639728364aef6b8c180d` |
| Archive-root PKL SHA-256 | `d8efd73c9744ed1ca1098a4599da91acdedc250bb2b6639728364aef6b8c180d` |
| Final-output PKL SHA-256 | `d8efd73c9744ed1ca1098a4599da91acdedc250bb2b6639728364aef6b8c180d` |
| Downloaded PKL SHA-256 | `d8efd73c9744ed1ca1098a4599da91acdedc250bb2b6639728364aef6b8c180d` |
| Matrix-C CSV SHA-256 | `3936e1b0aaf44acff39597befec1b466a26511123655946f8829a4e6263db0fa` |
| Notebook-10 all-contribution CSV SHA-256 | `973f526d235501bb47c7aef0c88aaa2dbe77cdf4ad53db94d4c8e91981134d14` |
| Prior supplementary reproduction SHA-256 | `00f20e3018cedb8e56268873a4dfd59f3ff897fdb7b43de4874b061e6a32bf4a` |
| Observation | `X01_PLX_G01_0006_000000` |
| Model output | Anomaly; score `0.5935161327457337` |

All located copies of the saved model are byte-identical. The mismatch is therefore not explained by selecting a different located PKL.

## Exact normalization function

The following source was captured with `inspect.getsource` from the imported current module:

```python
def normalize_score(values):
    values = np.asarray(values, dtype=float)
    max_val = np.nanmax(np.abs(values))

    if not np.isfinite(max_val) or max_val == 0:
        return np.zeros_like(values)

    return np.abs(values) / max_val
```

The combined score in the current function is the sum of normalized PCA contribution, normalized KMeans squared centroid distance, normalized positive Isolation Forest occlusion delta, and normalized absolute standardized value.

## Exact-function result for all 15 Sco X-1 features

| Rank | Feature | Combined score | z-score | PCA contribution | KMeans contribution | Isolation contribution |
|---:|---|---:|---:|---:|---:|---:|
| 1 | `t1A_energy_peak_channel` | 2.454499032 | 4.894105812 | 0.252939915 | 0 | 0.092515253 |
| 2 | `t1A_energy_weighted_mean_channel` | 2.207368658 | -3.432505250 | 0.556524650 | 0 | 0.046813988 |
| 3 | `t1A_energy_channel_entropy` | 1.813967986 | -2.855661897 | 0.507086535 | 0 | 0.029541195 |
| 4 | `t1B_src_roll_smoothness_norm` | 0.706647134 | 1.217371825 | 0.211387175 | 0 | 0.007222698 |
| 5 | `t1A_energy_high_channel_fraction` | 0.687848695 | -1.071661718 | 0.199306021 | 0 | 0.010246313 |
| 6 | `t2_det_lc_rate_balance_cv` | 0.529629188 | 1.001474693 | 0.143525421 | 0 | 0.006208195 |
| 7 | `t1A_energy_anode_balance_cv` | 0.508962251 | 1.122756567 | 0.155577747 | 0 | -0.001714870 |
| 8 | `t1B_src_peak_to_median_roll` | 0.434104081 | 0.711291230 | 0.138115354 | 0 | 0.003755477 |
| 9 | `t1A_exp_max_to_min_roll` | 0.424172547 | 0.665901163 | 0.129599625 | 0 | 0.005110318 |
| 10 | `t1A_energy_weighted_std_channel` | 0.207418788 | 0.441078077 | 0.065277249 | 0 | -0.002976819 |
| 11 | `t2_lc_rate_cv` | 0.187474566 | 0.356135439 | 0.040333739 | 0 | 0.003907106 |
| 12 | `t1B_src_roll_entropy` | 0.153440600 | -0.274290906 | 0.049779059 | 0 | 0.000735419 |
| 13 | `t2_lc_peak_to_median_rate` | 0.147798032 | -0.384729941 | 0.038504358 | 0 | -0.002707583 |
| 14 | `t1A_exp_uniformity_cv` | 0.123039718 | 0.179081335 | 0.035113789 | 0 | 0.002160576 |
| 15 | `t2_det_pha_centroid_spread` | 0.039626214 | 0.147545215 | 0.005275120 | 0 | -0.003932997 |

The machine-readable table, including comparison columns, is `supplementary_experiments/deployed_xai_exact_from_model_service.csv`.

## Four-way comparison

| Evidence source | Peak-channel score/rank | Entropy score/rank | Finding |
|---|---|---|---|
| Current imported `model_service.py` | 2.454499 / rank 1 | 1.813968 / rank 3 | Peak first |
| Saved website output as described by the user | approximately 2.454 / rank 2 | approximately 2.814 / rank 1 | Entropy first; no saved machine-readable or screenshot artifact was located |
| `deployed_xai_reproduction.csv` | 2.454499 / rank 1 | 1.813968 / rank 3 | Exact agreement for its retained top five |
| Original Notebook-10 Matrix-C contribution output | 2.454499 / rank 1 | 1.813968 / rank 3 | Maximum absolute difference from current exact output: \(7.63\times10^{-17}\) |
| Reviewed report | No score stated / rank 2 | No score stated / rank 1 | Narrative agrees with the asserted historical website ranking, but conflicts with Notebook 10 and current deployed code |

The project presentation was also inspected. It contains spaces/instructions for future website screenshots, not the saved result screenshot or the numerical 2.814 value.

## Cause analysis

### What is established

1. The current imported Flask function, committed `model_service.py`, Notebook-10 Matrix-C output, and new exact-function execution agree.
2. All located model PKL files have the same SHA-256.
3. Sco X-1 is the sole member of KMeans cluster 3 in the saved model. Its standardized row equals that cluster centroid exactly. Consequently, every current raw KMeans feature contribution is zero and `normalize_score` returns an all-zero KMeans component.
4. The asserted historical entropy score, approximately 2.814, is approximately **one normalized unit greater** than the verified current entropy score, 1.813968. The asserted peak score is unchanged.

### Most specific defensible explanation

The numerical fingerprint is consistent with the historical output assigning entropy an additional normalized component of approximately 1.0. The KMeans component is the leading candidate because its current contribution is identically zero for Sco X-1, while a feature that is maximal within a nonzero KMeans contribution vector would receive exactly 1.0 after normalization.

However, the historical website artifact, its exact input row, and the code hash that produced it were not found. The repository contains only one commit, so an earlier overwritten or uncommitted implementation cannot be reconstructed from Git. It is therefore not possible to prove whether the extra unit came from a different KMeans calculation, a different input vector/cluster assignment, a duplicated normalized term, or a transcription error.

## Audit verdict

- **Authoritative result for the current versioned deployment and frozen Matrix-C evidence:** `t1A_energy_peak_channel` is rank 1; entropy is rank 3.
- **Historical website/report claim:** not reproducible from any located versioned artifact.
- **Mismatch classification:** historical version/provenance mismatch, not a disagreement between the current deployed function and Notebook 10.
- **Manuscript action:** remain frozen as Draft 0 until the authors either (a) accept the versioned result above, or (b) supply the original website screenshot/export plus its exact input CSV so the historical computation can be reconstructed.
- **Report action:** do not overwrite the reviewed report. Carry the issue in the separate errata file.

## Reproduction files

- `supplementary_experiments/xai_version_audit.py`
- `supplementary_experiments/deployed_xai_exact_from_model_service.csv`
- `supplementary_experiments/xai_version_audit_metadata.json`

