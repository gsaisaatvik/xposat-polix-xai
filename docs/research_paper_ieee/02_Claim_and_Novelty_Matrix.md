# Claim and Novelty Matrix

## Publication-positioning statement

The defensible positioning is:

> This work investigates an integrated, product-aware framework for unsupervised screening of POLIX Level-2 observations, observation- and product-level explanation, and a scientifically independent blank-sky-referenced physical modulation diagnostic.

The literature audit identified limited published work that combines these elements for POLIX. It did not establish priority, superiority, or uniqueness.

Draft-1 evidence control: observation-specific explanation claims use the exact versioned-function audit. For Sco X-1, the accepted order is energy peak channel (2.454499), energy weighted mean channel (2.207369), and energy channel entropy (1.813968). The historical entropy-first narrative is superseded and is not manuscript evidence.

## Novelty matrix

| Existing work | What it provides | What it does not provide for this paper’s problem | Verified evidence | Project contribution | Strength of claim |
|---|---|---|---|---|---|
| Official XPoSat/POLIX mission and handbook material | Instrument purpose, Level-2 product semantics, calibration/background boundaries | Archive-level unsupervised screening and model-specific explanations | Official ISRO/ISSDC pages and handbook | Encodes multiple documented products into an observation-level analysis representation | Moderate applied-method contribution |
| Stokes and modulation analysis literature | Physical basis, Q/U additivity, background and calibration requirements | Product-aware anomaly screening over heterogeneous POLIX Level-2 outputs | Kislat *et al.*; Fabiani review | Keeps WeightedRoll fitting and empirical blank-sky Q/U comparison independent from the primary anomaly input | Moderate systems/methodology contribution |
| Isolation Forest, PCA, and KMeans | Generic unsupervised structure and anomaly methods | POLIX-specific feature provenance or physical interpretation | Primary method papers and code | Combines complementary evidence in a small, archive-specific screening pipeline | Integration contribution; algorithms are established |
| Astronomy anomaly detection | Archive ranking and expert-in-the-loop inspection | Directly comparable POLIX Level-2 product engineering and physical modulation branch | Baron and Poznanski; Astronomaly | Applies cautious candidate screening to 25 POLIX observations | Applied contribution; no superiority claim |
| SHAP and anomaly-explanation literature | General local feature attribution and anomaly-explanation taxonomies | A verified attribution aligned to this deployed PCA/KMeans/Isolation-Forest score stack | Lundberg and Lee; Yepmo *et al.* | Four-component, model-specific feature score with product-family mapping | Moderate implementation/method contribution; not a general XAI theorem |
| Explanation-faithfulness literature | Perturbation-based concepts for testing explanation behavior | POLIX-specific neutralization evidence | Yeh *et al.*; original and reproduced faithfulness CSVs | Tests whether neutralizing top-ranked features reduces PCA and Isolation-Forest evidence | Useful validation contribution; limited to six exploratory candidates |
| Multi-view representation literature | General motivation for retaining complementary heterogeneous views | A directly comparable, small-sample POLIX feature matrix | Reviewed literature search | Product-family feature tiers and explicit WR exclusion prevent circular confirmation | Moderate design contribution |
| Research software and reproducible pipelines | Modular processing and researcher-facing interfaces | This specific end-to-end POLIX evidence path | Flask source, services, configs, exporter | Reproducible extraction, screening, physical diagnostics, explanation, and export | Implementation contribution, not principal scientific novelty |

## Proposed contributions after audit

1. A 15-feature, product-aware observation representation spanning exposure, energy-resolved azimuthal behavior, source azimuth, temporal variability, and detector balance for the 25 POLIX Level-2 observations included in the project archive.
2. An archive-relative unsupervised screening pipeline combining standardized features, PCA geometry, KMeans structure, and Isolation Forest classification, accompanied by seed, contamination, jackknife, and feature-tier sensitivity checks.
3. A model-specific four-component explanation score based on PCA separation, KMeans centroid distance, Isolation Forest occlusion, and standardized feature abnormality, mapped back to POLIX product families.
4. A feature-neutralization faithfulness test reproduced from primary artifacts, yielding five Strong and one Moderate verdict across the exploratory six-candidate set.
5. An independent WeightedRoll branch using weighted least-squares modulation fits and an empirical 13-observation blank-sky Q/U reference, demonstrating that archive-relative anomaly evidence and modulation evidence answer different questions.

## Allowed claims and evidence

| Claim | Evidence strength | Safe wording |
|---|---|---|
| Product-aware feature engineering | Strong | “We constructed a 15-feature product-aware representation.” |
| Unsupervised observation screening | Strong for this archive | “The fixed model flagged four anomaly candidates relative to the project archive.” |
| Observation- and product-specific explanation | Strong for deployed code | “The explanation maps local model evidence to feature and product-family provenance.” |
| Sco X-1 local explanation | Strong for the frozen current implementation | “The leading deployed drivers are energy peak channel, energy weighted mean channel, and energy channel entropy, in that order.” |
| Explanation faithfulness | Moderate | “Neutralization reduced both main signals for five of six exploratory candidates.” |
| Robustness | Mixed | “Three candidates were seed-stable; the fourth fixed-seed candidate was seed-sensitive.” |
| Physical modulation fitting | Strong as a raw diagnostic | “WeightedRoll curves were fit with a two-fold weighted least-squares model.” |
| Empirical blank-sky comparison | Strong as an archive diagnostic | “Source modulation was compared with a 13-fit empirical blank-sky Q/U reference.” |
| End-to-end implementation | Strong for code presence; runtime download pending | “The Flask implementation integrates extraction, inference, diagnostics, plots, and export.” |

## Excluded claims

- Astrophysical discovery or detection of new source behavior.
- Confirmed anomaly or official anomaly ground truth.
- Polarization detection.
- Final calibrated polarization degree.
- Official sky polarization angle.
- Official POLIX background subtraction.
- Official POLIX \(\mu_{100}\).
- Superiority over another method.
- Coverage of all publicly available POLIX observations.
- Causal interpretation of candidate features.
- Use of SHAP in the deployed method.
- LLM-generated deterministic explanation text.
- Generalization beyond the 25-observation archive.

## Required cautious language

- “limited published work was identified”
- “the reviewed literature did not provide a directly comparable framework”
- “this work investigates”
- “flagged as an anomaly candidate”
- “statistically unusual relative to the project archive”
- “within empirical blank-sky scatter”
- “requires domain-expert inspection”
- “raw modulation”
- “fitted modulation phase”
- “PD sensitivity proxy”
