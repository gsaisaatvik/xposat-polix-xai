# Agent 2 - XPoSat/POLIX Domain Audit

**Role:** XPoSat/POLIX domain researcher  
**Audit date:** 2026-07-27  
**Scope:** Mission and instrument semantics, POLIX Level-2 product interpretation, WeightedRoll, Stokes-like diagnostics, and calibration/claim boundaries.  
**Manuscript status:** No manuscript file was edited.  
**Evidence rule:** A statement is marked **VERIFIED** only when supported by an identified primary or authoritative source. Project-derived interpretation is labelled separately. Missing page-level confirmation is marked **NOT VERIFIED**.

## 1. Sources and authority

| Source | Authority and use | Availability | Audit status |
|---|---|---:|---|
| *POLIX User Handbook*, Version 1.0, October 2025, local file `C:\Users\Saatvik\Downloads\POLIX_User_Handbook.pdf` | Controlling local source for released POLIX product semantics and release-specific limitations | Full text available | **VERIFIED for the specific pages cited below** |
| ISRO, “XPoSat” mission page, <https://www.isro.gov.in/XPoSat.html> | Mission identity and payload context | Web source identified | **Authoritative; exact current wording should be rechecked before submission** |
| ISSDC/PRADAN portal, <https://pradan.issdc.gov.in/> | Official data-access and data-use context | Web source identified | **Authoritative; exact current acknowledgement wording is outside this audit and must be rechecked before submission** |
| Project archive result tables under `D:\ISROtrial\Polix_L2_full_archive\final_project_outputs` | Evidence of what the project calculated; not authority for instrument calibration | Available | **Project evidence only** |
| Project feature and service code under `D:\polix_xai_webapp` | Evidence of implemented transformations; not authority for astrophysical interpretation | Available | **Project evidence only** |

No paper should treat a project CSV, notebook, or Flask display as a substitute for the POLIX handbook or official calibration documentation.

## 2. Mission and instrument statements

1. **VERIFIED - mission identity.** XPoSat is an Indian X-ray polarimetry mission, and POLIX is one of its scientific payloads. The manuscript may identify the mission and payload but should use the official current ISRO description when giving detailed energy ranges, observing modes, or performance specifications.
2. **VERIFIED - analysis level.** The project works with POLIX Level-2 products included in its frozen archive. This supports the wording “25 POLIX Level-2 observations included in the project archive,” not “all available POLIX data.”
3. **INTERPRETATION, NOT A CALIBRATION CLAIM.** The paper studies computational representation and observation screening. It is not an official POLIX reduction or calibration pipeline.
4. **NOT VERIFIED IN THIS AUDIT.** Exact numerical instrument specifications such as energy range, effective area, minimum detectable polarization, time resolution, detector geometry, and in-flight calibration performance require direct citation to the current handbook or a primary instrument paper before inclusion.

## 3. Level-2 product families actually used by the project

The project’s implemented representation draws information from the following scientific product families. The descriptions below state the role that is defensible for this paper; they do not upgrade the products into calibrated polarimetric measurements.

| Product family used | Project use | Scientifically safe interpretation | Audit status |
|---|---|---|---|
| Exposure metadata | Exposure-related features and normalization/context | Observation duration or exposure context can affect statistical precision and comparability | **Project use verified; exact handbook keyword mapping NOT VERIFIED here** |
| Energy-channel distribution | Peak channel, weighted mean channel, entropy, and related summaries | Describes the shape and concentration of the recorded channel distribution; it is not by itself a calibrated spectrum or a physical source classification | **Project use verified; physical calibration NOT CLAIMED** |
| Energy-resolved azimuthal products | Summaries of azimuthal behaviour across energy/channel groupings | Encodes distributional structure that can be useful for screening; it is not automatically evidence of polarization | **Project use verified; exact released-product nomenclature/page mapping NOT VERIFIED here** |
| Source-azimuth products | Features describing source-associated azimuthal distributions | Can support product-aware anomaly screening, subject to background and response limitations | **Project use verified; background-correction status must not be inferred** |
| Temporal/light-curve products | Variability and temporal summary features | Describes observation-level variability; causal or source-state interpretations require separate timing analysis | **Project use verified; exact binning and GTI semantics NOT VERIFIED here** |
| Detector-wise products | Detector-balance or detector-distribution summaries | Can reveal inter-detector imbalance or unusual detector response patterns; no hardware fault or astrophysical cause may be assigned without expert review | **Project use verified; detector-calibration interpretation NOT VERIFIED** |
| WeightedRoll product | Independent modulation diagnostic only; excluded from the primary Matrix-C anomaly input | Exposure-weighted roll/azimuth behaviour containing source and background contributions | **VERIFIED boundary; handbook p. 26** |

This table is intentionally conservative. Agent 3’s feature-semantics audit should supply the exact file, column, formula, unit, and shape mapping. Any disagreement between that mapping and the handbook must remain visible until a POLIX domain expert resolves it.

