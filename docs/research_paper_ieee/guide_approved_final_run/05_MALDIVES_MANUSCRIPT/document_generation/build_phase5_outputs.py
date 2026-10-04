from __future__ import annotations

import re
from pathlib import Path

from docx import Document
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "MALDIVES_Part_01_Canonical_Manuscript.md"
DOCX_OUT = ROOT / "MALDIVES_Part_02_IEEE_Manuscript.docx"
TEX_OUT = ROOT / "MALDIVES_Part_03_IEEE_Manuscript.tex"

CITATION_ORDER = [
    "isro_xposat", "rishin2010thomson", "fabiani2018instrumentation",
    "kislat2015stokes", "issdc_xposat_archive", "baron2017weirdest",
    "giles2019serendipity", "lochner2021astronomaly",
    "li2024explainable_anomaly", "lundberg2017shap", "yeh2019infidelity",
    "campos2016evaluation", "pearson1901pca", "macqueen1967kmeans",
    "liu2008isolation", "pedregosa2011sklearn", "issdc_xposat_ack",
]
CITE_NUM = {key: i + 1 for i, key in enumerate(CITATION_ORDER)}


def parse_blocks(text: str):
    lines = text.splitlines()
    blocks = []
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line:
            i += 1
            continue
        if line.startswith("$$"):
            equation = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("$$"):
                equation.append(lines[i].rstrip())
                i += 1
            i += 1
            blocks.append(("equation", "\n".join(equation).strip()))
            continue
        if re.match(r"^!\[.*\]\(.*\)$", line):
            m = re.match(r"^!\[(.*)\]\((.*)\)$", line)
            blocks.append(("image", m.group(1), m.group(2)))
            i += 1
            continue
        if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[|:\-\s]+\|$", lines[i + 1].strip()):
            rows = []
            rows.append([c.strip() for c in line.strip().strip("|").split("|")])
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            blocks.append(("table", rows))
            continue
        if line.startswith("# "):
            blocks.append(("h1", line[2:].strip()))
            i += 1
            continue
        if line.startswith("## "):
            blocks.append(("h2", line[3:].strip()))
            i += 1
            continue
        if re.match(r"^\d+\.\s+", line):
            blocks.append(("list", re.sub(r"^\d+\.\s+", "", line)))
            i += 1
            continue
        para = [line]
        i += 1
        while i < len(lines):
            nxt = lines[i].rstrip()
            if (not nxt or nxt.startswith("#") or nxt.startswith("$$") or
                    nxt.startswith("|") or re.match(r"^!\[.*\]\(.*\)$", nxt) or
                    re.match(r"^\d+\.\s+", nxt)):
                break
            para.append(nxt)
            i += 1
        blocks.append(("paragraph", " ".join(para)))
    return blocks


def replace_citations_plain(text: str) -> str:
    def repl(match):
        keys = [k.strip().lstrip("@") for k in match.group(1).split(";")]
        return ", ".join(f"[{CITE_NUM[k]}]" for k in keys)
    return re.sub(r"\[@([^\]]+)\]", repl, text)


def set_cell_shading(cell, fill: str):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def set_cell_margins(cell, top=50, start=50, bottom=50, end=50):
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    tc_mar = tc_pr.first_child_found_in("w:tcMar")
    if tc_mar is None:
        tc_mar = OxmlElement("w:tcMar")
        tc_pr.append(tc_mar)
    for m, v in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tc_mar.find(qn(f"w:{m}"))
        if node is None:
            node = OxmlElement(f"w:{m}")
            tc_mar.append(node)
        node.set(qn("w:w"), str(v))
        node.set(qn("w:type"), "dxa")


def set_columns(section, n=2, space=360):
    sect_pr = section._sectPr
    cols = sect_pr.xpath("./w:cols")
    col = cols[0] if cols else OxmlElement("w:cols")
    col.set(qn("w:num"), str(n))
    col.set(qn("w:space"), str(space))
    if not cols:
        sect_pr.append(col)


def set_section_page(section):
    section.top_margin = Inches(0.72)
    section.bottom_margin = Inches(0.78)
    section.left_margin = Inches(0.65)
    section.right_margin = Inches(0.65)
    section.header_distance = Inches(0.25)
    section.footer_distance = Inches(0.35)


