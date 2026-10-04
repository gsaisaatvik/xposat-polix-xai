# Learning Modules 1-18

**Current edition:** Modules 1-13 complete; Modules 14-18 not executed by instruction.

---

# Module 1 - X-ray Astronomy Basics

## Beginner explanation

Astronomy studies light from the Universe. “Light” includes much more than what our eyes see. X-rays are high-energy electromagnetic radiation. Earth's atmosphere absorbs most celestial X-rays, which protects life but prevents ground-based X-ray telescopes from observing the sky directly. X-ray instruments therefore fly on rockets or satellites.

Many extreme objects emit X-rays: accreting neutron stars, black holes, supernova remnants, pulsars, and active galactic nuclei. An instrument does not receive a photograph in the ordinary sense. It records detector events or counts. Each record may contain time, detector location, pulse height, and other instrument-specific information. Data processing converts those measurements into products such as a light curve, an energy distribution, or an azimuthal distribution.

Three questions must remain separate:

- **How bright and variable is the detected signal?**
- **How is detected energy distributed?**
- **Does the interaction direction carry polarization information?**

Background counts arise from the instrument, charged particles, diffuse radiation, and other sources. A high count rate is not automatically a strong source signal, and an unusual count pattern is not automatically new astrophysics.

## Technical explanation

An X-ray photon has energy

\[
E=h\nu=\frac{hc}{\lambda},
\]

where \(h\) is Planck's constant, \(\nu\) is frequency, \(c\) is the speed of light, and \(\lambda\) is wavelength. X-ray astronomy commonly reports energy in kilo-electronvolts (keV).

A detector records a stochastic sequence of interactions. For a time interval \(\Delta t\), a basic count rate is

\[
R=\frac{N}{\Delta t}.
\]

Counts are usually modeled with Poisson statistics before additional instrumental effects are considered. A light curve bins events in time. A pulse-height distribution groups events by detector response channel. Turning pulse height into a calibrated physical spectrum requires an energy calibration and instrument response. The POLIX handbook states that POLIX is not a spectroscopic instrument and that the current released data are not intended for spectroscopic analysis because ARF/RMF products are not currently supplied and background variation is not fully understood.

“Source” and “background” describe observing intervals or signal components, not perfect truth labels. Background correction requires a justified way to estimate the background contribution under conditions relevant to the source observation.

## Project-specific example

The project derives interpretable summaries from several POLIX Level-2 product families. A temporal coefficient of variation can indicate whether a light-curve-like product changes strongly relative to its mean. A PHA channel statistic can describe where counts occur in the recorded channel distribution. These are useful screening features, but the handbook cautions mean they must be described as diagnostic quantities or engineered proxies, not as calibrated source variability or spectroscopy without further validation.

## Terms to remember

- photon
- keV
- count
- event
- count rate
- exposure
- light curve
- pulse-height channel
- spectrum
- background
- calibration
- instrument response

## Common misunderstanding

**Misunderstanding:** “A detector channel is the same as a precisely calibrated photon energy.”

**Correction:** A channel is an instrument measurement bin. Converting it into a physical energy distribution requires calibration and response information. In this project, channel-derived summaries are features, not calibrated spectroscopy.

## Defense card

- **What the paper may say:** The archive contains Level-2 products from which diagnostic temporal, pulse-height, azimuthal, exposure, and detector-balance summaries were derived.
- **What it means simply:** Different files describe different aspects of how POLIX recorded counts.
- **How the project implemented it:** It converted selected arrays into observation-level numerical features.
- **What evidence supports it:** POLIX handbook product descriptions plus exact extraction code and feature matrix.
- **Reviewer question:** Are the PHA and light-curve features physically calibrated source quantities?
- **Student answer:** They are used as archive-relative diagnostic features; the handbook's limitations prevent presenting them as calibrated spectroscopy or unrestricted scientific light curves.
- **Must not claim:** The features are calibrated flux, spectrum, or source-intrinsic variability.

## Self-test questions

1. Why must most astronomical X-ray observations be made above Earth's atmosphere?
2. What is the difference between a detector count and an astrophysical flux?
3. What information does a light curve organize?
4. Why is a pulse-height channel not automatically a calibrated energy?
5. Why can background affect both count-rate and anomaly interpretation?

---

# Module 2 - X-ray Polarization, PD, and PA

## Beginner explanation

Light is an electromagnetic wave. Linear polarization describes whether the electric-field direction has a preferred orientation. Two common reported quantities are:

- **polarization degree (PD):** how strongly the detected radiation favors an orientation;
- **polarization angle (PA):** the orientation on the sky, after the detector geometry and coordinate transformation are handled.

POLIX does not measure the electric field directly. It uses the fact that polarized X-rays scatter anisotropically. If interaction counts are plotted against azimuthal angle, a linearly polarized signal can produce a repeating pattern with two maxima over \(360^\circ\). This two-fold pattern motivates sine and cosine terms containing \(2\phi\).

A fitted wave in an azimuthal histogram is not yet a polarization measurement. Background can also be modulated. Instrument response to a completely polarized beam is needed to convert measured modulation into PD. Detector-to-sky geometry is needed to convert a fitted detector-frame phase into official sky PA.

## Technical explanation

A simple second-harmonic model is

\[
y(\phi)=C+Q\cos(2\phi)+U\sin(2\phi),
\]

where \(C\) is the constant level and \(Q,U\) are coefficients in the chosen angular convention. The fitted amplitude is

\[
A=\sqrt{Q^2+U^2},
\]

and an archive-specific raw modulation may be formed as \(A/C\), subject to the exact normalization used by the fitting code.

The coefficient phase is commonly related to

\[
\psi_{\mathrm{fit}}=\tfrac12\operatorname{atan2}(U,Q).
\]

This is a fitted phase in the coordinate system and convention of the input angles. It becomes a sky PA only after the required instrument convention, reference direction, roll/attitude transformation, sign convention, and calibration have been verified.

For a calibrated polarimeter, a simplified relationship is

\[
\mathrm{PD}\approx\frac{m}{\mu_{100}},
\]

where \(m\) is a background-corrected modulation fraction and \(\mu_{100}\) is the calibrated response to a 100% polarized beam under appropriate energy and observing conditions. If \(\mu_{100}\) is only assumed, the result is a sensitivity scenario or proxy, not calibrated PD.

Stokes-style \(Q\) and \(U\) are attractive because they can be accumulated and background components can be subtracted at the Stokes level under a justified statistical model. However, using the symbols \(Q\) and \(U\) does not by itself guarantee a calibrated Stokes analysis.

## Project-specific example

The project's physical branch fits the second harmonic to exposure-weighted WeightedRoll modulation curves and compares fitted \(Q/U\)-type coefficients with an empirical distribution from acceptable blank-sky fits. That branch is kept outside the primary Matrix-C anomaly input. Its output may show whether a source lies within or outside the project's empirical blank-sky scatter. It cannot, under the current evidence, be reported as calibrated PD or official sky PA.

## Terms to remember

- linear polarization
- polarization degree (PD)
- polarization angle (PA)
- azimuthal angle
- modulation curve
- second harmonic
- \(C,Q,U\)
- raw modulation
- fitted phase
- modulation factor \(\mu_{100}\)
- detector frame
- sky frame

## Common misunderstanding

**Misunderstanding:** “If the fitted modulation is 2%, then PD is 2%.”

**Correction:** PD requires background treatment and division by an appropriate calibrated modulation factor. A fitted amplitude from the released product is raw modulation evidence, not calibrated PD.

## Defense card

- **What the paper may say:** A separate branch fits second-harmonic modulation and compares fitted coefficients with an empirical blank-sky reference.
- **What it means simply:** The project asks whether an observed azimuthal pattern differs from patterns seen in blank sky.
- **How the project implemented it:** Weighted least-squares fitting of \(C+Q\cos2\phi+U\sin2\phi\), followed by archive-specific diagnostics.
- **What evidence supports it:** Exact physical-fit CSVs/code, the handbook's WeightedRoll description, and Stokes-method literature.
- **Reviewer question:** Is the reported phase a sky polarization angle?
- **Student answer:** No. It is a fitted modulation phase in the available coordinate convention; the required official sky-frame conversion has not been verified.
- **Must not claim:** polarization detection, calibrated PD, official PA, or official background subtraction.

## Self-test questions

