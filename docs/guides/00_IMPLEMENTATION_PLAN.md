# XPoSat POLIX Research Portal - Implementation Plan

## Goal

Build a modern, researcher-facing Vue application around the completed POLIX analysis system without changing the trained model, feature definitions, scientific calculations, candidate results, or original Flask application.

The product will combine two experiences:

1. an accessible mission-and-method learning experience explaining XPoSat, POLIX, the Level-2 products, the 15-feature representation, unsupervised screening, local explanation, and the independent WeightedRoll branch; and
2. a scientific analysis console that accepts the same supported archives and Matrix-C CSV files and presents the existing backend results clearly.

The design may learn from the visual hierarchy and interactive storytelling of NASA Science, NASA Space Place, and ViewSpace, but it will not copy their layouts, text, images, trademarks, or interaction code.

## Protected boundary

The following existing files remain unchanged:

- `app.py`
- `feature_extractor.py`
- `model_service.py`
- `polarization_service.py`
- `visualization_service.py`
- `result_exporter.py`
- `model/polix_v2_matrixC_unsupervised_xai_model.pkl`
- `config/observation_metadata.json`
- `config/polarimetry_config.json`
- all original notebooks, data archives, CSVs, reports, and research-paper files

The new application will import the existing services through a thin API adapter. The adapter changes transport and presentation only; it does not retrain, refit, tune, or redefine the scientific pipeline.

## Source hierarchy for website content

1. The final research paper controls the approved project story and bounded findings.
2. The deployed code, saved PKL, and controlling CSVs control implementation details and numbers.
3. The reviewed final report supplies expanded project explanation where it agrees with the controlling artifacts.
4. Official mission/payload documents may support basic XPoSat and POLIX education, with source credits.
5. The friend repository is a structural reference only; its scientific wording and API changes are not authoritative.
6. NASA and ViewSpace pages are design references only.

## Confirmed archive locations

- 25 individual Level-2 packages: `D:\ISROtrial\Polix_L2_full_archive\data_raw\`
- Combined 25-observation upload: `D:\polix_xai_webapp\all_25_test.zip`
- Blank-sky test package: `D:\polix_xai_webapp\blank_sky_test.zip`
- Multi-observation test package: `D:\polix_xai_webapp\multi_obs_test.zip`

The 25 individual packages consist of 15 C24 blank-sky observations and 10 source observations. They will remain in place.

## Technology stack

### Frontend

- Vue 3 Single-File Components
- Vite
- TypeScript
- Vue Router
- Pinia for analysis-session state
- Apache ECharts for accessible interactive scientific charts
- Lucide Vue icons
- CSS design tokens and responsive component styles

Vue still renders HTML and CSS in the browser; the important change is from static pages to a structured component application.

### Scientific backend

- Existing Python/Flask services
- Astropy, NumPy, Pandas, scikit-learn, Matplotlib, joblib
- Saved Matrix-C model artifact

### Integration

- New additive Flask API adapter at `web_v2/api/`
- Vite development proxy from `/api` and `/generated` to port 5001
- No CORS dependency for local development
- Production build can be served by any static server while the API runs separately

## Proposed repository structure

```text
web_v2/
|-- README.md
|-- docs/
|   |-- 00_IMPLEMENTATION_PLAN.md
|   |-- 01_SCIENTIFIC_CONTENT_MAP.md
|   |-- 02_RUN_AND_TEST_GUIDE.md
|   `-- 03_ASSET_CREDITS.md
|-- api/
|   |-- app.py
|   |-- contracts.py
|   `-- requirements.txt
|-- frontend/
|   |-- package.json
|   |-- vite.config.ts
|   |-- tsconfig.json
|   |-- index.html
|   |-- public/
|   `-- src/
|       |-- main.ts
|       |-- App.vue
|       |-- router/
|       |-- stores/
|       |-- services/
|       |-- types/
|       |-- composables/
|       |-- assets/
|       |-- styles/
|       |-- components/
|       |   |-- shell/
|       |   |-- mission/
|       |   |-- analysis/
|       |   |-- charts/
|       |   `-- common/
|       `-- views/
|           |-- HomeView.vue
|           |-- MissionView.vue
|           |-- MethodView.vue
|           |-- AnalyzeView.vue
|           |-- ResultsView.vue
|           |-- ResearchView.vue
|           `-- LearnView.vue
`-- tests/
```

## Information architecture

### Home

- immersive, original space visual built from CSS/SVG
- one-sentence project purpose
- verified dataset counters: 25 observations, 10 source, 15 blank sky, 15 Matrix-C features
- clear paths to “Explore the mission” and “Analyze an observation”
- explicit boundary: screening candidates are inspection priorities, not confirmed anomalies

### Mission

