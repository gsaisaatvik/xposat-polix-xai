# Guide Review Brief

## Working paper title

**Product-Aware Explainable Anomaly Screening with Blank-Sky Modulation Diagnostics for XPoSat POLIX Level-2 Observations**

College project title: *An Explainable AI Framework for Analysis of X-Ray Polarimetry Data from XPoSat*.

## Research problem

POLIX Level-2 observations contain heterogeneous products describing exposure, energy-resolved azimuthal behavior, source azimuth, temporal variability, detector balance, and exposure-weighted roll modulation. The project asks whether these products can be represented through scientifically interpretable features and screened using explainable unsupervised learning, while retaining a scientifically independent comparison with blank-sky-referenced physical modulation behavior. The objective is observation screening and research prioritization, not automated astrophysical classification.

## Literature gap

The reviewed literature covers XPoSat/POLIX instrumentation, X-ray polarimetry and Stokes analysis, astronomy anomaly detection, explainable anomaly detection, and explanation-faithfulness evaluation. Limited published work was identified that combines POLIX Level-2 product-aware feature engineering, archive-relative unsupervised screening, observation- and product-level explanation, faithfulness testing, and an independent blank-sky-referenced modulation diagnostic. This is a cautious gap statement; the paper does not claim priority or superiority.

## Proposed paper contributions

1. A scientifically interpretable 15-feature Matrix-C representation spanning exposure, energy-resolved azimuth, source azimuth, light-curve variability, and detector balance.
2. An unsupervised screening pipeline using standardized features, principal component analysis, KMeans structure, and Isolation Forest candidate selection.
3. A model-specific four-component explanation method combining PCA separation, KMeans centroid distance, Isolation Forest feature occlusion, and standardized feature abnormality, with feature-to-product-family mapping.
4. A feature-neutralization faithfulness analysis, supplemented by random-seed, contamination, leave-one-out, feature-tier, and ranking-agreement checks.
5. A separate WeightedRoll branch using weighted second-harmonic fitting and an empirical blank-sky \(Q/U\) reference, preserving independence from the primary Matrix-C anomaly input.

## Dataset and verified results

The frozen project archive contains **25 POLIX Level-2 observations: 10 source observations and 15 blank-sky observations**.

The fixed deployed Matrix-C model returns **21 Normal results and four anomaly candidates**: Blank Sky-13, Sco X-1, Her X-1, and Blank Sky-5. Blank Sky-13, Sco X-1, and Her X-1 were flagged in all 100 tested Isolation Forest seed runs. Blank Sky-5 was flagged in 29 of 100 runs and is therefore a seed-sensitive threshold case rather than part of the equally stable core.

For Sco X-1, the accepted versioned XAI ranking is energy peak channel, energy weighted mean channel, and energy channel entropy. Its modulation vector remains within empirical blank-sky scatter.

## Main scientific finding

**Statistical unusualness and polarization-like modulation evidence are not equivalent.** An observation may be unusual in the product-aware feature space without showing unusual blank-sky-relative modulation, while a comparatively large raw modulation need not produce a Matrix-C anomaly flag. The two branches should therefore be interpreted as complementary inspection evidence rather than mutual confirmation.

## Scientific claim boundaries

The paper does not claim:

- an astrophysical discovery or confirmed physical anomaly;
- calibrated polarization degree (PD);
- official sky polarization angle (PA);
- official POLIX background subtraction or an official \(\mu_{100}\).

WeightedRoll is treated as an exposure-weighted product containing source and background modulation contributions. Reported modulation and phase values remain raw or fitted diagnostics.

## Decisions requested from the guide

The authors request guidance on:

- the final framing and ordering of the paper contributions;
- author order, affiliations, and corresponding author;
- target venue, template, and page limit;
- scientific wording for feature semantics and candidate interpretation;
- the treatment of WeightedRoll and the empirical blank-sky reference;
- the final selection and number of figures.

## Current status

**Draft 1 is complete and awaiting guide review.** The manuscript remains an evidence-audited working draft. No final PDF has been generated.
