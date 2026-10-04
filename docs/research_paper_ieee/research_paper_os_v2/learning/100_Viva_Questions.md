# Viva Questions

**Final learning edition:** Questions 1-100 cover Learning Modules 1-18 and the specialist audits through Agent 9.

## Questions 1-20

1. **Why are astronomical X-ray instruments usually placed in space?**  
   Earth's atmosphere absorbs most celestial X-rays, so space deployment is required to detect them.

2. **What does a detector count represent?**  
   A registered interaction in the detector. It is not by itself a calibrated source flux.

3. **What is a light curve?**  
   Counts or count rate arranged as a function of time.

4. **Why is a PHA channel not identical to photon energy?**  
   It is an instrumental pulse-height bin; converting it into physical energy needs calibration and response information.

5. **Why is background central to this project?**  
   Background contributes counts, can vary, and can show azimuthal modulation, so it can affect both statistical unusualness and physical interpretation.

6. **What is linear polarization?**  
   A preferred orientation of the electric-field oscillation of radiation.

7. **Why does a linear-polarization modulation use twice the azimuthal angle?**  
   Linear orientation repeats after \(180^\circ\), giving a two-fold pattern over \(360^\circ\).

8. **What do \(Q\) and \(U\) mean in the project's fitted equation?**  
   They are the coefficients of \(\cos 2\phi\) and \(\sin 2\phi\) in the chosen fit convention; they are Stokes-like diagnostics, not automatically calibrated Stokes measurements.

9. **Why is raw modulation not polarization degree?**  
   PD requires background treatment and an appropriate calibrated response to a 100% polarized beam.

10. **Why is fitted phase not official sky PA?**  
    The instrument angle convention must be transformed and calibrated into a verified celestial reference frame.

11. **What are the two payloads on XPoSat?**  
    POLIX and XSPECT.

12. **What is POLIX's role and current official energy band?**  
    Medium-energy X-ray polarimetry using Thomson scattering, described by ISRO as 8-30 keV.

13. **What is XSPECT's role and energy band?**  
    X-ray spectroscopy and timing in 0.8-15 keV.

14. **Did Matrix C use XSPECT data?**  
    No. It represents POLIX Level-2 products in the frozen project.

15. **Why must you say “25 observations included in the project archive”?**  
    The project freeze verifies only that local collection; it does not establish that all public POLIX observations were used.

16. **What is a FITS HDU?**  
    A Header/Data Unit containing metadata and a data object such as a table or array.

17. **What information is in the energy-resolved source-azimuth product?**  
    Counts across azimuth, PHA values, and 48 anode cells in a three-dimensional data cube.

18. **What does the handbook say about WeightedRoll?**  
    It is the exposure-weighted final intensity modulation product and contains modulation contributions from both source and background count rates.

19. **Why is WeightedRoll excluded from Matrix C?**  
    To keep physical modulation evidence separate from the anomaly input and reduce circular confirmation.

20. **What is the strongest handbook boundary for physical claims?**  
    Under the documented variable background and spikes, polarization measurement is not possible with the currently released data described by handbook V1.0; future data/method releases are expected to address background subtraction.

## Questions 21-70

21. **What is the exact project dataset scope?**  
    Twenty-five POLIX Level-2 observations included in the project archive.

22. **How is that archive divided by project role?**  
    Ten source and fifteen blank-sky observations.

23. **Why are role labels not anomaly labels?**  
    Source/blank sky describes observing role, whereas no trusted normal/anomaly ground truth exists.

24. **Why should observation IDs appear in result tables?**  
    They are unique, while friendly metadata contains a duplicated “Blank Sky-2” label.

25. **Why can the project not report supervised accuracy?**  
    It has no trusted anomaly labels or independent labelled test set.

26. **How many Matrix-C features are there?**  
    Fifteen.

27. **Which two features summarize exposure over roll?**  
    `t1A_exp_uniformity_cv` and `t1A_exp_max_to_min_roll`.