def add_page_number(section):
    p = section.footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    run._r.append(fld)


def set_run_font(run, name="Times New Roman", size=9.2, bold=None, italic=None):
    run.font.name = name
    run._element.rPr.rFonts.set(qn("w:eastAsia"), name)
    run.font.size = Pt(size)
    run.font.color.rgb = RGBColor(0, 0, 0)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic


def add_inline(paragraph, text: str, size=9.2):
    text = replace_citations_plain(text)
    pattern = re.compile(r"(\*\*.*?\*\*|`.*?`|\$.*?\$|\*.*?\*)")
    pos = 0
    for match in pattern.finditer(text):
        if match.start() > pos:
            run = paragraph.add_run(text[pos:match.start()])
            set_run_font(run, size=size)
        token = match.group(0)
        if token.startswith("**"):
            run = paragraph.add_run(token[2:-2])
            set_run_font(run, size=size, bold=True)
        elif token.startswith("`"):
            run = paragraph.add_run(token[1:-1])
            set_run_font(run, name="Consolas", size=max(7.4, size - 1.0))
        elif token.startswith("$"):
            run = paragraph.add_run(token[1:-1])
            set_run_font(run, name="Cambria Math", size=size, italic=True)
        else:
            run = paragraph.add_run(token[1:-1])
            set_run_font(run, size=size, italic=True)
        pos = match.end()
    if pos < len(text):
        run = paragraph.add_run(text[pos:])
        set_run_font(run, size=size)


def add_full_width_break(doc, columns: int):
    sec = doc.add_section(WD_SECTION.CONTINUOUS)
    set_section_page(sec)
    set_columns(sec, columns)
    add_page_number(sec)
    return sec


