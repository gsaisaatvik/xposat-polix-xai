# Research Paper Glossary - Modules 1-18

| Term | Student-safe meaning | Project boundary |
|---|---|---|
| Anode | Charge-collecting element in a proportional counter. | The energy-resolved product includes information across 48 anode cells. |
| Anomaly candidate | An observation flagged as statistically unusual by the deployed rule. | Not a confirmed physical anomaly. |
| Azimuth | Angle around a chosen instrument/reference axis. | Its convention must be traced before interpreting phase. |
| Background | Counts not attributable to the intended source signal under the analysis model. | It can be variable and modulated; it is not automatically removed from WeightedRoll. |
| Calibration | Mapping instrument measurements to defensible physical quantities. | Required for official PD/PA and spectroscopy claims. |
| Channel | Discrete detector or pulse-height bin. | Not automatically a physical energy. |
| Collimator | Structure limiting the instrument field of view. | POLIX is non-imaging and collimated. |
| Count | A registered detector interaction. | Not identical to calibrated source flux. |
| Count rate | Counts divided by an observing time or bin duration. | Background and dead-time/exposure effects may matter. |
| Detector frame | Coordinate system fixed to the instrument. | A fitted phase here is not automatically sky PA. |
| Earth occultation | Interval in which Earth blocks the astronomical source direction. | A separate observing/data interval in POLIX products. |
| Energy | Photon energy, usually stated in keV in X-ray astronomy. | A PHA channel needs calibration before physical energy interpretation. |
| Exposure | Effective observing opportunity or time accumulated under specified conditions. | POLIX provides exposure versus azimuth products. |
| FITS | Flexible Image Transport System, a standard astronomy data format. | A file can contain multiple HDUs, tables, arrays, and metadata. |
| Fitted phase | Phase parameter of the fitted second harmonic. | Not official sky polarization angle. |
| Good Time Interval (GTI) | Time interval accepted for analysis under processing rules. | GTIs influence exposure and event selection. |
| HDU | Header/Data Unit inside a FITS file. | Code must select the intended HDU explicitly. |
| Instrument response | Mapping between incident radiation and recorded detector quantities. | Needed for calibrated spectral/polarimetric inference. |
| ISRO | Indian Space Research Organisation. | Operates XPoSat. |
| ISSDC | Indian Space Science Data Centre. | Archives XPoSat data through its science-data services. |
| keV | Kilo-electronvolt, an energy unit. | POLIX's official mission-page band is 8-30 keV. |
| Level 1 | Earlier processed mission data product level. | The project principally uses Level-2 products. |
| Level 2 | Higher-level processed data products for scientific analysis. | Release-specific handbook limitations still apply. |
| Light curve | Counts or count rate versus time. | Count-mode POLIX light curves are described as quick diagnosis, not further scientific analysis. |
| Linear polarization | Preferred orientation of the electric field of radiation. | POLIX probes it through azimuthal scattering. |
| Matrix C | Frozen 15-feature observation representation used by the deployed model. | WeightedRoll is not part of the primary input. |
| Modulation curve | Counts/intensity as a function of azimuthal angle. | A two-fold pattern may arise from source or background contributions. |
| Modulation factor \(\mu_{100}\) | Instrument response to a 100% polarized signal under defined conditions. | No official project-specific value is currently verified. |
| PA | Polarization angle on the sky. | Requires verified coordinate conversion and calibration. |
| PD | Polarization degree. | Requires background and response calibration; proxy scenarios are not measurements. |
| PHA | Pulse Height Analyzer quantity/channel. | May be used as a diagnostic feature, not calibrated spectroscopy. |
| Photon | Quantum of electromagnetic radiation. | X-ray photons have higher energy than visible-light photons. |
| POLIX | Polarimeter Instrument in X-rays on XPoSat. | Project data source; not XSPECT. |
| PRADAN | ISRO science-data archive service used for XPoSat access. | Official data-use guidance should be checked before submission. |
| Proportional counter | Gas detector whose electrical pulse relates to deposited energy. | POLIX uses four such detector units around the scatterer. |
| Q/U coefficients | Cosine and sine coefficients of the project's second-harmonic fit. | Prefer “harmonic coefficients”; symbols alone do not establish calibrated Stokes measurements. |
| Raw modulation | Uncalibrated fitted modulation magnitude under the project's definition. | Must not be called PD. |
| Roll | Rotation coordinate used by the Level-2 exposure/modulation analysis. | Exact reference direction and convention matter. |
| Scatterer | Material in which incident photons change direction. | POLIX uses low-Z material for Thomson scattering. |
| Sky frame | Celestial-coordinate reference system. | Required for official PA. |
| Source interval | Time/selection associated with observing the intended target. | May still contain background counts. |
| Spectrum | Distribution of signal with physical energy after appropriate response treatment. | Current released POLIX products are not intended for spectroscopy. |
| Thomson scattering | Elastic scattering of electromagnetic radiation by free or weakly bound electrons in the relevant regime. | Its polarization-dependent angular distribution underlies POLIX. |
| WeightedRoll | POLIX exposure-weighted modulation versus roll azimuth. | Contains both source and background modulation contributions. |
| XPoSat | ISRO's X-ray polarimetry satellite. | The project uses a fixed local POLIX archive, not all XPoSat data. |
| XSPECT | X-ray Spectroscopy and Timing payload on XPoSat. | Not an input to Matrix C. |
| Yaw | A spacecraft/instrument rotation axis used for an alternate azimuth product. | The handbook says roll exposure is used in later pipeline analysis. |
| Absolute standardized value | Magnitude of a feature after subtracting training mean and dividing by training SD. | One of four custom XAI components; not a physical effect size. |
| Acceptable fit | Project label for reduced chi-square <=2. | A heuristic quality class, not official POLIX certification. |
| Ablation | Comparison after removing a feature tier or input set. | Matrices A/B/C show representation sensitivity; WR remains separate. |
| Anomaly score | Numeric archive-relative unusualness output. | Not a probability or calibrated confidence. |
| Contamination | Isolation Forest parameter used to set an expected outlier fraction/threshold. | 0.16 produces four fixed candidates among 25 rows. |
| Centroid | Mean vector of a KMeans cluster in feature space. | Does not represent a physical source class. |
| Centroid-distance contribution | Squared feature-wise deviation from the assigned KMeans centroid. | A local geometric XAI component. |
| Component normalization | Dividing a component vector by its maximum absolute feature value. | Makes each XAI component's largest feature equal to one within an observation. |
| Correlation p-value | Tail probability under a stated null model for a correlation statistic. | Here it is descriptive and not external validation. |
| Data drift | Change between future observations and the distribution used to fit the model. | Not tested by internal seed or jackknife checks. |
| Descriptive result | A summary of the observed archive without a population-generalization claim. | Most project results belong in this category. |
| Diagonal standardized distance | Euclidean distance after separately scaling q and u by their SDs. | Ignores q-u covariance and baseline-estimation uncertainty. |
| Fractional harmonic coordinates | \(q=Q/C\) and \(u=U/C\) from the project's empirical second-harmonic fit. | Safer than unqualified Stokes \(q/u\); not calibrated polarimetry. |
| Explained-variance ratio | Fraction of total standardized variance represented by a PCA component. | Two Matrix-C components represent about 61%, not all variation. |
| Feature attribution | Assignment of model-linked relevance to input features. | Here, only “project-specific heuristic attribution of composite evidence” is safe; “local feature-importance ranking” is preferred. |
| Feature neutralization | Setting selected standardized features to zero. | Zero is the scaler mean, but the joint perturbed row may be unrealistic. |
| Faithfulness test | Perturbation check asking whether changing highly ranked features changes selected fitted-model summaries. | The six-case test is an in-sample, method-aligned sanity check, not general or causal validation. |
| Fit quality | Project classification derived from reduced chi-square. | Acceptable/caution/poor does not replace physical calibration review. |
| Harmonic coefficient | Coefficient multiplying a sine or cosine basis function. | Safer term than unqualified Stokes Q/U for the project fit. |
| Isolation Forest | Tree ensemble that isolates unusual rows through random partitions. | The primary fixed candidate detector in the saved model. |
| Jackknife | Repeating an analysis after omitting one observation. | Tests internal leave-one-out sensitivity, not future generalization. |
| KMeans | Algorithm partitioning rows around \(k\) centroids. | Supplies local geometry, not astrophysical classes. |
| Local explanation | Explanation specific to one observation and fitted model state. | Does not establish global feature importance or physical cause. |
| Deployed anomaly label | The fixed `Anomaly` or `Normal` output used by the application. | It is set solely by `IsolationForest.predict`; the other XAI components do not vote on it. |
| Matrix ablation | Comparison of results using feature tiers A, B, C, or WR. | Shows candidate sensitivity to representation choice. |
| Normalization baseline | Reference value used when perturbing or scaling a feature. | The XAI neutralization baseline is standardized zero. |
| Occlusion contribution | Change in Isolation Forest score after setting one feature to zero. | Only positive deltas enter the combined XAI score. |
| PCA | Linear rotation to orthogonal directions of decreasing variance. | Used for visualization and geometric evidence, not ground truth. |
| PCA distance | Distance from the origin in the first two PCA coordinates. | Ignores later components. |
| Product family | Group of features derived from one class of Level-2 products. | Prefix mapping is deterministic but does not confer calibration. |
| Pseudoinverse | Generalized inverse used when solving the weighted normal equations. | Does not by itself guarantee stable or unbiased physical estimates. |
| Notebook/service uncertainty mismatch | Frozen notebook and current Flask service propagate \(A/C\) uncertainty differently. | Saved CSV errors use the notebook method; the formulas must not be silently conflated. |
| Random seed | Number fixing pseudorandom choices. | Seed sensitivity describes algorithmic repeatability on the same data. |
| Ranking stability | Similarity or persistence of ordering under a specified perturbation. | Not equivalent to label accuracy or future robustness. |
| Reduced chi-square | Chi-square divided by fitted degrees of freedom. | Interpretable only under the error and model assumptions. |
| Robust core | Short phrase for candidates stable under recorded procedures. | Must always be qualified as tested-procedure stability, not truth. |
| Strong/Moderate/Weak verdict | Project-defined sign-based category from the neutralization check. | Not a significance level, literature standard, or effect-size grade; KMeans does not determine it. |
| SHAP | Additive attribution framework based on Shapley values. | Not used by the deployed method. |
| Silhouette score | Internal clustering measure comparing within- and nearest-cluster separation. | Does not prove physical cluster validity. |
| StandardScaler | Transformation using training mean and population SD per feature. | Makes features comparable numerically; does not correct scientific bias. |
| Stokes-like | Resembling a Stokes coefficient representation without established calibration equivalence. | Must be explicitly qualified as empirical if used. |
| Tested-procedure robustness | Persistence under the specific seeds, contamination settings, or omissions examined. | Does not imply generalization to future observations. |
| Applied methodology contribution | A contribution based on a disciplined, useful scientific workflow rather than a newly invented algorithm. | Agent 8 rates the integrated framework Moderate and archive-bounded. |
| Archive-relative screening | Ranking or labeling observations relative to the distribution in the frozen project archive. | It does not estimate anomaly prevalence in all POLIX data. |
| Conditional acceptance | A review position that becomes favorable only after specified revisions and approvals. | Agent 9 describes a possible Weak Accept at an appropriate venue after bounded reconstruction and review. |
| Contribution | An evidence-supported addition made by the paper. | The project uses one primary and no more than three secondary contributions. |
| Cross-feature-tier persistence | Candidate membership shared across Matrices A, B, and C. | Only `C24_0018` and `G01_0006` persist across all three tested tiers. |
| Domain approval | Review by a person with appropriate POLIX/instrument expertise. | Required for unresolved feature semantics and physical-diagnostic wording. |
| Fatal claim-evidence conflict | A contradiction between a manuscript claim and the available evidence that prevents defensible submission under that framing. | No fatal numerical conflict was found for the bounded result; broad validation or calibrated claims would create one. |
| Fixed deployed result | Output of the frozen saved model and exact deployed rule. | It is 21 Normal observations and four candidates; it is not the same as a stability result. |
| Guide-ready | Content sufficiently checked for faculty review. | It is not synonymous with submission-ready or publication-ready. |
| Hostile review | Deliberately skeptical review intended to find rejection risks. | Agent 9's Weak Reject must inform reconstruction rather than be hidden. |
| Literature gap | A specific capability not provided by the reviewed, verified literature. | “Limited directly comparable work was identified” is safer than a priority claim. |
| Nearest false claim | The tempting broader statement immediately beyond what the evidence supports. | For “candidate,” the nearest false claim is “confirmed anomaly.” |
| Primary contribution | The paper's most important evidence-supported addition. | Here it is the traceable product-aware archive-screening framework, rated Moderate. |
| Proof of concept | An implementation demonstrating feasibility in a bounded setting. | The Flask interface is not production validation. |
| Secondary contribution | A supporting research addition subordinate to the primary contribution. | The representation, local ranking, and separate harmonic branch are the three proposed secondary contributions. |
| Submission-ready | Ready for a chosen venue after all scientific, authorship, formatting, reference, figure, and disclosure approvals. | The current learning and draft work cannot grant this status by itself. |
| Supporting evidence | Analysis that strengthens or limits a contribution without being a major contribution itself. | Seed, contamination, jackknife, ablation, and six-case perturbation results have this role. |
| Threshold neighborhood | Observations whose selection changes near the decision boundary under tested seeds or thresholds. | Blank Sky-5 and `C24_0020` illustrate this uncertainty. |
| Weak Accept | Marginally favorable peer-review recommendation under a suitable scope and venue. | Agent 9 says it is plausible after bounded reconstruction and guide/domain review. |
| Weak Reject | Marginally unfavorable peer-review recommendation reflecting important but potentially fixable scope/evidence concerns. | It does not mean the fixed result is irreproducible or false. |