28. **Why is `t1A_energy_peak_channel` not a spectral peak energy?**  
    It is the index of the largest bin in a collapsed detector-channel distribution, without conversion to calibrated keV.

29. **What is technically incomplete about source-roll smoothness?**  
    It uses adjacent stored-order differences but omits the circular last-to-first difference and explicit angle sorting.

30. **What important inputs are ignored by the light-curve features?**  
    FRAC_EXP, rate errors, quality information, explicit GTI filtering, and bin comparability.

31. **What does PCA do to standardized Matrix C?**  
    It rotates the data into orthogonal directions ordered by explained variance.

32. **How much variance do Matrix-C PC1 and PC2 explain in the existing audit?**  
    Approximately 0.6125, or 61.25%.

33. **What is the project's PCA distance?**  
    \(\sqrt{PC1^2+PC2^2}\).

34. **Why is a distant PCA point not a confirmed anomaly?**  
    PCA measures geometry and variance, not labelled scientific abnormality.

35. **Why should the PCA/Isolation correlation p-value be interpreted cautiously?**  
    The rankings come from the same small archive and the test is descriptive, not independent validation.

36. **What value of \(k\) is stored in the deployed KMeans model?**  
    Five.

37. **What is the KMeans feature contribution?**  
    The squared standardized difference between one feature and its assigned centroid coordinate.

38. **What does a silhouette score assess?**  
    Within-cluster cohesion relative to separation from the nearest other cluster.

39. **Why is a singleton cluster problematic for interpretation?**  
    Its sole member equals the centroid, giving zero centroid distance and no evidence of a physical class.

40. **Can KMeans clusters be named as source categories?**  
    No; no labels or physical validation establish that interpretation.

41. **What are the saved Isolation Forest settings central to the paper?**  
    100 trees, contamination 0.16, and random state 42.

42. **Why does contamination 0.16 produce four candidates?**  
    It sets a threshold corresponding to roughly 16% of 25 rows.

43. **Which candidates were flagged in every one of 100 tested seeds?**  
    Blank Sky-13, Sco X-1, and Her X-1.

44. **How seed-stable was Blank Sky-5?**  
    It was flagged in 29 of 100 tested seeds.

45. **What is the safe replacement for an unqualified “robust core”?**  
    “Three-candidate Matrix-C core stable under the tested seed, threshold, and included-observation jackknife procedures”; it is not a probability, truth, cross-matrix, or future-data claim.

46. **List the four custom XAI components.**  
    PCA contribution, squared KMeans centroid-distance contribution, positive Isolation Forest occlusion delta, and absolute standardized value.

47. **How is each XAI component normalized?**  
    Its fifteen feature values are divided by that component's maximum absolute value within the observation.

48. **What is the usual possible range of the combined score?**  
    Zero to four because four normalized nonnegative components are summed.

49. **Why can Sco X-1 have a zero KMeans component?**  
    It is the only member of its assigned cluster and equals that centroid.

50. **What is the accepted Sco X-1 feature order?**  
    Peak channel first, weighted mean channel second, and channel entropy third.

51. **How many features are neutralized in the faithfulness test?**  
    The top three.

52. **What does setting a standardized feature to zero mean?**  
    Replacing it with the training mean of that feature.

53. **What defines a Strong faithfulness verdict?**  
    Both PCA distance and Isolation Forest anomaly score decrease.

54. **What defines a Moderate verdict?**  
    Either PCA distance or Isolation Forest score decreases, but not both.

55. **What are the verified verdict counts?**  
    Five Strong, one Moderate, and zero Weak across six exploratory cases.

56. **What product does the physical branch fit?**  
    The POLIX WeightedRoll Level-2 curve.

57. **What is the fitted model?**  
    \(C+Q\cos(2\phi)+U\sin(2\phi)\).

58. **How is raw modulation calculated, and which uncertainty method controls the saved CSV?**  
    It is \(\sqrt{Q^2+U^2}/C\), usually reported as a percentage. The saved errors use the frozen notebook method; the current Flask service uses a different \(A/C\) propagation and must not be silently substituted.

