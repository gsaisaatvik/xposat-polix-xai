# Agent 3 — Matrix-C Data and Feature Semantics Audit

**Audit scope:** the frozen 15-feature Matrix-C representation only.  
**Audit date:** 2026-07-27.  
**Method:** independent read-only inspection of the feature CSV, Notebook 08 source, the Flask upload extractor, and representative archive product paths. No experiment or regeneration was performed.

## 1. Controlling implementation evidence

The following sources agree on the names and order of the 15 deployed features:

1. `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\02_feature_engineering\polix_matrix_v2_C_primary_plus_supporting.csv` (header plus 25 rows);
2. Notebook 08, code cell 10, `matrix_C_cols`;
3. `D:\polix_xai_webapp\feature_extractor.py`, lines 10–27, `MATRIX_C_COLUMNS`.

The final archived CSV was produced by Notebook 08. The Flask extractor is a separate upload-time implementation of the same feature definitions. It agrees algebraically for ordinary finite inputs, but it is not byte-for-byte the notebook implementation: it uses `nan`-aware reductions, detects the largest EnergyRes dimension as the channel axis, detects a dimension of length 48 as the anode axis, and can compute detector summaries from fewer than four located products. Therefore, statements about the **frozen matrix** should cite Notebook 08 and the archived CSV; statements about **new uploads** should cite `feature_extractor.py`.

Verified product shapes in the Notebook 08 implementation comments are:

- exposure roll table: 360 rows × 4 detector-exposure columns;
- EnergyRes cube in Astropy order: 360 roll bins × 8192 channels × 48 anodes;
- source-azimuth `ANODE_COUNTS`: 360 roll bins × 48 anodes.

These shapes were not independently re-read from every one of the 25 FITS files in this audit. Uniformity of shape across the archive is therefore **NOT VERIFIED**.

### Classification meaning

- **VERIFIED:** exact source and computation are established; restrained descriptive use does not require an additional physical assumption.
- **REASONABLE PROXY:** computation is verified, but its physical label is an engineered summary rather than a calibrated measurement.
- **REQUIRES DOMAIN APPROVAL:** computation is verified, but scientific use depends on POLIX product semantics, calibration, extraction, or quality guidance not resolved here.
- **UNSAFE CLAIM:** the stated physical interpretation must not be made from this feature.

## 2. Feature-by-feature trace

