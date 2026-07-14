# An Explainable AI Framework for Analysis of X-Ray Polarimetry Data from XPoSat

A Flask-based web application for explainable analysis of **XPoSat POLIX Level-2** observations. The system combines unsupervised machine learning, explainable AI (XAI), and physical polarimetry diagnostics to analyze X-ray polarimetry data while preserving scientifically accurate interpretation.

---

## Project Overview

This project provides an end-to-end pipeline that:

- Extracts engineered Matrix-C features from POLIX Level-2 FITS observations
- Detects unusual observations using unsupervised machine learning
- Explains model decisions using a custom model-specific XAI framework
- Fits POLIX WeightedRoll modulation curves
- Compares observations against an empirical blank-sky modulation baseline
- Computes background-relative modulation diagnostics
- Reports polarization-degree (PD) sensitivity proxies under assumed modulation factors
- Exports combined ML + XAI + Polarimetry results as downloadable CSV files

---

## Key Features

### Machine Learning

- Principal Component Analysis (PCA)
- K-Means Clustering
- Isolation Forest
- Consensus anomaly detection
- Model-specific explainable AI (No SHAP)

### Physical Polarimetry

- WeightedRoll modulation curve fitting
- Least-squares sinusoidal fitting
- Raw modulation measurement
- Modulation phase estimation
- Blank-sky baseline comparison
- Q/U modulation vector diagnostics
- PD sensitivity proxy calculation
- Automatic scientific confidence reporting

### Web Application

- Upload compressed POLIX Level-2 archives
- Upload precomputed Matrix-C CSV files
- Interactive XAI visualizations
- Physical polarimetry diagnostics
- Downloadable analysis results
- Human-readable scientific interpretations

---

## Dataset Used During Development

The framework was developed and validated using **25 XPoSat POLIX Level-2 observations**.

| Observation Type | Count |
|------------------|------:|
| Source observations | 10 |
| Blank-sky observations | 15 |
| Total observations | **25** |

The original FITS data are **not included** in this repository.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/gsaisaatvik/xposat-polix-xai.git
cd xposat-polix-xai
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

**Windows**

```powershell
.\venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## Supported Inputs

### Raw POLIX Level-2 Archives

- `.zip`
- `.tgz`
- `.tar.gz`

### Precomputed Features

- Matrix-C `.csv`

---

## Workflow

```text
POLIX Level-2 Archive
           │
           ▼
 Feature Extraction
(Matrix-C Engineering)
           │
           ▼
 Unsupervised ML
(PCA + KMeans + Isolation Forest)
           │
           ▼
 Explainable AI
(Model-specific feature attribution)
           │
           ▼
 WeightedRoll Analysis
(Modulation Curve Fitting)
           │
           ▼
 Blank-Sky Baseline Comparison
           │
           ▼
 Physical Polarimetry Diagnostics
           │
           ▼
 Combined Scientific Report
```

---

## Repository Structure

```
xposat-polix-xai/
│
├── app.py
├── feature_extractor.py
├── model_service.py
├── polarization_service.py
├── visualization_service.py
├── result_exporter.py
│
├── config/
│   ├── observation_metadata.json
│   └── polarimetry_config.json
│
├── model/
│   └── polix_v2_matrixC_unsupervised_xai_model.pkl
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── uploads/
├── static/
└── requirements.txt
```

---

## Explainable AI Strategy

This project intentionally **does not use SHAP**.

Instead, the XAI layer combines:

- PCA separation contribution
- K-Means centroid-distance contribution
- Isolation Forest contribution
- Standardized feature abnormality (Z-score)

This produces observation-specific explanations that are directly tied to the deployed unsupervised model.

---

## Scientific Notes

The physical polarimetry module reports:

- Raw modulation
- Fitted modulation phase
- Background-relative modulation
- Blank-sky comparison
- Q/U vector diagnostics
- PD sensitivity proxies

These are intended for **diagnostic interpretation** and **scientific exploration**.

---

## Scientific Limitations

The application **does not claim**:

- Final calibrated Polarization Degree (PD)
- Official Polarization Angle (PA)
- Astrophysical discovery
- Replacement of the official POLIX scientific analysis pipeline

Displayed PD values are **sensitivity proxies** computed under assumed modulation-factor scenarios and should not be interpreted as final calibrated astrophysical measurements.

---

## Technologies Used

- Python
- Flask
- Astropy
- NumPy
- Pandas
- SciPy
- Scikit-learn
- Matplotlib
- Jinja2

---

## Project Status

**Current Status:** Completed (Version 1.0)

- Feature Engineering ✅
- Unsupervised Machine Learning ✅
- Explainable AI ✅
- Physical Polarimetry Diagnostics ✅
- Flask Web Application ✅
- Full 25-observation Validation ✅
- CSV Export ✅

---

## License

This repository is intended for academic and research purposes.
