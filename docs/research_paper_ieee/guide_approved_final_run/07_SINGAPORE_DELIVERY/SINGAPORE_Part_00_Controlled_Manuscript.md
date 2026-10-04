# An Explainable AI Framework for Analysis of X-Ray Polarimetry Data from XPoSat

**[Student Author 1], [Student Author 2], [Student Author 3], and [Student Author 4]**

**[Department], [Institution], [City, Country]**  
**Email:** [author emails to be inserted after guide approval]

## Abstract

X-ray Polarimeter Satellite (XPoSat) observations from the Polarimeter Instrument in X-rays (POLIX) contain heterogeneous Level-2 products that are difficult to compare at the observation level. This study represents 25 observations in the project archive—10 project-labelled sources and 15 project-labelled blank skies—using 15 interpretable features derived from exposure, channel-space, source-azimuth, delivered-light-curve, and detector-balance products. Standardization, principal component analysis, KMeans, and Isolation Forest provide complementary archive-relative screening evidence, while a deterministic four-component local ranking links unusual observations to features and product families. The frozen Isolation Forest configuration labelled 21 observations Normal and flagged four candidates. Three candidates were selected under all 100 tested seeds; the fourth was seed-sensitive. A six-case feature-neutralization check provided bounded in-sample support for the ranking. WeightedRoll was excluded from the machine-learning input and analysed independently using weighted second-harmonic fits and a 13-fit empirical blank-sky reference. The machine-learning candidates and harmonic summaries did not agree one-to-one, indicating that statistical unusualness and modulation-like behaviour answer different diagnostic questions within this archive. The study does not report calibrated polarization degree, official sky polarization angle, anomaly ground truth, or future-data performance; its principal limitation is the small, retrospectively analysed archive without trusted labels.

**Index Terms—** XPoSat, POLIX, X-ray polarimetry, unsupervised anomaly detection, explainable artificial intelligence, scientific machine learning.

# I. Introduction

X-ray polarimetry adds orientation-dependent information to the timing and spectral views of energetic astronomical sources. The X-ray Polarimeter Satellite (XPoSat) carries the Polarimeter Instrument in X-rays (POLIX), a scattering polarimeter operating in the 8–30 keV range, together with the X-ray Spectroscopy and Timing payload [@isro_xposat]. POLIX uses a low-atomic-number scatterer surrounded by four proportional-counter detectors; the azimuthal distribution of scattered photons provides the physical basis for polarimetric analysis [@rishin2010thomson; @fabiani2018instrumentation]. Converting a measured modulation into calibrated polarization quantities requires response, background, uncertainty, and reference-frame treatment [@fabiani2018instrumentation; @kislat2015stokes]. This paper therefore separates computational screening from calibrated polarimetry.

POLIX Level-2 observation folders contain products with different dimensions and diagnostic roles: exposure versus roll, energy-resolved source azimuth, source azimuth, delivered source and detector light curves, detector pulse-height products, and WeightedRoll curves. Direct observation-to-observation comparison across these products is difficult because their arrays have different axes, scales, and provenance. This study treats the multi-product comparison task as an applied scientific-computing problem.

In this paper, the **frozen project archive** denotes the fixed collection of 25 POLIX Level-2 observations used in the completed study, not all public POLIX observations. The official XPoSat archive provides the data-service context [@issdc_xposat_archive], while the local observation identifiers, matrices, model artifacts, and result tables define the numerical scope of this analysis. Trusted anomaly labels were unavailable. Consequently, the aim is not classification accuracy or anomaly confirmation, but reproducible ranking of observations that are statistically unusual relative to the project archive.

The central research question is: *Can heterogeneous POLIX Level-2 products be represented through interpretable, product-aware features and screened using explainable unsupervised learning, while maintaining an independent comparison with blank-sky-referenced harmonic modulation behaviour?* Because trusted anomaly labels were unavailable, the final pipeline used a project-specific unsupervised explanation method rather than supervised or general post-hoc explainers.

The primary contribution is a traceable, product-aware explainable-artificial-intelligence framework for archive-relative screening of heterogeneous POLIX Level-2 observations. Three secondary contributions support it:

1. a 15-feature observation representation that preserves provenance across exposure, channel-space, source-azimuth, delivered-light-curve, and detector-balance product families;
2. a deterministic, project-specific, model-informed local feature-ranking heuristic that connects statistical unusualness to original feature and product families; and
3. an independent WeightedRoll second-harmonic branch with a selected empirical blank-sky reference, preventing circular confirmation by excluding WeightedRoll from the primary Matrix-C input.