1. What physical preference does linear polarization describe?
2. Why does the model contain \(2\phi\), not simply \(\phi\)?
3. What do \(\sqrt{Q^2+U^2}\) and \(\tfrac12\operatorname{atan2}(U,Q)\) represent in the fitted model?
4. What additional information is required to convert raw modulation into PD?
5. Why is a fitted detector-frame phase not automatically sky PA?

---

# Module 3 - XPoSat, POLIX, and XSPECT

## Beginner explanation

XPoSat is an Indian Space Research Organisation satellite launched on 1 January 2024 to study bright cosmic X-ray sources. It carries two payloads with different jobs:

- **POLIX (Polarimeter Instrument in X-rays):** measures azimuthal scattering information for medium-energy X-ray polarimetry, officially described in the 8-30 keV range.
- **XSPECT (X-ray Spectroscopy and Timing):** provides spectroscopy and timing information in the softer 0.8-15 keV range.

The two instruments are complementary, but they are not interchangeable. This project analyzes POLIX Level-2 products. It does not combine XSPECT measurements into Matrix C.

## Technical explanation

POLIX is a non-imaging, collimated Thomson-scattering polarimeter. A low-atomic-number scatterer is surrounded by four X-ray proportional-counter detectors. A collimator restricts the field of view. The direction-dependent scattering probability encodes linear-polarization information in an azimuthal distribution.

XSPECT uses swept-charge devices for spectral and timing measurements. Its energy response, products, and calibration are different. An XSPECT claim cannot be inferred from a POLIX PHA channel, and a POLIX product should not be described using XSPECT's spectroscopic capability.

Mission descriptions establish the intended payload capabilities. The current POLIX Level-2 handbook establishes what the released products can safely support. When the mission page and the release-specific handbook operate at different levels, the handbook controls analysis claims about the local Level-2 data.

## Project-specific example

Matrix C combines fifteen summaries derived from POLIX product families. Even though XPoSat also carries XSPECT, no XSPECT spectrum or light curve is part of the frozen deployed anomaly matrix. Therefore, the paper may describe XPoSat as a spectro-polarimetry mission context, but it must describe the implemented analysis as POLIX Level-2 observation screening.

## Terms to remember

- XPoSat
- ISRO
- ISSDC
- PRADAN
- POLIX
- XSPECT
- Thomson scattering
- proportional counter
- collimator
- non-imaging
- Level 1
- Level 2

## Common misunderstanding

**Misunderstanding:** “Because XPoSat has a spectrometer, every XPoSat file can be used for spectroscopy.”

**Correction:** XSPECT and POLIX are separate instruments. The POLIX handbook explicitly states that current released POLIX data are not meant for spectroscopic analysis.

## Defense card

- **What the paper may say:** The study processes POLIX Level-2 products from 25 observations included in the project archive.
- **What it means simply:** The data come from one XPoSat payload and from a fixed local archive.
- **How the project implemented it:** POLIX product files were converted into feature matrices and a separate WeightedRoll diagnostic.
- **What evidence supports it:** Local file inventory, the official mission page, and the handbook.
- **Reviewer question:** Did the project use XSPECT or all public XPoSat data?
- **Student answer:** No. It used the 25 POLIX Level-2 observations in the project archive; XSPECT products were not part of the deployed inputs.
- **Must not claim:** all public POLIX observations, combined POLIX-XSPECT modeling, or XSPECT-calibrated spectroscopy.

## Self-test questions

1. What are the separate roles of POLIX and XSPECT?
2. What energy band does the current ISRO mission page assign to POLIX?
3. What instrument principle allows POLIX to probe linear polarization?
4. Why does the handbook control Level-2 analysis claims more directly than a general mission page?
5. Did the project's Matrix C use XSPECT products?

---

# Module 4 - POLIX Detector and FITS Products

## Beginner explanation

A FITS file is a standard astronomy data container. It can hold tables, images, arrays, metadata, and multiple named sections called Header/Data Units (HDUs). A filename tells you the product family, but the header and array structure tell you what is actually stored.

The POLIX Level-2 archive contains several product types:

- light curves (`.lc`);
- pulse-height distributions (`.pha`);
- exposure versus azimuth;
- total source azimuth distributions;
- energy-resolved source azimuth data cubes;
- exposure-weighted modulation (`WeightedRoll`).

These products are related, but they answer different questions. Combining them into one feature row is a computational representation choice. It does not make the measurements physically equivalent.

## Technical explanation

The handbook describes the relevant products as follows:

- **Light curves and spectra:** generated for source, background, and Earth-occultation intervals, with detector-specific versions for processed events. Count-mode light curves are for quick diagnosis and are not intended for further scientific analysis. POLIX has no current ARF/RMF products and the released data are not intended for spectroscopy.
- **Exp_Azimuth_Roll/Yaw:** exposure distribution with azimuth. The Level-2 pipeline uses the roll distribution in further analysis.
- **Src_Azimuth_Roll/Yaw:** total counts by azimuth for each of 48 anode cells; the handbook says these products are not used in later pipeline analysis, although the research project may still derive screening summaries from them.
- **EnergyRes_Src_Azimuth_Roll:** a three-dimensional cube containing counts across azimuth, PHA channel, and 48 anode cells.
- **WeightedRoll:** final intensity modulation versus azimuth obtained after exposure weighting. It contains both source and background count-rate modulation.

FITS auditing must check:

1. selected HDU and column names;
2. array axis order and dimensions;
3. units in headers;
4. finite-value, zero-exposure, and empty-array handling;
5. whether aggregation mixes detectors, channels, azimuth bins, or observing intervals;
6. whether a statistic is a direct quantity or an engineered proxy.

The handbook also records time-dependent detector limitations: Detector 4 Channel 2 is unusable after 25 May 2024, Detector 3 data are unusable from 14 November 2024, and Detector 4 gain changed over time. Any project interpretation involving detector balance or channel distributions needs observation-date-aware domain review.

## Project-specific example

The deployed Matrix C uses fifteen observation-level features from exposure, energy-resolved azimuth, source azimuth, temporal, PHA, and detector-balance product families. WeightedRoll is deliberately excluded from Matrix C and used in a separate physical diagnostic. This prevents the physical modulation curve from being both the anomaly input and the supposed confirmation of the same anomaly.

Feature extraction must still be audited against exact axes and formulas. A statistic can be computationally reproducible yet scientifically overnamed. For example, entropy over PHA channels is a dimensionless description of channel occupancy, not “spectral entropy” in the sense of a calibrated photon spectrum unless a domain expert approves that wording.

## Terms to remember

- FITS
- HDU
- header
- binary table
- array axis
- GTI
- source interval
- background interval
- Earth occultation
- roll
- yaw
- azimuth bin
- anode
- PHA
- exposure weighting
- WeightedRoll

## Common misunderstanding

**Misunderstanding:** “WeightedRoll is already a pure, background-subtracted source polarization curve.”

**Correction:** The handbook states that WeightedRoll includes modulation of both source and background count rates. It is an exposure-weighted diagnostic product and requires justified background treatment and calibration before physical polarization claims.

## Defense card

- **What the paper may say:** Product-aware features preserve the provenance of several heterogeneous POLIX Level-2 families, while WeightedRoll is analyzed separately.
- **What it means simply:** The model uses summaries from different files, and the polarization-like curve is kept out of the ML input.
- **How the project implemented it:** Extraction code reduces product arrays to fifteen Matrix-C values and sends WeightedRoll to a separate fitting path.
- **What evidence supports it:** Exact extraction code, Matrix-C column list, representative FITS headers/shapes, and handbook pp. 25-26.
- **Reviewer question:** Are all product-derived features direct physical measurements?
- **Student answer:** No. Some are direct file summaries and some are reasonable screening proxies; each must retain its source-product and calibration caveat.
- **Must not claim:** all features are calibrated physical parameters, WeightedRoll is background-corrected, or PHA features are spectroscopy.

## Self-test questions

1. What is an HDU in a FITS file?
2. Which product contains energy-resolved azimuth and PHA information across anode cells?
3. Why must FITS axis order be checked rather than guessed?
4. What does the handbook say is included in WeightedRoll?
5. Why is keeping WeightedRoll outside Matrix C scientifically useful?

---

# Answers to Modules 1-4

## Module 1 answers

1. Earth's atmosphere absorbs most celestial X-rays, so a detector must be placed above it.
2. A count is a registered detector interaction; flux is a calibrated physical rate per area and usually per energy range, requiring response and exposure treatment.
3. A light curve organizes counts or count rate as a function of time.
4. Channel is an instrumental pulse-height bin; calibrated energy requires a channel-energy relation and response information.
5. Background contributes counts and may vary, so it can create or alter apparently unusual patterns without a source-intrinsic cause.

