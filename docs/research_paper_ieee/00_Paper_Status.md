# Paper Status

## Working title

**Product-Aware Explainable Anomaly Screening with Blank-Sky Modulation Diagnostics for XPoSat POLIX Level-2 Observations**

College project title: *An Explainable AI Framework for Analysis of X-Ray Polarimetry Data from XPoSat*.

## Current status

**Draft 1 — evidence-audited working draft; not publication-ready.**

Data freeze: **2026-07-27**.

The research-paper workspace is separate from the completed project. No source file, notebook, report, model, figure, result, or dataset outside `research_paper_ieee` was modified.

## Completed

- Located and inspected the reviewed report, official POLIX Level-2 handbook, Review-I literature material, notebooks 01–11, feature matrices, saved model, ML/XAI results, faithfulness outputs, physical-polarimetry results, blank-sky results, figures, Flask source, and configuration.
- Reproduced the deployed Matrix-C model output: 25 observations, 21 Normal, and 4 anomaly candidates, with zero score or prediction differences from the saved artifact.
- Executed 100-seed Isolation Forest stability, contamination sensitivity, leave-one-out jackknife, Matrix A/B/C feature-tier ablation, separate WR diagnostic comparison, rank agreement, and XAI faithfulness reproduction.
- Verified the official XPoSat acknowledgment wording from the current ISSDC/PRADAN page.
- Visually inspected the official 67-page `POLIX_User_Handbook.pdf`, including the product descriptions and background-modulation limitations.
- Prepared an IEEE-style Markdown draft, LaTeX draft, BibTeX file, claim audit, literature audit, figure/table plan, reviewer-risk checklist, AI-use disclosure, and reproducibility checklist.
- Accepted the exact versioned-function XAI audit as authoritative for Sco X-1 and promoted the paper workspace from Draft 0 to Draft 1 without rerunning the project or adding experiments.

## Material audit corrections to the reviewed report

1. The deployed model artifact and `model_service.py` do not contain or apply a median imputer. The frozen Matrix-C table has zero missing values, so no imputation occurred for the reported 25-observation run.
2. The 13-observation blank-sky Q/U baseline uses fits labeled `acceptable`, which corresponds to reduced chi-square ≤ 2.0. It does not use every fit with reduced chi-square ≤ 5.0.
3. The exact imported `model_service.py` audit establishes the deployed Sco X-1 ranking as `t1A_energy_peak_channel` (2.454499), `t1A_energy_weighted_mean_channel` (2.207369), and `t1A_energy_channel_entropy` (1.813968). The historical entropy-first narrative is not reproducible from a located versioned artifact and is superseded for Draft 1.
4. Several physical-polarimetry tables carry the exploratory six-candidate consensus flag. These must not be read as the deployed four-candidate Matrix-C classification.

## Main verified result

The fixed deployed model flags four archive-relative candidates. Three of these are flagged in all 100 Isolation Forest seed repetitions; the fourth, Blank Sky-5, is flagged in 29% of seed repetitions. All ten source observations remain within the empirical blank-sky scalar raw-modulation range. Sco X-1 is statistically unusual in Matrix-C energy features while its modulation vector is within blank-sky scatter. This is direct evidence that statistical unusualness and polarization-like modulation evidence are not equivalent.

## Draft size

- Markdown manuscript: **4,518 words including the manually formatted reference list; 4,092 words before references**.
- Abstract: **219 words**.
- Estimated IEEE two-column length: **approximately 8–10 pages** with the current five tables, references, and a compact selection of three or four figures. The exact length depends on the target conference template and figure selection.
- No final PDF was generated.

## Blocking items before submission

- Author names, affiliations, author order, corresponding author, venue, page limit, and conference template version.
- POLIX/domain-expert review of feature semantics, candidate interpretation, background treatment, and the use of source light-curve and PHA-derived features given handbook cautions.
- Confirmation that the local handbook is the version the target venue permits authors to cite or distribute.
- Full-text review of Saini *et al.* and Yepmo *et al.*, or removal/narrowing of claims that depend on them.
- Regeneration of paper-specific, vector-quality figures from the verified CSVs and author inspection of every plotted number.
- External validation on future POLIX releases or an independent archive; the current analysis is retrospective and archive-specific.
- End-to-end verification of the web result-download path, which the reviewed report marks as pending.
- Venue-specific AI-use, data-use, and ethics disclosure review.

## Prohibited final label

Do not describe this manuscript as “publication-ready” until every number, citation, figure, claim, and venue requirement has been reviewed by the authors and relevant domain expert.
