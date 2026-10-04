# Final Reference–Claim Map

**Audit date:** 2026-07-28  
**Library:** `03_FINAL_REFERENCES.bib`  
**Rule:** A source is retained only when its identity was verified, an authoritative page or full text was inspected, the supported manuscript claim is explicit, and the source limitation is recorded.

| Ref. ID | BibTeX key | Source inspected | Manuscript claim supported | Claim IDs | Limitation | Status |
|---|---|---|---|---|---|---|
| R01 | `isro_xposat` | Official ISRO mission page | XPoSat mission and payload identity | C042, C063 | Mission overview; not detailed POLIX analysis guidance | VERIFIED AND RETAIN |
| R02 | `polix_handbook_2025` | POLIX User Handbook V1.0 | Level-2 product semantics; WeightedRoll source-plus-background boundary; release-specific physical limits | C005–C010, C019, C022, C023, C027, C064 | Version-specific user guidance; does not validate project ML features | VERIFIED AND RETAIN |
| R03 | `issdc_xposat_archive` | Official ISSDC archive page | XPoSat/POLIX archive context | C042, C043 | Archive access context; not evidence that this project used all released observations | VERIFIED AND RETAIN |
| R04 | `issdc_xposat_ack` | Official ISSDC acknowledgment page, rechecked 2026-07-28 | Required mission acknowledgment wording and abstract identification rule | C060, C061 | Wording may change; must be rechecked immediately before submission | VERIFIED AND RETAIN |
| R05 | `rishin2010thomson` | Primary POLIX prototype/instrument paper | Thomson-scattering design and POLIX instrument context | C042 | Earlier instrument/prototype context; not current Level-2 calibration guidance | VERIFIED AND RETAIN |
| R06 | `fabiani2018instrumentation` | Full review article | X-ray polarimetry instrumentation and need for calibration/background context | C044, C064 | General review; not an official POLIX calibration source | VERIFIED AND RETAIN |
| R07 | `kislat2015stokes` | Full primary methods paper | Cosine/sine harmonic and Stokes-analysis foundations | C020, C044 | General method; does not make project coefficients calibrated POLIX Stokes quantities | VERIFIED AND RETAIN |
| R08 | `pearson1901pca` | Primary paper | Historical/method foundation for PCA | C011, C045 | General method only | VERIFIED AND RETAIN |
| R09 | `macqueen1967kmeans` | Primary proceedings paper | KMeans method foundation | C011, C045 | General method only | VERIFIED AND RETAIN |
| R10 | `pedregosa2011sklearn` | Full software paper | scikit-learn implementations used by the saved stack | C011, C062 | Software citation; not evidence of project correctness or original environment identity | VERIFIED AND RETAIN |
| R11 | `liu2008isolation` | Full primary paper | Isolation Forest method foundation | C011, C029, C045 | General algorithm; does not validate contamination or candidate truth | VERIFIED AND RETAIN |
| R12 | `baron2017weirdest` | Full primary astronomy paper | Unsupervised ranking of unusual astronomical objects | C025, C046 | Different data modality and scale | VERIFIED AND RETAIN |
| R13 | `giles2019serendipity` | Full primary astronomy paper | Serendipitous astronomical anomaly search | C025, C046 | Different archive and scientific objective | VERIFIED AND RETAIN |
| R14 | `lochner2021astronomaly` | Full primary methods paper | Human-in-the-loop astronomical anomaly discovery | C025, C046 | Not a POLIX framework and not the deployed project method | VERIFIED AND RETAIN |
| R15 | `li2024explainable_anomaly` | Full review/survey | Explainable anomaly-detection concepts and distinction from supervised explanation | C018, C047 | Survey; does not validate this project-specific heuristic | VERIFIED AND RETAIN |
| R16 | `yeh2019infidelity` | Full primary paper | Behavioural/perturbation motivation for explanation evaluation | C035, C047 | General explanation metric paper; the project does not implement its complete formal metric | VERIFIED AND RETAIN |
| R17 | `campos2016evaluation` | Full primary paper | Difficulty of evaluating unsupervised outlier methods without labels | C048 | Benchmark context; not direct evidence for project candidate correctness | VERIFIED AND RETAIN |
| R19 | `lundberg2017shap` | Full primary paper | SHAP identity and guarantee; comparator for stating what was not deployed | C018, C049 | SHAP was considered conceptually but not implemented or benchmarked | VERIFIED CONTEXT AND RETAIN |

## Citation controls

- The manuscript uses all 18 entries and contains no uncited BibTeX record.
- Chandra and XSPEC are not cited as analysed datasets or project methods.
- General methods references support definitions and context only; all project numbers are controlled by CSV/code evidence.
- R02 and R04 require a final version/access check immediately before submission.
- R19 supports only the project-evolution and method-boundary statement; it is not evidence for the custom score.
