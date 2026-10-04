# SRI LANKA Part 03 — Figure Quality Audit

## Generation controls

- Generator: `figure_generation/generate_phase4_figures.py`.
- Scientific fitting, retraining and threshold selection in the generator: None.
- PCA operation: transform only, using the saved scaler and PCA parameters. A manual parameter-based transform is asserted equal to the saved object’s `transform` result.
- Fixed labels/scores: read from the accepted deployed reproduction CSV.
- Seed frequencies: read from the existing 100-seed summary CSV.
- Harmonic coordinates and fit quality: read from saved Notebook-11 outputs.
- Blank-sky membership: existing declared rule, project-labelled blank sky with reduced chi-square at most 2.
- Model methods containing `.fit(` in generation code: None.

## Content checks

| Check | Result |
|---|---|
| Fig. 1 shows StandardScaler fan-out to PCA, KMeans and Isolation Forest | Pass |
| Fig. 1 states that only Isolation Forest sets the label | Pass |
| Fig. 1 keeps WeightedRoll outside Matrix C | Pass |
| Fig. 1 excludes confidence fusion and calibrated polarization output | Pass |
| Fig. 2 contains all 25 Matrix-C observations | Pass |
| Fig. 2 outlines exactly four fixed candidates | Pass |
| Fig. 2 axis variance is 38.74% and 22.51% | Pass |
| Fig. 3 contains all 25 fixed scores | Pass |
| Fig. 3 hatches exactly four fixed candidates | Pass |
| Fig. 3 annotates the saved 100-seed counts | Pass |
| Fig. 4 contains all 25 saved fractional-harmonic coordinates | Pass |
| Fig. 4 distinguishes 13 accepted and two excluded blank-sky fits | Pass |
| Fig. 4 uses no confidence or detection contour | Pass |
| Fig. 4 identifies exactly four fixed ML candidates | Pass |
| Role encoding has redundant shape as well as colour | Pass |

## Visual inspection

All four 300-dpi PNGs were inspected at original resolution.

- Fig. 1: node text, branch arrows and independence statement are visible; no unsupported elements from the uploaded architecture are retained.
- Fig. 2: candidate annotations are within the image bounds; the legend does not obscure candidates.
- Fig. 3: all 25 observation labels and seed annotations are readable at the exported two-column size; hatching provides a non-colour candidate cue.
- Fig. 4: case annotations do not overlap points; the legend is outside the data region; the component-wise sample-SD cross is labelled descriptively and is not drawn as a contour.

## Format checks

- Each figure has a vector PDF for LaTeX and a 300-dpi PNG for Word.
- Fig. 1, Fig. 3 and Fig. 4 are sized for approximately 7.16-inch two-column width.
- Fig. 2 is sized for approximately 3.50-inch one-column width.
- Manuscript text remains black; figure colours are restrained and paired with shapes, outlines or hatching.
- Scientific figures were not AI-generated and use only frozen project artifacts.
- No manuscript PDF was generated.

## Known presentation limitations

- Final font appearance must be rechecked after insertion into the selected IEEE template.
- Fig. 3 is information-dense and should remain two-column width; a one-column placement is not recommended.
- Fig. 4’s component-wise sample-SD cross ignores coordinate covariance and must retain the caption boundary.
- The PCA transform uses the saved artifact in the currently available environment; exact visual coordinates are reproducible from the saved numerical parameters, while the unpinned original environment remains a manuscript limitation.

