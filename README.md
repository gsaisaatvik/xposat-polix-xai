# An Explainable AI Framework for Analysis of X-Ray Polarimetry Data from XPoSat (v2.0)

A modern full-stack research portal and scientific analysis system for explainable analysis of XPoSat POLIX Level-2 observations. The system couples unsupervised machine learning, model-specific explainable AI (XAI), and physical polarimetry diagnostics with an interactive Vue 3 scientific dashboard.

---

## 🛰️ Project Overview

This project provides an end-to-end scientific pipeline and modern portal that:

- **Extracts engineered Matrix-C features** (15 physical and spectral dimensions) from POLIX Level-2 FITS observations.
- **Screens unusual observations** using an unsupervised machine learning consensus (PCA + K-Means + Isolation Forest).
- **Explains model decisions** via an observation-specific XAI framework directly tied to the deployed model components (no SHAP).
- **Fits POLIX WeightedRoll modulation curves** using weighted least-squares second-harmonic modeling.
- **Compares observations against empirical blank-sky baselines** for background-relative modulation diagnostics.
- **Reports polarization-degree (PD) sensitivity proxies** under assumed modulation factors with strict scientific boundaries.
- **Provides an interactive research interface** featuring a guided mission story, interactive formula boards, dynamic SVG instrumentation diagrams, and an upload/inspection workspace.
- **Exports combined ML + XAI + Polarimetry results** as downloadable CSV packages with generated diagnostic plots.

---

## ⚡ Key Features

### Machine Learning & XAI
- **Principal Component Analysis (PCA)**: Dimensionality reduction and projection of observation feature vectors.
- **K-Means Clustering**: Neighborhood structuring and centroid distance tracking across observations.
- **Isolation Forest**: Unsupervised anomaly screening with fixed contamination baselines.
- **Model-Specific Explainable AI (No SHAP)**: Combines PCA separation, K-Means centroid distance, Isolation Forest occlusion, and standardized Z-scores into normalized local feature attributions.

### Physical Polarimetry Diagnostics
- **WeightedRoll Modulation Curve Fitting**: Second-harmonic sinusoidal regression ($y(\phi) = C + Q\cos(2\phi) + U\sin(2\phi)$).
- **Raw Modulation & Phase Estimation**: Diagnostic modulation percentage and phase angles.
- **Blank-Sky Baseline Comparison**: Evaluates observations against empirical non-source scatter.
- **Q/U Modulation Vector Diagnostics**: Orthogonal harmonic component analysis.
- **PD Sensitivity Proxies**: Evaluates candidate sensitivity across assumed modulation factors ($\mu$).

### Modern Web Portal (v2.0)
- **Interactive Vue 3 Frontend**: Single-page application built with TypeScript, Vite, and Pinia state management.
- **Interactive Scientific Charts**: Responsive, accessible data visualizations powered by Apache ECharts.
- **Study Archive Explorer**: Instant inspection of the 25 validated study observations and 100-seed stability metrics.
- **Live Analysis Studio**: Supports raw Level-2 archives (`.zip`, `.tgz`, `.tar.gz`) and precomputed Matrix-C CSV tables.
- **Evidence Lab**: Step-by-step formula boards, calculation cards, and scientific provenance tracking.

---

## 📁 Repository Structure

```text
xposat-polix-xai/
│
├── frontend/                   # Vue 3 + TypeScript + Vite web portal
│   ├── src/
│   │   ├── components/         # Interactive diagrams, ECharts, and UI modules
│   │   ├── views/              # Mission, Method, Data, Learn, Archive, Analyze views
│   │   ├── stores/             # Pinia analysis and UI state management
│   │   └── services/           # Backend API integration client
│   ├── index.html
│   ├── package.json
│   └── vite.config.ts          # Vite configuration with API reverse proxy
│
├── backend/                    # Python scientific backend & REST API
│   ├── app.py                  # Standalone Flask REST API server (port 5001)
│   ├── feature_extractor.py    # Matrix-C 15-feature extraction from Level-2 FITS files
│   ├── model_service.py        # Unsupervised XAI (Isolation Forest + PCA + KMeans)
│   ├── polarization_service.py # WeightedRoll modulation curve analysis
│   ├── visualization_service.py# Batch and per-observation diagnostic plot generation
│   ├── result_exporter.py      # Combines ML, XAI, and polarimetry into CSV reports
│   ├── model/                  # Frozen trained Matrix-C model artifact (.pkl)
│   ├── config/                 # Observation metadata and polarimetry configurations
│   ├── data/                   # Reproduction benchmarks and seed stability datasets
│   ├── runtime/                # Transient session uploads and generated plot storage
│   └── requirements.txt        # Python backend dependencies
│
├── .gitignore                  # Git ignore rules for node, python, & large archives
└── README.md                   # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Node.js 18+ and `pnpm` (or `npm`)

### 1. Clone the Repository
```bash
git clone -b version2 https://github.com/gsaisaatvik/xposat-polix-xai.git
cd xposat-polix-xai
```

### 2. Start the Backend API
In your terminal:
```bash
cd backend
python -m venv venv

