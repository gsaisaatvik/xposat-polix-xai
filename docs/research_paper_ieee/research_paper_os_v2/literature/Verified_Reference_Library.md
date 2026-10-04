# Verified Reference Library

**Library freeze:** 2026-07-27  
**Scope:** Literature screened during Research Paper OS V2 Phase 2  
**Controlled vocabulary:** VERIFIED AND RETAIN / CONTEXT ONLY

## Reading rule

A card records the largest claim the inspected source can safely support. It does not authorize every statement made in the source, and it does not override POLIX handbook limitations.

## VERIFIED AND RETAIN

### R01 - Official XPoSat mission page

- **Citation:** Indian Space Research Organisation, “XPoSat,” ISRO.
- **DOI/URL:** https://www.isro.gov.in/XPoSat.html
- **Source type:** Current official mission page.
- **Full text available:** Yes.
- **Inspected location:** Payload overview; “POLIX” and “XSPECT” subsections.
- **May support:** mission purpose; separate payload roles; POLIX 8-30 keV band; scatterer, collimator, and four proportional-counter detectors; XSPECT 0.8-15 keV role.
- **Must not support:** the archive composition; current Level-2 product semantics; calibrated values; project performance.
- **Project relevance:** Authoritative mission and instrument introduction.
- **Importance:** Essential.
- **Verification status:** VERIFIED AND RETAIN.

### R02 - POLIX Level-2 User Handbook

- **Citation:** N. Anand, K. Rikame, and K. Roy, *XPoSat-POLIX User Handbook: User Guide for Scientific Data Analysis Level2*, Version 1.0, Indian Space Research Organisation, Oct. 2025. Reviewed by V. Rana and Rishin P. V.; approved by B. Paul.
- **DOI/URL:** Local official PDF: `C:\Users\Saatvik\Downloads\POLIX_User_Handbook.pdf`.
- **Source type:** Official technical handbook.
- **Full text available:** Yes, 67-page PDF.
- **Inspected location:** pp. 7-26 (instrument, processing and Level-2 products); p. 25 (light-curve/PHA cautions); p. 26 (WeightedRoll); pp. 56-57 (detector timeline and background limitations); Annex A.
- **May support:** product semantics; source/background/occultation intervals; exposure weighting; WeightedRoll content; quick-look status of count-mode light curves; absence of current POLIX ARF/RMF; documented detector and variable-background limitations.
- **Must not support:** official background subtraction for this project; an official modulation factor; calibrated PD; official sky PA; claims for a later handbook version.
- **Project relevance:** Controlling source for the scientific meaning and limits of all POLIX products.
- **Importance:** Essential.
- **Verification status:** VERIFIED AND RETAIN.

### R03 - Official XPoSat science archive

- **Citation:** Indian Space Science Data Centre, “ISRO Science Data Archive: XPoSat,” PRADAN/ISSDC, n.d.
- **DOI/URL:** https://pradan1.issdc.gov.in/x01/index.xhtml
- **Source type:** Official data-service page.
- **Full text available:** Yes.
- **Inspected location:** XPoSat archive landing page and payload links.
- **May support:** official archive identity and payload/data-service context.
- **Must not support:** that the project used all public observations; the contents of the local 25-observation freeze.
- **Project relevance:** Data provenance and archive naming.
- **Importance:** Essential.
- **Verification status:** VERIFIED AND RETAIN; access date must be recorded at submission.

### R04 - Official acknowledgment guidance

- **Citation:** Indian Space Science Data Centre, “XPoSat Acknowledgment Guidance,” PRADAN/ISSDC, n.d.
- **DOI/URL:** https://pradan1.issdc.gov.in/x01/ack.xhtml
- **Source type:** Official data-use guidance.
- **Full text available:** Yes.
- **Inspected location:** Abstract-identification instruction and acknowledgment text.
- **May support:** requirement to identify XPoSat and the payload; exact current acknowledgment wording.
- **Must not support:** scientific findings or authorship decisions.
- **Project relevance:** Submission compliance.
- **Importance:** Essential.
- **Verification status:** VERIFIED AND RETAIN; wording must be rechecked immediately before submission.