59. **What makes a fit acceptable in the project rule?**  
    Reduced chi-square less than or equal to 2; this is a project screening rule, not a p-value or detection threshold.

60. **Why is fitted phase not official PA?**  
    The detector-to-sky convention, sign, offsets, and official calibration are not verified.

61. **How many blank-sky curves were fitted and how many entered the baseline?**  
    Fifteen were fitted; thirteen acceptable fits entered the baseline.

62. **What is the empirical mean blank-sky raw modulation?**  
    Approximately 1.147820%.

63. **What is the empirical mean normalized coefficient pair?**  
    \(q=0.0090920\) and \(u=-0.0064782\).

64. **What does the project's blank-sky fractional-harmonic-coordinate distance omit?**  
    \(q/u\) covariance, coefficient errors, baseline-estimation uncertainty, and observation-condition matching.

65. **Does being inside blank-sky scatter prove a source is unpolarized?**  
    No.

66. **Why are the pipeline and XAI components not four independent models, and what sets the deployed label?**  
    StandardScaler, PCA, KMeans, and Isolation Forest form one pipeline; the XAI terms are correlated views of the standardized row. Only `IsolationForest.predict` sets the deployed label.

67. **Why is WeightedRoll separation important?**  
    It prevents the physical modulation product from being both an anomaly input and its own apparent confirmation.

68. **What does the central non-equivalence statement mean?**  
    An observation can be statistically unusual in Matrix C without showing modulation beyond the archive's empirical blank-sky behavior, and vice versa.

69. **What does the central non-equivalence statement not mean?**  
    It does not establish or rule out astrophysical polarization and does not validate either branch as ground truth.

70. **What is the safest one-sentence description of the entire project at this stage?**  
    It is a proof-of-concept, archive-relative POLIX Level-2 screening framework with project-specific local explanations and a scientifically separate empirical modulation diagnostic.

## Questions 71-100

71. **What are the four candidates returned by the frozen deployed model?**  
    `C24_0018` (project-labelled Blank Sky-13), `G01_0006` (Sco X-1), `G01_0003` (Her X-1), and `C24_0010` (project-labelled Blank Sky-5).

72. **What is the fixed deployed class count?**  
    Twenty-one Normal observations and four anomaly candidates among the 25 archived observations.

73. **Which observations form the three-candidate Matrix-C core stable under the tested procedures?**  
    `C24_0018`, `G01_0006`, and `G01_0003`.

74. **What procedures support that qualified three-candidate statement?**  
    The existing 100-seed Isolation Forest test, tested contamination thresholds, and included-observation jackknife refits on Matrix C.

75. **Why must the phrase “robust core” be avoided?**  
    It sounds like general or external validation. The evidence supports only Matrix-C stability under the named retrospective procedures.

76. **What does Blank Sky-5's 29/100 seed frequency show?**  
    It is a seed-sensitive fixed candidate near the threshold. The frequency is not anomaly probability or confidence.

77. **Why is `C24_0020` important even though it is not in the fixed four?**  
    It was selected in 68/100 seed fits, showing that the boundary neighborhood is uncertain and that the fixed four are not equally stable.

78. **Which two observations persist across Matrix A, B, and C candidate sets?**  
    `C24_0018` and `G01_0006`; Her X-1 (`G01_0003`) is part of the Matrix-C trio but is absent from the Matrix A and B candidate sets.

79. **What is the accepted current Sco X-1 local feature order?**  
    Energy peak channel (2.454499), energy weighted mean channel (2.207369), and energy channel entropy (1.813968). The historical entropy-first narrative is superseded.

80. **How do the six exploratory XAI cases differ from the four deployed candidates?**  
    The six were selected for an in-sample feature-neutralization sanity check and include cases beyond the fixed deployed candidate set.