- What XPoSat studies
- What POLIX measures operationally
- Level-2 product-family explorer
- interactive product-to-feature provenance map
- image/source credit panel

### Method

- accurate two-branch architecture
- Matrix C to StandardScaler, then PCA/KMeans descriptive geometry and Isolation Forest screening
- four-component local evidence ranking
- separate WeightedRoll harmonic branch
- expandable definitions and safe-interpretation cards

### Analyze

- archive/CSV mode selector
- drag-and-drop input with validation
- file summary and privacy notice
- real processing stages reflecting actual backend operations
- error states that preserve technical details without confusing the user

### Results

- overview counts and fixed labels
- sortable observation table
- interactive PCA scatter and Isolation Forest ranking
- per-observation feature/product-family explanation
- separate harmonic diagnostic panel
- result CSV download
- visible scientific boundaries near each relevant result

### Research

- final paper problem, method, and bounded findings
- four fixed candidates, three-seed-stable core, two cross-tier persistent cases, and six exploratory perturbation cases kept distinct
- limitations and reproducibility notes
- no calibrated PD/PA claim

### Learn

- plain-language explainers for PCA, KMeans, Isolation Forest, XAI, and harmonic fitting
- glossary and “what this result does not mean” prompts
- progressive disclosure suitable for students and domain reviewers

## Visual direction

- deep near-black/navy background with warm solar amber and restrained cyan accents
- wide editorial sections and strong typographic hierarchy rather than a dense admin dashboard
- scientific plots on light-neutral chart surfaces for legibility
- original animated polarization-wave and orbit motifs with reduced-motion support
- scroll-driven narrative transitions that do not block navigation
- cards used only where they represent a real object or decision
- WCAG-aware contrast, keyboard access, focus states, alt text, and non-colour status cues

## Scientific presentation rules

- Only Isolation Forest sets the deployed candidate label.
- PCA and KMeans are descriptive context.
- The four XAI components are explanation components, not four models.
- XAI is described as a project-specific, model-informed local feature-ranking heuristic.
- WeightedRoll is excluded from Matrix C and appears in a separate panel.
- Harmonic coefficients are not presented as calibrated Stokes parameters.
- Raw modulation is not polarization degree.
- Fitted phase is not official sky polarization angle.
- The empirical blank-sky rule is descriptive, not a confidence region or significance test.
- The fixed four, seed-stable three, cross-tier two, and exploratory six remain separate.

## API contract

The additive API adapter will expose:

- `GET /api/health`
- `GET /api/project`
- `POST /api/analyze`
- `GET /api/download/<session>/<filename>`
- `GET /generated/<session>/<plot>`

`POST /api/analyze` will call the existing extractor, predictor, polarimetry service, visualization service, and exporter. Its response will contain the same predictions and values already produced by the current application, serialized for Vue.

## How it will run

Terminal 1 - scientific API:

```powershell
cd D:\polix_xai_webapp
python web_v2\api\app.py
```

Terminal 2 - Vue frontend:

```powershell
cd D:\polix_xai_webapp\web_v2\frontend
npm install
npm run dev
```

Open `http://127.0.0.1:5173`. Vite proxies API and generated-plot requests to `http://127.0.0.1:5001`.

The existing application remains independently runnable at port 5000 using `python app.py`.

## Implementation phases

### Phase A - Freeze and contracts

- hash protected scientific files
- record current response schema
- create TypeScript API types
- implement health and analysis adapter without changing scientific modules

### Phase B - Design system and public experience

- create tokens, typography, responsive shell, navigation, hero, mission/product explorer, and method story
- create original SVG/CSS visual assets
- add content credits and claim boundaries

### Phase C - Analysis console

- implement uploads, validation, progress, cancellation-safe state, and API error handling
- implement results routing and persisted in-memory session state

### Phase D - Scientific visualizations

- interactive PCA and score-ranking charts
- per-observation XAI evidence chart
- harmonic result cards and independent-branch comparison
- accessible tabular fallbacks and download flow

### Phase E - Verification

- build/type-check/lint frontend
- test health endpoint and CSV/raw uploads
- compare API results with the existing backend for the same input
- run the combined 25-observation package only as an inference regression test
- test desktop, tablet, mobile, keyboard, reduced-motion, and failure states
- confirm hashes of protected files remain unchanged

## Acceptance criteria

- No protected backend/model/data file changes.
- Existing fixed scientific results are unchanged.
- All 25 archives remain traceable at their current location.
- Vue application is componentized; no monolithic `App.vue`.
- Public education and scientific analysis are clearly separated.
- Every displayed numerical result comes from the API response, not hard-coded mock data.
- The four scientific distinctions and all claim boundaries remain visible.
- Frontend and backend can be started with documented commands.
- Production build succeeds and the main routes pass browser smoke tests.

