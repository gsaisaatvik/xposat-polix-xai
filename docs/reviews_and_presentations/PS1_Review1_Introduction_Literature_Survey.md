# An Explainable AI Framework for Analysis of X-Ray Polarimetry Data from XPoSat

## Project Stage-I — Review 1 Report

| Field | Details |
|---|---|
| Team number | [TO BE FILLED] |
| Team members | [TO BE FILLED] |
| Roll numbers | [TO BE FILLED] |
| Faculty supervisor | [TO BE FILLED] |
| Department | [TO BE FILLED] |
| Institution | [TO BE FILLED] |
| Branch and section | [TO BE FILLED] |
| Academic year | [TO BE FILLED] |
| Date of review | [TO BE FILLED] |

---

## Abstract

X-ray astronomy investigates high-energy processes associated with compact objects, accretion flows, supernova remnants and relativistic particles. Imaging, spectroscopy and timing reveal where X-rays originate, how their energy is distributed and how emission changes with time, but these observables can leave competing source geometries insufficiently constrained. Linear X-ray polarization provides complementary information through polarization degree and angle, which are sensitive to emission asymmetry, magnetic-field structure and scattering geometry. India’s X-ray Polarimeter Satellite (XPoSat) carries POLIX for medium-energy polarimetry and XSPECT for spectroscopy and timing [1], [4].

The proposed study addresses the heterogeneous Level-2 FITS products associated with each POLIX observation when trusted anomaly labels are unavailable. The project aims to develop an unsupervised, interpretable screening framework representing exposure, energy-resolved azimuthal behaviour, source azimuthal distributions, timing and detector balance through scientifically meaningful features. PCA, clustering and anomaly detection are intended to prioritize observations rather than make automated discovery claims. Product-aware explanations are planned so that a score can be traced to its contributing features and original product families.

An independent physical diagnostic is intended for the `WeightedRoll_L2.fits` modulation product, supported by blank-sky comparison and established Stokes or modulation-curve concepts [2], [8]. The expected contribution is a reproducible researcher-oriented screening method that separates statistical unusualness from polarization evidence. The major scientific limitation is that current modulation products contain source and background contributions. Calibrated polarization degree and official sky polarization angle therefore cannot be claimed without appropriate background treatment, response calibration and mission-approved conventions [2].

---

# 1. Introduction

## 1.1 Background of X-Ray Astronomy

X-ray astronomy studies celestial radiation at energies substantially higher than visible light. The Earth’s atmosphere absorbs astronomical X-rays, so observational X-ray astronomy depends mainly on space-borne detectors. Cosmic X-rays are commonly produced where matter reaches very high temperatures, particles are accelerated to relativistic energies, or material interacts with strong gravitational and magnetic fields. Accreting black holes and neutron stars, pulsars, supernova remnants and hot plasma in galaxies and clusters are therefore prominent X-ray sources [5], [7].

Three established observational approaches are especially important:

1. **Imaging** determines where X-ray photons originate and reveals spatial structures such as shocks, jets, compact cores and supernova-remnant filaments. Chandra is a leading example of a mission optimized for high-angular-resolution X-ray imaging, with instruments that also support spectroscopy [5].
2. **Spectroscopy** measures photon energy distributions. Spectral continua and lines can constrain temperature, composition, absorption, ionization and emission mechanisms.
3. **Timing** examines variability over timescales ranging from milliseconds to years. Pulsations, eclipses, bursts and quasi-periodic variations can connect emission to orbital motion, rotation or changing accretion states.

These approaches are powerful but may not uniquely determine a source model. Two geometrically different emitting regions can sometimes produce similar spectra or light curves, particularly when the source is too small to be spatially resolved. Polarimetry adds observables that depend on directional asymmetry. It can therefore help distinguish between otherwise degenerate descriptions of an accretion disc, corona, jet, magnetic pole or scattering region [7], [8].

For a Computer Science project, the practical implication is that an X-ray observation is not a single number or image. It is a set of related data products, each preserving a different aspect of the observation. A computational framework must retain those relationships rather than compress all information into an unexplained score.

## 1.2 X-Ray Polarization

An electromagnetic wave is linearly polarized when its electric-field oscillation has a preferred orientation perpendicular to the direction of propagation. An astronomical beam normally contains many photons and is described statistically. The **polarization degree** (PD) denotes the fraction of the measured radiation associated with a preferred linear orientation, while the **polarization angle** (PA) specifies that orientation under an adopted reference convention. Because linear polarization is unchanged by a 180° rotation of its direction, azimuthal polarimetry has a characteristic two-fold periodicity [7], [8].

Polarization is connected to physical structure because many X-ray emission and interaction processes are direction-dependent. Synchrotron radiation is related to ordered magnetic fields; scattering in an asymmetric medium can create or modify polarization; and emission from a disc-plus-corona system can carry information about inclination and coronal geometry. In pulsars and accreting neutron stars, phase-dependent polarization can constrain the relation between the rotation axis, magnetic axis and observer [9]. In black-hole binaries, the energy dependence and orientation of polarization can constrain the geometry of the inner X-ray-emitting region relative to a jet or disc [10].

Polarization should nevertheless be interpreted with care. A measured azimuthal modulation is not automatically a calibrated PD. Instrument response, background, modulation factor, exposure distribution and angle conventions must be considered. Similarly, a fitted phase in a detector-coordinate modulation curve is not automatically an official sky PA. These distinctions are central to the proposed study [2], [8].

