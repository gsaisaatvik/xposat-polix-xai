# Product-Aware Explainable Anomaly Screening with Blank-Sky Modulation Diagnostics for XPoSat POLIX Level-2 Observations

**Author One**, **Author Two**, **Author Three**, and **Project Guide**  
Department of [Department Name], [College/University], [City, Country]  
Email: [corresponding-author email]

## Abstract

The Polarimeter Instrument in X-rays (POLIX) aboard the X-ray Polarimeter Satellite (XPoSat) produces heterogeneous Level-2 products whose scientific roles differ across exposure, energy-resolved azimuth, source azimuth, light-curve, detector, and roll-resolved measurements. This paper investigates whether those products can support interpretable, label-free observation screening while retaining a scientifically independent physical diagnostic. A product-aware representation was constructed for 25 POLIX Level-2 observations included in the project archive: 10 source observations and 15 blank-sky observations. The deployed 15-feature Matrix-C representation is standardized and analyzed using principal component analysis, KMeans, and Isolation Forest. A model-specific explanation score combines PCA separation, assigned-centroid distance, Isolation Forest feature occlusion, and standardized feature abnormality, then maps influential features to their originating product families. The fixed model flagged four anomaly candidates; three remained flagged across all 100 tested Isolation Forest seeds, whereas the fourth was seed-sensitive. Neutralization tests reproduced five Strong and one Moderate faithfulness verdict over a separate six-case exploratory set. An independent WeightedRoll branch fitted second-harmonic modulation and compared normalized \(Q/U\) coefficients with 13 qualifying blank-sky fits. All ten source raw-modulation values were within the empirical blank-sky range. These results show that archive-relative statistical unusualness and polarization-like modulation evidence are related inspection questions but are not equivalent. The analysis is a small-sample screening study and does not report calibrated polarization degree or official sky polarization angle.

**Index Terms—** XPoSat, POLIX, X-ray polarimetry, unsupervised anomaly detection, explainable artificial intelligence, scientific machine learning.

## I. Introduction

The X-ray Polarimeter Satellite (XPoSat) is an Indian Space Research Organisation mission dedicated to X-ray polarimetry and spectroscopy [1], [5]. Its Polarimeter Instrument in X-rays (POLIX) is a Thomson-scattering polarimeter whose Level-2 archive exposes several product families rather than a single homogeneous table [2], [6], [7]. These products describe complementary aspects of an observation: roll-dependent exposure, energy-resolved azimuthal behavior, source azimuth, temporal rate variability, detector balance, and exposure-weighted roll modulation. Their different physical and computational roles make direct archive-level comparison difficult.

The completed B.Tech project addressed this problem as an applied scientific-computing task. It converted each observation into interpretable summary features, used unsupervised learning to screen observations without anomaly labels, produced observation-specific feature explanations, and exposed the results through a researcher-facing Flask application. A separate physical branch fitted the WeightedRoll modulation product and compared source behavior with the blank-sky observations present in the same archive. The separation between these branches is important. WeightedRoll contains source and background modulation contributions [2]; it is not assumed here to be an officially background-corrected polarization product. Conversely, a multivariate anomaly flag need not indicate a polarization-like signature.

Archive screening has precedents in astronomy [12], [13], while principal component analysis (PCA), KMeans, and Isolation Forest are established methods [9]–[11]. General local-explanation and anomaly-explanation literature also provides relevant concepts [14]–[16]. However, the reviewed literature did not provide a directly comparable framework combining POLIX Level-2 product-aware representation, model-specific unsupervised explanation, perturbation-based faithfulness checks, and an independent blank-sky-referenced modulation branch. This statement is a scoped literature finding, not a priority claim.

The research question is: *Can heterogeneous POLIX Level-2 data products be represented through scientifically interpretable features and screened using explainable unsupervised learning, while preserving a scientifically independent comparison with blank-sky-referenced physical modulation behavior?*

This paper makes five bounded contributions:

1. It specifies a 15-feature observation representation spanning exposure, energy-resolved azimuth, source azimuth, temporal variability, and detector balance.
2. It applies complementary geometric, clustering, and isolation-based evidence to label-free screening of the 25 observations included in the project archive.
3. It defines a four-component, model-specific feature-attribution score and maps local drivers back to POLIX product families.
4. It reproduces a feature-neutralization faithfulness test and evaluates seed, contamination, leave-one-out, feature-tier, and ranking stability.
5. It keeps exposure-weighted WeightedRoll fitting and empirical blank-sky \(Q/U\) comparison outside the deployed anomaly input, permitting a non-circular comparison between statistical unusualness and modulation behavior.

The web application is treated as an implementation and reproducibility contribution. No result is presented as an astrophysical discovery, an officially confirmed anomaly, calibrated polarization degree (PD), or official sky polarization angle (PA).

## II. Related Work

### A. XPoSat, POLIX, and X-Ray Polarimetry

Official mission and archive sources define XPoSat and POLIX, while the POLIX user handbook documents the Level-2 product semantics and current analysis boundaries [1]–[4]. Thomson-scattering polarimetry and the broader instrumentation context are described in [6], [7]. Modulation curves encode a second-harmonic response in azimuth, but the inference of calibrated polarization requires instrument response, background treatment, and coordinate conventions. Stokes-based analysis provides a useful linear representation through cosine and sine coefficients [8].

For the released products examined here, the handbook is particularly consequential. It describes WeightedRoll as including source and background count-rate modulation and cautions that the source/blank-sky configuration in the current release is insufficient for a polarization measurement [2]. The physical branch in this paper therefore reports raw modulation, fitted modulation phase, fit quality, and empirical blank-sky-relative quantities only.

### B. Unsupervised Anomaly Screening in Astronomy

Astronomical archives are frequently label-poor and high-dimensional. Unsupervised outlier ranking can prioritize unusual objects for expert inspection, as illustrated by work on unusual Sloan Digital Sky Survey galaxies [12]. Astronomaly combines anomaly detection with active learning and human feedback [13]. These studies motivate candidate ranking rather than automatic scientific classification.

The present archive is much smaller and its unit of analysis is an observation assembled from multiple POLIX products. Consequently, conventional held-out predictive accuracy is neither available nor appropriate. The relevant questions are reproducibility, sensitivity to modeling choices, interpretability of the selected features, and agreement or disagreement with an independent physical diagnostic.

### C. Explainable Anomaly Detection and Faithfulness

SHAP is a widely used general explanation framework [14], but it is not the deployed method in this project. Instead, the explanation is constructed directly from the fitted PCA, KMeans, and Isolation Forest components. Reviews of anomaly explanation emphasize that explaining an unusual instance differs from explaining a supervised class decision [15]. An explanation should also be evaluated behaviorally rather than accepted from visual plausibility alone. Perturbation-based infidelity and sensitivity concepts motivate checking whether modifying influential features changes model evidence [16].

The project’s faithfulness test neutralizes high-ranked standardized features and recomputes PCA distance and Isolation Forest score. This test is narrower than a general causal claim: it measures consistency between the explanation ranking and this fitted model’s behavior.

### D. Product-Aware Representation

Multi-view representation learning studies how multiple information views can be combined [18]. This project uses a simpler, traceable approach appropriate to \(n=25\): domain-named summary statistics are grouped by product family, and feature tiers are compared explicitly. This preserves provenance at the cost of not learning a representation end to end.

## III. Data and Problem Formulation

### A. Data Freeze

The data freeze is dated 27 July 2026. It contains 25 POLIX Level-2 observations included in the project archive: 10 source observations and 15 blank-sky observations. The source set represents Crab (three observations), Sco X-1, Her X-1, GX 301-2, Cyg X-1, 4U 1700-37, Cen X-3, and Cas-A SNR. “Blank Sky-2” occurs as a repeated display label for two distinct observation identifiers; identifiers, not display labels, are used as keys.

**Table I — Dataset composition**