## Module 2 answers

1. It describes a preferred orientation of the electric-field oscillation.
2. Linear-polarization orientation is axial: orientations separated by \(180^\circ\) are equivalent, producing a two-fold response over \(360^\circ\).
3. They give the fitted second-harmonic amplitude and phase in the chosen coefficient/angle convention.
4. A justified background-corrected modulation and an appropriate calibrated \(\mu_{100}\), including energy/response conditions.
5. The detector-frame phase still needs verified reference-axis, sign, roll/attitude, and sky-coordinate transformations.

## Module 3 answers

1. POLIX is the medium-energy polarimeter; XSPECT is the softer X-ray spectroscopy/timing payload.
2. 8-30 keV.
3. Direction-dependent Thomson scattering in a low-Z scatterer, measured by surrounding detectors.
4. It documents the actual released products, processing, and release-specific limitations.
5. No.

## Module 4 answers

1. A Header/Data Unit: one metadata-plus-data section inside a FITS file.
2. `EnergyRes_Src_Azimuth_Roll_L2.fits`.
3. A transposed or misunderstood axis changes which physical dimension a calculation summarizes.
4. Exposure-weighted modulation containing both source and background count-rate modulation.
5. It reduces circular confirmation: physical modulation evidence remains an independent question rather than an input to the anomaly score.

---

# Module 5 - Project Dataset and Source/Blank-Sky Observations

## Beginner explanation

The project uses a fixed local collection of 25 POLIX Level-2 observations. Project metadata maps 10 as source observations and 15 as blank-sky observations. A source observation points at a named astronomical target. A blank-sky observation is intended to characterize measurements away from a selected bright source, but it is not an empty or perfectly known background.

The archive is a research sample, not a statistical random sample of the sky. It was not demonstrated to contain every public POLIX observation. For this reason, conclusions are relative to the observations included in this archive.

## Technical explanation

Each observation is keyed by its unique observation identifier. The 25 identifiers agree across the frozen Matrix-C table, WeightedRoll fit table, extracted observation folders, and role metadata. Friendly names are secondary metadata: two identifiers are both labelled “Blank Sky-2,” so identifiers must remain the primary keys.

The model is fitted and evaluated descriptively on the same 25-row archive. There is no trusted anomaly label and no independent holdout release. “Source” and “blank sky” are roles, not anomaly classes. A blank-sky observation may itself be statistically unusual, and a source observation need not be unusual.

## Project-specific example

The fixed model flags two source observations and two blank-sky observations. This illustrates why the task is archive screening rather than source classification: the model compares feature patterns without treating source status as ground truth.

## Terms to remember

- observation identifier
- source observation
- blank-sky observation
- role metadata
- data freeze
- archive-relative
- ground truth
- holdout data

## Common misunderstanding

**Misunderstanding:** “Blank sky means zero signal and therefore supplies normal labels.”

**Correction:** Blank-sky measurements contain instrumental and environmental counts and may vary. They are an empirical comparison group, not official normal labels.

## What the paper may say

The study uses 25 POLIX Level-2 observations included in the project archive, comprising 10 source and 15 blank-sky observations according to project metadata.

## What the paper must not claim

It must not claim that all public POLIX observations were used, that blank sky is signal-free, or that source/blank-sky roles are anomaly ground truth.

## Likely reviewer question

**Question:** How can the model be validated when the same 25 observations define the archive and there are no labels?

## Student-safe answer

The study does not report predictive accuracy. It treats the output as descriptive archive-relative screening and uses sensitivity, jackknife, matrix, explanation, and separate physical-diagnostic checks to identify stable and fragile conclusions.

## Self-test questions

1. How many source and blank-sky observations are in the project archive?
2. Why is observation ID safer than a friendly label?
3. Why is blank sky not a normal-class label?
4. What does archive-relative mean?
5. What independent evaluation set is available?

---

# Module 6 - All 15 Matrix-C Features

## Beginner explanation

Matrix C turns each observation into fifteen numbers. These numbers summarize several product families so that the model can compare observations in one table. They are interpretable engineering summaries, but most are not calibrated astrophysical measurements.

## Technical explanation

| # | Feature | Exact numerical idea | Safe meaning |
|---:|---|---|---|
| 1 | `t1A_exp_uniformity_cv` | SD/mean of total exposure over roll bins | Exposure non-uniformity proxy |
| 2 | `t1A_exp_max_to_min_roll` | Maximum/minimum total roll exposure | Extreme exposure contrast |
| 3 | `t1A_energy_peak_channel` | Index of maximum collapsed channel count | Peak count channel, not keV |
| 4 | `t1A_energy_weighted_mean_channel` | Count-weighted mean channel | Channel centroid |
| 5 | `t1A_energy_weighted_std_channel` | Count-weighted channel SD | Channel-distribution width |
| 6 | `t1A_energy_high_channel_fraction` | Fraction of counts at channel index >=4000 | High-channel fraction; energy boundary unverified |
| 7 | `t1A_energy_channel_entropy` | Shannon entropy of positive channel counts | Channel-distribution concentration |
| 8 | `t1A_energy_anode_balance_cv` | SD/mean across 48 anode totals | Anode-count balance proxy |
| 9 | `t1B_src_peak_to_median_roll` | Maximum/median source-roll count | Roll-profile peakiness |
| 10 | `t1B_src_roll_entropy` | Entropy of source-roll counts | Roll-profile concentration |
| 11 | `t1B_src_roll_smoothness_norm` | Mean absolute adjacent difference/mean | Non-circular stored-order roughness |
| 12 | `t2_lc_rate_cv` | SD/mean of delivered source RATE array | Light-curve-array variation proxy |
| 13 | `t2_lc_peak_to_median_rate` | Maximum/median delivered RATE | Light-curve-array peakiness |
| 14 | `t2_det_lc_rate_balance_cv` | SD/mean of detector mean rates | Cross-detector rate-balance proxy |
| 15 | `t2_det_pha_centroid_spread` | SD of detector weighted mean channels | Cross-detector channel-centroid spread |

All standard deviations use NumPy's population definition (`ddof=0`). The feature code does not use measurement-error weights. The frozen matrix has no missing values, but the current upload extractor can produce NaN and has no imputer.

Important implementation cautions:

- channel values are not calibrated keV;
- channel 4000 is a hard-coded index threshold;
- entropy depends on binning and is not normalized by the maximum possible entropy;
- roll smoothness omits the circular last-to-first difference;
- light-curve calculations do not apply FRAC_EXP, error, quality, or explicit GTI filtering;
- the Flask detector features can use fewer than four discovered detector files.

## Project-specific example

For Sco X-1, the current deployed local explanation ranks peak channel, weighted mean channel, and channel entropy highest. This means channel-space summaries drive its model explanation. It does not identify a spectral state, detector fault, or physical source cause.

## Terms to remember

- coefficient of variation
- weighted mean
- weighted standard deviation
- entropy
- peak-to-median ratio
- channel space
- proxy
- population standard deviation
- product provenance

## Common misunderstanding

**Misunderstanding:** “Because the features have scientific names, each one is a calibrated physical parameter.”

**Correction:** The formulas are verified, but their physical meaning is limited by product semantics, calibration, quality filtering, and detector comparability.

## What the paper may say

Matrix C is a fifteen-feature product-aware representation containing exposure-pattern, channel-distribution, source-roll, light-curve-array, and cross-detector summaries.

## What the paper must not claim

It must not describe channel features as calibrated spectroscopy, light-curve features as intrinsic variability, detector-balance features as diagnosed hardware faults, or roll features as polarization evidence.

## Likely reviewer question

**Question:** Why should these proxies be scientifically meaningful?

## Student-safe answer

They retain traceable relationships to specific Level-2 product families and support relative screening. The paper must publish the exact formulas and caveats, while reserving stronger physical interpretation for POLIX experts and calibrated analyses.

## Self-test questions

1. Which features come from exposure products?
2. Why is channel 4000 not automatically an energy threshold?
3. What is omitted from the roll-smoothness calculation?
4. Which light-curve quality information is not used?
5. Is WeightedRoll one of the fifteen Matrix-C features?

---

# Module 7 - Principal Component Analysis

## Beginner explanation

Principal Component Analysis (PCA) rotates a table into new axes that capture large directions of variation. It helps visualize whether observations occupy similar or unusual positions. PCA does not know which observations are scientifically anomalous.

## Technical explanation

After standardization, PCA finds orthogonal loading vectors. For standardized row \(x\), the first two coordinates are