## 1.3 Existing X-Ray Missions and Context

The missions relevant to this study have distinct scientific roles:

| Mission or payload | Primary role relevant to this study | Verified operating context |
|---|---|---|
| **Chandra X-ray Observatory** | High-resolution X-ray imaging, imaging spectroscopy and dispersive spectroscopy | Chandra provides sub-arcsecond-class imaging and spectroscopic capability; it is not treated here as a dedicated polarimetry mission [5]. |
| **Imaging X-ray Polarimetry Explorer (IXPE)** | Dedicated imaging X-ray polarimetry | IXPE uses three telescope systems with polarization-sensitive imaging detectors and operates principally over 2–8 keV [6]. |
| **XPoSat** | Indian space observatory dedicated to X-ray polarimetry with supporting spectroscopic and timing capability | XPoSat carries POLIX and XSPECT and was launched on 1 January 2024 [1], [4]. |
| **POLIX** | Collimated medium-energy X-ray polarimetry | POLIX measures azimuthal scattering information in the 8–30 keV band [1], [2]. |
| **XSPECT** | X-ray spectroscopy and timing | XSPECT provides spectroscopic and temporal information in the 0.8–15 keV band [1], [4]. |

This comparison prevents two category errors. First, Chandra’s contribution is primarily its imaging and spectroscopic capability, not dedicated polarimetry. Second, IXPE and POLIX are both polarimetric instruments but use different observational and detector arrangements and cover different principal energy bands. XSPECT complements POLIX rather than duplicating its polarimetric role.

## 1.4 XPoSat Mission

XPoSat is India’s first dedicated X-ray polarimetry mission. It was launched by PSLV-C58 from the Satish Dhawan Space Centre on 1 January 2024 and placed in a low-inclination, low-Earth orbit [1], [4]. Its scientific motivation is to add polarization information to the established spectral and temporal study of bright cosmic X-ray sources. The mission carries two co-aligned scientific payloads:

- **POLIX (Polarimeter Instrument in X-rays)**, developed by the Raman Research Institute in collaboration with ISRO centres, is intended for polarization measurements in the 8–30 keV band.
- **XSPECT (X-ray Spectroscopy and Timing)**, developed by the U R Rao Satellite Centre, provides spectroscopy and timing in the 0.8–15 keV band [1], [4].

The mission is important in Indian space astronomy because it extends the country’s space-based high-energy astronomy programme from multi-wavelength observation toward dedicated X-ray polarimetry. Long source observations that are necessary for polarimetry can also support complementary spectral and timing studies. For this Review-I proposal, POLIX Level-2 data are the main computational scope; XSPECT is described to establish mission context but is not included in the primary analysis plan.

## 1.5 POLIX Instrument and Working Principle

POLIX is a collimated Thomson-scattering polarimeter. The current official Level-2 handbook describes a **central beryllium scatterer** surrounded by **four position-sensitive X-ray proportional counters**. Each counter contains 12 anode cells, giving **48 anode cells in total** [2]. This configuration must be preserved accurately because the azimuthal distribution is directly connected to the detector geometry.

The operating principle is conceptualized as follows:

1. The collimator restricts the instrument’s field of view toward a bright target.
2. Incident X-ray photons interact in the low-atomic-mass beryllium scatterer.
3. For linearly polarized radiation, Thomson scattering is anisotropic with respect to the incident electric-field direction.
4. The four surrounding proportional counters register scattered photons at different azimuths.
5. The spacecraft rotation and instrument geometry allow the detected counts to be accumulated as an azimuthal distribution.
6. A two-fold modulation in this distribution can contain polarization information, after exposure, background, response and coordinate conventions are addressed [2], [7], [8].

A common conceptual curve is

\[
C(\phi)=A+B\cos\left[2(\phi-\phi_0)\right],
\]

where \(C(\phi)\) is the count rate or intensity at azimuth \(\phi\), \(A\) is a mean level, \(B\) is a fitted modulation amplitude and \(\phi_0\) is a fitted phase under the selected convention. The raw ratio \(B/A\) is a modulation measure. A calibrated PD additionally requires an appropriate modulation factor for a fully polarized beam and valid background treatment. Conversion of a fitted phase to an official sky PA additionally requires the mission’s reference-vector, orientation and convention handling [2], [8]. The proposed study will therefore keep raw/fitted modulation diagnostics separate from calibrated polarimetric claims.

## 1.6 POLIX Level-2 Data Products

The POLIX Level-2 release does not represent an observation through a single FITS file. The official handbook identifies related products created by different pipeline modules [2]. For Review-I, the main product groups are introduced conceptually:

| Product group | Representative content | Proposed analytical role |
|---|---|---|
| Exposure-related products | Roll- and yaw-referenced distributions such as `Exp_Azimuth_Roll_L2.fits` | Examine exposure coverage, non-uniformity and validity of comparisons across azimuth. |
| Energy-resolved azimuthal products | A data cube such as `EnergyRes_Src_Azimuth_Roll_L2.fits` containing anode, energy-channel and azimuth information | Represent energy-dependent count structure without claiming calibrated spectroscopy. |
| Source azimuthal profiles | Products such as `Src_Azimuth_Roll_L2.fits` | Examine detector/anode azimuthal behaviour and profile shape. |
| Source light curves | Event- or count-derived `.lc` products for source intervals | Represent time variability and data quality. |
| Detector-wise light curves and spectra | Processed source `.lc` and `.pha` products for individual detectors | Examine detector balance and possible detector-local behaviour. |
| WeightedRoll modulation product | `WeightedRoll_L2.fits` | Support a separate physical modulation diagnostic. The product includes source and background count-rate modulation and is not assumed to be fully background-corrected [2]. |

