# Literature and Citation Audit

## Search scope

The publication-focused search supplemented the existing Review-I documents with current official and primary sources on:

- XPoSat/POLIX mission, data service, handbook, and acknowledgment guidance;
- X-ray polarimetry, modulation curves, Stokes analysis, calibration, and background;
- astronomy anomaly detection;
- explainable anomaly detection;
- explanation faithfulness;
- heterogeneous or multi-view representation; and
- the deployed PCA, KMeans, Isolation Forest, and software stack.

Search completed: **2026-07-27**.

## Literature synthesis

Official sources define XPoSat, POLIX, and the data-use boundaries. The handbook is the controlling product-level source: it identifies WeightedRoll as containing both source and background modulation and warns that the current released-data configuration is insufficient for a polarization measurement. Stokes-analysis literature supports treating Q and U as additive physical quantities, while also requiring appropriate background and response calibration.

Astronomy anomaly-detection work demonstrates the value of archive ranking and human inspection but does not make an anomaly score a physical measurement. Explainable-anomaly literature distinguishes explanation from detection and emphasizes feature-, value-, reference-, or structure-based evidence. Explanation-faithfulness work motivates perturbation tests that compare an explanation with changes in the predictor.

The reviewed literature did not provide a directly comparable framework combining heterogeneous POLIX Level-2 product features, unsupervised observation screening, product-aware local explanation, explanation neutralization tests, and a separate blank-sky-referenced WeightedRoll branch. This is a cautious gap statement, not a priority claim.

## Reference verification table

| Key | Source | Full text available | Primary/authoritative source | DOI | Claim supported | Status |
|---|---|:---:|---|---|---|---|
| `isro_xposat_2023` | ISRO XPoSat mission page | Yes | ISRO | — | Mission/payload roles and energy bands | VERIFIED |
| `polix_handbook_2025` | XPoSat-POLIX Level-2 User Handbook V1.0 | Yes, local PDF | Official technical handbook | — | Product semantics; WeightedRoll source+background; released-data limitation | VERIFIED |
| `pradan_xposat` | ISDA/PRADAN XPoSat archive | Yes | ISSDC/ISRO | — | Official archive and payload identity | VERIFIED AS n.d.; no displayed publication year/version |
| `xposat_ack` | XPoSat acknowledgment page | Yes | ISSDC/ISRO | — | Abstract naming requirement and exact acknowledgment | VERIFIED |
| `saini2025xposat` | Saini, Madhu, and Karidhal | Abstract/first-page text; full article not locally retained | Springer DOI record | 10.1007/s10686-025-09988-6 | Launch, payload, mission-operations context | PARTIALLY VERIFIED |
| `rishin2010thomson` | Development of a Thomson X-ray Polarimeter | Yes | Author manuscript/arXiv | 10.48550/arXiv.1009.0846 | Development lineage and Thomson-polarimeter design | VERIFIED; prototype-era values not used as flight values |
| `fabiani2018instrumentation` | X-ray polarimetry instrumentation review | Yes | Open-access journal | 10.3390/galaxies6020054 | Scattering modulation and instrument context | VERIFIED |
| `kislat2015stokes` | Stokes analysis for X-ray polarimeters | Yes | Author manuscript + journal DOI | 10.1016/j.astropartphys.2015.02.007 | Q/U additivity, signal/background treatment | VERIFIED |
| `pearson1901pca` | Pearson PCA foundation | Yes | Journal record | 10.1080/14786440109462720 | Orthogonal least-squares directions | VERIFIED |
| `macqueen1967kmeans` | MacQueen KMeans foundation | Yes | Proceedings archive | — | Iterative clustering objective | VERIFIED |
| `liu2008isolation` | Isolation Forest | Yes via author PDF | IEEE metadata + author manuscript | 10.1109/ICDM.2008.17 | Random isolation and anomaly scoring | VERIFIED; resolves legacy warning [14] |
| `baron2017weirdest` | Weirdest SDSS galaxies | Yes | MNRAS full text | 10.1093/mnras/stw3021 | Unsupervised astronomy outlier ranking and inspection | VERIFIED |
| `lochner2021astronomaly` | Astronomaly | Yes | arXiv author manuscript + journal DOI | 10.1016/j.ascom.2021.100481 | Modular, expert-in-the-loop astronomy anomaly detection | VERIFIED |
| `lundberg2017shap` | SHAP | Yes | NeurIPS proceedings | — | General additive feature attribution; contextual comparison only | VERIFIED |
| `yepmo2022anomaly` | Anomaly explanation: A review | Abstract and displayed section summaries; full text not locally retained | Elsevier DOI record | 10.1016/j.datak.2021.101946 | High-level anomaly-explanation taxonomy and motivation | PARTIALLY VERIFIED |
| `yeh2019infidelity` | Explanation infidelity/sensitivity | Yes | NeurIPS proceedings | — | Objective, perturbation-based explanation evaluation | VERIFIED |
| `pedregosa2011sklearn` | scikit-learn | Yes | JMLR | — | Software implementation context | VERIFIED |
| `hwang2021multiview` | Multi-view representation learning | Yes | NeurIPS proceedings | — | General heterogeneous-view representation context | VERIFIED; no direct equivalence claimed |

BibTeX entries audited: **18**. Fully verified: **16**. Partial/full-text follow-up: **2**.

## Legacy citation warnings [3], [4], [14], and [18]

### Legacy [3] — ISDA/PRADAN

The page is current and authoritative, but it displays no publication year or version. The warning is resolved for citation purposes by using `year = {n.d.}` and an access date. If the venue rejects n.d. website references, request an archival citation from ISSDC.

### Legacy [4] — Saini *et al.*

DOI, authors, title, journal, volume, article number, dates, and abstract are verified. The full paper was not retained locally. Preserve **PARTIALLY VERIFIED** and use it only for high-level mission context unless the authors obtain and inspect the full text.

### Legacy [14] — Isolation Forest

Resolved. IEEE/Monash metadata and the author-hosted full paper agree on authors, title, venue, year, pages 413–422, and DOI 10.1109/ICDM.2008.17.

### Legacy [18] — Yepmo *et al.*

DOI, authors, journal, volume, article number, abstract, and high-level four-category taxonomy are visible on the publisher page. Full text was not retained locally. Preserve **PARTIALLY VERIFIED** and avoid detailed paraphrase beyond the visible abstract/section summaries.

## Official data-use wording

The current ISSDC/PRADAN acknowledgment page requires publications using XPoSat data to identify “XPoSat” together with the payload name in the abstract. The draft abstract names both XPoSat and POLIX.

Required acknowledgment for a paper using XPoSat data:

> This publication uses the data from the XPoSat mission of the Indian Space Research Organisation (ISRO), archived at the Indian Space Science Data Centre (ISSDC).

Source checked: `https://pradan1.issdc.gov.in/x01/ack.xhtml`, accessed 2026-07-27.

## Novelty conclusion

Use:

> Limited published work was identified on integrated, product-aware screening and physical-diagnostic analysis of POLIX Level-2 archives. The reviewed literature did not provide a directly comparable framework combining the five elements evaluated here.

Do not use “first,” “never attempted,” “novel,” or a superiority statement.
