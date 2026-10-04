# NEPAL Part 02 - Code, CSV and Model Lineage

## Primary Matrix-C branch

```text
25 archived observation directories
        |
        v
Notebook 08 corrected product discovery and V2 extractor
        |
        +--> Matrix A: 8 features
        +--> Matrix B: 11 features
        +--> Matrix C: 15 features, 25 rows, zero missing values
        +--> WR: 6 separate diagnostic features
        |
        v
Notebook 10 Matrix-C fit and saved PKL
        |
        v
StandardScaler --> shared standardized feature rows
        |                 |                    |
        v                 v                    v
      PCA              KMeans          Isolation Forest
                                             |
                                             v
                              fixed Normal/candidate label
        |
        v
four-component local feature-ranking heuristic
```

The architecture is not a sequential PCA-to-KMeans-to-Isolation-Forest chain. PCA, KMeans and Isolation Forest operate on the standardized Matrix-C representation. Only `IsolationForest.predict` supplies the fixed label.

## Matrix identity and organization

Notebook 08 writes the final matrices at the archive root. Their organized copies under `final_project_outputs\02_feature_engineering` are byte-identical:

| Matrix | Rows | Features | Missing | SHA-256 |
|---|---:|---:|---:|---|
| A | 25 | 8 | 0 | `C9031C30...5ED6C4` |
| B | 25 | 11 | 0 | `21411E20...F723C8` |
| C | 25 | 15 | 0 | `3936E1B0...DB0FA` |
| WR | 25 | 6 | 0 | `B8A49EE9...811DB` |

The copy/organization operation itself is not documented in Notebooks 01–09, but the matching hashes verify content identity.

## Saved model and deployed code

| Artifact | Control role | SHA-256 |
|---|---|---|
| `polix_v2_matrixC_unsupervised_xai_model.pkl` | Frozen model package | `D8EFD73C...8C180D` |
| `model_service.py` | Prediction rule and deployed XAI function | `F749FFD0...C877` |
| `feature_extractor.py` | Deployed 15-feature schema and extraction | `45A9AE59...569CB` |
| Matrix-C CSV | Frozen input rows | `3936E1B0...DB0FA` |

The accepted XAI audit records Git commit `15628ee7cc434de9ba03caaae5dd115d8cd09f9a`. The code, model and Matrix-C hashes match that audit.

### Saved parameters

- `StandardScaler`; no imputer.
- PCA: two components, random state 42.
- KMeans: `k=5`, `n_init=20`, random state 42.
- Isolation Forest: 100 trees, contamination 0.16, random state 42.
- Fixed anomaly score: negative `score_samples`.
- Fixed label: `IsolationForest.predict` only.

The frozen KMeans cluster sizes are 1, 9, 10, 1 and 4. Sco X-1 and Blank Sky-13 occupy singleton clusters, so their assigned-centroid distances are zero.

## Exact XAI lineage

`model_service.py::PolixXAIPredictor.explain_one` computes four feature-wise components:

1. PCA separation contribution from the first two loadings and explained-variance ratios.
2. Squared distance from the assigned KMeans centroid.
3. Isolation Forest occlusion delta after setting one standardized feature to zero.
4. Absolute standardized feature value.

Each component vector is normalized within the observation by its maximum absolute value. Negative occlusion deltas are clipped to zero before combination. The four normalized vectors are summed with equal implicit weight. The result ranks features within one observation; it is not a calibrated cross-observation importance and does not decompose the Isolation Forest label.

The service returns the top five features and generates a deterministic Python-template sentence. No LLM generates the deployed sentence.

## Reproduction and robustness lineage

| Evidence | Controlling file | Boundary |
|---|---|---|
| Exact fixed scores and labels | `deployed_model_reproduction.csv` | Existing replay; zero score differences |
| Sco X-1 current XAI | `deployed_xai_exact_from_model_service.csv` | Current service function and saved PKL |
| Seed sensitivity | `isolation_seed_stability_summary.csv` | Algorithmic frequency, not probability |
| Contamination sensitivity | `contamination_candidate_stability.csv` | Threshold sensitivity over one ordering |
| Jackknife | `jackknife_observation_stability.csv` and `jackknife_run_summary.csv` | Retrospective influence, not future validation |
| A/B/C comparison | `matrix_ablation_summary.csv` | No Matrix-C superiority claim |
| Ranking agreement | `ranking_agreement.csv` and `ranking_metrics.csv` | Descriptive within-archive correlations |
| Six-case verdict | `faithfulness_verdict_reproduction.csv` | In-sample sign-only sanity check |

## Independent harmonic branch

```text
WeightedRoll_L2.fits: angle, total count rate, error
        |
        v
Notebook 11 weighted second-harmonic fit
        |
        +--> C, cosine coefficient, sine coefficient
        +--> raw modulation A/C
        +--> fitted modulation phase
        +--> reduced chi-square and project fit category
        |
        v
15 project-labelled blank skies
        |
        v
13 fits satisfying reduced chi-square <= 2
        |
        v
descriptive empirical blank-sky reference
```

This branch is not an input to the fixed Matrix-C label.

## Harmonic implementation split

Notebook 11 uses a matrix solve/inverse and relative-quadrature propagation for `A/C`; that propagation omits covariance between amplitude and fitted mean. The later `polarization_service.py` uses a pseudoinverse and a full three-parameter gradient, including cross-covariances.

Consequently:

- the saved Notebook-11 CSV controls reported project values;
- the service is a later non-identical implementation;
- uncertainty values must not be silently combined;
- detailed comparison belongs in supplementary material.

## Role and physical-table join rule

The physical tables contain an older `is_xai_consensus_anomaly` field for six exploratory cases. It is not the fixed deployed label. Any combined paper table must join physical values to `deployed_model_reproduction.csv` by the full `observation_id` and ignore the historical priority/consensus fields.