The handbook also cautions that count-mode and event-mode light curves are not directly interchangeable and that POLIX is not a spectroscopic instrument [2]. Consequently, the planned feature representation will preserve product identity and measurement meaning.

One observation requires inspection of multiple products because an unusual pattern may appear in only one domain. Exposure irregularity can affect an azimuthal profile; timing variability may not be visible in an aggregate spectrum; a detector imbalance can be hidden in an all-detector total; and a modulation-like pattern can be influenced by background. A defensible screening method must therefore combine evidence without erasing its provenance.

## 1.7 Motivation for the Project

The proposed study is motivated by seven connected observations:

1. A single POLIX observation contains multiple heterogeneous FITS products rather than one uniform feature table [2].
2. Repeated manual inspection of light curves, detector products, exposure distributions and azimuthal products is time-consuming.
3. Manual interpretation may vary between analysts, particularly when multiple weak deviations occur together.
4. Trusted labels identifying scientifically meaningful POLIX anomalies are not presently assumed to exist.
5. Unusual observations may originate from energy-dependent structure, timing variation, exposure imbalance, detector balance or azimuthal behaviour.
6. A statistical outlier may represent an instrumental condition, background behaviour, a rare but valid source state, a processing issue or another contextual effect. It does not automatically establish polarization or an astrophysical discovery [15], [16], [18].
7. Scientific users require explanations that connect a score back to observable quantities and original data products. A black-box ranking alone is insufficient for scientific review [17], [18].

The intended contribution is therefore not an automated “discovery engine.” It is a traceable screening and prioritization framework in which ML output remains subordinate to scientific evidence.

## 1.8 Research Problem

**Formal problem statement:**  
Given a collection of source and blank-sky POLIX Level-2 observations, each represented by multiple heterogeneous FITS products and lacking trusted anomaly labels, the proposed study seeks to design an automatic multi-product analysis framework that (i) constructs scientifically meaningful observation-level features, (ii) identifies observations that are unusual relative to the available collection through justified unsupervised methods, (iii) provides feature-level and product-level explanations for each screening decision, (iv) compares selected observations cautiously with independent azimuthal-modulation and blank-sky diagnostics without claiming calibrated PD or official PA, and (v) presents the evidence in a researcher-friendly and traceable form.

## 1.9 Aim of the Project

The project aims to propose and investigate an explainable, unsupervised framework for screening heterogeneous POLIX Level-2 observations and relating statistical unusualness to traceable data-product evidence and independent physical modulation diagnostics.

## 1.10 Proposed Objectives

The proposed study intends to:

1. study the scientific purpose, payload roles and observational context of XPoSat and POLIX;
2. understand the structure, semantics and limitations of POLIX Level-2 FITS products;
3. identify scientifically meaningful, reproducible features from exposure, energy-resolved azimuthal, timing, detector-wise and source-azimuth products;
4. build an unsupervised observation-screening framework suitable for a dataset without trusted anomaly labels;
5. investigate PCA, KMeans or related clustering, and Isolation Forest where justified by dataset size, scaling and validation constraints [12]–[14];
6. develop product-aware explanations that connect a screening score to contributing features and their source FITS product families;
7. investigate `WeightedRoll_L2.fits` separately as a physical modulation diagnostic, without treating its raw modulation or fitted phase as calibrated PD or official PA;
8. compare source-observation diagnostics with blank-sky behaviour to expose possible background or instrument-related structure [2], [8];
9. provide an accessible researcher-oriented interface for observation prioritization, traceability and cautious interpretation.

## 1.11 Scope

The primary scope is POLIX Level-2 data. Both source and blank-sky observations are considered because unusual source behaviour cannot be interpreted responsibly without reference to background and instrument behaviour. The purpose is observation screening and scientific interpretation support, not autonomous confirmation of astrophysical discoveries.

The scope is bounded as follows:

- An ML anomaly denotes statistical unusualness relative to the available feature representation and dataset. It is not a confirmed discovery or causal explanation.
- Physical modulation analysis is treated as an independent diagnostic branch.
- `WeightedRoll_L2.fits` is not assumed to be fully background-corrected [2].
- Final calibrated PD and official sky PA are outside the present claim unless the required mission-approved response, calibration and background procedure becomes available.
- The fitted phase of a two-fold curve will not be reported as official PA.
- XSPECT integration may be considered as future work, but it is not part of the present primary scope.
- Detailed architecture, software requirements, code modules, implementation, website evaluation, model results and testing belong to later project stages and are excluded from Review-I.

## 1.12 Significance of the Proposed Study

If developed and validated carefully, the proposed framework could reduce repetitive multi-file inspection and prioritize observations that merit expert attention. Its main scientific value would be traceability: an observation-level score would be linked to explicit features, each feature would retain its product origin, and the user could distinguish an exposure issue from timing variability, detector imbalance or azimuthal structure.

This structure could support reproducible archive screening because the same feature definitions and preprocessing decisions could be applied across observations. It could also enforce a separation between **statistical unusualness** and **physical modulation evidence**, reducing the risk of overstating an ML result. Finally, a modular product-aware representation could be extended as future POLIX releases, calibration information or nearby blank-sky observations become available.

---

# 2. Base Paper and Research Foundation