The seed, contamination, jackknife, feature-tier, and six-case perturbation analyses are supporting evidence rather than separate contributions. A Flask research interface packages the workflow for inspection and export, but it is treated as an implementation contribution rather than the principal scientific claim.

# II. Related Work

## A. X-ray Polarimetry and POLIX Context

Scattering polarimeters infer polarization-related information from an azimuthal modulation produced by anisotropic scattering. Instrument response and modulation factor determine how a fitted amplitude can be interpreted physically [@fabiani2018instrumentation]. Event-based Stokes analysis provides an additive formulation for polarization-sensitive measurements and makes background treatment explicit [@kislat2015stokes]. The present study uses the same second-harmonic mathematical structure only as a raw diagnostic. Its fitted coefficients are not claimed as calibrated POLIX Stokes measurements.

The POLIX development literature describes the Thomson-scattering instrument lineage [@rishin2010thomson], while the current mission page establishes the flight payload and broad energy range [@isro_xposat]. Neither source validates the project’s engineered feature definitions, candidate labels, empirical blank-sky rule, or physical interpretations. Those quantities are controlled by the versioned code and result tables.

## B. Anomaly Screening in Astronomy

Unsupervised astronomical anomaly methods are commonly used to rank unusual objects for expert follow-up rather than to provide definitive ground truth. Baron and Poznanski used an outlier-ranking approach to identify unusual Sloan Digital Sky Survey galaxies and emphasized that outliers may arise from scientific, instrumental, or processing effects [@baron2017weirdest]. Giles and Walkowicz evaluated unsupervised anomaly discovery using known unusual objects, illustrating the distinction between statistical outlyingness and scientific interest [@giles2019serendipity]. Astronomaly further demonstrates a modular, researcher-facing framework in which expert feedback guides inspection [@lochner2021astronomaly]. These studies motivate archive triage but do not supply labels or physical explanations for POLIX observations.

## C. Explainable Anomaly Detection

Explainable anomaly detection distinguishes the detector from the mechanism used to interpret its output and includes model-specific, post-model, local, and global settings [@li2024explainable_anomaly]. SHAP is a general additive feature-attribution framework with Shapley-based guarantees under its formulation [@lundberg2017shap]. It was considered only as a conceptual comparator and was not implemented or benchmarked in the completed pipeline. The project instead uses a deterministic score constructed from the saved unsupervised models and standardized feature values.

Explanation evaluation should test whether a proposed explanation tracks changes in model behaviour under a stated intervention. Perturbation-based work formalizes infidelity and sensitivity as functional properties of explanations [@yeh2019infidelity]. The project’s feature-neutralization check follows the broader perturbation motivation but does not reproduce that published metric or inherit its guarantees.

## D. Research Gap

Unsupervised outlier evaluation is difficult without trusted labels and is sensitive to data, preprocessing, parameters, and evaluation choices [@campos2016evaluation]. Limited published work was identified on an integrated framework that simultaneously: (i) converts heterogeneous POLIX Level-2 products into product-traceable observation features, (ii) screens observations without anomaly labels, (iii) ranks local feature evidence, and (iv) preserves a scientifically separate blank-sky-referenced harmonic diagnostic. The reviewed literature addresses these elements individually, but it did not provide a directly comparable POLIX workflow. This finite review does not establish priority, novelty, or superiority.

# III. Dataset, Scope, and Problem Formulation

The project archive contains 25 observation directories with unique full identifiers: 10 are mapped by the project as source observations and 15 as blank-sky observations. These role labels support interpretation and construction of the independent blank-sky diagnostic; they are not targets for the unsupervised model. The archive is retrospective, small, and not claimed to represent every public observation or the future POLIX distribution.

**TABLE I — Dataset and product families**

| Product family | Implemented structure | Use in this study |
|---|---|---|
| Exposure azimuth | 360 roll rows with four detector-exposure columns | Exposure uniformity and roll-ratio features |
| Energy-resolved source azimuth | Operational array shape 360 × 8192 × 48 | Six PHA-channel and anode-balance summaries |
| Source azimuth | 360 roll rows with 48 anode counts per row | Peak-to-median, entropy, and roughness summaries |
| Delivered light-curve and detector products | Source RATE series; four detector light curves and four detector PHA products | Four supporting diagnostic features |
| WeightedRoll | 360 roll-angle bins with delivered total count rate and error | Separate weighted second-harmonic diagnostic; excluded from Matrix C |

All 25 observations have a Matrix-C row. The final matrix has 15 numeric features and zero missing values; the deployed code therefore performs no imputation. Earlier notebooks produced a superseded V1 feature table and exploratory candidate sets. They are retained as development history but do not control the paper’s numerical results.