def build_docx(blocks):
    doc = Document()
    for sec in doc.sections:
        set_section_page(sec)
        set_columns(sec, 1)
        add_page_number(sec)

    styles = doc.styles
    normal = styles["Normal"]
    normal.font.name = "Times New Roman"
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    normal.font.size = Pt(9.2)
    normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    normal.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    normal.paragraph_format.space_after = Pt(2.3)
    normal.paragraph_format.widow_control = True

    title_seen = False
    abstract_seen = False
    in_references = False
    in_two_col = False
    pending_table_title = None
    fig_number = 0

    for idx, block in enumerate(blocks):
        kind = block[0]
        if kind == "h1" and not title_seen:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_after = Pt(6)
            r = p.add_run(block[1])
            set_run_font(r, size=17.0, bold=True)
            title_seen = True
            continue
        if kind == "h2" and block[1] == "Abstract":
            abstract_seen = True
            continue
        if kind == "h2" and block[1] == "References":
            in_references = True
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(5)
            p.paragraph_format.space_after = Pt(3)
            r = p.add_run("REFERENCES")
            set_run_font(r, size=9.5, bold=False)
            continue
        if kind == "h2" and block[1] == "Acknowledgment":
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(5)
            p.paragraph_format.space_after = Pt(3)
            r = p.add_run("ACKNOWLEDGMENT")
            set_run_font(r, size=9.5)
            continue
        if kind == "h1":
            if not in_two_col:
                add_full_width_break(doc, 2)
                in_two_col = True
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.keep_with_next = True
            p.paragraph_format.space_before = Pt(5)
            p.paragraph_format.space_after = Pt(2.5)
            r = p.add_run(block[1].upper())
            set_run_font(r, size=9.5)
            continue
        if kind == "h2":
            p = doc.add_paragraph()
            p.paragraph_format.keep_with_next = True
            p.paragraph_format.space_before = Pt(3.5)
            p.paragraph_format.space_after = Pt(1.5)
            r = p.add_run(block[1])
            set_run_font(r, size=9.2, italic=True)
            continue
        if kind == "paragraph":
            txt = block[1]
            if txt.startswith("**TABLE "):
                pending_table_title = re.sub(r"\*\*", "", txt)
                continue
            if txt.startswith("**Fig. "):
                # Captions are handled immediately after images.
                continue
            p = doc.add_paragraph()
            if not in_two_col:
                p.paragraph_format.left_indent = Inches(0.35)
                p.paragraph_format.right_indent = Inches(0.35)
            if abstract_seen and txt.startswith("**Index Terms"):
                p.paragraph_format.space_after = Pt(4)
                add_inline(p, txt, size=8.8)
                abstract_seen = False
            elif abstract_seen:
                p.paragraph_format.left_indent = Inches(0.35)
                p.paragraph_format.right_indent = Inches(0.35)
                p.paragraph_format.space_after = Pt(4)
                label = p.add_run("Abstract—")
                set_run_font(label, size=8.8, bold=True)
                add_inline(p, txt, size=8.8)
            elif in_references:
                p.paragraph_format.left_indent = Inches(0.18)
                p.paragraph_format.first_line_indent = Inches(-0.18)
                p.paragraph_format.space_after = Pt(1.0)
                add_inline(p, txt, size=7.2)
            else:
                p.paragraph_format.first_line_indent = Inches(0.14)
                add_inline(p, txt)
            continue
        if kind == "list":
            p = doc.add_paragraph(style=None)
            p.style = doc.styles["List Number"]
            p.paragraph_format.left_indent = Inches(0.22)
            p.paragraph_format.first_line_indent = Inches(-0.12)
            p.paragraph_format.space_after = Pt(1.2)
            add_inline(p, block[1])
            continue
        if kind == "equation":
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.keep_together = True
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            eq = (block[1].replace("\\qquad", "    ").replace("\\mathrm", "")
                  .replace("\\sqrt", "√").replace("\\sum", "Σ").replace("\\frac", "frac")
                  .replace("\\operatorname", "").replace("\\tfrac", "1/2 ")
                  .replace("\\bar", "bar ").replace("\\leftarrow", "←")
                  .replace("\\in", "∈").replace("\\mathbb", "R")
                  .replace("\\", ""))
            r = p.add_run(eq)
            set_run_font(r, name="Cambria Math", size=9.0, italic=True)
            continue
        if kind == "table":
            # Tables are full-width for readability.
            if in_two_col:
                add_full_width_break(doc, 1)
            if pending_table_title:
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.keep_with_next = True
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                r = p.add_run(pending_table_title.upper())
                set_run_font(r, size=8.2)
                pending_table_title = None
            rows = block[1]
            table = doc.add_table(rows=len(rows), cols=len(rows[0]))
            table.alignment = WD_TABLE_ALIGNMENT.CENTER
            table.autofit = True
            table.style = "Table Grid"
            for ri, row in enumerate(rows):
                for ci, value in enumerate(row):
                    cell = table.cell(ri, ci)
                    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
                    set_cell_margins(cell)
                    if ri == 0:
                        set_cell_shading(cell, "D9E2F3")
                    p = cell.paragraphs[0]
                    p.paragraph_format.space_after = Pt(0)
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if ri == 0 else WD_ALIGN_PARAGRAPH.LEFT
                    add_inline(p, value, size=7.2)
                    if ri == 0:
                        for r in p.runs:
                            r.bold = True
            if in_two_col:
                add_full_width_break(doc, 2)
            continue
        if kind == "image":
            fig_number += 1
            full_width = fig_number in (1, 3, 4)
            if full_width and in_two_col:
                add_full_width_break(doc, 1)
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.keep_with_next = True
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(1)
            p.add_run().add_picture(block[2], width=Inches(6.85 if full_width else 3.15))
            # Find the next caption text in the parsed stream by using alt text plus known numbering.
            cap = {
                1: "Product-aware screening and independent harmonic-diagnostic architecture. PCA, KMeans, and Isolation Forest receive the same standardized Matrix-C rows; only Isolation Forest defines the fixed label. WeightedRoll is analysed separately, and the branches are compared without confidence fusion.",
                2: "Two-component PCA projection of the standardized Matrix-C observations. Circles denote source observations, squares denote blank skies, and open diamonds outline the fixed four candidates. The projection is descriptive and does not determine or validate the label.",
                3: "Fixed Isolation Forest anomaly-score ranking for all 25 observations. Hatched bars identify the fixed candidates; annotations report selection counts across 100 tested seeds. The counts are algorithmic frequencies rather than confidence levels.",
                4: "Fractional second-harmonic coordinates for all 25 observations. Filled squares form the 13-fit blank-sky reference; open squares are excluded by the fit rule; open diamonds identify the fixed ML candidates. The cross is the component-wise sample mean plus or minus one sample standard deviation, not a confidence or detection contour.",
            }[fig_number]
            cp = doc.add_paragraph()
            cp.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            cp.paragraph_format.keep_together = True
            cp.paragraph_format.space_after = Pt(3)
            rr = cp.add_run(f"Fig. {fig_number}. ")
            set_run_font(rr, size=7.5, italic=True)
            rr = cp.add_run(cap)
            set_run_font(rr, size=7.5)
            if full_width and in_two_col:
                add_full_width_break(doc, 2)
            continue

    core = doc.core_properties
    core.title = "An Explainable AI Framework for Analysis of X-Ray Polarimetry Data from XPoSat"
    core.subject = "Guide-review IEEE conference manuscript candidate"
    core.author = "[Student authors pending guide approval]"
    core.comments = "Generated from the controlled Phase-5 canonical manuscript."
    doc.save(DOCX_OUT)