## 2.1 Identification of the Base Paper

No single verified paper was identified that covers the complete combination of POLIX Level-2 products, unsupervised archive screening, anomaly explanation and calibrated polarimetry. Forcing one unrelated article to serve as the sole base paper would misrepresent the project. The proposed study is therefore grounded in a **base-source set**:

1. the official *XPoSat-POLIX User Handbook: User Guide for Scientific Data Analysis Level2* for the mission product and instrument foundation [2];
2. Kislat *et al.* for event-level Stokes analysis and the distinction between signal, background and polarimetric inference [8];
3. Liu, Ting and Zhou for the Isolation Forest anomaly-detection foundation [14]; and
4. Yepmo, Smits and Pivert for the taxonomy and limitations of anomaly explanations [18].

The handbook is the strongest verified technical base for the exact POLIX products in scope. The remaining papers supply method foundations that the handbook does not attempt to provide.

## 2.2 Base-Paper Summary

| Base source | Problem studied | Data or instrument | Methodology | Main contribution | Limitation | Relevance to the proposed project |
|---|---|---|---|---|---|---|
| N. Anand, K. Rikame and K. Roy, *XPoSat-POLIX User Handbook: User Guide for Scientific Data Analysis Level2*, V1.0, 2025 [2] | How users should understand and operate the POLIX Level-2 analysis chain and products | POLIX Level-1/Level-2 files, pipeline modules and calibration context | Product definitions, processing workflow, FITS descriptions and documented limitations | Authoritative description of the beryllium scatterer, four proportional counters, 48 anodes, Level-2 product families and `WeightedRoll` background limitation | It is an operational handbook rather than an archive-level ML study; future background methodology is explicitly anticipated | Defines the instrument truth, data semantics and scientific boundary conditions |
| F. Kislat *et al.*, “Analyzing the data from X-ray polarimeters with Stokes parameters,” 2015 [8] | How to estimate linear polarization from scattering or photoelectric polarimeter events with tractable statistics | Generic X-ray polarimeter events including signal and background | Additive Stokes \(Q/U\) treatment, uncertainty derivation, background subtraction and MDP relations | Provides a rigorous bridge from azimuthal event directions to polarization statistics | It is not specific to POLIX Level-2 archive products or the current POLIX background condition | Supports the independent physical diagnostic and the separation of raw modulation from calibrated inference |
| F. T. Liu, K. M. Ting and Z.-H. Zhou, “Isolation Forest,” 2008 [14] | Detect anomalies without constructing a full model of normal data | General high-dimensional benchmark datasets | Random partition trees isolate rare points with short expected path lengths | Introduces a scalable unsupervised anomaly score suitable for multivariate data | An anomaly score is model- and sample-dependent and has no intrinsic scientific meaning or causal explanation | Supplies one candidate screening method, subject to small-sample and stability checks |
| V. Yepmo, G. Smits and O. Pivert, “Anomaly explanation: A review,” 2022 [18] | How anomaly-detection outputs can be explained to users | Cross-domain anomaly-detection literature | Taxonomy of explanation by feature importance, feature values, reference points and structure | Shows that anomaly explanation is distinct from classification explanation and is necessary for contextual trust | The reviewed techniques are general and do not supply POLIX product semantics | Motivates feature-level and product-level explanations tied to scientific provenance |

## 2.3 Extension Beyond the Base Paper

The planned methodology intends to connect these otherwise separate foundations. The official POLIX handbook describes the files but does not provide unsupervised archive-level screening. Isolation Forest provides a general anomaly score but does not know whether a feature represents exposure, time variability or a detector imbalance. General anomaly-explanation literature categorizes explanation forms but does not map them to POLIX products. Stokes analysis explains how polarimetric evidence should be handled but does not establish that an archive outlier is polarized.

The proposed extension is therefore to investigate:

- a multi-product POLIX feature representation;
- unsupervised observation-level screening rather than target-specific final inference;
- explanations organized by feature and source-product family;
- an independent `WeightedRoll` diagnostic kept outside the primary anomaly feature set;
- source-versus-blank-sky comparison;
- and a researcher-facing presentation layer that preserves evidence and limitations.

These are intended research directions, not claims of completed improvement or superiority.

---

# 3. Literature Survey

## 3.1 Foundations of X-Ray Polarimetry

Fabiani reviews the physical and instrumental foundations of X-ray polarimetry and emphasizes that polarization adds degree and angle to the better-established observables of imaging, spectroscopy and timing [7]. The literature identifies several energy-dependent polarimetric mechanisms, including Bragg diffraction, photoelectric absorption and scattering. For a scattering polarimeter, the relevant observable is an azimuthal distribution whose two-fold modulation is related to the incident linear polarization.

Kislat *et al.* formulate linear X-ray polarimetry through Stokes parameters [8]. For each event with azimuth \(\phi_i\), quantities proportional to \(\cos 2\phi_i\) and \(\sin 2\phi_i\) contribute to \(Q\) and \(U\). Their additive structure supports combination of events and subtraction of background Stokes contributions. This is methodologically important because PD and PA are nonlinear functions of \(Q\) and \(U\); their uncertainties can behave differently from those of the underlying Stokes quantities.

Together, these works establish four principles relevant to the proposed study:

- polarization provides geometrical and magnetic information not contained completely in flux alone;
- the measured azimuthal pattern depends on instrument response and exposure;
- background must be represented explicitly;
- and derived PD/PA require calibrated conventions rather than a direct reading of raw curve amplitude and phase.

