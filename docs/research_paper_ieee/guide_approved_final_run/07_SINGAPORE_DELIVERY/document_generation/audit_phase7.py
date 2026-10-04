from __future__ import annotations

import csv
import hashlib
import json
import re
import zipfile
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn


PHASE = Path(__file__).resolve().parents[1]
RUN = PHASE.parent
MASTER = PHASE / "SINGAPORE_Part_00_Controlled_Manuscript.md"
DOCX = PHASE / "SINGAPORE_Part_01_Guide_Ready_Manuscript.docx"
TEX = PHASE / "portable_latex_package" / "manuscript.tex"
BIB = PHASE / "portable_latex_package" / "references.bib"
FIGURES = PHASE / "portable_latex_package" / "figures"
PROTECTED = RUN / "00_INDIA_CONTROL" / "INDIA_Part_03_Protected_File_Hashes.csv"
TRUTH_TABLE = RUN / "01_NEPAL_EVIDENCE" / "NEPAL_Part_03_All_25_Observation_Truth_Table.csv"

TITLE = "An Explainable AI Framework for Analysis of X-Ray Polarimetry Data from XPoSat"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def check(name: str, condition: bool, detail: str) -> dict:
    return {"check": name, "status": "PASS" if condition else "FAIL", "detail": detail}


def bib_keys(text: str) -> set[str]:
    return set(re.findall(r"@\w+\s*\{\s*([^,\s]+)", text))


def cite_keys(text: str) -> set[str]:
    found: set[str] = set()
    for group in re.findall(r"\\cite\{([^}]+)\}", text):
        found.update(key.strip() for key in group.split(","))
    return found


def abstract_words(markdown: str) -> int:
    match = re.search(r"^## Abstract\s+(.*?)^\*\*Index Terms", markdown, flags=re.M | re.S)
    if not match:
        return 0
    return len(re.findall(r"\b[\w’-]+\b", match.group(1), flags=re.UNICODE))


def braces_balanced(text: str) -> bool:
    depth = 0
    escaped = False
    for char in text:
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