\[
z_k=x^\mathsf{T}v_k,\qquad k=1,2.
\]

The project uses two components and describes separation from the origin with

\[
d_{\mathrm{PCA}}=\sqrt{z_1^2+z_2^2}.
\]

For Matrix C, PC1 and PC2 explain about 0.6125 of the standardized variance in the existing ablation output. This leaves substantial variation outside the plotted plane. PCA distance is therefore a two-dimensional descriptive score, not a complete anomaly measure.

Existing rankings show a strong Spearman association between PCA distance and Isolation Forest score (\(\rho\approx0.895\)), but the reported p-value is descriptive for these same 25 observations. It is not evidence of independent validation, causality, or future generalization.

## Project-specific example

An observation can appear far from the center in the two-component PCA plot and also receive a high Isolation Forest score. That agreement shows that two summaries of the same standardized archive rank it similarly; it does not create two independent confirmations.

## Terms to remember

- loading
- principal component
- explained-variance ratio
- orthogonal
- score/coordinate
- dimensionality reduction
- PCA distance

## Common misunderstanding

**Misunderstanding:** “PC1 and PC2 contain all important information.”

**Correction:** They contain the largest two linear variance directions, not all information and not necessarily the directions most relevant to scientific interpretation.

## What the paper may say

PCA provides a low-dimensional geometric view and a descriptive distance used by the explanation layer.

## What the paper must not claim

It must not call PCA a ground-truth anomaly detector, interpret components causally, or use the correlation p-value as external validation.

## Likely reviewer question

**Question:** Why use two components when they explain only about 61% of Matrix-C variance?

## Student-safe answer

Two components were used for interpretable visualization and one contribution term, while Isolation Forest operates in the full standardized feature space. The paper should report the explained fraction and avoid implying that the plot contains the complete structure.

## Self-test questions

1. Why is StandardScaler applied before PCA?
2. What does an explained-variance ratio describe?
3. How is the project's two-component PCA distance calculated?
4. Why is PCA/Isolation correlation not independent confirmation?
5. What information is lost in a two-component plot?

---

# Module 8 - KMeans

## Beginner explanation

KMeans groups observations around a chosen number of centers. Each observation is assigned to its nearest center. The distance to that center describes how typical it is within the assigned group, but a cluster is not automatically a physical source class.

## Technical explanation

KMeans minimizes the within-cluster sum of squared Euclidean distances:

\[
\sum_i \left\|x_i-\mu_{c(i)}\right\|_2^2.
\]

The saved project model uses standardized Matrix-C features, \(k=5\), `n_init=20`, and random state 42. Its stored silhouette score is approximately 0.311. With only 25 observations, five clusters average five members and may contain very small or singleton groups.

The XAI layer assigns a feature-wise KMeans term

\[
(x_j-\mu_{c,j})^2.
\]

If an observation equals its cluster centroid, all KMeans contribution terms are zero. This occurs for a singleton cluster such as the current Sco X-1 assignment, so the KMeans explanation component adds no ranking information for that observation.

## Project-specific example

KMeans centroid distance has weak rank association with the PCA and Isolation Forest rankings in the existing results. This indicates that it describes local group geometry different from global separation, not that it is an independently validated anomaly detector.

## Terms to remember

- centroid
- cluster
- \(k\)
- within-cluster sum of squares
- initialization
- silhouette score
- singleton cluster
- centroid distance

## Common misunderstanding

**Misunderstanding:** “Five KMeans clusters mean five scientifically real classes.”

**Correction:** They are a mathematical partition of this small standardized archive. Physical classes require independent labels and domain evidence.

## What the paper may say

KMeans supplies local cluster context and a feature-wise squared distance from the assigned centroid.

## What the paper must not claim

It must not call KMeans an independent anomaly classifier, interpret clusters as source populations, or treat a singleton as scientific uniqueness.

## Likely reviewer question

**Question:** Is \(k=5\) credible for only 25 observations?

## Student-safe answer

It is an exploratory geometric setting retained in the frozen model, supported only by the recorded internal comparison. The small sample makes cluster membership fragile, so KMeans is used as contextual evidence rather than physical classification.

## Self-test questions

1. What objective does KMeans minimize?
2. Why must distance be interpreted in standardized feature space?
3. What does a silhouette score measure?
4. What happens to KMeans contribution for a singleton centroid?
5. Why are clusters not astrophysical classes?

---

# Module 9 - Isolation Forest

## Beginner explanation

Isolation Forest repeatedly splits feature space at random. Observations that can be isolated in fewer splits receive stronger anomaly evidence. The model ranks how unusual a row is relative to the fitted archive; it does not explain why the observation is scientifically unusual.

## Technical explanation

The saved model uses 100 trees, contamination 0.16, and random state 42. Contamination determines the fraction used to set the decision threshold. With \(n=25\), 0.16 corresponds to four flagged rows in the fixed run. Therefore, the four-candidate count is partly built into the threshold choice.

The fixed model flags Blank Sky-13, Sco X-1, Her X-1, and Blank Sky-5. In the existing 100-seed analysis, the first three are flagged 100/100 times, while Blank Sky-5 is flagged 29/100. Across the tested contamination settings 0.12-0.24, the first three remain flagged in every setting; boundary candidates change.

The leave-one-out refits show high rank agreement with the full fit, but this is internal perturbation of the same archive. The three cases are selected in every refit in which they remain in the training data; Sco X-1 is not flagged in its single held-out refit. This is not external validation or a test of future data drift. Feature-tier sensitivity also matters: only Blank Sky-13 and Sco X-1 are selected by all three A/B/C Isolation Forest fits, while Her X-1 is Matrix-C-specific.

## Project-specific example

“Three-candidate Matrix-C core stable under the tested procedures” means three identifiers persist under the recorded seed, threshold, and included-observation jackknife procedures. It does not mean they are true anomalies with 100% probability or stable across feature representations. The unqualified phrase “robust core” is unsafe.

## Terms to remember

- isolation tree
- path length
- anomaly score
- contamination
- decision threshold
- random seed
- stability frequency
- internal sensitivity
- data drift

## Common misunderstanding

**Misunderstanding:** “A 100/100 seed frequency is a 100% probability of being anomalous.”

**Correction:** It is an algorithmic stability count under tested random seeds on the same dataset and assumptions.

## What the paper may say

The fixed model flags four archive-relative anomaly candidates. Three form a Matrix-C stability core under the tested seeds, thresholds, and included-observation jackknife refits.

## What the paper must not claim

It must not report accuracy, probability, confirmed anomaly status, or future-data robustness without labels and an independent dataset.

## Likely reviewer question

**Question:** Why was contamination fixed at 0.16?

## Student-safe answer

It fixes a small candidate set of four within 25 observations and is an analysis assumption, not an estimated anomaly prevalence. The paper reports sensitivity across nearby values so readers can see which candidates depend on the threshold.

## Self-test questions

1. What intuition underlies Isolation Forest?
2. What does contamination control?
3. Which three candidates were stable in 100/100 tested seeds?
4. Why is Blank Sky-5 called seed-sensitive?
5. Why does leave-one-out stability not prove future generalization?

---

# Module 10 - Custom Four-Component XAI Method

## Beginner explanation

The XAI method asks which features provide the largest combined local evidence under several views of the frozen pipeline. It gives each feature four scores, rescales each score family within that observation, and adds them. The result is a project-specific ranking heuristic, not a causal explanation or an exact decomposition of the deployed label.

## Technical explanation

For standardized feature \(x_j\), the four raw components are:

1. **PCA contribution**

\[
|x_jv_{1j}|r_1+|x_jv_{2j}|r_2,
\]

where \(v_{kj}\) is a loading and \(r_k\) is its explained-variance ratio.

2. **KMeans contribution**

\[
(x_j-\mu_{c,j})^2.
\]

3. **Isolation Forest occlusion delta**

\[
s(x)-s(x\text{ with }x_j=0).
\]

Only positive deltas enter the combined score.

4. **Standardized abnormality**

\[
|x_j|.
\]

Each fifteen-value component vector is divided by its own maximum absolute value. A zero component becomes all zeros. The combined score is the unweighted sum of the four normalized components, normally between 0 and 4. This normalization is observation-relative: scores are well suited to ranking features within one observation but are not naturally comparable as calibrated magnitudes between observations.