This foundation supports keeping the physical diagnostic separate from unsupervised anomaly features. If the same modulation estimate were included in the anomaly model and later used as “independent” physical confirmation, the reasoning would be circular.

## 3.2 X-Ray Astronomy Missions and Instruments

Chandra demonstrates the scientific value of high-resolution imaging and spectroscopy. Its mirror and detector systems provide detailed images and spectra across a broad soft X-ray band [5]. Chandra is relevant to source context and to examples such as the Crab and Cassiopeia A, but it is not a dedicated X-ray polarimetry mission.

IXPE represents dedicated imaging X-ray polarimetry. Its three telescope systems focus X-rays onto gas pixel detectors that preserve polarization-sensitive photoelectron-direction information in the 2–8 keV operational band [6]. IXPE literature shows how calibrated imaging polarimetry can connect polarization maps or phase dependence to source geometry [9]–[11].

XPoSat occupies a different but complementary mission space. POLIX is a collimated Thomson-scattering polarimeter in 8–30 keV, while XSPECT provides 0.8–15 keV spectroscopy and timing [1], [4]. The Saini *et al.* mission paper describes the spacecraft, payload roles, operations and launch context [4]. The comparison indicates that results or procedures cannot be transferred between missions without considering detector principle, energy range, imaging capability, response and background.

## 3.3 XPoSat and POLIX Instrument Literature

The most directly relevant technical source is the official POLIX Level-2 handbook [2]. It provides the verified detector description, pipeline workflow, file naming, Level-2 FITS structures and limitations of the current release. In particular, it confirms:

- a central beryllium scatterer;
- four surrounding position-sensitive proportional counters;
- 12 anode cells per detector and 48 in total;
- exposure, source-azimuth, energy-resolved azimuth, light-curve, spectrum and `WeightedRoll` product families;
- and the presence of both source and background modulation in `WeightedRoll_L2.fits`.

The handbook further notes that POLIX background modulation can vary and that some azimuthal distributions contain narrow structures. It describes a future observation strategy involving a bright source and nearby blank-sky regions for polarization measurement [2]. This is not a minor implementation detail; it constrains the scientific claims that can be made from the currently released products.

The official ISRO mission page and PRADAN archive establish payload roles, energy ranges and data-service context [1], [3]. The mission paper by Saini *et al.* adds peer-reviewed discussion of the spacecraft and operational design [4]. These sources are complementary: the mission paper explains the observatory, while the handbook governs product-level interpretation.

For the proposed project, the literature implies that feature engineering must be **product-aware**. A light-curve statistic, an exposure statistic and an anode-balance statistic may all be numerical, but they do not share the same physical meaning. It also implies that missing calibration cannot be repaired by an ML model; calibration uncertainty must remain visible as a limitation.

## 3.4 Literature on Relevant Astronomical Sources

The local source collection did not contain a uniformly verified paper set for every target named in the project material. The survey therefore prioritizes three strong, directly relevant polarimetric studies rather than increasing the reference count with weak or indirect sources.

### Crab pulsar and nebula

Bucciantini *et al.* used IXPE imaging and pulse-phase information to separate spatial and rotationally dependent polarization behaviour in the Crab pulsar–nebula system [11]. The study demonstrates that polarization can vary across a source and with pulse phase, and that polarized structure can constrain magnetic-field organization and emission location. Its relevance to POLIX is conceptual rather than directly transferable: IXPE is an imaging photoelectric polarimeter in a different band, while POLIX is collimated and scattering-based. The paper therefore supports the importance of geometry and phase dependence, but not a direct POLIX calibration.

### Cygnus X-1

Krawczynski *et al.* combined IXPE polarimetry with multi-wavelength context to constrain the relation among the accretion disc, hot X-ray-emitting plasma and radio jet in Cyg X-1 [10]. The result illustrates why spectra alone may leave multiple coronal geometries plausible and why polarization orientation and energy dependence add discriminatory power. For the proposed study, Cyg X-1 motivates retaining energy- and azimuth-related information. It does not justify inferring the same geometry from a POLIX anomaly score.

### Hercules X-1

Doroshenko *et al.* used phase-resolved IXPE polarimetry of Her X-1 to constrain the neutron-star spin and magnetic geometry [9]. The study shows that PD and PA can vary with pulse phase and that time-resolved polarimetric analysis can be more informative than a single observation-average quantity. This supports retaining timing features and cautions against interpreting an aggregate modulation without considering source state and temporal structure.

### Evidence boundary for other targets

Sco X-1, GX 301-2, Cen X-3, 4U 1700-37 and Cassiopeia A are scientifically relevant source classes, but the verified reference set assembled for this Review-I document was not sufficient to make detailed source-specific polarization claims for each. They may be described in a later targeted bibliography after full-text source verification. Their absence from the present synthesis is an evidence-control decision, not a statement that relevant literature does not exist.

## 3.5 Machine Learning in Astronomy

Astronomical archives contain high-dimensional images, spectra and time series in which rare objects are difficult to label in advance. This has encouraged unsupervised and human-in-the-loop anomaly detection.

Baron and Poznanski applied an unsupervised random-forest-based outlier method to more than two million Sloan Digital Sky Survey galaxy spectra and examined the highest-scoring objects [15]. The study demonstrates that archive-scale ranking can focus expert attention on a manageable subset. Its limitation for the proposed project is the difference in scale and data type: millions of spectra provide a statistical regime unlike a small collection of heterogeneous POLIX observations. The paper supports prioritization, not the assumption that an outlier is a discovery.

