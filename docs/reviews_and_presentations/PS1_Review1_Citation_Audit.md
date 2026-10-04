# Project Stage-I — Review 1 Citation Audit

## Project Title

**An Explainable AI Framework for Analysis of X-Ray Polarimetry Data from XPoSat**

## Audit Method

The audit checked each source against a local full-text file, a publisher record, a primary repository, an official mission page or an official archive page. Reference numbers match `PS1_Review1_Introduction_Literature_Survey.md` and `PS1_Review1_Literature_Comparison_Table.md`.

Status meanings:

- **VERIFIED** — bibliographic identity and the cited claim were checked against full text or an authoritative primary/official page.
- **PARTIALLY VERIFIED** — bibliographic metadata and the claim-bearing abstract or publisher description were checked, but full text was not locally available for inspection.
- **NEEDS VERIFICATION** — at least one required bibliographic detail remains unavailable or conflicting.

## Reference-by-Reference Audit

| Ref. | Full title | Source type | Local filename or verified URL | Full text available | Report section(s) using source | Claim supported | Verification status | Missing bibliographic details | Indirect-citation warning |
|---:|---|---|---|:---:|---|---|---|---|---|
| 1 | XPoSat: India’s X-Ray Polarimetry Mission | Official ISRO webpage | https://www.isro.gov.in/ISRO_EN/XPoSat_X-Ray_Polarimetry_Mission.html | Yes | Abstract; 1.3; 1.4; 3.2; 3.3; 3.8; 3.9 | XPoSat mission purpose; POLIX 8–30 keV; XSPECT 0.8–15 keV; payload roles | VERIFIED | None identified | None; cited directly from ISRO |
| 2 | XPoSat-POLIX User Handbook: User Guide for Scientific Data Analysis Level2, V1.0 | Official technical handbook | `C:\Users\Saatvik\Downloads\POLIX_User_Handbook.pdf` | Yes | Abstract; 1.2; 1.5–1.7; 1.10–1.12; 2.1–2.3; 3.3; 3.7–3.10; 4.1–4.2; 5.2 | Central beryllium scatterer; four proportional counters; 48 anodes; Level-2 products; `WeightedRoll` contains source and background modulation; current background limitation | VERIFIED | None identified; preparers, reviewers, approver, version and date appear in the document | None; local full text extracted and pages 10, 25, 26 and 57 visually checked |
| 3 | ISRO Science Data Archive (ISDA): XPoSat | Official ISSDC/ISRO archive webpage | https://pradan1.issdc.gov.in/x01/index.xhtml; acknowledgement: https://pradan1.issdc.gov.in/x01/ack.xhtml | Yes | 3.3; reference note | Official archive context, payload identity and XPoSat data acknowledgement guidance | NEEDS VERIFICATION | Publication year/version is not displayed; written as `[BIBLIOGRAPHIC DETAIL TO VERIFY]` | None for claims; official page used directly |
| 4 | Mission analysis, design and operations plan of India’s first polarimetry satellite: X-ray Polarimetry Satellite (XPoSat) | Peer-reviewed journal article | https://doi.org/10.1007/s10686-025-09988-6 | No | Abstract; 1.3; 1.4; 3.2; 3.3; 3.8; 3.9 | Launch date/context, mission operations, payload roles and energy bands | PARTIALLY VERIFIED | None identified | Publisher/DOI metadata and article abstract checked; full text not locally retained |
| 5 | An overview of the performance and scientific results from the Chandra X-Ray Observatory | Peer-reviewed journal article | https://arxiv.org/abs/astro-ph/0110308; DOI: https://doi.org/10.1086/338108 | Yes | 1.1; 1.3; 3.2; 3.8 | Chandra’s high-resolution imaging and spectroscopic capabilities; Chandra is not presented as a dedicated polarimetry mission | VERIFIED | None identified | None; author manuscript and journal metadata agree |
| 6 | The Imaging X-Ray Polarimetry Explorer (IXPE): Pre-Launch | Peer-reviewed journal article | https://www.spiedigitallibrary.org/journals/Journal-of-Astronomical-Telescopes-Instruments-and-Systems/volume-8/issue-02/026002/Imaging-X-ray-Polarimetry-Explorer-prelaunch/10.1117/1.JATIS.8.2.026002.full; preprint: https://arxiv.org/abs/2112.01269 | Yes | 1.3; 3.2; 3.8 | IXPE as a dedicated imaging polarimetry mission using three telescope systems and polarization-sensitive detectors | VERIFIED | None identified | None. Important correction: the reviewed predecessor report listed this work as *ApJS*, vol. 261, art. 5; the verified record is *JATIS*, vol. 8, no. 2, art. 026002 |
| 7 | Instrumentation and future missions in the upcoming era of X-ray polarimetry | Peer-reviewed open-access review | https://www.mdpi.com/2075-4434/6/2/54 | Yes | 1.1; 1.2; 1.5; 3.1; 3.2; 3.7; 3.8 | Physical basis, science motivation and major detector approaches for X-ray polarimetry | VERIFIED | None identified | None. Its pre-launch POLIX band description is not used for current mission values; current values come from Refs. [1] and [2] |
| 8 | Analyzing the data from X-ray polarimeters with Stokes parameters | Peer-reviewed journal article | https://arxiv.org/abs/1409.6214; DOI: https://doi.org/10.1016/j.astropartphys.2015.02.007 | Yes | Abstract; 1.1; 1.2; 1.5; 1.10; 1.11; 2.1–2.3; 3.1; 3.7–3.10; 4.1–4.2 | Event-wise Stokes analysis, additivity of \(Q/U\), signal/background treatment, modulation and calibration distinctions | VERIFIED | None identified | None; preprint and journal metadata agree |
| 9 | Determination of X-ray pulsar geometry with IXPE polarimetry | Peer-reviewed journal article | https://www.nature.com/articles/s41550-022-01799-5; preprint: https://arxiv.org/abs/2206.07138 | Yes | 1.2; 3.3; 3.4; 3.8 | Phase-dependent polarization can constrain the geometry of Her X-1 | VERIFIED | None identified | None; source-specific quantitative results are discussed only as published literature, not as project results |
| 10 | Polarized x-rays constrain the disk-jet geometry in the black hole x-ray binary Cygnus X-1 | Peer-reviewed journal article | https://www.science.org/doi/10.1126/science.add5399; preprint: https://arxiv.org/abs/2206.09972 | Yes | 1.2; 3.3; 3.4; 3.8 | Calibrated IXPE polarimetry adds constraints on the Cyg X-1 disc/corona/jet geometry | VERIFIED | None identified | None; interpretation is not transferred to POLIX anomaly scores |
| 11 | Simultaneous space and phase resolved X-ray polarimetry of the Crab pulsar and nebula | Peer-reviewed journal article | https://www.nature.com/articles/s41550-023-01936-8; preprint: https://arxiv.org/abs/2207.05573 | Yes | 3.3; 3.4; 3.8 | Crab polarization is spatially and phase dependent and informs magnetic/emission geometry | VERIFIED | None identified | None; IXPE imaging results are used only for scientific context |
| 12 | On lines and planes of closest fit to systems of points in space | Peer-reviewed journal article | https://doi.org/10.1080/14786440109462720 | Yes | 1.10; 3.5; 3.8; 4.1 | Least-squares orthogonal directions forming the foundation of PCA | VERIFIED | None identified | None |
| 13 | Some methods for classification and analysis of multivariate observations | Conference proceedings paper | https://projecteuclid.org/euclid.bsmsp/1200512992 | Yes | 1.10; 3.5; 3.8; 4.1 | KMeans partitioning and its within-group variance objective | VERIFIED | No DOI is assigned in the verified proceedings record | None |
| 14 | Isolation Forest | Peer-reviewed IEEE conference paper | https://doi.org/10.1109/ICDM.2008.17 | No | 1.10; 2.1–2.3; 3.5; 3.8; 4.1–4.2 | Random isolation trees provide an unsupervised anomaly score with favourable computational properties | PARTIALLY VERIFIED | None identified | IEEE publisher metadata and abstract checked; full paper was not locally retained |
| 15 | The weirdest SDSS galaxies: results from an outlier detection algorithm | Peer-reviewed journal article | https://academic.oup.com/mnras/article/465/4/4530/2568826; preprint: https://arxiv.org/abs/1611.07526 | Yes | 1.7; 3.5; 3.8–3.9 | Archive-scale unsupervised outlier ranking of SDSS galaxy spectra can prioritize expert review | VERIFIED | None identified | None; its large-dataset findings are not assumed to hold unchanged for a small POLIX dataset |
| 16 | Astronomaly: Personalised active anomaly detection in astronomical data | Peer-reviewed journal article | https://www.sciencedirect.com/science/article/pii/S2213133721000354; preprint: https://arxiv.org/abs/2010.11202 | Yes | 1.7; 3.5; 3.8–3.9 | Modular astronomy anomaly detection and expert relevance feedback; anomaly interest is contextual | VERIFIED | None identified | None; reported literature performance is not a result of the proposed project |
| 17 | A unified approach to interpreting model predictions | Peer-reviewed conference paper | https://proceedings.neurips.cc/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html; preprint: https://arxiv.org/abs/1705.07874 | Yes | 1.7; 3.6; 3.8–3.9; 4.1–4.2 | SHAP additive feature attribution and the importance of explaining individual predictions | VERIFIED | No DOI is required for the NeurIPS proceedings version | None; the report explicitly states that SHAP attribution is not physical causality |
| 18 | Anomaly explanation: A review | Peer-reviewed journal article | https://www.sciencedirect.com/science/article/pii/S0169023X21000720; DOI: https://doi.org/10.1016/j.datak.2021.101946 | No | 1.7; 2.1–2.3; 3.5–3.10; 4.1–4.2 | Taxonomy of anomaly explanations and need for contextual, feature- or reference-based explanations | PARTIALLY VERIFIED | None identified | Publisher metadata, abstract and displayed section summaries checked; full text not locally retained |