The deployed `Anomaly`/`Normal` label comes only from `IsolationForest.predict`. PCA, KMeans, and the absolute standardized-value term do not vote on the label. When a component is nonzero, its maximum receives a normalized value of one even if its raw effect is small. Equal weighting is therefore a transparent heuristic choice, not evidence that the four components have equivalent scientific meaning. The components are also not independent: several are related functions of the same standardized row.

Features are mapped deterministically to product families by name prefixes. The website sentence is filled from a template using the prediction, score, top features, directions, and standardized values. It is not generated by an LLM.

## Project-specific example

For Sco X-1 the current order is:

1. peak channel — 2.454499;
2. weighted mean channel — 2.207369;
3. channel entropy — 1.813968.

Its assigned KMeans cluster is a singleton, so the KMeans component is zero. The historical entropy-first text is superseded.

## Terms to remember

- local explanation
- component normalization
- occlusion
- neutralization
- standardized value
- combined score
- product-family mapping
- deterministic template
- heuristic attribution
- local feature-importance ranking
- within-observation normalization

## Common misunderstanding

**Misunderstanding:** “The combined XAI score is SHAP.”

**Correction:** It is a project-specific sum of four normalized diagnostic components. It has no Shapley-value guarantee and SHAP was not used.

## What the paper may say

The project uses a deterministic, project-specific, model-informed local feature-ranking heuristic combining PC1/PC2 loading-weighted separation, assigned-centroid squared distance, positive Isolation Forest occlusion sensitivity, and absolute standardized abnormality.

## What the paper must not claim

It must not claim SHAP, causal attribution, globally comparable importance magnitudes, a unique decomposition of the Isolation Forest decision, four independent models, or that all four components determine the deployed label.

## Likely reviewer question

**Question:** Why are the four normalized components added with equal weight?

## Student-safe answer

Equal weighting is a transparent project design choice, but it has not been theoretically justified or empirically benchmarked. The paper should call the method a project-specific ranking heuristic and report its perturbation behavior rather than claim universal attribution validity.

## Self-test questions

1. What are the four explanation components?
2. How is each component normalized?
3. Why are negative occlusion deltas excluded from the combined score?
4. Why are scores mainly within-observation rankings?
5. Is the explanation sentence generated by an LLM?

---

# Module 11 - Faithfulness Testing

## Beginner explanation

An explanation is more useful if changing the features it ranks highly also changes the model's unusualness evidence. The project tests this by replacing the top three standardized features with zero, which represents the training mean after standardization, and then recomputing several scores.

## Technical explanation

For each of six exploratory cases, the test:

1. selects the top three Matrix-C features from the custom score;
2. sets those standardized values to zero simultaneously;
3. recomputes two-component PCA distance;
4. recomputes distance to the original KMeans centroid;
5. recomputes the Isolation Forest anomaly score.

The labels are project-defined from the sign of the changes:

- **Strong:** PCA distance and Isolation Forest anomaly score both decrease;
- **Moderate:** either PCA distance or Isolation Forest score decreases;
- **Weak:** neither decreases.

KMeans reduction is recorded but does not define the overall verdict. No minimum effect-size or statistical-significance threshold is required. Existing outputs reproduce five Strong, one Moderate, and zero Weak labels. These six are exploratory multi-matrix cases, not the fixed four deployed candidates.

The intervention can produce feature combinations not observed in the archive. It also uses the same zero baseline, top-three choice, fitted archive, and metrics that help construct the explanation. There is no random-feature, bottom-feature, or alternative-baseline comparator. Therefore, it is an in-sample, method-aligned perturbation sanity check under one intervention, not causal truth, scientific correctness, or general faithfulness.

## Project-specific example

If neutralizing the three highest-ranked features lowers both PCA separation and Isolation Forest score, the explanation is consistent with those two model summaries under that intervention. It does not prove that the features caused the real observation or that a domain expert would choose the same explanation.

## Terms to remember

- faithfulness
- perturbation
- neutralization
- baseline
- top-\(k\)
- score reduction
- intervention
- out-of-distribution perturbation

## Common misunderstanding

**Misunderstanding:** “Five Strong verdicts prove that the explanation method is correct.”

**Correction:** They show internal score reduction for five selected cases under one top-three-to-zero intervention.

## What the paper may say

For six exploratory cases, neutralizing the top three ranked features reduced both PCA and Isolation Forest evidence in five cases and one of those measures in the remaining case, under the project's sign-based verdict definitions.

## What the paper must not claim

It must not call the verdicts causal validation, domain validation, statistically significant validation, proof of universal faithfulness, or evidence covering all 25 observations.

## Likely reviewer question

**Question:** Why is six cases enough?

## Student-safe answer

It is enough only as a small, transparent internal diagnostic for the selected exploratory cases. The paper must not generalize the verdict rates and should treat wider baselines, more cases, and alternative perturbations as future evaluation.

## Self-test questions

1. How many top features are neutralized?
2. What does zero mean in standardized space?
3. What defines Strong, Moderate, and Weak?
4. Does KMeans reduction determine the verdict?
5. Name two things the test does not prove.

---

# Module 12 - WeightedRoll Fitting and Harmonic Coefficients

## Beginner explanation

WeightedRoll records exposure-weighted count-rate modulation with roll azimuth. The handbook says it includes source and background contributions. The project fits a two-fold wave to summarize each curve, but this is a raw diagnostic rather than a calibrated polarization measurement.

## Technical explanation

For valid bins with angle \(\phi_i\), rate \(y_i\), and supplied error \(\sigma_i>0\), the design matrix contains \(1\), \(\cos2\phi_i\), and \(\sin2\phi_i\). The weighted least-squares solution is

\[
\hat\beta=(X^\mathsf{T}WX)^{-1}X^\mathsf{T}Wy,
\quad
W_{ii}=\sigma_i^{-2},
\]

where \(\hat\beta=(C,Q,U)\). The frozen notebook uses a matrix inverse and controls the saved CSV results; the current Flask service uses a pseudoinverse.

The code derives:

\[
A=\sqrt{Q^2+U^2},\qquad
m_{\mathrm{raw}}=\frac{A}{C},\qquad
\psi_{\mathrm{fit}}=\frac12\operatorname{atan2}(U,Q)\bmod180^\circ.
\]

The notebook takes the inverse normal matrix as coefficient covariance and does not multiply it by reduced chi-square. Its amplitude and phase propagation include \(Q/U\) covariance, but its \(A/C\) uncertainty omits covariance between amplitude and \(C\). The current Flask service uses a different full three-parameter gradient for \(A/C\). Saved CSV uncertainties are therefore notebook-method results, and the two implementations must not be silently conflated. All formal errors rely on the supplied FITS errors, independence assumptions, and adequacy of the simple harmonic model.

Fit quality is a project rule:

- acceptable: reduced chi-square <=2;
- caution: >2 and <=5;
- poor simple sinusoid fit: >5.

Because official equivalence to calibrated Stokes products is not established, “cosine and sine harmonic coefficients” and “fractional harmonic coordinates” are safer than unqualified “Stokes Q/U.” “Stokes-like” is acceptable only with an explicit empirical qualifier and guide approval.

## Project-specific example

All 25 curves have fit rows, but some have poor or caution fit quality. Her X-1 has a very poor simple-sinusoid fit, so its harmonic summary should not be treated with the same confidence as an acceptable fit even if another branch flags it.

## Terms to remember

- weighted least squares
- design matrix
- pseudoinverse
- harmonic coefficient
- covariance
- reduced chi-square
- raw modulation
- fitted phase
- fit quality

## Common misunderstanding

**Misunderstanding:** “A high signal-to-noise fitted harmonic automatically proves polarization.”

**Correction:** Background modulation, model mismatch, systematic effects, calibration, and the handbook's release limits still apply.

## What the paper may say

The project fits a weighted second-harmonic model and reports raw modulation, fitted phase, propagated formal uncertainty, and fit-quality class as archive diagnostics.

## What the paper must not claim

It must not call the coefficients official Stokes measurements, the modulation calibrated PD, the phase sky PA, WeightedRoll officially background-subtracted, or the fit-quality thresholds p-values or detection criteria.

## Likely reviewer question

**Question:** Are the formal uncertainties reliable when reduced chi-square is large?

## Student-safe answer

They are conditional on the supplied errors and simple harmonic model. Large reduced chi-square signals model mismatch or underestimated/systematic uncertainty, so the result is downgraded and interpreted cautiously rather than used as a calibrated measurement. The saved CSV values specifically use the notebook propagation, whose \(A/C\) error omits amplitude-mean covariance.

## Self-test questions