Lochner and Bassett introduced Astronomaly, a modular framework combining feature extraction, anomaly detection and active learning for astronomical data [16]. Using Galaxy Zoo and simulations, they showed that expert relevance feedback could increase the number of interesting anomalies found near the top of a ranked list. The main lesson is that “interesting” is contextual and cannot always be learned from an initial unsupervised score. The limitation is that Astronomaly is a general framework; it does not encode POLIX product semantics or solve the calibration problem.

The primary statistical methods considered for the planned methodology have different roles:

- **PCA** represents correlated variables through orthogonal directions of variance [12]. It can support visualization, compression and multicollinearity analysis. However, high variance is not identical to scientific importance, and PCA loadings may change strongly in a small dataset.
- **KMeans** partitions points by distance to cluster centroids and seeks low within-cluster variation [13]. It may expose broad observation groupings, but requires scaling choices and a selected number of clusters; non-spherical or very small groups can be unstable.
- **Isolation Forest** isolates points through random recursive partitions; shorter average path lengths correspond to more readily isolated observations [14]. It does not require labelled anomalies, but contamination settings, random seeds and small-sample variation can affect rankings.

The literature therefore supports a cautious multi-method plan. PCA and clustering are useful for structure and diagnostics; an anomaly detector may provide a ranking; and stability analysis or expert review is necessary because no trusted labels are available.

## 3.6 Explainable AI in Scientific Applications

Lundberg and Lee introduced SHAP as an additive feature-attribution framework for model predictions [17]. SHAP provides a principled way to distribute the difference between a prediction and a reference expectation among input features for compatible predictive models. It is influential, but it does not automatically make a feature scientifically causal, nor is every unsupervised detector naturally represented by a supervised prediction explanation.

Yepmo *et al.* distinguish several families of anomaly explanation: feature importance, feature values, comparison with reference data points and structural explanations [18]. This distinction is valuable for scientific screening. A useful POLIX explanation may need to state not only that “feature \(x\) was important,” but also that the feature came from an exposure product, differed from a transparent reference distribution and should be checked in a specified FITS file.

Scientific interpretability requires:

- a clear definition of the quantity being explained;
- preservation of feature units and product provenance;
- local explanations for individual observations and global descriptions of model behaviour;
- stability checks when the sample is small;
- and language that distinguishes association from physical causation.

Small datasets create additional challenges. Feature rankings can change after one observation is added, a scaler can be influenced by an extreme value, and a post-hoc explainer may be less stable than the detector itself. The planned methodology should therefore prefer transparent transformations and detector-specific or distance-based contributions where defensible, while treating generic XAI outputs as evidence requiring validation. The project does not claim that a custom explanation is already superior to SHAP or other methods.

## 3.7 Physical Modulation and Blank-Sky Analysis

A polarization-sensitive azimuthal distribution is commonly represented through a two-fold sinusoid or through Stokes \(Q/U\) quantities [7], [8]. These descriptions are related, but several levels of inference must be kept distinct:

1. **Raw modulation:** variation of counts or rates with azimuth in a released product.
2. **Fitted modulation amplitude and phase:** parameters of a selected model fitted to the distribution.
3. **Calibrated polarization degree:** a background-corrected modulation normalized by an appropriate response or modulation factor.
4. **Official sky polarization angle:** an angle derived using the mission’s detector-to-sky convention, attitude and calibration.

The handbook states that the `WeightedRoll` product contains the azimuthal modulation of both source and background count rates [2]. It also documents variable background modulation and other azimuthal structures in currently released observations. Therefore, a visually sinusoidal or statistically strong fit is not enough to establish source polarization.

Blank-sky observations can help characterize background and instrument behaviour, but their use is also contextual. A blank field observed at a different time or geometry may not be an exact background for a source observation. The planned study will treat blank sky as a reference distribution for diagnostic comparison, not as an automatically valid subtraction. Where possible, Stokes-space comparison is attractive because signal and background terms are additive [8]. Final PD/PA claims remain outside scope until suitable calibration and background procedures are available.

## 3.8 Literature Synthesis

### What is already well established?

The physical value of X-ray polarization, the two-fold nature of linear-polarization modulation, Stokes-based analysis, and the need for response and background calibration are well established [7], [8]. The roles of Chandra, IXPE, XPoSat, POLIX and XSPECT are documented [1], [4]–[6]. POLIX Level-2 product structure and present background limitations are explicitly described in the official handbook [2].

### What methods are commonly used?

In polarimetry, modulation-curve fitting and Stokes \(Q/U\) analysis are common. In astronomical anomaly detection, feature extraction, unsupervised ranking and expert-in-the-loop review recur [15], [16]. PCA, centroid-based clustering and Isolation Forest are established generic tools for multivariate structure and anomaly detection [12]–[14]. Feature attribution and reference-based comparison are common explanation forms [17], [18].

### What limitations recur across the literature?

Recurring limitations include instrument-specific calibration, background contamination, data heterogeneity, weak or missing labels, context-dependent definitions of “interesting,” unstable inference in small samples and the gap between a numerical explanation and a physical explanation.

### What is missing for POLIX Level-2 archive screening?

The reviewed mission and handbook sources define the instrument and products but do not supply an integrated, product-aware unsupervised archive-screening framework. General astronomy anomaly systems do not encode POLIX product semantics. General XAI methods do not automatically trace an explanation to a Level-2 FITS product.