| # | Matrix-C feature | FITS product and field | Exact implementation | Units / status | Shape and edge handling | Permitted interpretation and caveat | Classification |
|---:|---|---|---|---|---|---|---|
| 1 | `t1A_exp_uniformity_cv` | `Polix_l2_polarization\*_Exp_Azimuth_Roll_L2.fits`; Notebook explicitly reads `DET1_Exposure`…`DET4_Exposure` | Sum four detector exposures for each roll bin, then `std(total_per_roll) / mean(total_per_roll)`. Flask: lines 161–180. | Dimensionless ratio. | Expected 360×4; notebook uses ordinary sums/statistics. Flask discovers columns containing `Exposure`, stacks them, uses `nansum/nanstd/nanmean`; zero/nonfinite denominator returns NaN. | Relative nonuniformity of recorded exposure over roll bins. It is not source variability, detector efficiency, or polarization. | **REASONABLE PROXY** |
| 2 | `t1A_exp_max_to_min_roll` | Same exposure product and fields | `max(total_per_roll) / min(total_per_roll)`. It is added in Notebook 08 cell 10; Flask lines 177–181. | Dimensionless ratio. | A zero minimum yields NaN through `safe_div`; a very small minimum can make the ratio unstable. Notebook’s initial `safe_div` does not explicitly reject infinite denominators. | Extreme exposure contrast across roll bins. “Exposure imbalance” is acceptable; an instrumental cause is not established. | **REASONABLE PROXY** |
| 3 | `t1A_energy_peak_channel` | `Polix_l2_polarization\*_EnergyRes_Src_Azimuth_Roll_L2.fits`, primary image cube | Collapse roll and anode axes to a channel profile; return the array index of its largest bin. Notebook 08 cell 6; Flask lines 186–202. | Channel index, not keV. | Notebook assumes 360×8192×48 and uses `argmax`; Flask assumes the largest dimension is channel and uses `nanargmax`. Empty/all-NaN spectra would fail in Flask. | Channel at the maximum of the archive-provided count distribution. It can describe spectral-shape unusualness in channel space. It is not a calibrated line energy or physical spectral peak. | **REASONABLE PROXY** |
| 4 | `t1A_energy_weighted_mean_channel` | Same EnergyRes cube | For channel values \(c\) and collapsed counts \(n_c\), \(\sum c n_c/\sum n_c\). Notebook 08 cell 6; Flask helper lines 58–70 and call lines 203–206. | Channel, not keV. | Nonpositive total returns NaN in Flask. Negative bin content is not rejected before the weighted moment. | Count-weighted centroid in channel space. Any energy interpretation requires a verified channel-to-energy calibration. | **REASONABLE PROXY** |
| 5 | `t1A_energy_weighted_std_channel` | Same EnergyRes cube | \(\sqrt{\sum (c-\bar c)^2n_c/\sum n_c}\). Same locations as feature 4. | Channel-width units. | Same total-count and possible negative-content caveats as feature 4; numerical radicand validation is absent. | Width of the collapsed distribution in channel space, not calibrated energy resolution or source spectral width. | **REASONABLE PROXY** |
| 6 | `t1A_energy_high_channel_fraction` | Same EnergyRes cube | \(\sum_{c\ge4000}n_c/\sum_c n_c\). Notebook uses `channel_profile[4000:]`; Flask lines 208–209. | Dimensionless fraction. | Threshold 4000 is hard-coded and index-based; no energy-boundary metadata is consulted. Nonpositive/zero total is not explicitly rejected in the notebook and zero returns NaN through `safe_div`. | Fraction of collapsed counts in channels 4000–8191. Calling this a “high-energy fraction” is unsafe until the channel-energy mapping and valid channel range are approved. | **REQUIRES DOMAIN APPROVAL** |
| 7 | `t1A_energy_channel_entropy` | Same EnergyRes cube | Remove nonfinite and nonpositive collapsed-bin values; normalize remaining values \(p_c=n_c/\sum n_c\); compute \(-\sum p_c\log_2p_c\). Helper: Flask lines 36–45; Notebook 08 cell 5. | Bits; dimensionless but dependent on channel binning and number of occupied bins. | Returns NaN when no positive bins. Not normalized by \(\log_2 N\); ignores zero/negative values. | Dispersion/concentration summary of the channel-count distribution. It is not thermodynamic entropy or physical source disorder. | **REASONABLE PROXY** |
| 8 | `t1A_energy_anode_balance_cv` | Same EnergyRes cube | Collapse roll and channel axes to 48 anode totals; `std(anode_totals)/mean(anode_totals)`. Notebook 08 cell 6; Flask lines 212–220. | Dimensionless ratio. | Notebook assumes axis 2 is anode. Flask chooses the first dimension of length 48 or returns NaN if none. It does not confirm detector/anode identity from FITS metadata. | Relative spread of counts among the 48 array positions. “Anode-count balance proxy” is supportable. Detector health, gain, or efficiency causes are unverified. | **REQUIRES DOMAIN APPROVAL** |
| 9 | `t1B_src_peak_to_median_roll` | `Polix_l2_polarization\*_Src_Azimuth_Roll_L2.fits`, explicitly excluding `EnergyRes`; `ANODE_COUNTS` | Sum 48 anodes for each roll bin; `max(roll_sum)/median(roll_sum)`. Notebook 08 cell 6; Flask lines 225–237. | Dimensionless ratio. | Expected 360×48. Flask uses NaN-aware statistics; zero/nonfinite median yields NaN. A low median makes the ratio unstable. | Peakiness of the released source-azimuth count profile over roll bins. The product name does not justify interpreting a peak as polarization. | **REASONABLE PROXY** |
| 10 | `t1B_src_roll_entropy` | Same source-azimuth product and `ANODE_COUNTS` | Entropy helper applied to the 360 roll-bin sums: \(-\sum p_r\log_2p_r\). Notebook 08 cell 6; Flask lines 236–239. | Bits; dimensionless and binning-dependent. | Positive finite bins only; unnormalized; does not use exposure correction; ignores zero/negative bins. | Concentration/dispersion of source-azimuth counts across the archived roll-bin order. It is not polarization significance or randomness. | **REASONABLE PROXY** |
| 11 | `t1B_src_roll_smoothness_norm` | Same source-azimuth product and `ANODE_COUNTS` | Mean absolute first difference between consecutive roll-bin sums divided by their mean. Notebook first creates `t1B_src_roll_smoothness`, then normalizes in cell 10; Flask helpers lines 48–55 and lines 235–239. | Dimensionless ratio. | Requires at least two finite values. Filtering nonfinite values before differencing can join formerly nonadjacent bins. The difference between the final and first roll bin is omitted, although azimuth is circular. Row order is assumed to be roll order and angles are not explicitly sorted. | Local roughness proxy for the stored sequence. “Smoothness” should be qualified as non-circular, order-dependent first-difference roughness. | **REQUIRES DOMAIN APPROVAL** |
| 12 | `t2_lc_rate_cv` | `Polix_l2_lcpha\*_EventdataSource_L2.lc`, `RATE` | `std(RATE)/mean(RATE)`. Notebook 08 cell 6; Flask lines 244–253. | Dimensionless ratio; underlying `RATE` unit is not needed for the ratio but was **NOT VERIFIED** from headers. | Number and duration of bins vary by product/observation (**NOT VERIFIED**). Flask ignores NaNs but does not filter bins by `FRAC_EXP`, `QUALITY`, GTI, rate uncertainty, or exposure. Zero/nonfinite mean returns NaN. | Descriptive coefficient of variation of the delivered source light-curve rate array. It must not be called intrinsic source variability without time-bin, GTI, fractional-exposure, background, and product-suitability review. | **REQUIRES DOMAIN APPROVAL** |
| 13 | `t2_lc_peak_to_median_rate` | Same event light curve, `RATE` | `max(RATE)/median(RATE)`. Notebook 08 cell 6; Flask lines 249–254. | Dimensionless ratio. | Same unfiltered-bin caveats as feature 12. Zero/nonfinite median returns NaN; isolated bins can dominate the maximum; errors are unused. | Peakiness of the delivered rate array only. A flare, burst, or astrophysical variability claim is unsafe without time-series quality analysis. | **REQUIRES DOMAIN APPROVAL** |
| 14 | `t2_det_lc_rate_balance_cv` | Four detector products `Polix_l2_polarization\*_ProcessedEventdataSource_Det{1..4}_L2.lc`, `RATE` | Compute mean `RATE` per located detector; then `std(detector_means)/mean(detector_means)`. Notebook globs detector files; Flask lines 259–280. | Dimensionless ratio. | Notebook expects the glob results; Flask silently uses any located subset and can produce 0 from one detector. Neither code aligns time bins, applies `FRAC_EXP`/quality filters, weights by exposure/errors, nor verifies all four were present. | Cross-detector spread of delivered mean rates. It is not a calibrated detector-efficiency or health metric. Comparability of detector products requires approval. | **REQUIRES DOMAIN APPROVAL** |
| 15 | `t2_det_pha_centroid_spread` | Four detector products `Polix_l2_polarization\*_ProcessedEventdataSource_Det{1..4}_L2.pha`, `CHANNEL`, `COUNTS` | For each detector, compute count-weighted mean channel; feature is the population standard deviation of those centroids. Notebook 08 cell 6; Flask lines 262–280. | Channel units, not keV. | Flask uses any located subset; one centroid gives 0. Nonpositive totals yield NaN, and `nanstd` can hide missing centroids. No grouping, response, gain alignment, quality, or background check is performed. | Spread of detector PHA centroids in raw channel coordinates. It must not be presented as spectral disagreement, gain shift, energy offset, or detector malfunction without calibration and domain review. | **REQUIRES DOMAIN APPROVAL** |