1. What columns form the harmonic design matrix?
2. Why are weights \(1/\sigma^2\)?
3. How are raw modulation and fitted phase calculated?
4. What are the three fit-quality ranges?
5. Why is “harmonic coefficient” safer than unqualified “Stokes parameter” here?

---

# Module 13 - Empirical Blank-Sky Comparison

## Beginner explanation

The project uses blank-sky observations to learn what raw modulation patterns look like in this local archive. It does not subtract a blank-sky curve from each source. Instead, it compares fitted summary coefficients with the mean and scatter of selected blank-sky fits.

## Technical explanation

Fifteen blank-sky observations were fitted. Thirteen classified as acceptable under reduced chi-square <=2 form the empirical baseline. For those fits:

- mean raw modulation: 1.147820%;
- sample SD: 0.565960%;
- mean normalized cosine coefficient \(q=Q/C\): 0.0090920;
- sample SD of \(q\): 0.0048569;
- mean normalized sine coefficient \(u=U/C\): -0.0064782;
- sample SD of \(u\): 0.0040190.

The project computes a diagonal standardized distance

\[
d_{\mathrm{blank}}
=
\sqrt{
\left(\frac{q-\bar q}{s_q}\right)^2+
\left(\frac{u-\bar u}{s_u}\right)^2
}.
\]

This ignores covariance between \(q\) and \(u\), parameter uncertainty, observation matching, and uncertainty in the estimated baseline. Thresholds at 2 and 3 are project heuristics, not calibrated confidence contours. A separate scalar raw-modulation z-score uses the blank mean and sample SD.

All ten source raw-modulation values fall within the empirical blank-sky mean plus or minus two sample standard deviations under the project's declared scalar rule. The ML branch nevertheless flags source and blank-sky observations. This supports the bounded statement that statistical unusualness in Matrix C and modulation-like evidence are non-equivalent within this archive.

## Project-specific example

Sco X-1 is a stable ML candidate but lies within the empirical blank-sky modulation scatter. Her X-1 is also an ML candidate and has a moderate project vector distance, but its simple harmonic fit is poor, so the displacement is not reliable physical confirmation. Crab P01_0005 is not a fixed ML candidate although it has the largest source raw modulation, and it remains within the declared scalar and vector blank-sky rules. None supports polarization detection; together they show why the two branches must remain separate.

## Terms to remember

- empirical baseline
- acceptable fit
- normalized coefficient
- sample standard deviation
- standardized distance
- diagonal metric
- covariance
- heuristic threshold
- non-equivalence

## Common misunderstanding

**Misunderstanding:** “Subtracting the blank-sky mean coefficients performs official background subtraction.”

**Correction:** It creates an archive-relative comparison vector. It does not reproduce the official observation-matched background pipeline.

## What the paper may say

Thirteen acceptable blank-sky fits define an empirical archive reference used to compare raw harmonic coefficients and modulation summaries.

## What the paper must not claim

It must not call the reference an official background model, a polarization-detection threshold, a calibrated confidence region, an independent calibration dataset, or proof that sources within the scatter are unpolarized.

## Likely reviewer question

**Question:** Is thirteen blank-sky observations enough for a two-dimensional statistical baseline?

## Student-safe answer

It is sufficient only for a descriptive archive diagnostic. The small, non-random sample and diagonal metric limit inference; a calibrated background analysis would require more data, matched conditions, covariance and uncertainty treatment, and official guidance.

## Self-test questions

1. Why were only thirteen of fifteen blank-sky fits used?
2. What do \(q=Q/C\) and \(u=U/C\) represent here?
3. What information does the diagonal distance ignore?
4. Why are thresholds 2 and 3 heuristic?
5. What is the safe central non-equivalence conclusion?

---

# Answers to Modules 5-13

## Module 5 answers

1. Ten source and fifteen blank-sky observations.
2. IDs are unique; friendly labels include a duplicated “Blank Sky-2.”
3. Blank-sky measurements contain variable instrumental/environmental counts and have no anomaly ground-truth status.
4. Results describe relative position within the frozen 25-observation collection.
5. None.

## Module 6 answers

1. `t1A_exp_uniformity_cv` and `t1A_exp_max_to_min_roll`.
2. The code uses an index threshold without consulting an official channel-to-energy calibration.
3. The last-to-first circular difference and an explicit angle sort.
4. FRAC_EXP, uncertainties, quality flags, and explicit GTI/bin comparability.
5. No.

## Module 7 answers

1. To prevent features with large numerical scales from dominating covariance and distance.
2. The fraction of standardized variance represented by a component.
3. \(\sqrt{PC1^2+PC2^2}\).
4. Both rankings come from the same standardized 25 observations and are not independent samples.
5. Variation represented by components 3-15 and any nonlinear structure.

## Module 8 answers

1. The sum of squared distances from observations to their assigned centroids.
2. Standardization defines the scale on which Euclidean distance is computed.
3. Separation between clusters relative to within-cluster compactness.
4. The row equals the centroid, so all feature-wise squared distances are zero.
5. No physical labels or independent validation establish such an interpretation.

## Module 9 answers

1. Unusual points tend to be isolated by fewer random partitions.
2. The decision threshold/candidate fraction assumed for the fitted data.
3. Blank Sky-13, Sco X-1, and Her X-1.
4. It is flagged in only 29 of 100 tested seeds.
5. It repeatedly perturbs and refits the same small archive rather than testing unseen future observations.

## Module 10 answers

1. PCA contribution, squared centroid-distance contribution, positive Isolation Forest occlusion delta, and absolute standardized value.
2. Divide its fifteen feature values by that component's maximum absolute value; a zero component becomes zeros.
3. A negative delta means neutralization increased rather than reduced anomaly score, so the implemented heuristic clips it to zero.
4. Normalization is recalculated within each observation and component.
5. No; it is deterministic template text.

## Module 11 answers

1. Three.
2. The training mean for that feature after StandardScaler transformation.
3. Strong: PCA and IF reduce; Moderate: either reduces; Weak: neither reduces.
4. No.
5. Causal correctness, domain correctness, all-observation coverage, baseline robustness, and future-data faithfulness are not proved.

## Module 12 answers

1. A constant column, \(\cos2\phi\), and \(\sin2\phi\).
2. Under independent Gaussian-error assumptions, inverse variance gives higher weight to more precise bins.
3. \(100\sqrt{Q^2+U^2}/C\) and \(\tfrac12\operatorname{atan2}(U,Q)\bmod180^\circ\).
4. Acceptable <=2; caution >2 to <=5; poor >5.
5. Official equivalence, calibration, coordinate convention, and background treatment are not established.

## Module 13 answers

1. Two failed the project's acceptable-fit rule of reduced chi-square <=2.
2. Empirical normalized cosine and sine harmonic coefficients.
3. Q/U covariance, coefficient uncertainty, baseline-estimation uncertainty, and observing-condition matching.
4. They are project-configured descriptive cutoffs, not derived confidence contours.
5. Matrix-C statistical unusualness and raw modulation evidence need not agree within this archive.

---

# Modules 14-18

# Module 14 - Results and Candidate Sets

## Beginner explanation

The project produced several related lists, but they answer different questions. The saved deployed model flags four observations under one frozen decision rule. Repeating Isolation Forest with 100 seeds asks whether that decision is sensitive to randomness. Comparing Matrices A, B, and C asks whether it changes when the feature representation changes. The six observations used in the explanation check are a separate exploratory set. None of these lists is anomaly ground truth.

## Technical explanation

The fixed artifact uses Matrix C, StandardScaler, Principal Component Analysis (PCA), KMeans, and Isolation Forest with contamination 0.16. Its binary label comes only from `IsolationForest.predict`, producing 21 Normal rows and four candidates:

1. `X01_PLX_C24_0018_000000` (project-labelled Blank Sky-13);
2. `X01_PLX_G01_0006_000000` (Sco X-1);
3. `X01_PLX_G01_0003_000000` (Her X-1);
4. `X01_PLX_C24_0010_000000` (project-labelled Blank Sky-5).

Across the existing 100-seed test, the first three were selected in 100/100 fits, while Blank Sky-5 was selected in 29/100. `C24_0020`, which is not in the fixed four, was selected in 68/100 and therefore belongs to the uncertain threshold neighborhood. Across the tested contamination values 0.12, 0.16, 0.20, and 0.24, the same first three remained selected. In included-observation jackknife refits they were selected in 24/24 applicable fits, but Sco X-1 was not selected in its single held-out refit. Only `C24_0018` and `G01_0006` persist across the Matrix A, B, and C candidate sets. These distinctions prevent seed stability, feature-tier persistence, and fixed deployment from being conflated.