### Why is explainability required?

Scientists must determine whether a high score is driven by exposure, time variability, detector imbalance, azimuthal shape or a preprocessing choice. Product-aware explanations make this check possible and reduce the risk that a score is interpreted as physical evidence without inspection [18].

### Why should physical modulation diagnostics remain independent?

Independence prevents circular confirmation. If modulation amplitude were a primary anomaly feature and the same amplitude were later presented as physical support, the two branches would not be independent. Keeping `WeightedRoll` outside the primary screening features enables a cautious comparison between statistical unusualness and physical modulation evidence, while retaining the calibration boundary [2], [8].

## 3.9 Research Gap

Mission papers and official documents explain XPoSat, POLIX and their data products [1]–[4]. Source studies demonstrate how polarimetry can constrain individual compact-object or nebular geometries [9]–[11]. ML papers provide general anomaly-detection and archive-ranking techniques [14]–[16]. XAI literature provides feature-attribution and anomaly-explanation frameworks [17], [18]. Polarimetry literature explains modulation, Stokes analysis, background treatment and calibration [7], [8].

However, **limited published work was identified** that integrates:

- multiple POLIX Level-2 product families;
- scientifically interpretable feature engineering;
- unsupervised observation-level screening;
- product-aware anomaly explanations;
- blank-sky-referenced physical modulation diagnostics;
- and a unified researcher-facing analysis framework.

The reviewed literature does not provide a directly comparable integrated framework for this specific POLIX Level-2 problem. An opportunity remains to investigate whether transparent multi-product features, cautious unsupervised ranking and an independent physical diagnostic can support reproducible expert screening. This is a proposed research opportunity, not a claim that no related work exists.

## 3.10 Literature Survey Conclusion

The literature provides a strong foundation but in separate layers. Mission and handbook sources define what the POLIX products contain and what they do not yet justify. Polarimetry research explains how azimuthal information, Stokes parameters, background and calibration relate. Source studies demonstrate the diagnostic power of polarization. Astronomy ML research shows that unsupervised ranking can prioritize rare objects, while XAI research shows why anomaly scores require contextual explanation.

The remaining limitation is integration at the POLIX observation level. The proposed study is positioned as a cautious bridge among these layers: a product-aware feature representation, unsupervised screening, traceable explanations and a separate modulation diagnostic. Its relevance lies in supporting expert review without converting statistical unusualness into an unsupported astrophysical or polarimetric claim.

---

# 4. Existing Approaches

Existing practice is best understood as a combination of approaches rather than a single “existing system”:

- manual inspection of separate FITS light curves, spectra, exposure distributions and azimuthal products;
- mission-provided standard products and Level-2 utilities [2];
- target-specific spectral, timing or polarimetric studies [9]–[11];
- general-purpose unsupervised anomaly-detection algorithms [14]–[16];
- and generic XAI or anomaly-explanation techniques [17], [18].

## 4.1 Advantages of Existing Approaches

- Mission products preserve direct access to original measurements and processing context.
- Expert-controlled inspection supports physically informed interpretation.
- Standard polarimetric methods have explicit statistical foundations.
- Official documentation defines instrument limitations and data semantics.
- PCA, clustering and Isolation Forest are mature, widely examined statistical techniques.
- Generic XAI methods provide established vocabulary for local feature attribution and reference-based explanation.

## 4.2 Limitations of Existing Approaches

- Multi-file inspection is repetitive and difficult to scale across an archive.
- Standard products do not themselves provide archive-level observation prioritization.
- Trusted anomaly labels are absent or expensive to construct.
- General anomaly scores can be opaque and dependent on preprocessing.
- Generic explanations may have a weak connection to the original science product.
- A statistical anomaly can be confused with polarization evidence if the analysis branches are not separated.
- Final PD and PA interpretation depends on valid background subtraction, response calibration and angle conventions [2], [8].

---

# 5. Proposed Conceptual System

The proposed concept is:

`POLIX Level-2 observations → multi-product understanding → interpretable feature representation → unsupervised observation screening → product-aware explanation → independent physical modulation diagnostic → cautious scientific interpretation`

At the first stage, the project aims to catalogue product families and define features whose scientific meaning can be stated concisely. At the second stage, scaled observation-level features are intended to support PCA, clustering and anomaly ranking where stability checks justify them. At the third stage, each high-ranked observation is intended to receive feature-level and product-level evidence rather than only a scalar score. Finally, `WeightedRoll` and blank-sky behaviour are intended to be inspected through an independent physical diagnostic. The combined interpretation will retain separate labels for statistical unusualness and modulation evidence.

This is a conceptual research pipeline. It does not specify software architecture, routes, modules, database design, completed algorithms, interfaces or results.

## 5.1 Expected Advantages

- automated screening across multiple POLIX product families;
- prioritization of observations for expert review;
- explainable feature-level evidence;
- traceability from a score to an original FITS product family;
- explicit separation of ML anomaly evidence and physical modulation evidence;
- reproducible preprocessing and reporting;
- and extensibility to future observations, calibration information and nearby blank-sky releases.

## 5.2 Expected Limitations

- The currently available dataset may be small for stable multivariate modelling.
- Trusted anomaly labels are not assumed to exist.
- Final PD/PA depends on official calibration and valid background treatment.
- Model boundaries and rankings may change when new observations arrive.
- Expert validation remains necessary.
- An unsupervised anomaly does not establish physical causality.
- Blank-sky observations may not constitute exact source-specific backgrounds.
- Feature extraction can omit information or introduce modelling assumptions.