## 3. Verified implementation facts

- Matrix C has exactly 15 numeric features plus `observation_id`.
- It contains 8 Tier-1A features, 3 Tier-1B source-azimuth diagnostics, and 4 Tier-2 supporting features.
- WeightedRoll features are not columns of Matrix C.
- The channel-profile features from EnergyRes and the event-PHA features were found to be treated as redundant during Notebook 08 matrix construction; the standalone event-PHA summaries were dropped, while only the detector-centroid spread was retained.
- No imputation occurs in `feature_extractor.py`; the function can emit NaN. Whether downstream prediction performs imputation is outside this agent’s scope.
- The implementations use population standard deviation (`numpy.std`, default `ddof=0`), not sample standard deviation.
- No Matrix-C feature uses measurement uncertainties as weights.

## 4. Evidence versus interpretation

### Directly evidenced

- Product filenames, FITS fields, aggregation formulas, thresholds, and the final column set are evidenced by code.
- Matrix C is an engineered observation-level table: one row per archived observation and 15 summaries per row.
- WeightedRoll separation is evidenced by Notebook 08’s separate `matrix_WR_cols`.

### Interpretation requiring restraint

- “Exposure uniformity,” “anode balance,” “source roll smoothness,” “light-curve variability,” and “detector balance” are convenient engineering labels. The code establishes only the numerical summaries.
- A change in any feature can reflect source signal, exposure pattern, detector response, processing choices, statistics, background, missing/invalid bins, or their combination. The implementation does not identify cause.
- No EnergyRes/PHA channel feature is an energy in keV.
- No roll-profile feature by itself is polarization evidence.

