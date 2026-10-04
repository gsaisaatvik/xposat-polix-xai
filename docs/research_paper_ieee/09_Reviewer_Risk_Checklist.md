# Reviewer Risk Checklist

## Critical scientific risks

- [ ] Authors explicitly state that the model was trained and evaluated retrospectively on the same 25-observation archive.
- [ ] Contamination 0.16 is presented as an assumed screening fraction, not an empirically learned prevalence.
- [ ] The four fixed-model candidates are not presented as equally stable; Blank Sky-5 is seed-sensitive.
- [ ] C24_0020’s seed sensitivity is discussed even though it is not in the fixed-seed deployed four.
- [ ] The exploratory six-candidate faithfulness set is never conflated with deployed predictions.
- [ ] Statistical unusualness is never equated with astrophysical or polarimetric evidence.
- [ ] WeightedRoll is described as exposure-weighted and containing both source and background contributions.
- [ ] The empirical mean Q/U subtraction is not called official POLIX background subtraction.
- [ ] Raw modulation is not called polarization degree.
- [ ] Fitted modulation phase is not called sky polarization angle.
- [ ] Assumed \(\mu_{100}\) values are sensitivity scenarios only.
- [ ] Handbook restrictions on released-data polarization measurement are quoted or paraphrased accurately.
- [ ] Her X-1’s moderate vector distance is qualified by its poor simple-sinusoid fit.
- [ ] Sco X-1 is discussed as an example of ML/physical non-equivalence.
- [ ] Sco X-1’s accepted XAI order is peak channel (2.454499), weighted mean channel (2.207369), and entropy (1.813968).
- [ ] The historical entropy-first narrative is identified as superseded and is not used as manuscript evidence.
- [ ] Crab P01_0005 is not presented as a polarization detection.

## Method risks

- [ ] Matrix-C feature definitions match the CSV and extractor.
- [ ] No median-imputation step is claimed for the frozen/deployed pipeline.
- [ ] The paper states that the frozen matrix has zero missing values.
- [ ] KMeans is described as one component, not as a separate anomaly model.
- [ ] The four XAI terms are called explanation components, not four models.
- [ ] XAI explanations are described as local model evidence, not causality.
- [ ] The explanation text is described as deterministic templates, not LLM output.
- [ ] SHAP is discussed only as related work and is not claimed as deployed.
- [ ] Matrix A/B/C candidate-set sensitivity is disclosed.
- [ ] WR results are kept out of Matrix-C selection/confirmation.
- [ ] Small-\(n\) rank-correlation \(p\)-values are not overinterpreted.
- [ ] XAI faithfulness is limited to the six exploratory candidates and one neutralization baseline.
- [ ] The audit environment is distinguished from the unknown original training environment.

## Evidence risks

- [ ] Every paper number points to a CSV or saved artifact.
- [ ] Sco X-1’s three reported feature ranks and scores use the exact imported-function CSV.
- [ ] The 13-fit baseline uses `acceptable` fits (reduced chi-square ≤ 2).
- [ ] All ten source rows are checked against the source-only CSV.
- [ ] File hashes and freeze date are archived with the submission.
- [ ] No superseded report value overrides the reviewed report or primary CSV.
- [ ] No target label is treated as unique without checking observation ID.
- [ ] The duplicate “Blank Sky-2” display label is resolved or noted.

## Literature and venue risks

- [ ] Saini *et al.* full text is inspected or claims are limited to verified abstract metadata.
- [ ] Yepmo *et al.* full text is inspected or only the visible high-level taxonomy is used.
- [ ] Official acknowledgment wording is rechecked immediately before submission.
- [ ] XPoSat and POLIX are named in the abstract.
- [ ] Venue template, page limit, reference style, and AI-use policy are confirmed.
- [ ] Author list, affiliations, funding, conflicts, and contributions are complete.
- [ ] Permission is confirmed for handbook-derived material and any screenshots.
- [ ] Figures use vector/high-resolution exports and readable two-column labels.

## Required domain-expert approvals

- [ ] Scientific meaning and thresholds of all 15 features.
- [ ] Use of POLIX light-curve and PHA-derived quantities given handbook cautions.
- [ ] Interpretation of the two blank-sky candidates.
- [ ] Whether the empirical 13-fit Q/U baseline is suitable as a diagnostic.
- [ ] Whether any source/blank-sky pairing is scientifically meaningful.
- [ ] Phase convention and the decision not to convert to sky PA.
- [ ] No official \(\mu_{100}\) or calibration product was overlooked.
- [ ] Final statements about the current POLIX release.