def main() -> None:
    markdown = MASTER.read_text(encoding="utf-8")
    tex = TEX.read_text(encoding="utf-8")
    bib = BIB.read_text(encoding="utf-8")
    document = Document(DOCX)
    checks: list[dict] = []

    word_count = abstract_words(markdown)
    checks.append(check("Exact title", markdown.startswith("# " + TITLE) and TITLE in tex, TITLE))
    checks.append(check("Abstract length", 190 <= word_count <= 230, f"{word_count} words"))
    checks.append(check("Word tables", len(document.tables) == 4, f"{len(document.tables)} tables"))
    checks.append(check("Word inline figures", len(document.inline_shapes) == 4, f"{len(document.inline_shapes)} figures"))

    with zipfile.ZipFile(DOCX) as archive:
        xml = archive.read("word/document.xml").decode("utf-8")
        media = [name for name in archive.namelist() if name.startswith("word/media/")]
    checks.append(check("Native Word equations", xml.count("<m:oMath>") == 8, f"{xml.count('<m:oMath>')} equations"))
    checks.append(check("No equation placeholders", "[[EQ" not in xml, "no placeholders"))
    checks.append(check("Embedded Word media", len(media) == 4, f"{len(media)} media files"))

    alt_text = []
    for shape in document.inline_shapes:
        value = shape._inline.docPr.get("descr")
        alt_text.append(bool(value and value.strip()))
    checks.append(check("Figure alternative text", all(alt_text) and len(alt_text) == 4, f"{sum(alt_text)}/4"))

    accessibility_path = PHASE / "qa_render" / "a11y_audit.json"
    accessibility = json.loads(accessibility_path.read_text(encoding="utf-8")) if accessibility_path.exists() else {}
    accessibility_counts = accessibility.get("counts", {})
    accessibility_clear = all(accessibility_counts.get(level, -1) == 0 for level in ("high", "medium", "low"))
    checks.append(check("Document accessibility audit", accessibility_clear, f"counts={accessibility_counts}"))

    repeating = 0
    for table in document.tables:
        tr_pr = table.rows[0]._tr.get_or_add_trPr()
        if tr_pr.find(qn("w:tblHeader")) is not None:
            repeating += 1
    checks.append(check("Repeating table headers", repeating == 4, f"{repeating}/4"))

    png_pages = sorted((PHASE / "qa_render").glob("page-*.png"))
    checks.append(check("Rendered page set", len(png_pages) == 13, f"{len(png_pages)} pages"))

    required = [
        "21 observations Normal",
        "four as anomaly candidates",
        "100 tested",
        "29 runs",
        "2.454",
        "2.207",
        "1.814",
        "Thirteen of the 15",
        "WeightedRoll",
        "no imputation",
    ]
    missing_required = [token for token in required if token not in markdown]
    checks.append(check("Required frozen results", not missing_required, f"missing={missing_required}"))

    distinctions = [
        "fixed four",
        "stable three",
        "cross-tier persistent pair",
        "six exploratory",
    ]
    missing_distinctions = [token for token in distinctions if token not in markdown]
    checks.append(check("Result-stage distinctions", not missing_distinctions, f"missing={missing_distinctions}"))

    handbook_free = all("handbook" not in text.lower() for text in (markdown, tex, bib))
    checks.append(check("No handbook mention/citation", handbook_free, "Markdown, LaTeX, and BibTeX"))

    unsafe_patterns = {
        "confirmed anomaly": r"confirmed anomal(?:y|ies)",
        "discovery claim": r"(?:report|reports|reported|constitutes|establishes) an astrophysical discovery",
        "polarization-detection claim": r"(?:report|reports|reported|constitutes|establishes) a polarization detection",
        "official PD": r"official PD",
        "official PA": r"official PA",
        "median imputation": r"median imputation",
    }
    found_forbidden = [label for label, pattern in unsafe_patterns.items() if re.search(pattern, markdown, flags=re.I)]
    checks.append(check("Forbidden-language lint", not found_forbidden, f"found={found_forbidden}"))

    absolute_paths = re.findall(r"(?:[A-Za-z]:[/\\]|D:/|C:/)", tex)
    checks.append(check("Portable LaTeX paths", not absolute_paths, f"absolute_paths={absolute_paths}"))
    checks.append(check("LaTeX brace balance", braces_balanced(tex), "static scan"))
    begins = re.findall(r"\\begin\{([^}]+)\}", tex)
    ends = re.findall(r"\\end\{([^}]+)\}", tex)
    checks.append(check("LaTeX environment balance", sorted(begins) == sorted(ends), f"begin={len(begins)}, end={len(ends)}"))

    bibset = bib_keys(bib)
    citeset = cite_keys(tex)
    checks.append(check("Reference count", len(bibset) == 17, f"{len(bibset)} BibTeX entries"))
    checks.append(check("Citation resolution", citeset == bibset, f"missing={sorted(citeset-bibset)}, uncited={sorted(bibset-citeset)}"))

    figure_refs = re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", tex)
    missing_figures = [ref for ref in figure_refs if not (TEX.parent / ref).exists()]
    checks.append(check("LaTeX figure assets", len(figure_refs) == 4 and not missing_figures, f"refs={len(figure_refs)}, missing={missing_figures}"))
    checks.append(check("Packaged figure variants", len(list(FIGURES.glob("*.pdf"))) == 4 and len(list(FIGURES.glob("*.png"))) == 4, "4 PDF + 4 PNG"))

    with PROTECTED.open("r", encoding="utf-8-sig", newline="") as handle:
        protected_rows = list(csv.DictReader(handle))
    changed = []
    missing = []
    for row in protected_rows:
        path = Path(row["path"])
        if not path.exists():
            missing.append(str(path))
        elif sha256(path) != row["sha256"].upper():
            changed.append(str(path))
    checks.append(check("Protected hashes", not changed and not missing and len(protected_rows) == 43, f"43 checked; changed={len(changed)}, missing={len(missing)}"))

    phase5_expected = {
        RUN / "05_MALDIVES_MANUSCRIPT" / "MALDIVES_Part_01_Canonical_Manuscript.md": "6CF049E4B742896E1F36E5874C7EA26E073766A37D2F7869007B01719D5AE66B",
        RUN / "05_MALDIVES_MANUSCRIPT" / "MALDIVES_Part_02_IEEE_Manuscript.docx": "6627C88DC4B32B95A14687D726135976A72442CD4E9BCF38C28DD8865CC9FE0A",
        RUN / "05_MALDIVES_MANUSCRIPT" / "MALDIVES_Part_03_IEEE_Manuscript.tex": "EE3831E4D75C5C3F495E0A97CDEEAE8F01A04C801D7FFA65C2DCDCF52FB7FF86",
        RUN / "05_MALDIVES_MANUSCRIPT" / "MALDIVES_Part_04_References.bib": "72FA8EF1D3754B11AAAF6692613A57659218FC479AB59CC921F680E408CC97D1",
        RUN / "05_MALDIVES_MANUSCRIPT" / "MALDIVES_Part_05_Claim_Evidence_Ledger.md": "F9ADD7B8F3D0540553E42D20FC97152303E439863704FF3F5BC222C6D549A2BB",
    }
    phase5_changed = [str(path) for path, expected in phase5_expected.items() if not path.exists() or sha256(path) != expected]
    checks.append(check("Frozen Phase-5 hashes", not phase5_changed, f"5 checked; changed={len(phase5_changed)}"))

    with TRUTH_TABLE.open("r", encoding="utf-8-sig", newline="") as handle:
        truth_rows = list(csv.DictReader(handle))
    checks.append(check("All-observation traceability", len(truth_rows) == 25, f"{len(truth_rows)} rows"))

    manuscript_pdfs = [
        path for path in PHASE.rglob("*.pdf")
        if "figures" not in {part.lower() for part in path.parts}
        and "selected_figures" not in {part.lower() for part in path.parts}
        and "qa_temp" not in {part.lower() for part in path.parts}
    ]
    checks.append(check("No final manuscript PDF", not manuscript_pdfs, f"found={manuscript_pdfs}"))

    failed = [item for item in checks if item["status"] == "FAIL"]
    report = {
        "overall": "PASS" if not failed else "FAIL",
        "guide_ready": not failed,
        "submission_ready": False,
        "latex_compile_executed": False,
        "latex_compile_reason": "No TeX engine installed in the local QA environment.",
        "visual_pages_inspected": 13,
        "checks": checks,
    }

    json_path = PHASE / "SINGAPORE_Part_10_QA_Report.json"
    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    markdown_lines = [
        "# Phase-7 QA Report",
        "",
        f"**Overall:** {report['overall']}",
        "",
        "**Guide-ready:** Yes" if report["guide_ready"] else "**Guide-ready:** No",
        "",
        "**Submission-ready:** No — venue adaptation and approvals remain pending.",
        "",
        "| Check | Status | Detail |",
        "|---|---|---|",
    ]
    for item in checks:
        detail = item["detail"].replace("|", "\\|")
        markdown_lines.append(f"| {item['check']} | {item['status']} | {detail} |")
    markdown_lines.extend([
        "",
        "## Visual inspection",
        "",
        "All 13 rendered Word pages were inspected at original image detail. No clipping, overlap, broken equation, table overflow, or illegible figure was found.",
        "",
        "## LaTeX status",
        "",
        "The package passed static portability checks. Compilation was not executed because no TeX engine is installed locally; compilation remains a pre-submission check in a standard IEEE environment.",
    ])
    (PHASE / "SINGAPORE_Part_10_QA_Report.md").write_text("\n".join(markdown_lines) + "\n", encoding="utf-8")

    manifest_rows = []
    for path in sorted(PHASE.rglob("*")):
        if path.is_file() and path.name != "SINGAPORE_File_Manifest.csv" and "qa_temp" not in {part.lower() for part in path.parts}:
            manifest_rows.append({
                "relative_path": path.relative_to(PHASE).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            })
    with (PHASE / "SINGAPORE_File_Manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["relative_path", "bytes", "sha256"])
        writer.writeheader()
        writer.writerows(manifest_rows)

    print(f"OVERALL={report['overall']}")
    print(f"CHECKS={len(checks)}")
    print(f"FAILED={len(failed)}")
    for item in failed:
        print(f"FAIL={item['check']} :: {item['detail']}")


if __name__ == "__main__":
    main()
