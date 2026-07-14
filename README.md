\# An Explainable AI Framework for Analysis of X-Ray Polarimetry Data from XPoSat



A Flask-based analysis framework for POLIX Level-2 observations.



\## Main Functions



\- Extracts Matrix C features from POLIX Level-2 FITS archives

\- Detects unusual observations using PCA, KMeans and Isolation Forest

\- Explains model results using model-specific feature contributions

\- Fits WeightedRoll modulation curves

\- Compares source observations against an empirical blank-sky baseline

\- Reports PD sensitivity proxies without claiming final calibrated PD/PA

\- Exports combined results as CSV



\## Dataset Used During Development



The project was developed and tested using 25 POLIX Level-2 observations:



\- 10 source observations

\- 15 blank-sky observations



Raw FITS archives are not included in this repository.



\## Installation



```powershell

python -m venv venv

.\\venv\\Scripts\\activate

pip install -r requirements.txt

Run the Application
python app.py

Open:

http://127.0.0.1:5000

Supported Inputs
Raw POLIX Level-2 .zip
.tgz
.tar.gz
Pre-extracted Matrix C .csv
Scientific Limitation

The displayed polarization-degree values are sensitivity proxies based on assumed modulation factors.

The application does not claim:

final calibrated polarization degree,
official polarization angle,
or astrophysical discovery.
Repository Structure
feature_extractor.py — Matrix C feature extraction
model_service.py — unsupervised prediction and XAI
polarization_service.py — WeightedRoll diagnostics
visualization_service.py — result plots
result_exporter.py — downloadable CSV
config/ — metadata and polarimetry configuration
model/ — saved deployed model
templates/ — Flask/Jinja pages