The statistical task is to rank observations relative to the fixed archive without assuming anomaly ground truth. Let $X_C \in \mathbb{R}^{25\times15}$ denote Matrix C. The model output is an inspection priority, not a physical or categorical truth. The physical task is deliberately narrower: summarize each delivered WeightedRoll curve with a weighted second harmonic and compare the resulting raw coordinates with a selected empirical blank-sky reference. The study does not report calibrated polarization degree, official sky polarization angle, polarization significance, or an official background-subtraction result.

![Product-aware screening and independent harmonic-diagnostic architecture.](D:/polix_xai_webapp/research_paper_ieee/guide_approved_final_run/04_SRI_LANKA_FIGURES/figures/Fig1_corrected_framework.png)

**Fig. 1.** Product-aware screening and independent harmonic-diagnostic architecture. PCA, KMeans, and Isolation Forest receive the same standardized Matrix-C rows; only Isolation Forest defines the fixed label. WeightedRoll is analysed separately, and the branches are compared without confidence fusion.

# IV. Product-Aware Feature Engineering

## A. Matrix Development and Provenance

The representation was developed in tiers so that the effect of added product families could be examined. Matrix A contains eight Tier-1A exposure and energy-resolved features. Matrix B adds three source-azimuth diagnostics, giving 11 features. Matrix C adds four delivered-light-curve and detector-context features, giving 15. A separate six-feature WR matrix was used only in exploratory comparison and is not a fourth tier of the deployed representation.

Matrix C was selected as the deployed primary representation because it preserves the high-priority exposure and channel-space summaries while adding source-azimuth, light-curve, and detector context. This is a design choice, not a claim that Matrix C is statistically superior. The A/B/C comparison later shows that candidate identity depends on feature tier.

## B. Feature Definitions

**TABLE II — Matrix-C feature groups**

| Product group | Count | Matrix-C features and interpretation boundary |
|---|---:|---|
| Exposure | 2 | Exposure uniformity coefficient of variation; maximum-to-minimum roll-exposure ratio |
| Energy-resolved channel space | 6 | Peak channel; weighted mean channel; **weighted channel spread** (`t1A_energy_weighted_std_channel`); high-channel fraction for channel index at least 4000; channel entropy; anode-balance coefficient of variation |
| Source azimuth | 3 | Roll peak-to-median ratio; roll entropy; normalized adjacent-bin **order-dependent roughness proxy** without circular wrap |
| Delivered source light curve | 2 | Rate coefficient of variation; peak-to-median rate, both treated as delivered-light-curve diagnostic proxies rather than intrinsic source variability |
| Detector context | 2 | Coefficient of variation across detector mean rates; spread of detector PHA weighted channel centroids |

For exposure row $r$, detector exposures are summed to $E_r$. The two exposure features are $\mathrm{std}(E_r)/\mathrm{mean}(E_r)$ and $\max(E_r)/\min(E_r)$. For the energy-resolved product, counts are summed across roll and anode to obtain channel counts $n_j$. The peak, count-weighted mean, and weighted channel spread are

$$
j_{\mathrm{peak}}=\arg\max_j n_j,\qquad
\bar j=\frac{\sum_j jn_j}{\sum_j n_j},\qquad
s_j=\sqrt{\frac{\sum_j(j-\bar j)^2n_j}{\sum_jn_j}}.
$$

The high-channel fraction is the fraction of counts at channel indices $j\ge4000$; it is not called a calibrated high-energy fraction. Channel and roll entropies use base-2 Shannon entropy over positive counts. The source-azimuth roughness proxy is the mean absolute difference between adjacent roll rows divided by the mean roll count. Because the implementation does not include a last-to-first difference, unrestricted circular smoothness is not claimed. NumPy population standard deviations use `ddof=0`.

## C. Leakage and Circularity Control

No target or anomaly label enters feature construction. Observation role is not part of Matrix C. WeightedRoll features and all harmonic outputs are excluded from the deployed anomaly input, so the later physical comparison cannot mechanically confirm a label that already contains modulation evidence. The same separation also prevents the 13-fit blank-sky rule from influencing the fixed four candidates.

# V. Explainable Unsupervised Methodology

## A. Standardization and Descriptive Geometry

Each Matrix-C feature is standardized using the mean and scale fitted to the 25 archive rows. Principal Component Analysis (PCA) supplies a two-dimensional descriptive projection and one component of the local ranking [@pearson1901pca]. PC1 and PC2 explain 0.387435 and 0.225051 of standardized variance, respectively, or 0.612486 together. The two-dimensional plot is therefore a partial archive view rather than the complete anomaly input.

