# Visual and interaction QA

Date: 2026-10-04

## Design intent

The redesign uses an original dark space visual system inspired by the editorial hierarchy and interactive learning quality of public space-education websites. No external site layout, text, illustration, or source code was copied.

## Checked views

- Home hero and central-result framing
- Mission product narrative and five-stage Product Lens
- Study Archive list, filters, fixed-result detail, and seed-frequency display
- Analyze page and upload-mode distinction
- Evidence Lab calculation cards, formula board, tally checks, provenance reveal, and tabbed tables
- Responsive single-column behavior at the in-app browser viewport

## Interaction checks

- Product Lens advances to the independent harmonic-comparison stage.
- Evidence Lab next/previous card controls update the formula and text.
- Implementation provenance can be shown and hidden.
- Archive endpoint renders all 25 saved observations.
- A raw two-observation upload completes through the Vue interface and renders the results workspace.
- Navigation has a compact mobile menu at the tested viewport.
- Focus-visible styles are present for interactive Evidence Lab controls.
- Reduced-motion media query suppresses nonessential animation.

## Scientific-display checks

- Study archive and live upload are visibly separated.
- Isolation Forest is identified as the fixed-label source.
- WeightedRoll is presented as a separate branch.
- No polarization-detection claim appears in the primary interface.
- Fixed four, seed-stable three, cross-tier two, and exploratory six are not merged.
- Sco X-1 feature-ranking values are shown only as local heuristic evidence.

## Remaining deployment work

- Choose the hosting platform.
- Configure production WSGI serving for the Python adapter.
- Configure reverse proxy/CORS and storage cleanup policy.
- Pin and reproduce the Python scientific environment before public hosting.
- Add institution-approved logos or mission imagery only after rights/credit review.