---

# References

[1] Indian Space Research Organisation, “XPoSat: India’s X-Ray Polarimetry Mission,” 2023. [Online]. Available: https://www.isro.gov.in/ISRO_EN/XPoSat_X-Ray_Polarimetry_Mission.html. [Accessed: Jul. 27, 2026].

[2] N. Anand, K. Rikame, and K. Roy, *XPoSat-POLIX User Handbook: User Guide for Scientific Data Analysis Level2*, version 1.0, Oct. 2025. Reviewed by V. Rana and Rishin P. V.; approved by B. Paul. Official technical handbook, local file: `C:\Users\Saatvik\Downloads\POLIX_User_Handbook.pdf`.

[3] Indian Space Research Organisation, Indian Space Science Data Centre, “ISRO Science Data Archive (ISDA): XPoSat,” [BIBLIOGRAPHIC DETAIL TO VERIFY]. [Online]. Available: https://pradan1.issdc.gov.in/x01/index.xhtml. Data acknowledgement guidance: https://pradan1.issdc.gov.in/x01/ack.xhtml. [Accessed: Jul. 27, 2026].

[4] H. Saini, K. V. Madhu, and R. Karidhal, “Mission analysis, design and operations plan of India’s first polarimetry satellite: X-ray Polarimetry Satellite (XPoSat),” *Experimental Astronomy*, vol. 59, no. 2, art. no. 17, 2025, doi: 10.1007/s10686-025-09988-6.

[5] M. C. Weisskopf, B. Brinkman, C. Canizares, G. Garmire, S. Murray, and L. P. Van Speybroeck, “An overview of the performance and scientific results from the Chandra X-Ray Observatory,” *Publications of the Astronomical Society of the Pacific*, vol. 114, no. 791, pp. 1–24, 2002, doi: 10.1086/338108.

[6] M. C. Weisskopf *et al.*, “The Imaging X-Ray Polarimetry Explorer (IXPE): Pre-Launch,” *Journal of Astronomical Telescopes, Instruments, and Systems*, vol. 8, no. 2, art. no. 026002, 2022, doi: 10.1117/1.JATIS.8.2.026002.

[7] S. Fabiani, “Instrumentation and future missions in the upcoming era of X-ray polarimetry,” *Galaxies*, vol. 6, no. 2, art. no. 54, 2018, doi: 10.3390/galaxies6020054.

[8] F. Kislat, B. Clark, M. Beilicke, and H. Krawczynski, “Analyzing the data from X-ray polarimeters with Stokes parameters,” *Astroparticle Physics*, vol. 68, pp. 45–51, 2015, doi: 10.1016/j.astropartphys.2015.02.007.

[9] V. Doroshenko *et al.*, “Determination of X-ray pulsar geometry with IXPE polarimetry,” *Nature Astronomy*, vol. 6, pp. 1433–1443, 2022, doi: 10.1038/s41550-022-01799-5.

[10] H. Krawczynski *et al.*, “Polarized x-rays constrain the disk-jet geometry in the black hole x-ray binary Cygnus X-1,” *Science*, vol. 378, no. 6620, pp. 650–654, 2022, doi: 10.1126/science.add5399.

[11] N. Bucciantini *et al.*, “Simultaneous space and phase resolved X-ray polarimetry of the Crab pulsar and nebula,” *Nature Astronomy*, vol. 7, no. 5, pp. 602–610, 2023, doi: 10.1038/s41550-023-01936-8.

[12] K. Pearson, “On lines and planes of closest fit to systems of points in space,” *The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science*, 6th ser., vol. 2, no. 11, pp. 559–572, 1901, doi: 10.1080/14786440109462720.

[13] J. B. MacQueen, “Some methods for classification and analysis of multivariate observations,” in *Proc. 5th Berkeley Symp. Mathematical Statistics and Probability*, vol. 1, Berkeley, CA, USA: University of California Press, 1967, pp. 281–297.

[14] F. T. Liu, K. M. Ting, and Z.-H. Zhou, “Isolation Forest,” in *Proc. 8th IEEE Int. Conf. Data Mining (ICDM)*, Pisa, Italy, 2008, pp. 413–422, doi: 10.1109/ICDM.2008.17.

[15] D. Baron and D. Poznanski, “The weirdest SDSS galaxies: results from an outlier detection algorithm,” *Monthly Notices of the Royal Astronomical Society*, vol. 465, no. 4, pp. 4530–4555, 2017, doi: 10.1093/mnras/stw3021.

[16] M. Lochner and B. A. Bassett, “Astronomaly: Personalised active anomaly detection in astronomical data,” *Astronomy and Computing*, vol. 36, art. no. 100481, 2021, doi: 10.1016/j.ascom.2021.100481.

[17] S. M. Lundberg and S.-I. Lee, “A unified approach to interpreting model predictions,” in *Advances in Neural Information Processing Systems 30*, 2017, pp. 4765–4774.

[18] V. Yepmo, G. Smits, and O. Pivert, “Anomaly explanation: A review,” *Data & Knowledge Engineering*, vol. 137, art. no. 101946, 2022, doi: 10.1016/j.datak.2021.101946.

---

## Review-I Scope Confirmation

This document presents proposed research only. It contains no final anomaly count, case-study result, PD proxy value, website validation result, calibrated PD, official PA, completed implementation result, source-code architecture, software-requirements specification or Review-II detailed design.