KMeans supplies complementary cluster geometry [@macqueen1967kmeans]. Candidate values $k=2,\ldots,5$ were compared by in-sample silhouette score, yielding $k=5$, `n_init=20`, random state 42, and silhouette 0.310936. Cluster sizes are 1, 9, 10, 1, and 4. Sco X-1 and Blank Sky-13 form singleton clusters, making their assigned-centroid distances zero. The clusters are not interpreted as astrophysical classes.

## B. Isolation Forest Screening

Isolation Forest isolates observations using random recursive partitions and path-length evidence [@liu2008isolation]. The saved configuration uses 100 trees, contamination 0.16, and random state 42 through scikit-learn [@pedregosa2011sklearn]. The reported anomaly score is negative `score_samples`, so larger values indicate greater relative unusualness. Only `IsolationForest.predict` produces the fixed label. The contamination value is the frozen screening assumption that sets a four-observation threshold; it is not an estimate of true anomaly prevalence.

![Two-component PCA projection of the standardized Matrix-C observations.](D:/polix_xai_webapp/research_paper_ieee/guide_approved_final_run/04_SRI_LANKA_FIGURES/figures/Fig2_matrixC_PCA_space.png)

**Fig. 2.** Two-component PCA projection of the standardized Matrix-C observations. Circles denote source observations, squares denote blank skies, and open diamonds outline the fixed four candidates. The projection is descriptive and does not determine or validate the label.

## C. Four-Component Local Feature Ranking

For standardized observation $x$, feature $j$, PCA loading $l_{kj}$, explained-variance ratio $r_k$, assigned KMeans centroid $c$, and anomaly score $s(x)=-\mathrm{score\_samples}(x)$, the four local components are

$$
P_j=|x_jl_{1j}|r_1+|x_jl_{2j}|r_2,\quad
K_j=(x_j-c_j)^2,
$$

$$
I_j=s(x)-s(x^{(j\leftarrow0)}),\qquad Z_j=|x_j|.
$$

Neutralization sets one standardized coordinate to zero, corresponding to the scaler’s fitted archive mean for that feature. For any component vector $v$, the service applies $N(v)_j=|v_j|/\max_k|v_k|$, returning zeros when the maximum is invalid or zero. Negative Isolation Forest occlusion changes are clipped to zero. The combined score is

$$
E_j=N(P)_j+N(K)_j+N(\max(I,0))_j+N(Z)_j.
$$

The four normalized components have equal implicit weight. Scores rank features within one observation and map them to their product families. They are not SHAP values, calibrated cross-observation importances, causal explanations, or exact decompositions of the Isolation Forest label. A deterministic Python template produces the researcher-facing explanation sentence; no language model is used in the deployed explanation.

## D. Feature-Neutralization Check and Interface

The top three ranked features were jointly neutralized for six exploratory observations: the fixed four candidates plus Blank Sky-15 and Blank Sky-6. A Strong project verdict means both PCA distance and Isolation Forest score decreased; Moderate means exactly one decreased. KMeans distance was recorded but does not enter the verdict. This is a sign-only, in-sample sanity check motivated by perturbation-based explanation evaluation [@yeh2019infidelity], not a general faithfulness proof.

The saved scaler, PCA, KMeans, Isolation Forest, feature schema, local-ranking function, harmonic service, and configuration are exposed through a Flask research interface. The interface supports observation upload, inspection, plots, explanation text, and CSV export. It packages the implemented study workflow but does not change the algorithms or scientific claim boundaries.

# VI. Independent Harmonic Diagnostic

## A. Weighted Second-Harmonic Fit

For each observation, the project reads the 360 finite WeightedRoll angle, delivered total-count-rate, and positive-error values. It fits

$$
y(\phi)=C+Q\cos(2\phi)+U\sin(2\phi)
$$

using inverse-variance weights $w_i=1/\sigma_i^2$. The design matrix contains $1$, $\cos(2\phi)$, and $\sin(2\phi)$, and the saved Notebook-11 implementation solves the weighted normal equations. The fit uses the delivered per-bin uncertainties as diagonal weights; no inter-bin covariance or additional systematic-error model is introduced. Each fit has 357 degrees of freedom. The derived amplitude, raw modulation, fitted phase, and fractional harmonic coordinates are

$$
A=\sqrt{Q^2+U^2},\qquad
m_{\mathrm{raw}}=100A/C,
$$

$$
\phi_{\mathrm{fit}}=\tfrac12\operatorname{atan2}(U,Q)\bmod180^\circ,qquad
q=Q/C,\quad u=U/C.
$$