## Project-specific example

Blank Sky-5 belongs to the frozen four but is seed-sensitive. Her X-1 belongs to the three-candidate Matrix-C tested-procedure core but not to the cross-tier pair. Sco X-1 belongs to the fixed four, the 100-seed trio, and the cross-tier pair, yet it failed its one held-out refit. Its accepted local ranking is energy peak channel (2.454499), energy weighted mean channel (2.207369), and energy channel entropy (1.813968); the historical entropy-first narrative is superseded. Each statement is true under a different test.

## Terms to remember

- fixed deployed result;
- candidate, not confirmed anomaly;
- seed frequency;
- threshold neighborhood;
- contamination sensitivity;
- included-observation jackknife;
- held-out refit;
- cross-feature-tier persistence;
- exploratory XAI case.

## Common misunderstanding

“Four fixed candidates,” “three stable candidates,” “two cross-tier candidates,” and “six XAI cases” are not competing versions of one result. They describe one saved decision, procedure sensitivity, representation sensitivity, and an exploratory explanation sample, respectively.

## What the paper may say

The frozen model flagged four candidates. Three formed a Matrix-C core stable under the tested seed, contamination-threshold, and included-observation jackknife procedures. Candidate membership nevertheless depended on feature tier and the archive contained an uncertain boundary neighborhood.

## What the paper must not claim

It must not call the four observations confirmed anomalies, interpret seed frequencies as probabilities, call the three a generally robust core, describe the jackknife as external validation, or claim that Matrix C is superior.

## Likely reviewer question

Why should I trust four candidates when one appears in only 29 of 100 seed fits?

## Student-safe answer

The paper reports the four because they are the exact frozen deployment output. It separately discloses that Blank Sky-5 is seed-sensitive and that another blank-sky observation frequently competes near the threshold. The result is therefore an archive-relative screening list for inspection, not four equally stable discoveries.

## Self-test questions

1. Name the four fixed candidates.
2. Which three were selected in all 100 tested seeds?
3. What does Blank Sky-5's 29/100 frequency mean?
4. Which two candidates persist across Matrices A, B, and C?
5. Why are the six XAI cases not another deployed candidate set?

---

# Module 15 - Research Contribution and Novelty Boundaries

## Beginner explanation

A contribution is the useful, evidence-supported thing the paper adds. It need not be a brand-new algorithm. Here, the strongest contribution is the complete, traceable way of turning several POLIX Level-2 products into an observation-level screening workflow while keeping the harmonic branch scientifically separate.

## Technical explanation

Agent 8 rates the primary contribution **MODERATE**:

> A traceable, product-aware Explainable Artificial Intelligence framework for archive-relative screening of heterogeneous POLIX Level-2 observations.

Three secondary contributions are also MODERATE when bounded:

1. a 15-feature observation representation preserving provenance to selected product families;
2. a deterministic, project-specific, model-informed local feature-ranking method;
3. a separate WeightedRoll and empirical blank-sky harmonic diagnostic branch that avoids direct circular confirmation.

StandardScaler, PCA, KMeans, and Isolation Forest are established methods. Seed checks, contamination sensitivity, jackknife, feature-tier comparison, and the six-case perturbation test are supporting evidence. The Flask interface is a proof-of-concept implementation. None is a separate major contribution. The literature audit found limited directly comparable POLIX work, but it did not justify priority, uniqueness, superiority, or algorithmic novelty.

## Project-specific example

The framework can take Sco X-1 from its Matrix-C row to a frozen candidate label, rank peak channel, weighted mean channel, and entropy as its leading local evidence, map these features back to the energy-resolved product family, and then compare the observation separately in the WeightedRoll harmonic branch. The value lies in traceable integration and scientific separation.

## Terms to remember

- primary contribution;
- secondary contribution;
- applied methodology;
- systems integration;
- product-aware;
- provenance-preserving;
- archive-relative;
- supporting evidence;
- proof of concept;
- literature gap.

## Common misunderstanding

Using several established algorithms together does not automatically create a new algorithm. A defensible applied contribution can instead be a carefully bounded, reproducible integration for a scientific product ecosystem.

## What the paper may say

The work investigates an integrated, traceable framework, and the reviewed literature did not provide a directly comparable POLIX Level-2 workflow combining these elements.

## What the paper must not claim

It must not use “first,” “novel,” “unique,” “superior,” “breakthrough,” or “discovery”; claim that the ML stack is algorithmically new; elevate the six-case test or Flask interface to a major contribution; or imply SHAP/LIME deployment.

## Likely reviewer question

What is publishable here if PCA, KMeans, and Isolation Forest already exist?

## Student-safe answer

The claim is not algorithmic invention. The applied contribution is the traceable POLIX-specific representation and workflow: heterogeneous product summaries, archive-relative screening, local evidence linked to product provenance, and an independent uncalibrated harmonic diagnostic. Its strength is moderate and archive-bounded.

## Self-test questions

1. State the primary contribution in one sentence.
2. Name the three secondary contributions.
3. Why is the ML stack not a separate algorithmic contribution?
4. What role does the Flask interface play?
5. Why does “limited directly comparable work” not prove priority?

---

# Module 16 - Limitations and Safe Scientific Claims

## Beginner explanation

Limitations are not admissions that the project failed. They tell the reader exactly where the evidence stops. A strong defense separates verified implementation results from labels, calibrated physics, future generalization, and causal explanation.

## Technical explanation

The decisive limitations are: \(n=25\); no anomaly labels or independent test set; retrospective use of one archive; contamination-defined candidate count; feature-tier dependence; singleton KMeans clusters; project-specific heuristic XAI; six in-sample perturbation cases; no future-release validation; WeightedRoll containing source plus background; a selected 13-fit empirical reference; project-defined fit-quality and vector-distance rules; no official background procedure, \(\mu_{100}\), or sky-angle conversion; different Notebook-11 and Flask \(A/C\) uncertainty propagation; an unpinned original environment; and feature semantics needing POLIX-aware review.

Agent 9's present verdict is **WEAK REJECT**, with a plausible path to **Weak Accept** for an appropriate applied or student venue after evidence-bounded reconstruction and guide/domain review. No fatal numerical contradiction invalidates the central archive-screening result. Broader anomaly-validation, general-XAI, calibrated-polarimetry, or novelty claims would create fatal claim-evidence conflicts. No new experiment is mandatory for the narrow case-study framing; external validation becomes essential only if broader generalization or accuracy claims are retained.

## Project-specific example

The project may report the Notebook-11/CSV central harmonic results and disclose that the later Flask service propagates \(A/C\) uncertainty differently. It may not silently present both implementations as identical. Similarly, reduced chi-square at or below two is a project-defined acceptable-fit rule, not an official POLIX certification.

## Terms to remember

- claim boundary;
- threat to validity;
- retrospective analysis;
- external validation;
- domain approval;
- disclosure-only limitation;
- fatal claim-evidence conflict;
- uncertainty provenance;
- project-defined rule;
- future work.

## Common misunderstanding

A Weak Reject review does not mean that the project result is false. Here it means the current evidence is too narrow for a broad methodology claim, while a carefully reconstructed, archive-bounded case study may be acceptable.

## What the paper may say

The frozen workflow reproducibly screened the included archive and supports bounded descriptive comparisons. It requires expert inspection, future-release evaluation, and official calibration before broader scientific conclusions.

## What the paper must not claim

It must not claim predictive accuracy, future generalization, anomaly probability, causal explanations, calibrated Stokes quantities, polarization detection, official background subtraction, calibrated PD, official PA, or identical notebook/service uncertainty implementations.

## Likely reviewer question

Are the limitations so severe that the paper should not be submitted?

## Student-safe answer

They prevent a broad validation paper, but they do not invalidate a transparent applied case study. Agent 9 found no fatal numerical contradiction for the bounded archive-screening result and required no new experiment under that narrow framing. Guide and POLIX-aware review remain necessary.

## Self-test questions

1. Give five major threats to validity.
2. What does Agent 9's Weak Reject verdict mean?
3. When would an independent future-release experiment become essential?
4. How must the uncertainty mismatch be disclosed?
5. Why are project-defined thresholds not statistical significance levels?

---

# Module 17 - IEEE Conference Paper Structure

## Beginner explanation

An IEEE-style paper is an argument with evidence, not a chronological project diary. The introduction states the problem and contribution; related work positions it; methodology explains what was done; results report what was observed; discussion interprets carefully; limitations state what remains unknown; and the conclusion answers the research question without exaggeration.