## 5. Unresolved semantic and implementation issues

1. **Energy-channel mapping — NOT VERIFIED.** The hard-coded channel 4000 boundary has no calibration reference in code. Guide/POLIX-domain approval is required before using “high energy.”
2. **EnergyRes axis contract — NOT VERIFIED archive-wide.** Notebook assumes 360×8192×48. Flask uses largest-dimension and length-48 heuristics rather than FITS axis metadata.
3. **Exposure field discovery mismatch.** Notebook requires four named detector columns; Flask accepts every column containing case-sensitive `Exposure` or uppercase `EXPOSURE`. The two paths can diverge on changed schemas.
4. **Circular roll geometry omitted.** Source smoothness excludes the 359°–0° closing difference and does not explicitly sort by roll angle.
5. **Entropy is not normalized.** Comparisons are valid only if binning/coverage are comparable; that comparability is **NOT VERIFIED** for every product.
6. **Light-curve suitability — NOT VERIFIED.** The feature code ignores `FRAC_EXP`, bin errors, quality flags, GTIs, possible background contribution, and differing bin sizes/durations. Features 12–13 must remain archive-product summaries.
7. **Detector-product comparability — NOT VERIFIED.** Features 14–15 do not confirm all four detectors, common exposure, aligned GTIs, common gain/channel-energy scale, or valid response/calibration.
8. **Negative values.** The weighted moment functions do not reject negative count bins; entropy silently discards them. Whether negative values occur in these released products is **NOT VERIFIED**.
9. **Missing detector files.** Flask can return deceptively finite values from a subset, including zero spread for one detector. A validation check requiring all four products is absent.
10. **Semantic use of “source.”** A filename containing `Source` does not establish complete official background subtraction. Any claim that these are source-only physical quantities requires handbook/domain approval.

## 6. Unsafe manuscript claims

The following formulations are not supported by Matrix-C feature code:

- peak channel equals a physical spectral peak or line energy;
- channel 4000 defines a scientifically calibrated high-energy band;
- light-curve CV measures intrinsic source variability;
- detector-balance features diagnose detector health, gain drift, or malfunction;
- source-roll peakiness, entropy, or smoothness indicates polarization;
- any feature identifies the physical cause of an anomaly;
- the primary model uses WeightedRoll or independently confirms modulation.

Safe wording is: “engineered channel-space, roll-profile, light-curve-array, exposure-pattern, and cross-detector summary features from the released Level-2 products.”

## 7. Disagreements and decisions for the controlling register

| ID | Issue | Code evidence | Audit position |
|---|---|---|---|
| FS-D01 | Matrix C is sometimes described as “LC/PHA context.” | Its four Tier-2 columns include two event-light-curve summaries, one detector-light-curve summary, and one detector-PHA centroid-spread summary; no standalone event-PHA feature remains. | Use “light-curve and detector-PHA context,” not a claim that Matrix C contains a general PHA spectrum representation. |
| FS-D02 | Feature 6 name says `high_channel_fraction`, while prose may say “high-energy fraction.” | The threshold is the integer channel index 4000 with no calibration lookup. | “High-channel fraction” is allowed; “high-energy fraction” requires domain approval. |
| FS-D03 | `t1B_src_roll_smoothness_norm` may be described as azimuthal smoothness. | The calculation is a linear first-difference statistic with no circular closing term or angle sort. | Describe the exact computation; do not imply a complete circular smoothness measure. |
| FS-D04 | Detector-balance values may be interpreted as four-detector comparisons. | Notebook likely uses four files, but Flask does not enforce four and can use a subset. | The frozen CSV can be described as archive-derived; general deployment claims must disclose the missing-product behavior or add validation in a future implementation. |
| FS-D05 | Channel summaries may be described as spectral features. | They are moments and entropy of counts over raw channel index. | “Channel-distribution features” is preferred. “Spectral-shape proxies in channel space” is acceptable with the calibration caveat. |

## 8. Audit conclusion

The 15-feature Matrix-C schema and its numerical construction are traceable and internally coherent as an engineered screening representation. Eleven features are direct exposure-, channel-, or roll-profile summaries; four add light-curve and cross-detector context. Their use for relative, archive-specific unsupervised screening is technically understandable. However, nine features remain proxies whose scientific meaning depends on unverified product semantics or calibration, with the strongest concerns applying to the channel-4000 threshold, light-curve variability language, detector comparison, and the non-circular smoothness statistic. These issues do not invalidate the computed matrix, but they constrain the manuscript to descriptive feature language and require guide/POLIX-domain approval for stronger physical interpretation.
