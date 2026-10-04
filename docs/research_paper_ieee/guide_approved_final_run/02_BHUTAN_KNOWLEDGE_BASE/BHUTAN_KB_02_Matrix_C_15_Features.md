# BHUTAN Knowledge Card 02 — All 15 Matrix-C Features

## Beginner explanation

Each Matrix-C feature is a compact number derived from a delivered product. The features describe exposure imbalance across roll, count locations and spread in PHA-channel space, source-azimuth variation, delivered light-curve behaviour and differences among detector products. They are diagnostic summaries, not direct calibrated polarization measurements.

## Technical theory and exact project implementation

NumPy population standard deviations are used (`ddof=0`). For positive values \(v_j\), entropy is

\[
H(v)=-\sum_j p_j\log_2p_j,\qquad p_j=v_j/\sum_kv_k.
\]

### Exposure product — two features

Let \(E_r\) be total exposure across the four detectors at roll row \(r\).

1. `t1A_exp_uniformity_cv`: \(\operatorname{std}(E_r)/\operatorname{mean}(E_r)\).
2. `t1A_exp_max_to_min_roll`: \(\max(E_r)/\min(E_r)\).

### Energy-resolved azimuth product — six features

Let \(n_j\) be counts summed over roll and anode at PHA-channel index \(j\), and \(a_k\) counts summed over roll and channel for anode \(k\).

3. `t1A_energy_peak_channel`: \(\operatorname*{arg\,max}_j n_j\).
4. `t1A_energy_weighted_mean_channel`: \(\bar j=\sum_j jn_j/\sum_jn_j\).
5. `t1A_energy_weighted_std_channel`: weighted channel spread,
   \[
   \sqrt{\frac{\sum_j(j-\bar j)^2n_j}{\sum_jn_j}}.
   \]
   Preferred table label: **Weighted channel spread (`t1A_energy_weighted_std_channel`)**.
6. `t1A_energy_high_channel_fraction`: \(\sum_{j\ge4000}n_j/\sum_jn_j\). This is a high-channel fraction, not a calibrated high-energy fraction.
7. `t1A_energy_channel_entropy`: base-2 Shannon entropy of the positive channel-count distribution.
8. `t1A_energy_anode_balance_cv`: \(\operatorname{std}(a_k)/\operatorname{mean}(a_k)\).

### Source-azimuth product — three features

Let \(R_r\) be the sum of 48 anode counts at roll row \(r\).

9. `t1B_src_peak_to_median_roll`: \(\max(R_r)/\operatorname{median}(R_r)\).
10. `t1B_src_roll_entropy`: base-2 Shannon entropy of positive roll sums.
11. `t1B_src_roll_smoothness_norm`: normalized order-dependent roughness proxy,
    \[
    \frac{\operatorname{mean}_{r=1}^{n-1}|R_{r+1}-R_r|}{\operatorname{mean}(R_r)}.
    \]
    The implementation has no circular last-to-first difference.

### Delivered source light curve — two features

Let \(L_t\) be the delivered `RATE` array.

12. `t2_lc_rate_cv`: \(\operatorname{std}(L_t)/\operatorname{mean}(L_t)\).
13. `t2_lc_peak_to_median_rate`: \(\max(L_t)/\operatorname{median}(L_t)\).

These are delivered-light-curve diagnostic proxies, not calibrated intrinsic source variability.

### Four-detector products — two features

Let \(\bar L_d\) be the mean delivered light-curve rate for detector \(d\), and \(\bar j_d\) its PHA weighted channel centroid.

14. `t2_det_lc_rate_balance_cv`: \(\operatorname{std}_d(\bar L_d)/\operatorname{mean}_d(\bar L_d)\).
15. `t2_det_pha_centroid_spread`: \(\operatorname{std}_d(\bar j_d)\), where \(\bar j_d=\sum_jjN_{dj}/\sum_jN_{dj}\).

The corrected Notebook-08 extractor explicitly excludes `EnergyRes` when locating the source-azimuth product. The deployed extractor preserves this 15-feature schema. All final Matrix-C values are finite, and no imputation is performed.

## Parameters and implementation conventions

Matrix A retains features 1–8, Matrix B retains 1–11, and Matrix C retains all 15. PHA threshold 4000 is an implementation-defined channel index. Entropies use base 2, adjacent-bin roughness has no circular wrap, and standard deviations use `ddof=0`.

## Controlling sources and cells

- `D:\ISROtrial\Polix_L2_full_archive\08_Feature_Set_V2_Product_Tier_Engineering.ipynb`: JSON indices 3–6 for helper computations/extraction and index 9 for retained A/B/C schemas.
- `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\02_feature_engineering\polix_matrix_v2_C_primary_plus_supporting.csv`: exact feature values.
- `D:\polix_xai_webapp\feature_extractor.py`: `entropy_from_values`, `smoothness`, `weighted_mean_std`, and `extract_matrix_c_features`.
- `D:\polix_xai_webapp\research_paper_ieee\guide_approved_final_run\01_NEPAL_EVIDENCE\NEPAL_Part_01_Notebook_01_to_11_Map.md`: verified extraction lineage and terminology boundaries.

## Verified numerical results

- Matrix C has exactly 15 features and zero missing values.
- Matrix A candidates: C24_0018, C24_0020, G01_0006 and P01_0005.
- Matrix B candidates: C24_0010, C24_0018, C24_0020 and G01_0006.
- Matrix C candidates: C24_0010, C24_0018, G01_0003 and G01_0006.
- Only Blank Sky-13 and Sco X-1 persist across A/B/C. This demonstrates feature-tier dependence, not Matrix-C superiority.

## Safe inference

The features form a product-traceable representation: each model input has an explicit computation and can be mapped to an exposure, channel-space, source-azimuth, delivered-light-curve or detector family.

## Unsupported inference

Do not call channel index calibrated energy, high-channel fraction high-energy fraction, the roughness proxy circular smoothness, delivered-light-curve proxies intrinsic source variability, detector PHA-centroid spread a calibrated spectral parameter, or any feature a physical cause of a label.

## Paper-ready wording

> Matrix C contains 15 observation-level features grouped by product provenance: two exposure summaries, six energy-resolved channel-space summaries, three source-azimuth summaries, two delivered-light-curve diagnostic proxies and two detector-balance summaries. Channel quantities remain in PHA-channel space. The high-channel fraction uses channel index 4000, and the source-azimuth roughness proxy averages adjacent-bin absolute differences without a circular wrap. These operational definitions limit physical interpretation while preserving computational traceability.

## Likely reviewer challenge and safe answer

**Question:** Why are these handcrafted features scientifically interpretable?

**Safe answer:** Interpretability means computational traceability rather than complete physical calibration. Each value has a documented formula and product-family origin, allowing a local ranking to be traced back to a delivered product. The paper explicitly limits physical interpretation where calibration or additional timing analysis is absent.
