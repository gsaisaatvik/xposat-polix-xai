# AFGHANISTAN Part 04 — Required Corrections

## Control note

This file lists proposed corrections only. In accordance with the Phase-6 gate, **the Phase-5 Markdown, DOCX, LaTeX, BibTeX, and claim ledger were not edited**.

## Required before the manuscript is sent as a formatted submission

| Priority | Required correction | Reason | Result impact | Approval needed |
|---|---|---|---|---|
| Critical | Replace all rough DOCX equation strings with real Word equations or high-quality equation objects. | The Word file currently contains strings such as `bar j=frac{...}`, `phi_fit=1/2 12{atan2}...`, and raw LaTeX braces. These are not publication-quality equations. | None | User approval to revise DOCX formatting |
| High | Transfer the manuscript into the selected venue’s official IEEE template. | The current DOCX approximates conference geometry; it is not proof of official template compliance. | None | Guide must select venue/template |
| High | Complete page-image visual QA after a working renderer is available. | LibreOffice is unavailable, and Word PDF conversion timed out. Word opened the file and reported nine pages, but clipping, gaps, and table flow were not visually certified. | None | Operational/template decision |
| High | Reduce the nine-page Word draft to the selected page limit after figure selection. | Generic target is 6–8 pages; premature compression could remove evidence the guide wishes to retain. | None | Guide venue/page-limit and figure decisions |
| High | Compile the LaTeX source and fix any float, table-width, or path issue. | A TeX engine is not installed in the current environment. Absolute figure paths are not portable, and wide table specifications require compile inspection. | None | Venue/template environment |
| Medium | Add alt text to the four DOCX figures. | Accessibility audit reported four high-severity missing-alt findings. | None | None after correction approval |
| Medium | Mark first table rows as repeating header rows. | Accessibility audit reported four missing `w:tblHeader` markers. | None | None after correction approval |
| Medium | Use explicit table widths and column-specific geometry. | The current Word tables rely on autofit and equal-width construction, which may wrap poorly in an IEEE layout. | None | Venue template |
| Medium | Apply meaningful Word styles to title and section headings. | The style audit found the title and manuscript headings represented mainly through direct formatting, weakening navigation and accessibility. | None | Venue template |
| Medium | Add a limitation sentence stating that weighted least squares uses delivered per-bin uncertainties without a covariance or systematic-error model. | This clarifies the scope of the fit and empirical reference. | None | POLIX-aware/domain approval |

## Corrections that are recommended but not mandatory before guide review

1. Prefer “separate harmonic branch” where “independent” could be read as a statistical-independence claim; retain the explicit statement that statistical independence was not established.
2. Keep the tested seed, contamination, and included-observation scope adjacent to “stable under the tested procedures.”
3. Consider moving detailed rank correlations and contamination/jackknife values to supplementary material if the venue page limit is strict.
4. Consider moving Fig. 4 or the full representative harmonic table to supplementary material if domain review finds the empirical reference too preliminary for the main paper.
5. Replace author and affiliation placeholders after the guide approves author order.

## Corrections not permitted

- Changing the fixed title without guide instruction.
- Retraining, tuning contamination, changing feature definitions, or creating a new matrix.
- Replacing the project XAI method with SHAP or LIME.
- Altering candidate identities or saved numerical results.
- Adding calibrated polarization degree, official sky angle, official background subtraction, or astrophysical causes.
- Presenting optional future experiments as completed work.

## Proposed correction sequence after approval

1. Repair Word equations and accessibility metadata.
2. Add the one bounded weighted-fit limitation after domain approval.
3. Apply the selected official venue template to Word and LaTeX.
4. Convert absolute figure paths into a portable submission folder.
5. Compile/render and visually inspect every page.
6. Re-run numerical, citation, forbidden-language, and protected-hash checks.

