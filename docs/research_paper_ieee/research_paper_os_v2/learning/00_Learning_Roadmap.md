# Student Learning Roadmap

**Phase:** Final Research Paper Completion OS, Agent 10  
**Current execution scope:** Modules 1-18 complete  
**Audience:** A B.Tech student preparing to understand, explain, and defend the POLIX project

## How to use this roadmap

For each module:

1. read the beginner explanation without memorizing equations;
2. read the technical explanation and reproduce the definitions in your own notebook;
3. connect the idea to one real project product or claim;
4. answer the five self-test questions without looking at the answers;
5. explain the “defense card” aloud in two minutes;
6. mark a module complete only if you can state both what the project did and what it did **not** establish.

## Learning sequence and status

| Module | Topic | Why it comes here | Status |
|---:|---|---|---|
| 1 | X-ray astronomy basics | Establishes photons, energy, sources, counts, time, spectra, and background. | CREATED |
| 2 | X-ray polarization, PD, and PA | Separates polarization physics from a fitted modulation curve. | CREATED |
| 3 | XPoSat, POLIX, and XSPECT | Places the project within the mission and keeps payload roles distinct. | CREATED |
| 4 | POLIX detector and FITS products | Connects instrument measurements to the Level-2 files used by the project. | CREATED |
| 5 | Project dataset and source/blank-sky observations | Establishes the exact archive and absence of anomaly labels. | CREATED |
| 6 | All 15 Matrix-C features | Connects each feature to its exact formula and scientific boundary. | CREATED |
| 7 | PCA | Explains low-dimensional geometric evidence. | CREATED |
| 8 | KMeans | Explains local cluster context and centroid distance. | CREATED |
| 9 | Isolation Forest | Explains the fixed candidate rule and tested stability. | CREATED |
| 10 | Custom four-component XAI method | Explains the deployed local ranking heuristic. | CREATED |
| 11 | Faithfulness testing | Separates internal perturbation evidence from causal validation. | CREATED |
| 12 | WeightedRoll fitting and harmonic coefficients | Explains the physical-fit implementation and terminology limits. | CREATED |
| 13 | Blank-sky comparison | Explains the archive-specific empirical reference and non-equivalence result. | CREATED |
| 14 | Results and candidate sets | Separates the fixed four, tested-procedure three, cross-tier two, threshold neighborhood, and exploratory six. | CREATED |
| 15 | Research contribution | Applies Agent 8's Moderate one-primary/three-secondary contribution decision. | CREATED |
| 16 | Limitations and safe claims | Converts Agents 1-9 findings into precise claim boundaries. | CREATED |
| 17 | IEEE paper structure | Connects each evidence class to its proper manuscript section. | CREATED |
| 18 | Viva and reviewer defense | Integrates Agent 9's Weak Reject and conditional-acceptance requirements. | CREATED |

## Competency gate after Module 4

Before continuing, the student should be able to:

- explain why X-ray astronomy uses detectors above Earth's atmosphere;
- distinguish intensity, spectrum, timing, and polarization information;
- explain why linear polarization produces a two-fold azimuthal modulation;
- distinguish raw modulation, polarization degree, fitted phase, and sky polarization angle;
- state the roles and energy bands of POLIX and XSPECT;
- name the POLIX Level-2 product families used by the project;
- explain why WeightedRoll is not assumed to be fully background-corrected;
- quote the handbook boundary that current released data are not sufficient for polarization measurement under the documented background conditions;
- explain why count-mode light curves and PHA-derived quantities must be described as diagnostic features or proxies.

## Competency gate after Module 13

Before continuing, the student should also be able to:

- explain why the 25 observations do not support predictive-accuracy claims;
- define every Matrix-C feature without turning channel-space proxies into calibrated physics;
- distinguish PCA geometry, KMeans local grouping, and Isolation Forest thresholded ranking;
- explain why contamination 0.16 produces a four-candidate decision boundary;
- state why 100/100 seed frequency is not anomaly probability;
- derive the four XAI components and their within-observation normalization;
- define the Strong and Moderate faithfulness rules and their limitations;
- derive the weighted harmonic fit, raw modulation, and fitted phase;
- explain why the 13-fit blank-sky reference is empirical rather than official background subtraction; and
- defend the bounded conclusion that statistical unusualness and modulation-like evidence are non-equivalent.

## Competency gate after Module 18

Before treating the learning sequence as complete, the student should also be able to:

- name the fixed four candidates and distinguish them from the Matrix-C tested-procedure trio, cross-tier pair, threshold-neighborhood cases, and six exploratory XAI cases;
- explain why Blank Sky-5 is retained in the frozen result but described as seed-sensitive;
- state Agent 8's one Moderate primary and three Moderate secondary contributions;
- explain why established algorithms, robustness checks, the six-case test, and the Flask interface are supporting elements rather than separate major contributions;
- defend the central non-equivalence finding as bounded and descriptive;
- list the limitations that stop the work from becoming a general anomaly detector, a validated explainer, or calibrated polarimetry;
- explain Agent 9's Weak Reject verdict and the conditions under which a venue-appropriate paper could become Weak Accept without new experiments;
- place problem, method, results, interpretation, limitations, and future work in the correct IEEE sections;
- answer a hostile question using the define-evidence-boundary-escalation pattern; and
- state which remaining questions require guide or POLIX-aware approval.

## Evidence used for Modules 1-18

- ISRO XPoSat mission page: https://www.isro.gov.in/XPoSat.html
- *XPoSat-POLIX User Handbook: User Guide for Scientific Data Analysis Level2*, V1.0, Oct. 2025
- F. Kislat *et al.*, “Analyzing the Data from X-Ray Polarimeters with Stokes Parameters,” 2015, DOI: 10.1016/j.astropartphys.2015.02.007
- S. Fabiani, “Instrumentation and Future Missions in the Upcoming Era of X-Ray Polarimetry,” 2018, DOI: 10.3390/galaxies6020054
- Agent 1 project-provenance audit and Agent 3 feature-semantics audit
- Frozen Matrix A/B/C/WR files, saved model, Notebooks 08-11, and deployed service code
- Existing supplementary seed, contamination, jackknife, ablation, ranking, and faithfulness outputs
- Agents 4-6 Phase-4 reviews for the statistical, XAI-method, and physical-diagnostic claim boundaries
- Agent 7 controlled literature audit and verified reference library
- Agent 8 novelty and contribution audit, including the Moderate contribution ratings
- Agent 9 hostile IEEE review, including the Weak Reject and conditional Weak Accept assessment

## Current learning status

Modules 1-18 are available in `01_to_18_Module_Files.md`. The glossary covers the technical and manuscript-defense concepts introduced through Module 18. The viva file now contains Questions 1-100. Creation of learning material does not establish student mastery; the student must complete the self-tests and defend the claim boundaries without notes.