### R05 - POLIX development lineage

- **Citation:** P. V. Rishin, B. Paul, R. Duraichelvan, M. James, J. Devasia, and R. Cowsik, “Development of a Thomson X-Ray Polarimeter,” arXiv:1009.0846, 2010.
- **DOI/URL:** https://doi.org/10.48550/arXiv.1009.0846
- **Source type:** Primary instrument-development manuscript.
- **Full text available:** Yes.
- **Inspected location:** Abstract; instrument-principle and prototype-design sections.
- **May support:** Thomson-scattering polarimeter principle and development lineage.
- **Must not support:** current flight configuration, Level-2 formats, in-flight calibration, or current energy-response values.
- **Project relevance:** Historical technical context.
- **Importance:** Supporting.
- **Verification status:** VERIFIED AND RETAIN with prototype-era warning.

### R06 - X-ray polarimetry instrumentation

- **Citation:** S. Fabiani, “Instrumentation and Future Missions in the Upcoming Era of X-Ray Polarimetry,” *Galaxies*, vol. 6, no. 2, art. 54, 2018.
- **DOI/URL:** https://doi.org/10.3390/galaxies6020054
- **Source type:** Peer-reviewed, open-access review.
- **Full text available:** Yes.
- **Inspected location:** Secs. 1-3, especially scattering polarimetry and modulation-factor discussion.
- **May support:** general azimuthal modulation principle; role of modulation factor; calibration dependence.
- **Must not support:** POLIX-specific product semantics or a value of POLIX μ100.
- **Project relevance:** General physical-method background.
- **Importance:** Essential for methods context.
- **Verification status:** VERIFIED AND RETAIN.

### R07 - Stokes analysis for X-ray polarimetry

- **Citation:** F. Kislat, B. Clark, M. Beilicke, and H. Krawczynski, “Analyzing the Data from X-Ray Polarimeters with Stokes Parameters,” *Astroparticle Physics*, vol. 68, pp. 45-51, 2015.
- **DOI/URL:** https://doi.org/10.1016/j.astropartphys.2015.02.007
- **Source type:** Peer-reviewed primary methods paper; author manuscript available as arXiv:1409.6214.
- **Full text available:** Yes.
- **Inspected location:** Abstract; Secs. 2-4, pp. 45-50.
- **May support:** eventwise/additive Stokes quantities; signal/background treatment; statistical care for polarization fraction and direction.
- **Must not support:** that the project's fitted Q/U are calibrated Stokes measurements; official PD/PA; the project's blank-sky selection rule.
- **Project relevance:** Mathematical foundation and boundary for the physical diagnostic.
- **Importance:** Essential.
- **Verification status:** VERIFIED AND RETAIN.

### R08 - Principal component analysis foundation

- **Citation:** K. Pearson, “On Lines and Planes of Closest Fit to Systems of Points in Space,” *The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science*, vol. 2, no. 11, pp. 559-572, 1901.
- **DOI/URL:** https://doi.org/10.1080/14786440109462720
- **Source type:** Foundational peer-reviewed methods paper.
- **Full text available:** Yes.
- **Inspected location:** pp. 559-572.
- **May support:** orthogonal least-squares directions underlying PCA.
- **Must not support:** modern software implementation details, anomaly validity, or chosen component count.
- **Project relevance:** Algorithm provenance.
- **Importance:** Supporting.
- **Verification status:** VERIFIED AND RETAIN.

### R09 - KMeans foundation

- **Citation:** J. MacQueen, “Some Methods for Classification and Analysis of Multivariate Observations,” in *Proc. Fifth Berkeley Symposium on Mathematical Statistics and Probability*, vol. 1, pp. 281-297, 1967.
- **DOI/URL:** https://projecteuclid.org/euclid.bsmsp/1200512992
- **Source type:** Foundational proceedings paper.
- **Full text available:** Yes.
- **Inspected location:** Algorithm and convergence discussion, pp. 281-297.
- **May support:** iterative within-cluster sum-of-squares clustering.
- **Must not support:** that two clusters are physically real or that centroid distance is a probability.
- **Project relevance:** Algorithm provenance.
- **Importance:** Supporting.
- **Verification status:** VERIFIED AND RETAIN.

