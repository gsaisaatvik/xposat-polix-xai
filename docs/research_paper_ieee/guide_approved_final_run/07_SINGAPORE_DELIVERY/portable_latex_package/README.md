# Portable IEEE LaTeX Package

This folder contains the guide-approved content candidate in portable, venue-neutral IEEE conference form.

## Contents

- manuscript.tex — manuscript source using IEEEtran
- references.bib — 17 retained references
- figures/ — four paper figures in vector PDF and 300-dpi PNG form

No absolute local paths are used. No generated PDF is included.

## Typical build

    pdflatex manuscript.tex
    bibtex manuscript
    pdflatex manuscript.tex
    pdflatex manuscript.tex

The build environment must provide IEEEtran.cls and the standard packages listed in the preamble. The package has passed static checks for balanced braces/environments, citation-key resolution, relative figure paths, and required assets. A TeX engine was not installed in the local QA environment, so an actual compilation test remains pending in the guide's or venue's standard IEEE environment.

Final venue name, page limit, author order, affiliations, and venue-specific disclosure text remain pending. Do not force page compression until those decisions are made.