81. **What is Agent 8's primary contribution decision?**  
    A Moderate applied-methodology contribution: a traceable, product-aware XAI framework for archive-relative screening of heterogeneous POLIX Level-2 observations.

82. **What are the three proposed secondary contributions?**  
    The 15-feature provenance-preserving representation, the deterministic project-specific local feature-ranking method, and the scientifically separate WeightedRoll/empirical blank-sky harmonic branch.

83. **Why is the StandardScaler/PCA/KMeans/Isolation Forest stack not algorithmic novelty?**  
    These are established methods. The defensible contribution is their traceable and bounded integration for this POLIX archive.

84. **Why is the six-case perturbation result supporting evidence rather than a major contribution?**  
    It is small, in-sample, method-aligned, lacks comparison baselines and effect-size thresholds, and does not prove general explanation faithfulness.

85. **Why is the Flask interface not a principal research contribution?**  
    It is a proof-of-concept researcher-facing implementation and reproducibility aid, not scientific validation or a new algorithm.

86. **What does the reviewed literature gap safely support?**  
    That limited published work was identified and no directly comparable integrated POLIX Level-2 framework was found in the controlled review.

87. **What does the literature gap not support?**  
    Priority, uniqueness, superiority, “first,” “novel,” or “never attempted” claims.

88. **What is the principal empirical finding?**  
    Within the frozen archive, Matrix-C statistical unusualness and modulation-like harmonic evidence are non-equivalent diagnostic questions.

89. **Why does non-equivalence not mean statistical independence?**  
    Discordant cases show that the branches do not identify the same property, but no independence model or population-level statistical test was established.

90. **State Agent 9's current verdict and its meaning.**  
    Weak Reject: the evidence is too narrow for a broad methodology reading, but the fixed result is reproducible and a bounded applied case study could become Weak Accept after reconstruction and guide/domain review.

91. **Did Agent 9 find a fatal numerical contradiction in the central archive-screening result?**  
    No. Fatal problems arise only if the paper retains broad anomaly-validation, general-XAI, calibrated-polarimetry, superiority, or priority claims.

92. **Is a new experiment mandatory for the bounded paper?**  
    No. The essential remaining work is evidence-bounded reconstruction, terminology and citation checks, domain review, provenance disclosure, and manual author verification.

93. **When would prospective or independent evaluation become essential?**  
    If the paper claims future-release generalization, accuracy, transfer, or a generally validated anomaly detector.

94. **What are the main XAI limitations a student must disclose?**  
    The ranking is a project-specific heuristic, not exact label attribution or SHAP; normalization is within observation; the six-case test is in-sample and method-aligned; and no causal or general faithfulness claim follows.

95. **What are the main physical-diagnostic limitations?**  
    WeightedRoll contains source plus background; the reference uses 13 selected archive fits; thresholds are project rules; and official background, response, \(\mu_{100}\), and sky-angle calibration are absent.

96. **How should the Notebook-11/Flask uncertainty mismatch be presented?**  
    Report frozen Notebook-11/CSV uncertainty provenance, disclose that the later service uses a different \(A/C\) propagation, and do not claim numerical identity.

97. **What belongs in Results rather than Discussion?**  
    The fixed four, tested-procedure frequencies, cross-tier memberships, local rankings, and bounded harmonic values. Discussion explains their meaning and limitations.

98. **What is the safest structure for answering a hostile viva question?**  
    Define the term, identify controlling evidence, state the bounded result, distinguish nearby results, state the limitation, and escalate unresolved physical meaning to the guide or domain expert.

99. **Why may the paper answer its research question without claiming a discovery?**  
    It demonstrated a traceable archive-screening and independent diagnostic workflow. Demonstrating a workflow does not establish a new astrophysical event, calibrated polarization, or validated anomaly truth.

100. **What remains before the work is submission-ready?**  
     Guide and POLIX-aware approval, author order and venue/page-limit decisions, final figure and reference checks, manual revision by all authors, venue-compliant AI disclosure, and resolution or explicit marking of all submission blockers.