### R10 - scikit-learn

- **Citation:** F. Pedregosa *et al.*, “Scikit-learn: Machine Learning in Python,” *Journal of Machine Learning Research*, vol. 12, pp. 2825-2830, 2011.
- **DOI/URL:** https://jmlr.org/papers/v12/pedregosa11a.html
- **Source type:** Peer-reviewed software paper.
- **Full text available:** Yes.
- **Inspected location:** pp. 2825-2830.
- **May support:** software-library provenance.
- **Must not support:** project parameter choices, reproducibility without exact versions, or model validity.
- **Project relevance:** Implementation citation.
- **Importance:** Supporting.
- **Verification status:** VERIFIED AND RETAIN.

### R11 - Isolation Forest

- **Citation:** F. T. Liu, K. M. Ting, and Z.-H. Zhou, “Isolation Forest,” in *2008 Eighth IEEE International Conference on Data Mining*, pp. 413-422, 2008.
- **DOI/URL:** https://doi.org/10.1109/ICDM.2008.17
- **Source type:** Peer-reviewed primary algorithm paper.
- **Full text available:** Yes via author manuscript; IEEE metadata verified.
- **Inspected location:** Secs. 2-3, pp. 413-417; experimental discussion.
- **May support:** random isolation, path length, and anomaly-score basis.
- **Must not support:** contamination = 0.16; labels for the archive; robustness at n = 25; superiority in this project.
- **Project relevance:** Primary anomaly-detector provenance.
- **Importance:** Essential.
- **Verification status:** VERIFIED AND RETAIN.

### R12 - Unsupervised astronomical outlier ranking

- **Citation:** D. Baron and D. Poznanski, “The Weirdest SDSS Galaxies: Results from an Outlier Detection Algorithm,” *Monthly Notices of the Royal Astronomical Society*, vol. 465, no. 4, pp. 4530-4555, 2017.
- **DOI/URL:** https://doi.org/10.1093/mnras/stw3021
- **Source type:** Peer-reviewed astronomy application.
- **Full text available:** Yes.
- **Inspected location:** Abstract; Sec. 3, especially 3.3; Secs. 4-5.
- **May support:** unsupervised archive ranking; domain inspection; possibility of instrumental/pipeline as well as scientific outliers.
- **Must not support:** physical interpretation of any POLIX observation or superiority of this project's method.
- **Project relevance:** Closest retained astronomy precedent for unusual-object screening.
- **Importance:** Essential.
- **Verification status:** VERIFIED AND RETAIN.

### R13 - Evaluation of astronomical anomaly ranking

- **Citation:** D. Giles and L. Walkowicz, “Systematic Serendipity: A Test of Unsupervised Machine Learning as a Method for Anomaly Detection,” *Monthly Notices of the Royal Astronomical Society*, vol. 484, no. 1, pp. 834-849, 2019.
- **DOI/URL:** https://doi.org/10.1093/mnras/sty3461
- **Source type:** Peer-reviewed astronomy methods/application paper.
- **Full text available:** Yes.
- **Inspected location:** Abstract; methods and evaluation sections; discussion.
- **May support:** use of a known unusual object to test ranking; caution that “interesting” and “outlying” require interpretation.
- **Must not support:** this project's candidates, labels, or small-sample generalization.
- **Project relevance:** Astronomy-specific validation context.
- **Importance:** Essential.
- **Verification status:** VERIFIED AND RETAIN.

### R14 - Human-in-the-loop astronomical anomaly detection