The manuscript calls $Q$ and $U$ cosine and sine second-harmonic coefficients and defines $q=Q/C$ and $u=U/C$ as fractional harmonic coordinates. General Stokes methods motivate the harmonic structure [@kislat2015stokes], but the fitted values are not presented as calibrated POLIX Stokes parameters. Raw modulation is not polarization degree, and fitted modulation phase is not official sky polarization angle.

## B. Fit Quality and Empirical Reference

Project-defined fit categories are: acceptable for reduced chi-square at most 2; caution for values above 2 and at most 5; and poor simple-harmonic fit above 5. These are descriptive categories, not p-values or detection thresholds.

Thirteen of the 15 project-labelled blank-sky observations meet the acceptable rule and define the empirical reference. For scalar raw modulation, the declared comparison uses

$$
z_m=\frac{m_{\mathrm{raw}}-\bar m_{\mathrm{blank}}}{s_{\mathrm{blank}}}
$$

and describes a source as within the rule when $|z_m|<2$. The component-wise $q/u$ visualization reports the sample mean and sample standard deviation of the same 13 fits. Neither construction is a confidence region, covariance-aware null model, polarization significance, or official background subtraction.

## C. Uncertainty Provenance

The manuscript treats the frozen Notebook-11 CSV as the source of reported project uncertainty values. Notebook 11 propagates $A/C$ uncertainty through relative quadrature and omits amplitude–mean covariance. The later Flask service uses a full three-parameter gradient with coefficient cross-covariances. The implementations are not numerically identical and are not silently combined. Because uncertainty values are not required for the central non-equivalence argument, the main tables report central values and fit categories; the detailed implementation comparison is reserved for supplementary material.

# VII. Results

## A. Fixed Deployed Result

The exact saved-model reproduction matched all 25 stored scores and labels, with maximum score difference zero. The deployed Matrix-C configuration labelled 21 observations Normal and flagged four as anomaly candidates: Blank Sky-13, Sco X-1, Her X-1, and Blank Sky-5.

**TABLE III — Fixed candidates, tested stability, and leading local evidence**

| Candidate | Fixed score | Seeds selected | A/B/C persistence | Leading local feature |
|---|---:|---:|---|---|
| Blank Sky-13 (`C24_0018`) | 0.615964 | 100/100 | A, B, C | Weighted channel spread |
| Sco X-1 (`G01_0006`) | 0.593516 | 100/100 | A, B, C | Energy peak channel (2.454) |
| Her X-1 (`G01_0003`) | 0.572308 | 100/100 | C only | Delivered-light-curve rate coefficient |
| Blank Sky-5 (`C24_0010`) | 0.517611 | 29/100 | B, C | Source-azimuth order-dependent roughness proxy |

The leading features are local evidence under the project heuristic; they do not state physical causes. For Sco X-1, the accepted versioned order is energy peak channel (2.454), energy weighted mean channel (2.207), and energy-channel entropy (1.814). The historical entropy-first description is superseded and is not used.

## B. Procedure-Qualified Stability

Blank Sky-13, Sco X-1, and Her X-1 were selected in all 100 tested Isolation Forest seeds. Blank Sky-5 was selected in 29 runs, whereas fixed-Normal Blank Sky-15 was selected in 68. These frequencies reveal a seed-sensitive boundary and are not probabilities.

The existing contamination analysis tested 0.12, 0.16, 0.20, and 0.24, selecting the first 3, 4, 5, and 6 rows of one score ordering. The stable three were selected in all four settings; Blank Sky-5 in three; Blank Sky-15 in two; and Crab P01_0005 in one. In included-observation jackknife refits, the stable three remained selected in all 24 eligible fits, Blank Sky-5 in 19, Blank Sky-15 in 7, and Crab P01_0005 in 2. Common-observation score ranks had median Spearman correlation 0.989565 and minimum 0.968696 with the full-data ranking. The analysis is retrospective; Sco X-1 was not selected in its single held-out refit.

![Fixed Isolation Forest ranking and 100-seed selection frequencies.](D:/polix_xai_webapp/research_paper_ieee/guide_approved_final_run/04_SRI_LANKA_FIGURES/figures/Fig3_fixed_score_ranking_seed_frequency.png)

**Fig. 3.** Fixed Isolation Forest anomaly-score ranking for all 25 observations. Hatched bars identify the fixed candidates; annotations report selection counts across 100 tested seeds. The counts are algorithmic frequencies rather than confidence levels.

## C. Feature-Tier and Ranking Evidence

