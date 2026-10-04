# Run and test guide

## Prerequisites

- Python environment capable of running the root project `requirements.txt`
- Node.js and `pnpm`
- Existing saved model and project services in `D:\polix_xai_webapp`

## Development run

From the project root, use two terminals.

```powershell
.\web_v2\start_api.ps1
```

```powershell
.\web_v2\start_frontend.ps1
```

Frontend: `http://127.0.0.1:5173/`

API: `http://127.0.0.1:5001/`

Vite proxies `/api` and `/generated` to the Python adapter.

## Production frontend build

```powershell
Set-Location D:\polix_xai_webapp\web_v2\frontend
pnpm run build
```

The compiled frontend is written to `web_v2\frontend\dist`. A production deployment still needs the Python API served by a production WSGI server and the frontend host configured to forward `/api` and `/generated` to it.

## Recommended demonstration

1. Open **Mission** and use the Product Lens to explain Products → Matrix C → Screen → Explain → Compare.
2. Open **Archive** and show that the fixed 25-observation study is separate from new uploads.
3. Select Sco X-1 and explain that its fixed label comes from Isolation Forest, while its local evidence ranking points back to energy/channel-space summaries.
4. Open **Evidence Lab** to demonstrate the actual formulas, tally checks, and implementation provenance.
5. Open **Analyze** and upload `blank_sky_test.zip` for a fast two-observation workflow test, or a selected original `.tgz` archive.
6. Review the PCA view, Isolation Forest ranking, local evidence, harmonic diagnostics, and exported CSV.

## Verified regression checks — 2026-10-04

### API health and saved archive

- `/api/health`: `ready`
- `/api/study-archive`: 25 observations
- Fixed candidates: 4
- Seed counts for the four highest saved candidates: 100/100, 100/100, 100/100, 29/100

### Matrix-C CSV upload

Input:

`D:\ISROtrial\Polix_L2_full_archive\final_project_outputs\02_feature_engineering\polix_matrix_v2_C_primary_plus_supporting.csv`

Result:

- Success: true
- Rows: 25
- Four candidates: Blank Sky-13, Sco X-1, Her X-1, Blank Sky-5
- Result CSV and summary plots generated in the isolated `web_v2\runtime` workspace

### Raw archive upload

Input: `D:\polix_xai_webapp\blank_sky_test.zip`

Result:

- Success: true
- Rows: 2
- Both rows screened
- Independent polarimetry/harmonic result attached for both rows

### Frontend

- TypeScript check and production build: passed
- Home, Archive, Mission Product Lens, Analyze, and Evidence Lab visually inspected
- Evidence Lab card navigation and provenance reveal: passed
- Browser upload of `blank_sky_test.zip` completed end to end and navigated to the results workspace
- Rendered live summary: 2 processed, 2 not selected, 0 inspection candidates, decision source Isolation Forest
- Browser console errors/warnings during inspected routes: none

## Environment warning

The current local Python process reports that the model was saved under scikit-learn 1.9.0 while the active interpreter has scikit-learn 1.6.1. The saved outputs were reproduced in the existing project audits, but production deployment should pin the model-training library version or use a documented compatible environment. This redesign does not change or resave the model.