- **Citation:** M. Lochner and B. A. Bassett, “Astronomaly: Personalised Active Anomaly Detection in Astronomical Data,” *Astronomy and Computing*, vol. 36, art. 100481, 2021.
- **DOI/URL:** https://doi.org/10.1016/j.ascom.2021.100481
- **Source type:** Peer-reviewed astronomy software/method paper.
- **Full text available:** Yes via author manuscript.
- **Inspected location:** Abstract; framework/method sections; conclusions.
- **May support:** modular anomaly pipeline and expert feedback/inspection role.
- **Must not support:** that the Flask application implements Astronomaly or active learning.
- **Project relevance:** Researcher-facing anomaly-screening context.
- **Importance:** Essential.
- **Verification status:** VERIFIED AND RETAIN.

### R15 - Explainable anomaly detection taxonomy

- **Citation:** Z. Li, Y. Zhu, and M. van Leeuwen, “A Survey on Explainable Anomaly Detection,” *ACM Transactions on Knowledge Discovery from Data*, vol. 18, no. 1, pp. 1-54, 2024.
- **DOI/URL:** https://doi.org/10.1145/3609333
- **Source type:** Peer-reviewed survey; author manuscript arXiv:2210.06959.
- **Full text available:** Yes via author manuscript.
- **Inspected location:** Abstract; taxonomy and shallow/post-model explanation sections.
- **May support:** separation of detector and explanation; explanation taxonomies and access assumptions.
- **Must not support:** correctness, novelty, or formal guarantees of the project's four-component score.
- **Project relevance:** Primary explainable-anomaly positioning source.
- **Importance:** Essential.
- **Verification status:** VERIFIED AND RETAIN.

### R16 - Explanation faithfulness by perturbation

- **Citation:** C.-K. Yeh, C.-Y. Hsieh, A. Suggala, D. I. Inouye, and P. K. Ravikumar, “On the (In)fidelity and Sensitivity of Explanations,” in *Advances in Neural Information Processing Systems 32*, pp. 10965-10976, 2019.
- **DOI/URL:** https://proceedings.neurips.cc/paper/2019/hash/a7471fdc77b3435276507cc8f2dc2569-Abstract.html
- **Source type:** Peer-reviewed primary methods paper.
- **Full text available:** Yes.
- **Inspected location:** Abstract; Secs. 2-3; experiments.
- **May support:** the need for functional explanation metrics and perturbation-based comparison.
- **Must not support:** the project's neutralization protocol as the published infidelity metric; “Strong/Moderate” as standard categories; causal truth.
- **Project relevance:** Faithfulness-evaluation foundation and claim boundary.
- **Importance:** Essential.
- **Verification status:** VERIFIED AND RETAIN.

### R17 - Limits of unlabeled outlier evaluation

- **Citation:** G. O. Campos, A. Zimek, J. Sander, R. J. G. B. Campello, B. Micenková, E. Schubert, I. Assent, and M. E. Houle, “On the Evaluation of Unsupervised Outlier Detection: Measures, Datasets, and an Empirical Study,” *Data Mining and Knowledge Discovery*, vol. 30, no. 4, pp. 891-927, 2016.
- **DOI/URL:** https://doi.org/10.1007/s10618-015-0444-8
- **Source type:** Peer-reviewed empirical methods paper.
- **Full text available:** Yes; official supplementary material inspected.
- **Inspected location:** Abstract; Secs. 1, 5-6; supplementary dataset/evaluation page.
- **May support:** difficulty and bias in unsupervised outlier evaluation; sensitivity to datasets, preprocessing, parameters, and measures.
- **Must not support:** a numerical conclusion about this 25-observation archive without a direct benchmark.
- **Project relevance:** Strong limitation and evaluation reference.
- **Importance:** Essential.
- **Verification status:** VERIFIED AND RETAIN.

## CONTEXT ONLY

### R18 - XPoSat mission analysis