| Role | Observations | Use in this study |
|---|---:|---|
| Source | 10 | Archive screening and physical comparison |
| Blank sky | 15 | Archive screening; 13 qualifying fits define the empirical \(Q/U\) reference |
| Total | 25 | All processed by both branches |

No trusted observation-level anomaly labels are available. The learning problem is therefore archive-relative ranking and candidate screening, not supervised classification. “Anomaly” in model output means statistically unusual relative to this 25-observation feature distribution.

### B. Product Families

The inspected products provide four computational groups. Tier 1A contains roll-exposure and energy-resolved azimuth summaries. Tier 1B contains source-azimuth summaries. Tier 2 contains light-curve and detector diagnostics. WeightedRoll (WR) supplies an exposure-weighted modulation curve containing source and background contributions [2]. WR is excluded from Matrix C and analyzed only in the independent physical branch.

The separation prevents a circular argument in which modulation behavior both helps produce an anomaly flag and is then used to “confirm” that same flag. It also avoids treating an empirically blank-sky-referenced residual as official background subtraction.

## IV. Product-Aware Feature Engineering

### A. Feature Tiers

Four matrices were frozen. Matrix A contains eight exposure and energy-resolved features. Matrix B adds three source-azimuth features. Matrix C adds four temporal and detector-supporting features and is the deployed 15-feature input. WR contains six modulation diagnostics and is not part of the primary model.

**Table II — Matrix-C feature representation**

| Product family | Feature | Interpretation |
|---|---|---|
| Exposure | `t1A_exp_uniformity_cv` | Roll-exposure coefficient of variation |
| Exposure | `t1A_exp_max_to_min_roll` | Maximum-to-minimum roll exposure ratio |
| Energy-resolved azimuth | `t1A_energy_peak_channel` | Channel with greatest summarized response |
| Energy-resolved azimuth | `t1A_energy_weighted_mean_channel` | Response-weighted channel mean |
| Energy-resolved azimuth | `t1A_energy_weighted_std_channel` | Response-weighted channel spread |
| Energy-resolved azimuth | `t1A_energy_high_channel_fraction` | Fraction assigned to high channels |
| Energy-resolved azimuth | `t1A_energy_channel_entropy` | Channel-distribution entropy |
| Energy-resolved azimuth | `t1A_energy_anode_balance_cv` | Across-anode balance variability |
| Source azimuth | `t1B_src_peak_to_median_roll` | Peak-to-median roll ratio |
| Source azimuth | `t1B_src_roll_entropy` | Roll-distribution entropy |
| Source azimuth | `t1B_src_roll_smoothness_norm` | Normalized roll roughness/smoothness diagnostic |
| Light curve | `t2_lc_rate_cv` | Rate coefficient of variation |
| Light curve | `t2_lc_peak_to_median_rate` | Peak-to-median temporal rate |
| Detector light curve | `t2_det_lc_rate_balance_cv` | Detector-rate balance variability |
| Detector PHA | `t2_det_pha_centroid_spread` | Spread of detector pulse-height centroids |

All four frozen matrices have 25 rows and no missing values. Although the reviewed project report mentioned median imputation, neither the saved model artifact nor the deployed inference code contains an imputer. The manuscript therefore makes no imputation claim. Future inputs with missing values require an explicit policy before inference.

### B. Matrix-C Rationale

Matrix C retains human-interpretable statistics and broadens the representation beyond exposure and energy behavior. It was selected in the completed project as the deployed input. This paper does not claim that it is universally optimal. The new ablation shows that feature tier affects thresholded candidates even when overall anomaly rankings are similar, so the matrix choice is itself a source of uncertainty.

## V. Explainable Unsupervised Screening

### A. Preprocessing and Model Components

For observation \(i\), the 15-vector \(\mathbf{x}_i\) is transformed using the saved `StandardScaler`. PCA projects the standardized vector \(\mathbf{z}_i\) into two components [9]. In the frozen model, these components explain 38.74% and 22.51% of the variance, respectively. KMeans with \(k=5\), `n_init=20`, and random state 42 assigns a local centroid [10]. Isolation Forest with 100 trees, contamination 0.16, and random state 42 provides the deployed candidate decision and score [11]. The score is not a probability.