## 4. WeightedRoll boundary

### 4.1 What is verified

The local *POLIX User Handbook*, p. 26, describes the WeightedRoll product in a way that establishes two critical limits:

- it is exposure-weighted; and
- it includes source and background modulation contributions.

Therefore, the project must not describe WeightedRoll as fully background-subtracted or as an official source-only modulation curve. This is the controlling domain interpretation for the paper.

### 4.2 Permitted project use

The project may use WeightedRoll as a **separate physical diagnostic branch** and may fit its binned behaviour with

\[
y(\phi)=C+Q\cos(2\phi)+U\sin(2\phi),
\]

provided that:

- \(C\), \(Q\), and \(U\) are described as coefficients of the project’s empirical harmonic fit;
- the derived fractional coordinates, such as \(q=Q/C\) and \(u=U/C\), are identified as empirical or Stokes-like diagnostic quantities unless the official pipeline definition is demonstrated;
- source results are compared with an explicitly defined empirical blank-sky reference;
- fit quality and the blank-sky selection rule are reported;
- no source-only or fully background-corrected interpretation is implied; and
- WeightedRoll remains outside Matrix C so that it cannot circularly confirm an ML flag produced from the same physical diagnostic.

### 4.3 Prohibited descriptions

Do not write that WeightedRoll is:

- an official background-subtracted polarization product;
- a calibrated Stokes product;
- an official polarization measurement;
- independent of instrumental/background modulation merely because a blank-sky comparison was performed; or
- proof that an ML anomaly has a polarimetric origin.

## 5. Q/U, modulation amplitude, PD, and PA

### 5.1 Harmonic coefficients and empirical Q/U space

For the stated second-harmonic fit, the project may calculate a raw modulation amplitude from the fitted coefficients and place observations in an empirical \(q\)-\(u\) diagnostic space. This is a mathematical summary of the fitted curve. Its scientific interpretation depends on background treatment, response, calibration, coordinate convention, and uncertainty propagation.

Safe wording:

- “empirical \(Q/U\) diagnostic”
- “fractional \(q/u\) coordinates derived from the project fit”
- “raw modulation”
- “within empirical blank-sky scatter”
- “requires domain-expert inspection”

Unsafe wording:

- “measured source Stokes parameters” without official product-definition support;
- “background-free modulation”;
- “polarization detection”; or
- “instrument-corrected polarization.”

### 5.2 Polarization degree

Turning a modulation amplitude into polarization degree requires the relevant modulation response, commonly expressed through a 100%-polarized response or \(\mu_{100}\), together with the appropriate energy/source spectrum, selection, and calibration context. No official project-specific \(\mu_{100}\) artifact has been verified in the frozen evidence.

Accordingly:

- any calculations made under assumed \(\mu_{100}\) values are **PD sensitivity proxies** only;
- they are not calibrated polarization-degree measurements;
- they should not be used as a principal result; and
- uncertainty, response dependence, and background treatment must be made explicit if the sensitivity table is retained.

The local handbook’s release-specific warning on p. 57 states that the released configuration is not suitable for polarization measurement. That warning overrides any tendency to interpret a fitted modulation as a final PD result.

### 5.3 Polarization angle

For a generic second-harmonic representation, a phase-like quantity can be calculated from \(Q\) and \(U\), commonly through a half-angle relation. However, conversion to an official sky polarization angle requires verified sign conventions, coordinate frames, roll-angle handling, detector-to-sky transformation, and any instrument-specific offset.

The frozen project does not establish that complete conversion. Therefore:

- report only a **fitted modulation phase**;
- do not call it official sky PA;
- do not compare it physically with published sky PA values as if the coordinate convention were equivalent; and
- do not infer field geometry or emission mechanism from the phase.

## 6. Blank-sky interpretation

The blank-sky branch is an empirical reference derived from the project archive. It can characterize the scatter and offset present in that selected sample under the project’s fitting procedure. It does not establish an official POLIX background model.

The paper may state:

- fifteen blank-sky observations were included in the project archive;
- thirteen fits satisfying the project’s stated acceptance rule, reduced \(\chi^2\leq2.0\), formed the empirical baseline, if confirmed by the primary CSV;
- a source lies within or outside the empirical blank-sky scatter under the declared metric; and
- blank-sky behaviour helps test whether an ML flag and modulation-like behaviour tell the same story.

The paper may not state:

- the baseline is the official background subtraction;
- the thirteen observations exhaust all valid POLIX blank-sky data;
- the empirical scatter is a calibrated detection threshold;
- observations outside the scatter are polarized detections; or
- observations inside the scatter are proved unpolarized.

## 7. Handbook limitations controlling the manuscript