## Technical Claim Cross-Check

| Quality-control claim | Supporting source | Audit result |
|---|---|---|
| Chandra is described as an imaging and spectroscopy mission, not as a dedicated polarimetry mission | Refs. [5] and official Chandra context used during verification | PASS |
| IXPE is a dedicated imaging X-ray polarimetry mission | Ref. [6] | PASS |
| POLIX covers the official 8–30 keV medium-energy polarimetry band | Refs. [1], [2] and [4] | PASS |
| XSPECT provides spectroscopy/timing over 0.8–15 keV | Refs. [1] and [4] | PASS |
| POLIX contains a central beryllium scatterer | Ref. [2], p. 10 | PASS |
| POLIX contains four proportional counters | Ref. [2], pp. 9–10 | PASS |
| POLIX contains 48 anode cells in total | Ref. [2], p. 10 | PASS |
| `WeightedRoll_L2.fits` contains both source and background count-rate modulation | Ref. [2], p. 26 | PASS |
| Raw/fitted modulation is not equated with calibrated PD | Refs. [2] and [8] | PASS |
| Fitted detector-coordinate phase is not presented as official sky PA | Refs. [2] and [8] | PASS |
| An ML anomaly is not equated with an astrophysical discovery | Refs. [15], [16] and [18] | PASS |