Matrix A flagged Blank Sky-13, Blank Sky-15, Sco X-1, and Crab P01_0005. Matrix B flagged Blank Sky-5, Blank Sky-13, Blank Sky-15, and Sco X-1. Matrix C flagged Blank Sky-5, Blank Sky-13, Her X-1, and Sco X-1. Only Blank Sky-13 and Sco X-1 persist across A/B/C. This cross-tier persistent pair is distinct from both the fixed four and the tested-procedure stable three.

PCA distance and Isolation Forest score have Spearman rank correlation 0.894615 within the project archive. PCA distance versus KMeans distance is 0.155799, and KMeans distance versus Isolation Forest score is 0.186574. The nominal p-values are not used to validate candidates. The weak KMeans associations are interpreted cautiously because two clusters are singletons.

## D. Local Ranking and Neutralization

The six-case neutralization analysis yielded five Strong verdicts and one Moderate verdict, for Blank Sky-6; no case was Weak. Thus both PCA distance and Isolation Forest score decreased after joint top-three neutralization in five cases, while one of the two decreased in the sixth. This supports local sensitivity to the selected perturbation but does not establish uniqueness, causal attribution, or performance on unseen observations.

## E. Harmonic and Blank-Sky Results

Weighted second-harmonic fits were saved for all 25 observations. Nineteen meet the acceptable rule, three are caution, and three are poor simple-harmonic fits. Thirteen of the 15 blank-sky fits form the empirical reference. Their mean raw modulation is 1.147820%, with sample standard deviation 0.565960%; the component-wise means are $\bar q=0.009092005$ and $\bar u=-0.006478172$. All ten source raw-modulation values remain within the declared empirical blank-sky reference rule.

**TABLE IV — Representative harmonic and blank-sky-relative results**

| Observation | Fixed ML label | Raw modulation (%) | Reduced chi-square | Fit category | Reference interpretation |
|---|---|---:|---:|---|---|
| Sco X-1 | Candidate | 1.139578 | 2.030761 | Caution | Within declared empirical rule |
| Her X-1 | Candidate | 0.596632 | 57.433514 | Poor | Scalar value within rule; simple harmonic inadequate |
| Crab P01_0005 | Normal | 1.697346 | 1.062540 | Acceptable | Within declared empirical rule |
| Blank Sky-13 | Candidate | 0.853951 | 2.565811 | Caution | Excluded from 13-fit reference by fit rule |
| Blank Sky-5 | Candidate | 1.518535 | 0.713428 | Acceptable | Included in 13-fit reference |

![Source and blank-sky fractional second-harmonic coordinates.](D:/polix_xai_webapp/research_paper_ieee/guide_approved_final_run/04_SRI_LANKA_FIGURES/figures/Fig4_fractional_harmonic_diagnostic_space.png)

**Fig. 4.** Fractional second-harmonic coordinates for all 25 observations. Filled squares form the 13-fit blank-sky reference; open squares are excluded by the fit rule; open diamonds identify the fixed ML candidates. The cross is the component-wise sample mean plus or minus one sample standard deviation, not a confidence or detection contour.

# VIII. Discussion

## A. Non-Equivalent Diagnostic Questions

The main empirical finding is that statistical unusualness and modulation-like harmonic behaviour are non-equivalent within the project archive. The result does not mean that the branches are statistically independent. It means that the saved outputs do not identify the same property observation by observation, which is consistent with their different inputs and objectives.

Matrix C summarizes exposure, channel-space, source-azimuth, delivered-light-curve, and detector-balance products. Isolation Forest identifies rows that are comparatively easy to isolate in that representation. WeightedRoll is absent from Matrix C and is fitted separately. A harmonic amplitude therefore cannot mechanically cause the fixed label, and the label cannot serve as circular confirmation of a WeightedRoll pattern.

## B. Representative Observations

Sco X-1 is a fixed candidate, is selected under all 100 tested seeds, and persists across Matrix A/B/C. Its local ranking is led by three energy-resolved channel summaries. Yet its raw modulation, 1.139578%, remains within the declared empirical rule, and its reduced chi-square places the harmonic fit in the caution category. The safe conclusion is that Sco X-1 is persistently unusual in the engineered feature representation and warrants product-level inspection. The ranking does not identify a spectral, instrumental, or astrophysical cause.

Her X-1 is also selected in all tested seeds and eligible included-observation jackknife refits, but it appears only in Matrix C. Its reduced chi-square of 57.433514 shows that the selected second harmonic poorly summarizes the delivered curve. The fitted phase and raw modulation therefore receive no physical interpretation. This case demonstrates that a stable ML candidate can coexist with an inadequate harmonic summary.

