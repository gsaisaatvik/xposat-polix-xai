# XPoSat POLIX Explainable AI Research Portal (v2.0)

An Explainable AI (XAI) and unsupervised anomaly detection framework for X-Ray polarimetry observations from the **POLIX** instrument onboard ISRO's **XPoSat** (X-ray Polarimeter Satellite) mission.

---

## 🏛️ System Architecture

The repository is organized into distinct, clean workspaces:

```text
polix_xai_webapp/
├── frontend/                   # Modern Vue 3 + TypeScript + Vite portal
│   ├── src/
│   │   ├── components/         # Interactive diagrams, charts, and shell components
│   │   ├── views/              # Mission, Method, Data, Learn, Archive, Analyze views
│   │   ├── stores/             # Pinia analysis and UI state
│   │   └── services/           # Backend API integration client
│   ├── index.html
│   ├── package.json
│   └── vite.config.ts          # Dev server proxying /api and /generated to port 5001
│
├── backend/                    # Python Flask scientific backend & REST API
│   ├── app.py                  # Standalone REST API server (port 5001)
│   ├── feature_extractor.py    # Extracts 15 Matrix-C features from Level-2 FITS files
│   ├── model_service.py        # Unsupervised XAI (Isolation Forest + PCA + KMeans)
│   ├── polarization_service.py # WeightedRoll modulation curve analysis
│   ├── visualization_service.py# Generates anomaly ranking, PCA, and per-obs XAI plots
│   ├── result_exporter.py      # Exports combined results to CSV
│   ├── model/                  # Frozen trained Matrix-C model artifact (.pkl)
│   ├── config/                 # Metadata and polarimetry configuration JSONs
│   ├── data/                   # Seed stability and deployed reproduction benchmarks
│   ├── runtime/                # Transient session uploads and generated plot storage
│   └── requirements.txt        # Backend dependencies
│
├── docs/                       # Research documentation, audits, and literature (local)
│   ├── guides/                 # Implementation plan, content map, run & test guide
│   ├── research_paper_ieee/    # Research paper draft, figures, and supplementary scripts
│   ├── reviews_and_presentations/ # PS1 Review presentations and reference reports
│   ├── audits/                 # Contradiction, figure, and scientific audits
│   ├── source_material/        # Official POLIX handbooks and payload references
│   └── tools/                  # Asset preparation scripts
│
├── README.md                   # Project overview & documentation
└── .gitignore                  # Git ignore rules for node, python, & large archives
```

---

## 🚀 Quickstart

### Prerequisites
- Python 3.10+
- Node.js 18+ and `pnpm` (or `npm`)

### 1. Start Scientific Backend API
```powershell
cd backend
pip install -r requirements.txt
python app.py
```
The API server starts at `http://127.0.0.1:5001` (Health check: `http://127.0.0.1:5001/api/health`).

### 2. Start Frontend Application
In a separate terminal:
```powershell
cd frontend
pnpm install
pnpm run dev
```
Open your browser at `http://127.0.0.1:5173/`.

---

## 🛰️ 25 Observation Archives & Local Paths

### Exact Local Storage Path
The 25 primary Level-2 `.tgz` observation archives are stored locally at:
```text
D:\ISROtrial\Polix_L2_full_archive\data_raw\
```

### Observation Inventory
1. **15 C24 Blank-Sky Observations** (Instrument & background modulation baselines):
   - `X01_POL_C24_0001_2024_L2_V1P1.tgz`
   - `X01_POL_C24_0002_2024_L2_V1P1.tgz`
   - `X01_POL_C24_0007_2024_L2_V1P1.tgz`
   - `X01_POL_C24_0008_2024_L2_V1P1.tgz`
   - `X01_POL_C24_0009_2024_L2_V1P1.tgz`
   - `X01_POL_C24_0010_2024_L2_V1P1.tgz`
   - `X01_POL_C24_0014_2024_L2_V1P1.tgz`
   - `X01_POL_C24_0015_2024_L2_V1P1.tgz`
   - `X01_POL_C24_0018_2024_L2_V1P1.tgz`
   - `X01_POL_C24_0019_2024_L2_V1P1.tgz`
   - `X01_POL_C24_0020_2024_L2_V1P1.tgz`
   - `X01_POL_C24_0021_2024_L2_V1P1.tgz`
   - `X01_POL_C24_0022_2024_L2_V1P1.tgz`
   - `X01_POL_C24_0023_2024_L2_V1P1.tgz`
   - `X01_POL_C24_0024_2024_L2_V1P1.tgz`
   - `X01_POL_C24_0026_2024_L2_V1P1.tgz`
2. **10 Source Observations** (Astrophysical targets):
   - `X01_POL_G01_0002_2024_L2_V1P1.tgz` (Crab Nebula / Pulsar)
   - `X01_POL_G01_0003_2024_L2_V1P1.tgz`
   - `X01_POL_G01_0004_2024_L2_V1P1.tgz`
   - `X01_POL_G01_0005_2024_L2_V1P1.tgz`
   - `X01_POL_G01_0006_2024_L2_V1P1.tgz`
   - `X01_POL_P01_0005_2024_L2_V1P1.tgz` (Sco X-1)
   - `X01_POL_T24_0001_2024_L2_V1P1.tgz`
   - `X01_POL_T24_0002_2024_L2_V1P1.tgz`
   - `X01_POL_T24_0007_2024_L2_V1P1.tgz`

---

## 📦 Additional Test Packages (Outside the 25 Raw Files)

For regression testing without unpacking all 25 raw archives, convenience zip packages are located at:

1. **`D:\polix_xai_webapp\blank_sky_test.zip`** (24.3 MB):
   - Contains 2 blank-sky observations (`C24_0001` and `C24_0002`) for fast smoke testing of the extraction pipeline.
2. **`D:\polix_xai_webapp\multi_obs_test.zip`** (118 MB):
   - Contains a multi-target subset of observations for batch analysis testing.
3. **`D:\polix_xai_webapp\all_25_test.zip`** (474 MB):
   - All 25 observations packaged into a single composite zip upload.
   *(Note: Excluded from Git tracking via `.gitignore` to stay well within GitHub repository limits).*

---

## 🔬 Scientific Boundaries

1. **Unsupervised Screening**: The 15-feature Matrix-C model prioritizes observations for human inspection relative to the archive baseline; it does not claim automated astrophysical anomaly discovery.
2. **Harmonic Fit Separation**: WeightedRoll modulation curve analysis ($y(\phi) = C + Q\cos(2\phi) + U\sin(2\phi)$) is kept strictly decoupled from unsupervised screening.
3. **Calibrated Polarimetry**: Polarization Degree (PD) proxy sensitivity estimates are diagnostic indicators only; final polarization detection and official Sky Position Angle (PA) require expert background subtraction and ISRO instrument team calibration.