## Technical explanation

The planned paper uses:

1. Introduction: X-ray polarimetry context, multi-product problem, gap, scope, and one primary plus up to three secondary contributions.
2. Related Work: XPoSat/POLIX, harmonic foundations, astronomy anomaly screening, explainable anomaly detection, and the bounded gap.
3. Dataset, Scope, and Problem Formulation: 25 rows, project role mapping, product families, no ground truth, and calibration boundaries.
4. Product-Aware Feature Engineering: Matrix A/B/C history, final 15 features, provenance, proxy limitations, and WR exclusion.
5. Explainable Unsupervised Methodology: preprocessing, PCA, KMeans, Isolation Forest, contamination, local ranking, and perturbation sanity check.
6. Independent Harmonic Diagnostic: WeightedRoll semantics, weighted second harmonic, empirical 15/13 blank-sky reference, and no calibrated PD/PA.
7. Results: fixed four, procedure-qualified three, cross-tier pair, local examples, and bounded harmonic evidence.
8. Discussion: non-equivalence within the frozen archive.
9. Limitations and Threats to Validity.
10. Conclusion: implementation, archive observation, uses, exclusions, and future official calibration.

The title is the exact college project title, **“An Explainable AI Framework for Analysis of X-Ray Polarimetry Data from XPoSat.”** The abstract must state the archive size, method, bounded result, and principal limitation without citations. Figures and tables must carry real project evidence and must not imply confidence regions that were not computed.

## Project-specific example

The fixed four belong in Results, not in the Introduction as a headline discovery. The explanation of contamination belongs in Methodology; its sensitivity belongs in Results; and the absence of ground truth belongs in Dataset/Problem Formulation and Limitations.

## Terms to remember

- abstract;
- index terms;
- related work;
- methodology;
- results;
- discussion;
- threats to validity;
- acknowledgment;
- references;
- supplement.

## Common misunderstanding

Results and Discussion are not the same. Results state the controlled observations; Discussion explains their bounded meaning and alternatives without inventing causes.

## What the paper may say

Each section should make one traceable part of the argument and send detailed formulas, full stability tables, all 25 harmonic rows, and the uncertainty comparison to supplementary material.

## What the paper must not claim

The structure must not hide limitations, repeat results as novelty, cite sources in the abstract, use figures as unsupported physical confirmation, or allow the broad title to imply calibrated XPoSat polarimetry.

## Likely reviewer question

Why is the harmonic branch in the same paper if it is not part of the anomaly input?

## Student-safe answer

Its deliberate separation is part of the methodology. It provides an independent descriptive comparison and demonstrates that archive-relative statistical unusualness and modulation-like harmonic behavior answer different questions.

## Self-test questions

1. What belongs in the Introduction rather than Results?
2. Where should contamination be explained and evaluated?
3. What is the difference between Results and Discussion?
4. Which details should move to supplementary material?
5. Why must the abstract avoid citations and calibrated claims?

---

# Module 18 - Viva and Hostile-Reviewer Defense

## Beginner explanation

A safe defense does not try to “win” every question. It identifies the evidence, gives the narrow answer supported by that evidence, states the limitation, and names the approval or future test required for a broader conclusion.

## Technical explanation

A useful response pattern is:

1. **Define** the exact term.
2. **Locate** the controlling evidence.
3. **State** the archive-bounded result.
4. **Separate** it from nearby but different results.
5. **Limit** the interpretation.
6. **Escalate** unresolved physical semantics to the guide or POLIX-aware expert.

The hostile review's central challenge is that a standard methodology venue may expect external validation, benchmarked explanation quality, and calibrated physical interpretation. The response is not to invent experiments. It is to present one moderate applied integration contribution, demote robustness and faithfulness to supporting checks, disclose every material limitation, and choose a venue appropriate for a small unlabeled archive case study.

## Project-specific example

Question: “Did the model detect polarized Sco X-1 behavior?” Safe response: “No. Sco X-1 was statistically unusual under the frozen Matrix-C Isolation Forest rule. Its leading local ranked evidence was peak channel, weighted mean channel, and entropy. The separate source-plus-background harmonic diagnostic did not establish polarization and remained within the declared empirical blank-sky rules.”

## Terms to remember

- controlling evidence;
- bounded answer;
- nearest false claim;
- guide approval;
- domain approval;
- conditional acceptance;
- reviewer rebuttal;
- evidence hierarchy;
- manual author verification;
- submission readiness.

## Common misunderstanding

A confident answer is not necessarily a broad answer. The most defensible viva response is often: “The project established X within this archive; it did not establish Y; Z would require official calibration or external validation.”

## What the paper may say

The paper may answer the research question affirmatively as a proof-of-concept archive-relative implementation, while stating that scientific interpretation and future generalization remain open.

## What the paper must not claim

Students must not improvise causes, replace “candidate” with “anomaly,” turn frequency into probability, describe XAI as SHAP, call raw modulation PD, call phase PA, or conceal AI-assisted drafting and unresolved expert-review items.

## Likely reviewer question

Why should this paper be accepted after a Weak Reject audit?

## Student-safe answer

The audit addressed a broad methodology reading. Under the reconstructed scope, the paper offers a reproducible, moderate applied integration for an unusual scientific product archive, discloses its limitations, makes no calibrated or predictive claim, and requires guide/domain approval before submission. The venue must match that scope.

## Self-test questions

1. What are the six steps in the safe response pattern?
2. What is the nearest false claim to “archive-relative candidate”?
3. How should a student answer an unresolved POLIX semantic question?
4. Why must the hostile-review verdict remain visible?
5. What must happen before the content is submission-ready?

---

# Answers to Modules 14-18

## Module 14 answers

1. `C24_0018` (Blank Sky-13), `G01_0006` (Sco X-1), `G01_0003` (Her X-1), and `C24_0010` (Blank Sky-5).
2. `C24_0018`, `G01_0006`, and `G01_0003`.
3. It is selected in 29 of the 100 tested seed fits, showing seed sensitivity near the threshold; it is not a 29% anomaly probability.
4. `C24_0018` and `G01_0006`.
5. They were selected for an exploratory perturbation sanity check, not returned as the saved deployed candidate set.

## Module 15 answers

1. A traceable, product-aware XAI framework for archive-relative screening of heterogeneous POLIX Level-2 observations.
2. The provenance-preserving 15-feature representation, project-specific local ranking, and separate harmonic/blank-sky branch.
3. Its algorithms are established; the contribution is their bounded scientific integration and traceability.
4. Supporting proof-of-concept implementation and researcher-facing reproducibility, not a major scientific contribution.
5. A finite literature search can fail to locate a comparison without proving none exists or that this work has priority.

## Module 16 answers

1. Any five of: \(n=25\), no labels/test set, same-archive analysis, contamination-defined threshold, feature-tier dependence, singleton clusters, heuristic XAI, six in-sample perturbation cases, no future validation, uncalibrated/background-containing WeightedRoll, selected baseline, uncertainty mismatch, unpinned environment, or unresolved semantics.
2. The broad methodology framing is presently too strong, but a narrowly bounded applied case study could become Weak Accept after reconstruction and review.
3. If the paper claims accuracy, transfer, future-POLIX generalization, or a generally validated method.
4. Use frozen Notebook-11/CSV values as reported provenance and state that the later service uses a different propagation; do not merge them.
5. They were configured as descriptive decision rules without a calibrated null distribution or official detection interpretation.

## Module 17 answers

1. Context, the computational problem, the bounded gap, scope, research question, and contribution list.
2. Define it in Methodology and report existing sensitivity evidence in Results.
3. Results report observations; Discussion gives bounded interpretation and connects them to the research question.
4. Complete feature formulas, full seed/contamination/jackknife tables, six-case values, all harmonic rows, PD scenarios if retained, and uncertainty comparison.
5. The abstract must be self-contained and must not imply evidence or calibration that the paper does not possess.

## Module 18 answers

1. Define, locate evidence, state the bounded result, separate nearby results, limit interpretation, and escalate unresolved domain meaning.
2. “Confirmed anomaly,” “validated anomaly,” or a physical-discovery statement.
3. State the verified computation, avoid physical reinterpretation, and identify the required guide or POLIX-aware approval.
4. It records the actual submission risk and the conditions required for a defensible venue-matched paper.
5. Evidence and citation checks, guide/domain review, author order and venue decisions, manual author revision, figure approval, and venue-compliant AI disclosure.