## Review-Stage Language Audit

The report was checked for prohibited final-result language and excluded content.

| Check | Result |
|---|---|
| Proposal-stage wording such as “the proposed study,” “the project aims to,” “is intended to” and “planned methodology” | PASS |
| No completed anomaly count | PASS |
| No final case-study results from the project | PASS |
| No project PD proxy values | PASS |
| No website validation or performance result | PASS |
| No completed model output | PASS |
| No software architecture, routes, database or source-code module description | PASS |
| No Review-II software requirements or detailed design | PASS |

## References Requiring Follow-Up

1. **Ref. [3] — NEEDS VERIFICATION:** publication year/version of the official PRADAN XPoSat landing page is not displayed.
2. **Ref. [4] — PARTIALLY VERIFIED:** metadata and abstract were verified; obtain the publisher full text if a detailed mission-operations claim is added later.
3. **Ref. [14] — PARTIALLY VERIFIED:** IEEE metadata and abstract were verified; retain or obtain the full conference paper before reproducing equations or detailed parameter claims.
4. **Ref. [18] — PARTIALLY VERIFIED:** publisher metadata, abstract and visible section summaries were verified; obtain full text before reproducing its detailed taxonomy verbatim.

## Evidence Gaps Intentionally Preserved

- A uniformly verified, full-text source set was not available locally for Sco X-1, GX 301-2, Cen X-3, 4U 1700-37 and Cassiopeia A. No detailed source-specific claims were added for these targets.
- No verified source established that the currently released POLIX `WeightedRoll` product is fully background-corrected; the report states the opposite, as documented by the handbook.
- No verified source authorized conversion of a project-fitted phase into an official sky PA.
- No official calibration available in the reviewed material justified a final project PD value.

## XPoSat Data Acknowledgement Note

The official ISSDC/PRADAN acknowledgement page states that publications resulting from XPoSat data should identify “XPoSat” together with the payload name in the abstract. This Review-I report presents proposed research and does not publish a POLIX science result. The instruction should be applied to a future paper or report that presents analysis or interpretation of XPoSat/POLIX data, using the then-current wording at:

https://pradan1.issdc.gov.in/x01/ack.xhtml