- **Citation:** H. Saini, K. V. Madhu, and R. Karidhal, “Mission Analysis, Design and Operations Plan of India's First Polarimetry Satellite: X-Ray Polarimetry Satellite (XPoSat),” *Experimental Astronomy*, vol. 59, no. 2, art. 17, 2025.
- **DOI/URL:** https://doi.org/10.1007/s10686-025-09988-6
- **Source type:** Peer-reviewed mission paper.
- **Full text available:** No; bibliographic metadata, abstract, and first-page information inspected.
- **Inspected location:** Publisher metadata and abstract only.
- **May support:** high-level launch, payload, and operations context after full-text confirmation.
- **Must not support:** detailed mission design, exact operations, or project methods while full text remains uninspected.
- **Project relevance:** Optional mission context.
- **Importance:** Contextual.
- **Verification status:** CONTEXT ONLY - full-text follow-up required.

### R19 - SHAP comparator

- **Citation:** S. M. Lundberg and S.-I. Lee, “A Unified Approach to Interpreting Model Predictions,” in *Advances in Neural Information Processing Systems 30*, pp. 4765-4774, 2017.
- **DOI/URL:** https://proceedings.neurips.cc/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html
- **Source type:** Peer-reviewed primary XAI methods paper.
- **Full text available:** Yes.
- **Inspected location:** Abstract; Sec. 2; properties discussion.
- **May support:** definition of SHAP as an additive attribution approach and a comparison point.
- **Must not support:** that SHAP was used, that the custom score has Shapley guarantees, or that explanations are causal.
- **Project relevance:** Prevents method misidentification.
- **Importance:** Contextual.
- **Verification status:** CONTEXT ONLY.

### R20 - Earlier anomaly-explanation review

- **Citation:** V. Yepmo, G. Smits, and O. Pivert, “Anomaly Explanation: A Review,” *Data & Knowledge Engineering*, vol. 137, art. 101946, 2022.
- **DOI/URL:** https://doi.org/10.1016/j.datak.2021.101946
- **Source type:** Peer-reviewed survey.
- **Full text available:** No; publisher abstract and displayed section summaries inspected.
- **Inspected location:** Abstract and high-level four-category taxonomy only.
- **May support:** high-level motivation and broad anomaly-explanation categories.
- **Must not support:** detailed taxonomy claims or direct method comparison without full text.
- **Project relevance:** Historical context; largely superseded here by R15.
- **Importance:** Contextual.
- **Verification status:** CONTEXT ONLY - full-text follow-up required.

### R21 - Multi-view learning survey

- **Citation:** C. Xu, D. Tao, and C. Xu, “A Survey on Multi-view Learning,” arXiv:1304.5634, 2013.
- **DOI/URL:** https://doi.org/10.48550/arXiv.1304.5634
- **Source type:** Survey manuscript.
- **Full text available:** Yes.
- **Inspected location:** Abstract; taxonomy and conclusion.
- **May support:** broad definition of views as multiple sources or feature subsets and complementary/consensus principles.
- **Must not support:** claiming Matrix C is a multi-view learning method or has multi-view generalization benefits.
- **Project relevance:** Terminology only.
- **Importance:** Contextual.
- **Verification status:** CONTEXT ONLY.

### R22 - Multi-view representation objective

- **Citation:** H. Hwang, G.-H. Kim, S. Hong, and K.-E. Kim, “Multi-View Representation Learning via Total Correlation Objective,” in *Advances in Neural Information Processing Systems 34*, pp. 12194-12207, 2021.
- **DOI/URL:** https://proceedings.neurips.cc/paper/2021/hash/65a99bb7a3115fdede20da98b08a370f-Abstract.html
- **Source type:** Peer-reviewed primary representation-learning paper.
- **Full text available:** Yes.
- **Inspected location:** Abstract; Sec. 1; formulation.
- **May support:** contemporary multi-view representation terminology and the notion of shared versus view-specific information.
- **Must not support:** equivalence to early feature concatenation; any performance claim for Matrix C.
- **Project relevance:** Adjacent positioning only.
- **Importance:** Contextual.
- **Verification status:** CONTEXT ONLY.

## Library totals

- **VERIFIED AND RETAIN:** 17
- **CONTEXT ONLY:** 5
- **Reference cards in this file:** 22
- **REMOVE OR REPLACE:** 6 additional cards in `Rejected_or_Unnecessary_References.md`