Crab P01_0005 is Normal in the fixed Matrix-C result and is selected in only 3 of 100 seed runs. Its raw modulation of 1.697346% is larger than those of Sco X-1, Her X-1, and Blank Sky-13 while retaining an acceptable fit category. Consequently, larger raw harmonic amplitude does not imply Matrix-C candidate status. It also does not constitute a polarization detection.

Blank Sky-13 and Blank Sky-5 are both fixed candidates. Their roles show that the model is neither a source classifier nor a polarization classifier. Blank Sky-13 belongs to the tested-procedure stable three but has a caution harmonic fit and is excluded from the 13-fit reference. Blank Sky-5 has an acceptable harmonic fit but is selected in only 29 of 100 seeds. Neither fit category confirms or invalidates the archive-screening label.

## C. Interpretation of Explainability and Stability

The local score’s practical value is computational traceability: it connects an observation-level screening output to explicit feature definitions and product families. Equal component weighting and within-observation normalization make the score simple to inspect but prevent calibrated comparison of magnitudes between observations. The six-case perturbation check shows that the leading features affect the selected model summaries under a specific intervention; it does not demonstrate general explanation faithfulness.

The phrase “three-candidate Matrix-C core stable under the tested procedures” is deliberately qualified. Stability refers to the existing seed, contamination-threshold, and included-observation checks on the same archive. It does not establish true anomalies, predictive performance, or future-release generalization. The cross-tier persistent pair answers a separate representation question and must not be merged with the stable three.

## D. Researcher-Facing Use

The framework is best used as a triage system. A researcher can examine the fixed ranking, check seed and feature-tier sensitivity, inspect the local feature and product-family evidence, and then compare the independent harmonic summary and fit quality. Observations near the threshold, in singleton clusters, or with poor harmonic fits require additional caution. Domain review remains necessary before any physical interpretation.

# IX. Limitations and Threats to Validity

The principal limitation is sample size. With $n=25$, the fitted scaler, PCA directions, KMeans clusters, and Isolation Forest threshold are archive-specific. The same archive is used for representation development, model fitting, local explanation, perturbation checking, and retrospective stability analysis. No trusted anomaly labels or independent future-release test set are available, so accuracy, sensitivity, specificity, or generalization cannot be estimated.

The four-candidate count is contamination-defined. Random-seed sensitivity changes boundary membership, as shown by Blank Sky-5 and Blank Sky-15. Candidate identity also depends on feature tier; Her X-1 appears only in Matrix C, while Crab P01_0005 appears only in Matrix A. KMeans contains two singleton clusters, limiting centroid-distance interpretation and causing zero KMeans contribution for Sco X-1 and Blank Sky-13.

The feature semantics are operational rather than fully calibrated. Channel indices are not converted into a calibrated energy scale in this analysis. The high-channel fraction uses a fixed channel threshold. The source-azimuth feature is an order-dependent roughness proxy, and the delivered-light-curve features describe the delivered product rather than intrinsic source variability. These meanings require POLIX-aware domain review.

The local XAI score is a project-specific heuristic with equal component weighting. It is not SHAP, has no additive prediction-decomposition guarantee, and is not causal. The six-case joint neutralization check is in-sample, sign-only, and restricted to two model summaries. Its Strong and Moderate labels are project categories rather than statistical confidence statements.

The physical branch analyses the delivered WeightedRoll total-count-rate curve without applying an independently verified official background-subtraction procedure. The 13-fit blank-sky reference is selected by a project-defined reduced-chi-square rule and is too small for a covariance-aware population model. Fit-quality categories are descriptive. The study does not implement a calibrated modulation factor, official sky-angle conversion, polarization significance, or official background workflow; consequently it reports no calibrated polarization degree or official sky polarization angle.

Notebook 11 and the later Flask service use different $A/C$ uncertainty propagation. The manuscript controls reported project values through the frozen Notebook-11 CSV and does not claim numerical identity. The original software environment was not fully pinned; the saved artifact and exact-function audits provide provenance, but a future containerized release is preferable.

Finally, no POLIX domain expert has adjudicated the four candidates, the feature semantics, or the empirical blank-sky rule. The interface is a proof-of-concept research implementation rather than an operational mission pipeline. Future work should use later observations for prospective validation, obtain expert review, adopt supported background and calibration procedures, model blank-sky covariance with a larger sample, pin the environment, and compare alternative detectors only on an independent dataset with defensible evaluation targets.

# X. Conclusion