PCA, KMeans, and Isolation Forest are complementary components, not ground-truth adjudicators. PCA measures projected separation, KMeans describes distance from assigned local structure, and Isolation Forest supplies the fixed deployed threshold. The contamination value imposes an approximate candidate fraction and is evaluated for sensitivity rather than interpreted as a known prevalence.

### B. Four-Component Local Attribution

For feature \(j\), the PCA separation contribution is

\[
p_{ij}=\sum_{r=1}^{2}\left|z_{ij}w_{rj}\right|\lambda_r ,
\]

where \(w_{rj}\) is the loading and \(\lambda_r\) is the explained-variance ratio of component \(r\). The KMeans term is the squared feature-wise displacement from the assigned centroid,

\[
k_{ij}=(z_{ij}-c_{g(i)j})^2 .
\]

The Isolation Forest occlusion term compares the anomaly score before and after setting feature \(j\) to zero in standardized space,

\[
o_{ij}=s(\mathbf{z}_i)-s(\mathbf{z}_i^{(j\leftarrow0)}).
\]

The fourth term is standardized feature abnormality \(a_{ij}=|z_{ij}|\). Each feature-wise component is normalized by its maximum absolute value within the observation. Only positive Isolation Forest deltas are retained. The combined score is

\[
e_{ij}=N(p_{ij})+N(k_{ij})+N(\max(o_{ij},0))+N(a_{ij}),
\]

and the five largest scores are returned. This is a heuristic attribution tailored to the deployed stack; it is not SHAP and does not confer causal meaning. Product-family mapping turns a raw feature name into an exposure, energy, source-azimuth, light-curve, or detector explanation.

The researcher-facing sentence is produced by deterministic Python templates from the prediction, score, feature names, directions, and standardized values. It is not generated by a large language model.

### C. Faithfulness Test

The exploratory faithfulness set contains six candidates and predates the fixed deployed four-candidate output. For each case, its top-ranked features are neutralized to zero in standardized space. A Strong verdict requires reductions in both PCA distance and Isolation Forest anomaly score; Moderate denotes a partial response. This is an internal perturbation test and not a validation against physical ground truth.

## VI. Independent Physical Modulation Diagnostics

### A. WeightedRoll Fit

For roll-bin center \(\phi\), WeightedRoll is fitted by weighted least squares to

\[
y(\phi)=C+Q\cos(2\phi)+U\sin(2\phi),
\]

using inverse-variance weights. The raw modulation fraction is

\[
m_{\mathrm{raw}}=\frac{\sqrt{Q^2+U^2}}{C},
\]

and the fitted modulation phase is

\[
\psi_{\mathrm{fit}}=\frac{1}{2}\operatorname{atan2}(U,Q).
\]

Here \(C,Q,U\) are fit coefficients, not official calibrated sky Stokes products. The reported phase is not official sky PA. Reduced chi-square is used only as a simple-fit diagnostic: acceptable for \(\chi_\nu^2\le2\), caution for \(2<\chi_\nu^2\le5\), and poor otherwise.

### B. Empirical Blank-Sky Reference

Normalized coefficients \(q=Q/C\) and \(u=U/C\) are compared with empirical blank-sky means. Thirteen of the 15 blank-sky fits meet the `acceptable` criterion and define

\[
\bar q_{\mathrm{blank}}=0.0090920,\qquad
\bar u_{\mathrm{blank}}=-0.0064782,
\]

with sample standard deviations 0.0048569 and 0.0040190. A standardized two-dimensional distance summarizes displacement from that empirical center. This operation is an archive-specific diagnostic, not official POLIX background subtraction.

The code also tabulates PD sensitivity proxies for assumed \(\mu_{100}\) scenarios of 0.40, 0.42, and 0.44. These values are hypothetical sensitivity settings only. They are not an official POLIX \(\mu_{100}\), and the resulting ratios are not calibrated PD measurements.

## VII. Experimental Protocol

