# BHUTAN Knowledge Card 06 — Project-Specific Local XAI Heuristic

## Beginner explanation

The deployed label answers, “Did Isolation Forest flag this observation?” The local Explainable Artificial Intelligence (XAI) method answers, “Which Matrix-C features provide the strongest local evidence that this row differs from the project archive?” It combines four explanation components—not four models—and ranks the 15 features within one observation. It does not identify a physical cause.

## Technical theory

For standardized feature \(x_j\), PCA loading \(l_{kj}\), explained-variance ratio \(r_k\), assigned KMeans centroid coordinate \(c_j\), and project anomaly score \(s(x)=-\operatorname{score\_samples}_{\mathrm{IF}}(x)\),

\[
P_j=|x_jl_{1j}|r_1+|x_jl_{2j}|r_2,
\]
\[
K_j=(x_j-c_j)^2,
\]
\[
I_j=s(x)-s(x^{(j\leftarrow0)}),
\]
\[
Z_j=|x_j|.
\]

Setting a standardized feature to zero neutralizes it to the scaler’s fitted archive mean while leaving other coordinates unchanged. For a component vector \(v\),

\[
N(v)_j=\begin{cases}|v_j|/\max_k|v_k|,&\max_k|v_k|>0,\\0,&\text{otherwise}.
\end{cases}
\]

The combined score is

\[
E_j=N(P)_j+N(K)_j+N(\max(I,0))_j+N(Z)_j.
\]

Negative occlusion changes are clipped to zero. Each component is normalized separately within the observation and receives equal implicit weight. The scale is not calibrated across observations.

## Exact project implementation

- The saved scaler, two-component PCA, KMeans and Isolation Forest are used.
- One feature is neutralized at a time for the Isolation Forest occlusion term.
- The four normalized vectors are summed and sorted descending.
- Prefixes map features to exposure, energy-resolved, source-azimuth, light-curve or detector families.
- The service returns the top five features.
- A deterministic Python template creates the explanation sentence; no large language model is used.
- The score ranks evidence only and never changes the Isolation Forest label.

## Parameters and normalization conventions

The first two saved PCA components are used. Occlusion neutralizes one standardized coordinate to zero. Negative Isolation Forest deltas are clipped to zero. Each of the four component vectors is divided by its own within-observation maximum and the normalized vectors are summed with equal implicit weight.

## Controlling sources and functions

- `D:\polix_xai_webapp\model_service.py`: `normalize_score`, `PolixXAIPredictor.predict_dataframe`, `explain_one`, and `make_explanation_sentence`.
- `D:\polix_xai_webapp\model\polix_v2_matrixC_unsupervised_xai_model.pkl`: frozen model package.
- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\deployed_xai_exact_from_model_service.csv`: accepted exact-function output.
- `D:\polix_xai_webapp\research_paper_ieee\supplementary_experiments\faithfulness_verdict_reproduction.csv`: perturbation verdicts.
- Accepted audit commit: `15628ee7cc434de9ba03caaae5dd115d8cd09f9a`.

## Verified numerical results

For Sco X-1, the current versioned implementation ranks:

| Rank | Feature | Exact score | Main-paper score |
|---:|---|---:|---:|
| 1 | `t1A_energy_peak_channel` | 2.4544990315 | 2.454 |
| 2 | `t1A_energy_weighted_mean_channel` | 2.2073686585 | 2.207 |
| 3 | `t1A_energy_channel_entropy` | 1.8139679863 | 1.814 |

Sco X-1 occupies a singleton KMeans cluster, so its KMeans contribution is zero for every feature. The historical entropy-first narrative is not reproducible from a located versioned artifact and is superseded.

Six exploratory cases underwent joint top-three neutralization: Sco X-1, Blank Sky-13, Her X-1, Blank Sky-5, Blank Sky-15 and Blank Sky-6. Five verdicts were Strong, one was Moderate (Blank Sky-6), and none was Weak. Strong means both PCA distance and Isolation Forest score decreased; Moderate means exactly one decreased. KMeans was recorded but does not enter the verdict.

## Safe inference

The method gives an observation-specific, product-aware ranking under the frozen implementation. Sco X-1’s leading evidence comes from energy-product summaries under this heuristic. The perturbation check supports local sensitivity for the tested cases and quantities.

## Unsupported inference

Do not call the ranking causal, SHAP, a probability, calibrated importance, an exact label decomposition, cross-observation comparable, or a physical explanation. The six in-sample cases do not establish general explanation validity, and Strong/Moderate are not confidence categories.

## Paper-ready wording

> A deterministic, project-specific local feature-ranking heuristic combines normalized feature-wise evidence from the first two principal-component directions, squared deviation from the assigned KMeans centroid, positive Isolation Forest occlusion changes and absolute standardized deviation. The scores rank features within an observation and map them to originating product families; they are not causal attributions or calibrated quantities. For Sco X-1, the leading features were energy peak channel (2.454), energy weighted mean channel (2.207) and energy-channel entropy (1.814).

> As an in-sample sanity check, the three highest-ranked features were jointly neutralized in six exploratory observations. Both PCA distance and Isolation Forest score decreased in five cases, while one of the two decreased in the sixth. This supports local sensitivity under the tested perturbation but does not establish general explanation faithfulness.

## Likely reviewer challenge and safe answer

**Question:** Why call this attribution if it lacks formal additive guarantees such as SHAP?

**Safe answer:** The paper uses the narrower term “project-specific, model-informed local feature-ranking heuristic.” It orders four explicitly defined diagnostics; it does not claim Shapley values, causal explanations or exact decomposition. Its disclosed empirical check is limited to six in-sample neutralization cases.