This study implemented a traceable explainable-AI framework for screening 25 heterogeneous POLIX Level-2 observations. Fifteen product-aware features connect each observation to exposure, channel-space, source-azimuth, delivered-light-curve, and detector-context summaries. A saved StandardScaler, PCA, KMeans, and Isolation Forest stack provides complementary archive evidence, while a deterministic four-component heuristic ranks local features and product families.

The fixed result contains 21 Normal observations and four candidates. Three candidates remain selected throughout the tested seed, contamination, and included-observation procedures; Blank Sky-5 is seed-sensitive. WeightedRoll is analysed independently through raw second-harmonic fits and a selected empirical blank-sky reference. Representative observations show that Matrix-C unusualness and modulation-like harmonic behaviour do not identify the same property within the project archive.

The framework helps researchers prioritize product-level inspection. It does not establish anomaly ground truth, astrophysical discovery, calibrated polarization degree, official sky polarization angle, official background subtraction, or future-data performance. Extension to later POLIX observations should follow prospective expert review and supported calibration and background workflows.

## Acknowledgment

The data-use wording was checked against the current Indian Space Science Data Centre guidance [@issdc_xposat_ack].

This publication uses the data from the XPoSat mission of the Indian Space Research Organisation (ISRO), archived at the Indian Space Science Data Centre (ISSDC).

## References

[1] Indian Space Research Organisation, “XPoSat,” accessed Aug. 3, 2026.  
[2] P. V. Rishin *et al.*, “Development of a Thomson X-Ray Polarimeter,” arXiv:1009.0846, 2010.  
[3] S. Fabiani, “Instrumentation and Future Missions in the Upcoming Era of X-Ray Polarimetry,” *Galaxies*, vol. 6, no. 2, art. 54, 2018.  
[4] F. Kislat *et al.*, “Analyzing the Data from X-Ray Polarimeters with Stokes Parameters,” *Astroparticle Physics*, vol. 68, pp. 45–51, 2015.  
[5] Indian Space Science Data Centre, “ISRO Science Data Archive: XPoSat,” accessed Aug. 3, 2026.  
[6] D. Baron and D. Poznanski, “The Weirdest SDSS Galaxies: Results from an Outlier Detection Algorithm,” *Monthly Notices of the Royal Astronomical Society*, vol. 465, no. 4, pp. 4530–4555, 2017.  
[7] D. Giles and L. Walkowicz, “Systematic Serendipity: A Test of Unsupervised Machine Learning as a Method for Anomaly Detection,” *Monthly Notices of the Royal Astronomical Society*, vol. 484, no. 1, pp. 834–849, 2019.  
[8] M. Lochner and B. A. Bassett, “Astronomaly: Personalised Active Anomaly Detection in Astronomical Data,” *Astronomy and Computing*, vol. 36, art. 100481, 2021.  
[9] Z. Li, Y. Zhu, and M. van Leeuwen, “A Survey on Explainable Anomaly Detection,” *ACM Transactions on Knowledge Discovery from Data*, vol. 18, no. 1, pp. 1–54, 2024.  
[10] S. M. Lundberg and S.-I. Lee, “A Unified Approach to Interpreting Model Predictions,” in *Advances in Neural Information Processing Systems 30*, pp. 4765–4774, 2017.  
[11] C.-K. Yeh *et al.*, “On the (In)fidelity and Sensitivity of Explanations,” in *Advances in Neural Information Processing Systems 32*, pp. 10965–10976, 2019.  
[12] G. O. Campos *et al.*, “On the Evaluation of Unsupervised Outlier Detection: Measures, Datasets, and an Empirical Study,” *Data Mining and Knowledge Discovery*, vol. 30, no. 4, pp. 891–927, 2016.  
[13] K. Pearson, “On Lines and Planes of Closest Fit to Systems of Points in Space,” *Philosophical Magazine*, vol. 2, no. 11, pp. 559–572, 1901.  
[14] J. MacQueen, “Some Methods for Classification and Analysis of Multivariate Observations,” in *Proc. Fifth Berkeley Symp. Mathematical Statistics and Probability*, vol. 1, pp. 281–297, 1967.  
[15] F. T. Liu, K. M. Ting, and Z.-H. Zhou, “Isolation Forest,” in *Proc. 8th IEEE Int. Conf. Data Mining*, pp. 413–422, 2008.  
[16] F. Pedregosa *et al.*, “Scikit-learn: Machine Learning in Python,” *Journal of Machine Learning Research*, vol. 12, pp. 2825–2830, 2011.  
[17] Indian Space Science Data Centre, “XPoSat Acknowledgment Guidance,” accessed Aug. 3, 2026.