The fixed artifact was first replayed against the frozen Matrix-C file. Predictions, Isolation Forest scores, PCA coordinates, KMeans labels, and local explanations were reproduced. For Sco X-1, an exact imported-function audit was adopted as the controlling versioned evidence after it agreed with Notebook 10 and the supplementary reproduction. Supplementary experiments were then executed without altering original artifacts.

Random-seed stability refitted the Isolation Forest for seeds 0–99 while holding Matrix C, scaling, 100 trees, and contamination 0.16 fixed. Contamination sensitivity used 0.12, 0.16, 0.20, and 0.24 with seed 42. The leave-one-out experiment omitted each observation, refit the scaler and Isolation Forest on the remaining 24, and compared common-observation rankings with the full-data fit. Feature-tier ablation applied the same basic PCA, KMeans, and Isolation Forest settings to A, B, C, and the separate WR diagnostic matrix. Ranking agreement used Spearman correlation among PCA distance, assigned-centroid distance, and Isolation Forest score. The original faithfulness computation was independently reconstructed from the model and feature-contribution files.

The audit ran under Python 3.11.0, NumPy 2.4.6, pandas 3.0.3, scikit-learn 1.9.0 [17], SciPy 1.17.1, Astropy 8.0.1, and Flask 3.1.3. These are the audit versions, not necessarily the original training versions; the project requirements file is unpinned. The small \(n\) prevents a conventional train/test generalization study. All statistics are descriptive or sensitivity-oriented.

## VIII. Results

### A. Matrix Comparison

**Table III — Feature-tier comparison**

| Matrix | Features | PC1+PC2 variance | Silhouette | Fixed-seed Isolation Forest candidates |
|---|---:|---:|---:|---|
| A | 8 | 0.7518 | 0.4133 | C24_0018, C24_0020, G01_0006, P01_0005 |
| B | 11 | 0.7570 | 0.3586 | C24_0010, C24_0018, C24_0020, G01_0006 |
| C | 15 | 0.6125 | 0.3109 | C24_0010, C24_0018, G01_0003, G01_0006 |
| WR | 6 | 0.9484 | 0.4848 | C24_0023, G01_0003, G01_0004, T24_0007 |

The A/B/C Isolation Forest rankings correlate at 0.913–0.952, but their thresholded candidate-set Jaccard agreement is 0.333–0.600. Thus, broad rankings are similar while membership near the imposed threshold changes. The WR row is reported as a separate diagnostic and is not used to confirm Matrix-C candidates.

PCA distance and Isolation Forest score show strong rank agreement (\(\rho=0.8946\), two-sided \(p=1.64\times10^{-9}\)). KMeans centroid distance has weak, nonsignificant rank association with PCA distance (\(\rho=0.1558\), \(p=0.457\)) and Isolation Forest score (\(\rho=0.1866\), \(p=0.372\)). KMeans therefore contributes different local structure; it should not be called an independent anomaly classifier.

### B. Deployed Candidates and Robustness

The saved Matrix-C model reproduced 21 Normal outputs and four anomaly candidates.

**Table IV — Fixed-model candidates and leading local XAI evidence**

| Observation | Role/target | Isolation score | Leading deployed XAI evidence | Seed flags |
|---|---|---:|---|---:|
| C24_0018 | Blank Sky-13 | 0.615964 | Energy weighted standard channel | 100/100 |
| G01_0006 | Sco X-1 | 0.593516 | Peak channel 2.454499; weighted mean 2.207369; entropy 1.813968 | 100/100 |
| G01_0003 | Her X-1 | 0.572308 | Light-curve rate CV | 100/100 |
| C24_0010 | Blank Sky-5 | 0.517611 | Source-roll smoothness | 29/100 |

The first three cases were also selected under all four tested contamination settings and in all 24 leave-one-out refits in which each remained in the fitting set. C24_0010 was selected in three of four contamination settings and 19 of 24 included jackknife refits, but only 29 of 100 random-seed fits. C24_0020, not in the fixed deployed four, was selected in 68 seed runs, two contamination settings, and 7 of 24 included jackknife refits. Candidate interpretation should therefore emphasize a stable three-case core and an uncertain threshold neighborhood rather than treating the fixed four as equally robust.