def tex_escape_plain(text: str) -> str:
    repl = {
        "&": r"\&", "%": r"\%", "#": r"\#", "_": r"\_",
        "≤": r"$\leq$", "≥": r"$\geq$", "×": r"$\times$",
        "–": "--", "—": "---", "’": "'", "“": "``", "”": "''",
    }
    for a, b in repl.items():
        text = text.replace(a, b)
    return text


def tex_inline(text: str) -> str:
    def cite_repl(match):
        keys = [k.strip().lstrip("@") for k in match.group(1).split(";")]
        return "\\cite{" + ",".join(keys) + "}"
    text = re.sub(r"\[@([^\]]+)\]", cite_repl, text)
    protected = []
    def protect(value):
        protected.append(value)
        return f"@@PROT{len(protected)-1}@@"
    text = re.sub(r"\$.*?\$", lambda m: protect(m.group(0)), text)
    text = re.sub(r"\\cite\{[^}]+\}", lambda m: protect(m.group(0)), text)
    text = re.sub(r"`(.*?)`", lambda m: protect("\\texttt{" + tex_escape_plain(m.group(1)) + "}"), text)
    text = re.sub(r"\*\*(.*?)\*\*", lambda m: protect("\\textbf{" + tex_escape_plain(m.group(1)) + "}"), text)
    text = re.sub(r"\*(.*?)\*", lambda m: protect("\\emph{" + tex_escape_plain(m.group(1)) + "}"), text)
    text = tex_escape_plain(text)
    for i, value in enumerate(protected):
        text = text.replace(f"@@PROT{i}@@", value)
    return text


def table_to_tex(rows, title: str, label: str) -> str:
    cols = len(rows[0])
    spec = "p{" + str(round(0.94 / cols, 3)) + r"\textwidth}" * cols
    spec = "".join([r"p{" + str(round(0.94 / cols, 3)) + r"\textwidth}" for _ in range(cols)])
    out = [r"\begin{table*}[t]", r"\centering", r"\caption{" + tex_inline(title) + "}", r"\label{" + label + "}", r"\footnotesize", r"\begin{tabular}{" + spec + "}", r"\toprule"]
    out.append(" & ".join(tex_inline(c) for c in rows[0]) + r" \\")
    out.append(r"\midrule")
    for row in rows[1:]:
        out.append(" & ".join(tex_inline(c) for c in row) + r" \\")
    out.extend([r"\bottomrule", r"\end{tabular}", r"\end{table*}"])
    return "\n".join(out)