# Windows
.\venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt
python app.py
```
The scientific API service will start at `http://127.0.0.1:5001` (Health check: `http://127.0.0.1:5001/api/health`).

### 3. Start the Frontend Application
In a separate terminal window:
```bash
cd frontend
pnpm install   # or npm install
pnpm run dev   # or npm run dev
```
Open your browser at:
```text
http://127.0.0.1:5173/
```

---

## 📥 Supported Inputs

1. **Compressed POLIX Level-2 Archives**:
   - Formats: `.zip`, `.tgz`, `.tar.gz`, `.tar`
   - Accepts single-observation or multi-observation packages containing standard POLIX Level-2 FITS files (Tier 1A, Tier 1B, and Tier 2 products).
2. **Precomputed Feature Tables**:
   - Formats: Compatible Matrix-C `.csv` files containing the 15 standardized engineered features.

---

## 🔬 Scientific Workflow

```text
POLIX Level-2 Archive (.tgz / .zip)
                │
                ▼
      Feature Extraction
   (15-Feature Matrix-C Pipeline)
                │
                ▼
       Unsupervised ML Screening
   (Isolation Forest + PCA + K-Means)
                │
                ▼
       Explainable AI (XAI)
   (Model-Specific Feature Attribution)
                │
                ▼
      WeightedRoll Analysis
   (Sinusoidal Modulation Curve Fitting)
                │
                ▼
  Empirical Blank-Sky Comparison
   (Background-Relative Q/U Diagnostics)
                │
                ▼
    Physical Polarimetry Diagnostics
   (Modulation Factor & PD Sensitivity Proxy)
                │
                ▼
     Combined Scientific Report
 (Interactive UI + Diagnostic Plots + CSV Export)
```

---

## 📊 Dataset Used During Development

The framework was developed and validated on **25 XPoSat POLIX Level-2 observations**:

| Observation Type | Count | Description |
| :--- | :---: | :--- |
| **Blank-sky observations** | 15 | Empirical reference background observations (C24 cycle) |
| **Source observations** | 10 | Target observations (Crab Nebula/Pulsar, Sco X-1, etc.) |
| **Total** | **25** | Complete study archive |

*Note: Raw observational FITS datasets are archived by ISRO/RRI and are not hosted in this repository.*

---

## 🧠 Explainable AI Strategy

This project intentionally avoids black-box post-hoc explainers like SHAP, which can be computationally prohibitive on astronomical arrays and lack direct coupling with unsupervised anomaly models.

Instead, the XAI layer directly decomposes the model's geometry for each observation:
1. **PCA Projection Separation**: Measures how features shift the observation along dominant variance axes.
2. **K-Means Centroid Distance**: Quantifies feature-wise squared deviations from the assigned cluster center.
3. **Isolation Forest Occlusion**: Evaluates anomaly score shift when individual features are neutralized.
4. **Standardized Deviation**: Archive-relative Z-score abnormality.

The composite heuristic ranking highlights which physical features drove the screening decision without modifying or retraining the pipeline.

---

## ⚠️ Scientific Limitations & Boundaries

The application enforces strict diagnostic boundaries:
- **No Automated Astrophysical Discovery**: The system prioritizes candidates for inspection relative to archive baselines; it does not confirm physical anomalies.
- **Decoupled Architecture**: WeightedRoll modulation curve analysis is kept independent from unsupervised feature screening.
- **Sensitivity Proxies, Not Calibrated PD/PA**: Displayed values are diagnostic sensitivity proxies computed under assumed modulation scenarios. They do not constitute official background-subtracted polarization degrees or sky position angles, which remain the purview of the ISRO instrument science team.

---

## 🛠️ Technologies Used

### Backend
- **Python 3.10+**
- **Flask** (REST API)
- **Astropy** (FITS parsing and astronomical headers)
- **NumPy & Pandas** (Vectorized scientific computing and data wrangling)
- **Scikit-learn** (PCA, K-Means, Isolation Forest)
- **Matplotlib** (Scientific plot generation)
- **Joblib** (Model serialization)

### Frontend
- **Vue 3** (Single-File Components)
- **TypeScript** (Strict type safety)
- **Vite** (Next-generation frontend tooling)
- **Pinia** (Centralized reactive state store)
- **Vue Router 4** (Client-side routing)
- **Apache ECharts** (Interactive scientific visualization)
- **Lucide Icons** (Clean iconography)

---

## 📋 Project Status

**Current Status: Completed (Version 2.0)**

- Feature Engineering & FITS Extraction ✅
- Unsupervised Consensus Machine Learning ✅
- Model-Specific Explainable AI (No SHAP) ✅
- Physical Polarimetry Diagnostics & Modulation Fitting ✅
- Modern Vue 3 + TypeScript Web Portal ✅
- RESTful Flask API Backend ✅
- Full 25-Observation Validation & Seed Stability Audit ✅
- Single-Navbar Layout & Clean Repository Architecture ✅

---

## 📜 License

This repository is maintained for academic and scientific research purposes.