Across leave-one-out runs, the Spearman correlation of common-observation anomaly scores had median 0.9896 and minimum 0.9687. The overall ranking is stable despite local changes near the threshold.

### C. Explanation Faithfulness

The reconstruction matched the stored faithfulness metrics to within \(9\times10^{-16}\) and reproduced five Strong, one Moderate, and zero Weak verdicts. C24_0023 was Moderate because neutralization reduced PCA distance but not the Isolation Forest score. This result supports behavioral consistency for the tested exploratory cases, but its six observations must not be conflated with the deployed four.

### D. Physical and Blank-Sky Diagnostics

All 25 WeightedRoll products were fitted. Nineteen fits were acceptable, three caution, and three poor. Among the 15 blank-sky observations, 13 were acceptable, one caution, and one poor. The 13-fit empirical blank-sky raw-modulation mean was 1.147820%, with sample standard deviation 0.565960%, median 1.492835%, and range 0.294127–1.778927%.

**Table V — Source modulation and blank-sky-relative diagnostics**

| Target (observation) | Raw modulation (%) | Fit quality; \(\chi_\nu^2\) | Blank-sky vector distance | Interpretation boundary |
|---|---:|---|---:|---|
| Her X-1 (G01_0003) | 0.5966 ± 0.0167 | Poor; 57.4335 | 2.3174 | Moderate displacement, low confidence |
| Sco X-1 (G01_0006) | 1.1396 ± 0.0199 | Caution; 2.0308 | 0.3005 | Within empirical scatter |
| Crab (P01_0005) | 1.6973 ± 0.0310 | Acceptable; 1.0625 | 1.2649 | Within empirical scatter |
| GX 301-2 (G01_0004) | 0.7223 ± 0.0295 | Caution; 4.3745 | 1.2514 | Within empirical scatter |
| Cyg X-1 (T24_0007) | 0.6811 ± 0.0153 | Poor; 5.4080 | 1.1480 | Within empirical scatter |
| Crab (T24_0001) | 1.3955 ± 0.0627 | Acceptable; 0.8146 | 1.1352 | Within empirical scatter |
| Cas-A SNR (C24_0026) | 0.6927 ± 0.0294 | Acceptable; 1.7030 | 0.9385 | Within empirical scatter |
| Cen X-3 (G01_0002) | 0.9286 ± 0.0220 | Acceptable; 1.8972 | 0.7748 | Within empirical scatter |
| 4U 1700-37 (G01_0005) | 1.0806 ± 0.0581 | Acceptable; 1.2291 | 0.6305 | Within empirical scatter |
| Crab (T24_0002) | 1.2008 ± 0.0220 | Acceptable; 1.3671 | 0.5152 | Within empirical scatter |

All ten source scalar raw-modulation z-scores lie between -0.974 and 0.971 relative to the empirical blank-sky baseline and are classified within its range. These are raw diagnostic values, not calibrated PD.

### E. End-to-End Implementation

The Flask application connects feature extraction, saved-model inference, deterministic explanations, physical diagnostics, visualization, and result export. Input feature order is checked against the artifact. The implementation makes observation-level and product-family evidence inspectable, but it remains a proof-of-concept deployment. Browser-level export testing and an environment lock remain pending.

## IX. Discussion

The main empirical finding is that statistical unusualness and polarization-like modulation evidence are not equivalent.

Her X-1 is part of the stable Matrix-C anomaly core, with light-curve rate variability as its leading local driver. Its normalized \(Q/U\) vector has the largest source displacement from the blank-sky center (2.3174), but the simple second-harmonic fit is poor (\(\chi_\nu^2=57.4335\)). The physical result therefore cannot be used as clean confirmation; it instead indicates that a simple sinusoid is an inadequate summary for that WeightedRoll curve.