| Boundary | Evidence | Manuscript consequence |
|---|---|---|
| WeightedRoll contains source and background contributions | *POLIX User Handbook*, p. 26 | Call it an exposure-weighted raw diagnostic; do not call it background-corrected |
| Released configuration is not suitable for polarization measurement | *POLIX User Handbook*, p. 57 | No calibrated PD, no polarization detection, and no official PA claim |
| Official response/calibration chain not demonstrated in the project | No verified official \(\mu_{100}\), PA transformation, or source/background response artifact located in the frozen evidence | Treat PD scenarios as sensitivity proxies and phase as fitted phase |
| Blank-sky sample is archive-specific | Project archive composition, not an official calibration dataset | Use “empirical blank-sky reference” and state its selection |

Exact section titles corresponding to handbook pp. 26 and 57 are **NOT VERIFIED in this bounded audit**. Page references must be checked against the PDF’s printed page numbering before final submission.

## 8. Evidence versus interpretation

| Statement | Classification | Allowed? |
|---|---|---:|
| The project fits a second harmonic to WeightedRoll | Project method, subject to code/CSV confirmation | Yes |
| WeightedRoll contains source and background contributions | Handbook-supported fact | Yes |
| A larger raw modulation indicates a larger fitted second-harmonic component | Mathematical interpretation | Yes, with fit-quality context |
| A large raw modulation establishes source polarization | Unsupported physical inference | No |
| Blank-sky comparison supplies an empirical reference | Project-method interpretation | Yes |
| Blank-sky comparison performs official background subtraction | Unsupported domain claim | No |
| ML unusualness and polarization-like modulation are non-equivalent questions | Study-level interpretation supported when results show discordant cases | Yes, cautiously |
| A specific unusual observation has a named physical cause | Unsupported causal inference | No |

## 9. Claims requiring guide or POLIX-domain approval

The following should not enter a submission without explicit guide/domain review:

1. The exact description and energy range of POLIX and XPoSat.
2. The exact Level-2 product names, versions, columns, binning, units, and GTI/exposure conventions used by every feature family.
3. Whether the project’s \(Q\) and \(U\) notation could be confused with officially calibrated Stokes products; the safer default is “harmonic coefficients” or “empirical Stokes-like coordinates.”
4. Whether \(q=Q/C\), \(u=U/C\), and the raw modulation formula match the intended POLIX convention.
5. Whether the chosen WeightedRoll uncertainty column and weighted least-squares treatment are scientifically defensible.
6. Whether reduced \(\chi^2\leq2.0\) is acceptable as a project fit-quality rule and how it should be justified.
7. Whether the empirical blank-sky baseline should be summarized by mean/standard deviation, a robust estimator, or another region, especially with only thirteen accepted fits.
8. Whether any apparent source-versus-blank displacement may be discussed beyond descriptive language.
9. Whether any detector-balance or product-specific anomaly driver has a plausible instrumental interpretation; no cause should be assigned by the ML team alone.
10. Whether PD sensitivity-proxy material belongs in the main paper, supplement, or should be removed.
11. Whether the fitted phase should appear at all; if retained, its coordinate convention and limitations must be prominent.
12. The official current XPoSat/POLIX data acknowledgement and data-use wording from ISSDC/PRADAN.
13. The final choice of representative source and blank-sky cases, including Her X-1, Sco X-1, Crab P01_0005, and anomalous blank-sky observations.

## 10. Disagreements and unresolved items

| ID | Issue | Domain-audit position | Resolution needed |
|---|---|---|---|
| D2-01 | “Q/U” may imply calibrated Stokes parameters | Use “harmonic coefficients” and “empirical \(q/u\) diagnostic” unless official equivalence is demonstrated | Guide/POLIX expert |
| D2-02 | WeightedRoll background status | It includes source and background contributions; it is not assumed fully background-corrected | Controlling handbook evidence, p. 26 |
| D2-03 | PD/PA interpretation | No calibrated PD and no official sky PA are supported | Controlling handbook limitation, p. 57, plus missing calibration artifacts |
| D2-04 | Blank-sky baseline meaning | Archive-specific empirical reference, not official background subtraction or a detection threshold | Guide/statistical and domain review |
| D2-05 | Exact product-to-feature handbook mapping | **NOT VERIFIED** at page/column level in this bounded audit | Reconcile Agent 3 mapping with handbook before Phase 4 |
| D2-06 | Exact handbook section titles and printed-vs-PDF page numbering | **NOT VERIFIED** | Manual page check before citation freeze |

## 11. Domain-safe controlling language

The strongest defensible domain statement is:

> The project uses WeightedRoll as an exposure-weighted, source-plus-background modulation diagnostic that is scientifically independent of the Matrix-C anomaly input. Its fitted harmonic coefficients and blank-sky-relative position are interpreted empirically; they are not presented as official background-subtracted Stokes measurements, calibrated polarization degree, or sky polarization angle.

This audit finds the project’s methodology/scientific-computing framing compatible with the available domain boundaries. It does **not** authorize an astrophysical-discovery, polarization-detection, calibrated-PD, or official-PA claim.