def build_tex(blocks):
    title = blocks[0][1]
    out = [
        r"\documentclass[conference]{IEEEtran}",
        r"\usepackage{amsmath,amssymb,booktabs,graphicx,array}",
        r"\usepackage[hidelinks]{hyperref}",
        r"\title{" + tex_inline(title) + "}",
        "\\author{\\IEEEauthorblockN{[Student Author 1], [Student Author 2], [Student Author 3], and [Student Author 4]}%\n"
        "\\IEEEauthorblockA{[Department], [Institution], [City, Country]\\\\\n"
        "[author emails to be inserted after guide approval]}}",
        r"\begin{document}", r"\maketitle",
    ]
    in_abstract = False
    in_refs = False
    in_enum = False
    abstract_started = False
    pending_table_title = ""
    fig_number = 0
    table_number = 0
    for block in blocks[1:]:
        kind = block[0]
        if in_enum and kind != "list":
            out.append(r"\end{enumerate}")
            in_enum = False
        if kind == "h2" and block[1] == "Abstract":
            in_abstract = True
            abstract_started = True
            out.append(r"\begin{abstract}")
            continue
        if not abstract_started:
            # Author and affiliation lines are already represented by \author.
            continue
        if kind == "h2" and block[1] == "References":
            in_refs = True
            continue
        if in_refs:
            continue
        if kind == "h1":
            out.append(r"\section{" + tex_inline(re.sub(r"^[IVX]+\.\s*", "", block[1])) + "}")
        elif kind == "h2":
            if block[1] == "Acknowledgment":
                out.append(r"\section*{Acknowledgment}")
            else:
                out.append(r"\subsection{" + tex_inline(re.sub(r"^[A-Z]\.\s*", "", block[1])) + "}")
        elif kind == "paragraph":
            txt = block[1]
            if in_abstract and txt.startswith("**Index Terms"):
                out.append(r"\end{abstract}")
                terms = re.sub(r"^\*\*Index Terms[^*]*\*\*\s*", "", txt)
                out.append(r"\begin{IEEEkeywords}" + tex_inline(terms) + r"\end{IEEEkeywords}")
                in_abstract = False
            elif in_abstract:
                out.append(tex_inline(txt))
            elif txt.startswith("**TABLE "):
                pending_table_title = re.sub(r"\*\*", "", txt)
                pending_table_title = re.sub(r"^TABLE [IVX]+\s*[—-]\s*", "", pending_table_title)
            elif txt.startswith("**Fig. "):
                pass
            else:
                out.append(tex_inline(txt) + "\n")
        elif kind == "list":
            if not in_enum:
                out.append(r"\begin{enumerate}")
                in_enum = True
            out.append(r"\item " + tex_inline(block[1]))
        elif kind == "equation":
            out.append(r"\begin{equation*}" + "\n" + block[1] + "\n" + r"\end{equation*}")
        elif kind == "table":
            table_number += 1
            out.append(table_to_tex(block[1], pending_table_title, f"tab:{table_number}"))
            pending_table_title = ""
        elif kind == "image":
            fig_number += 1
            path = Path(block[2]).as_posix()
            caps = {
                1: "Product-aware screening and independent harmonic-diagnostic architecture. PCA, KMeans, and Isolation Forest receive the same standardized Matrix-C rows; only Isolation Forest defines the fixed label. WeightedRoll is analysed separately, and the branches are compared without confidence fusion.",
                2: "Two-component PCA projection of the standardized Matrix-C observations. Circles denote source observations, squares denote blank skies, and open diamonds outline the fixed four candidates. The projection is descriptive and does not determine or validate the label.",
                3: "Fixed Isolation Forest anomaly-score ranking for all 25 observations. Hatched bars identify the fixed candidates; annotations report selection counts across 100 tested seeds. The counts are algorithmic frequencies rather than confidence levels.",
                4: "Fractional second-harmonic coordinates for all 25 observations. Filled squares form the 13-fit blank-sky reference; open squares are excluded by the fit rule; open diamonds identify the fixed ML candidates. The cross is the component-wise sample mean plus or minus one sample standard deviation, not a confidence or detection contour.",
            }
            env = "figure" if fig_number == 2 else "figure*"
            width = r"\columnwidth" if fig_number == 2 else r"0.96\textwidth"
            out.extend([
                rf"\begin{{{env}}}[t]", r"\centering",
                rf"\includegraphics[width={width}]{{{path}}}",
                r"\caption{" + tex_inline(caps[fig_number]) + "}",
                rf"\label{{fig:{fig_number}}}", rf"\end{{{env}}}",
            ])
    if in_enum:
        out.append(r"\end{enumerate}")
    out.extend([
        r"\bibliographystyle{IEEEtran}",
        r"\bibliography{MALDIVES_Part_04_References}",
        r"\end{document}",
    ])
    TEX_OUT.write_text("\n\n".join(out), encoding="utf-8")


def main():
    text = MASTER.read_text(encoding="utf-8")
    blocks = parse_blocks(text)
    build_docx(blocks)
    build_tex(blocks)
    print(f"Wrote {DOCX_OUT}")
    print(f"Wrote {TEX_OUT}")


if __name__ == "__main__":
    main()