Sco X-1 is also a stable Matrix-C candidate. Its accepted deployed XAI ranking is energy peak channel (2.454499), energy weighted mean channel (2.207369), and energy channel entropy (1.813968). The historical entropy-first narrative was not reproducible from a located versioned artifact and is superseded by the exact imported-function audit. The three leading features all arise from the energy-resolved product family; they identify local model evidence and do not establish a physical cause. Sco X-1’s physical vector distance is only 0.3005, and its raw modulation lies within empirical blank-sky scatter. This is the clearest example that a multivariate product anomaly can arise without unusual blank-sky-relative modulation.

Crab P01_0005 provides the converse comparison. It has the largest source raw modulation in this archive and an acceptable sinusoidal fit, yet it is not in the fixed Matrix-C candidate set and is selected in only 3 of 100 seed fits. Its physical vector remains within empirical blank-sky scatter. The value must not be described as a polarization detection.

Two blank-sky observations are in the fixed candidate set. Blank Sky-13 is part of the stable core and is explained mainly by energy spread. Blank Sky-5 is explained by source-roll smoothness but is seed-sensitive. Their presence demonstrates why the output is an archive-quality screening signal rather than a source-physics classifier. Instrumental, exposure, background, processing, or other causes would require targeted investigation; none is assigned here.

The complementary branches are therefore most useful as a triage table. An observation can be statistically unusual, physically displaced, both, or neither. Fit quality supplies a further gate on the physical branch. This structured disagreement is informative because it prevents a single score from carrying more scientific meaning than the evidence supports.

## X. Limitations and Threats to Validity

The sample contains only 25 observations from a project-specific archive. The same archive defines scaling, clusters, isolation structure, and retrospective results; there is no external holdout. Isolation Forest contamination 0.16 is a screening assumption rather than an estimated anomaly prevalence. Candidate membership is sensitive to feature tier and, near the threshold, random seed. There are no trusted anomaly labels, so accuracy, precision, recall, and superiority claims are unavailable.

The representation uses engineered summaries and may omit informative event-level, timing, spectral, calibration, or observation-context structure. The model can drift when new POLIX releases change product distributions. The original training software versions were not recoverable from a lockfile.

WeightedRoll includes source and background contributions. Blank-sky background varies, and the empirical mean/scatter used here is limited to 13 acceptable fits from this archive. No official source-specific background subtraction, flight-calibrated \(\mu_{100}\), or verified phase-to-sky-PA conversion was available. The scalar and vector comparisons therefore cannot establish calibrated PD or official PA. Poor fits further limit interpretation.

No domain expert has adjudicated the candidates, and no causal timing or spectral follow-up was executed. The web application is a proof of concept; operational validation, access control, long-term data provenance, browser-level export testing, and independent environment reconstruction remain future work.

## XI. Conclusion

This study demonstrates a reproducible, product-aware workflow for screening 25 POLIX Level-2 observations included in the project archive. A 15-feature Matrix-C representation supported PCA, KMeans, and Isolation Forest analysis; a four-component local attribution related each observation to interpretable features and product families; and perturbation tests reproduced the stored faithfulness verdicts. Supplementary tests identified three candidates stable across the tested seeds and contamination values while revealing uncertainty at the fixed-model boundary.

An independent WeightedRoll branch fitted raw second-harmonic modulation and compared normalized \(Q/U\) behavior with 13 qualifying blank-sky observations. All ten source raw-modulation values were within the empirical blank-sky range. Representative cases showed that archive-relative unusualness does not automatically imply polarization-like modulation, and modulation amplitude does not automatically imply a multivariate anomaly.

The work does not claim an astrophysical discovery, official anomaly ground truth, official background subtraction, calibrated PD, or official sky PA. Future work should evaluate new POLIX releases, freeze the software environment, incorporate official calibration and background products when available, test prospective data drift, and obtain domain-expert review.

## Acknowledgment

This publication uses the data from the XPoSat mission of the Indian Space Research Organisation (ISRO), archived at the Indian Space Science Data Centre (ISSDC) [4].

The authors also acknowledge [college/project guide/laboratory/funding details to be supplied and approved].

## References

