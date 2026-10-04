# Scientific content map

## Central problem

A POLIX Level-2 observation is delivered through heterogeneous product families rather than one directly comparable observation vector. The implemented system summarizes selected product behaviour into a 15-feature, observation-level Matrix-C row, screens that row relative to the project archive, and traces local unusualness evidence back to features and product families.

## Two independent branches

### Matrix-C screening branch

`Level-2 products → 15 Matrix-C summaries → saved StandardScaler → PCA/KMeans context + Isolation Forest label → four-component local evidence ranking`

- Isolation Forest alone supplies the fixed Normal/Anomaly label.
- PCA and KMeans provide descriptive geometry.
- The local score combines normalized PCA, KMeans, Isolation Forest occlusion, and absolute standardized-value components.
- The score is a project-specific, model-informed local feature-ranking heuristic. It is not SHAP, probability, causal attribution, or a calibrated physical quantity.

### Independent WeightedRoll branch

`Delivered WeightedRoll curve → y(φ)=C+Q cos(2φ)+U sin(2φ) → raw harmonic summaries → declared empirical blank-sky reference rule`

- WeightedRoll is excluded from Matrix C.
- The fit coefficients are harmonic coefficients, not unqualified calibrated Stokes parameters.
- Raw modulation is not calibrated polarization degree.
- Fitted modulation phase is not official sky polarization angle.

## Study result shown on the website

- Dataset: 25 observations; 10 project-labelled source and 15 project-labelled blank sky.
- Fixed deployed result: 21 Normal and four inspection candidates.
- Fixed candidates: Blank Sky-13, Sco X-1, Her X-1, and Blank Sky-5.
- Seed test: Blank Sky-13, Sco X-1, and Her X-1 were selected in 100/100 tested seeds; Blank Sky-5 in 29/100.
- Cross-tier persistence: Sco X-1 and Blank Sky-13 persist across Matrix A/B/C. This is distinct from seed stability.
- Six exploratory XAI/neutralization cases are distinct from the four fixed candidates.
- Sco X-1 local order: energy peak channel, energy weighted mean channel, energy channel entropy.
- Central result: statistical unusualness and modulation-like harmonic behaviour answer different diagnostic questions within the project archive.

## How a researcher can use it

1. Load a compatible Level-2 observation package.
2. Generate traceable product-aware summaries using the existing extractor.
3. Review the saved-model archive-relative screening output.
4. Inspect the local feature and product-family ranking.
5. Return to the implicated original product family for scientific inspection.
6. Compare the separate WeightedRoll harmonic diagnostic when that product is available.
7. Escalate the observation for instrument, calibration, or domain review if warranted.

The framework organizes and prioritizes inspection; it does not automate scientific discovery.

## Content provenance

The website values are sourced from the frozen project services, saved model, controlling result CSVs, and accepted audits. Uploaded architecture artwork and external web designs were used only as design context, never as scientific evidence. The interface and visual assets in this workspace are original code/CSS/SVG work.