[1] Indian Space Research Organisation, “XPoSat: India’s X-Ray Polarimetry Mission,” Nov. 2023. [Online]. Available: https://www.isro.gov.in/ISRO_EN/XPoSat_X-Ray_Polarimetry_Mission.html

[2] N. Anand, K. Rikame, and K. Roy, *XPoSat-POLIX User Handbook: User Guide for Scientific Data Analysis Level2*, ver. 1.0, Indian Space Research Organisation, Oct. 2025.

[3] Indian Space Science Data Centre, “ISRO Science Data Archive: XPoSat.” [Online]. Available: https://pradan1.issdc.gov.in/x01/index.xhtml

[4] Indian Space Science Data Centre, “XPoSat Acknowledgment Guidance.” [Online]. Available: https://pradan1.issdc.gov.in/x01/ack.xhtml

[5] H. Saini, K. V. Madhu, and R. Karidhal, “Mission analysis, design and operations plan of India’s first polarimetry satellite: X-Ray Polarimetry Satellite (XPoSat),” *Experimental Astronomy*, vol. 59, no. 2, art. 17, 2025, doi: 10.1007/s10686-025-09988-6.

[6] P. V. Rishin *et al.*, “Development of a Thomson X-Ray Polarimeter,” arXiv:1009.0846, 2010, doi: 10.48550/arXiv.1009.0846.

[7] S. Fabiani, “Instrumentation and future missions in the upcoming era of X-ray polarimetry,” *Galaxies*, vol. 6, no. 2, art. 54, 2018, doi: 10.3390/galaxies6020054.

[8] F. Kislat, B. Clark, M. Beilicke, and H. Krawczynski, “Analyzing the data from X-ray polarimeters with Stokes parameters,” *Astroparticle Physics*, vol. 68, pp. 45–51, 2015, doi: 10.1016/j.astropartphys.2015.02.007.

[9] K. Pearson, “On lines and planes of closest fit to systems of points in space,” *Philosophical Magazine*, vol. 2, no. 11, pp. 559–572, 1901, doi: 10.1080/14786440109462720.

[10] J. MacQueen, “Some methods for classification and analysis of multivariate observations,” in *Proc. Fifth Berkeley Symp. Mathematical Statistics and Probability*, vol. 1, 1967, pp. 281–297.

[11] F. T. Liu, K. M. Ting, and Z.-H. Zhou, “Isolation Forest,” in *Proc. IEEE ICDM*, 2008, pp. 413–422, doi: 10.1109/ICDM.2008.17.

[12] D. Baron and D. Poznanski, “The weirdest SDSS galaxies: Results from an outlier detection algorithm,” *MNRAS*, vol. 465, no. 4, pp. 4530–4555, 2017, doi: 10.1093/mnras/stw3021.

[13] M. Lochner and B. A. Bassett, “Astronomaly: Personalised active anomaly detection in astronomical data,” *Astronomy and Computing*, vol. 36, art. 100481, 2021, doi: 10.1016/j.ascom.2021.100481.

[14] S. M. Lundberg and S.-I. Lee, “A unified approach to interpreting model predictions,” in *Advances in Neural Information Processing Systems*, vol. 30, 2017, pp. 4765–4774.

[15] V. Yepmo, G. Smits, and O. Pivert, “Anomaly explanation: A review,” *Data & Knowledge Engineering*, vol. 137, art. 101946, 2022, doi: 10.1016/j.datak.2021.101946.

[16] C.-K. Yeh, C.-Y. Hsieh, A. Suggala, D. I. Inouye, and P. K. Ravikumar, “On the (in)fidelity and sensitivity of explanations,” in *Advances in Neural Information Processing Systems*, vol. 32, 2019, pp. 10965–10976.

[17] F. Pedregosa *et al.*, “Scikit-learn: Machine learning in Python,” *Journal of Machine Learning Research*, vol. 12, pp. 2825–2830, 2011.

[18] H. Hwang, G.-H. Kim, S. Hong, and K.-E. Kim, “Multi-view representation learning via total correlation objective,” in *Advances in Neural Information Processing Systems*, vol. 34, 2021.
