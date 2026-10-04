from pathlib import Path
import json
import zipfile
from lxml import etree

DOCX = Path(r"D:\polix_xai_webapp\research_paper_ieee\guide_approved_final_run\final_friend_review\confrenece_temp_final_review_copy.docx")
OUT = DOCX.parent
NS = {}

def text_of(node):
    parts = []
    for child in node.iter():
        if child.tag in {f"{{{NS['w']}}}t", f"{{{NS['w']}}}delText", f"{{{NS['m']}}}t"} and child.text:
            parts.append(child.text)
        elif child.tag == f"{{{NS['w']}}}tab":
            parts.append("\t")
        elif child.tag == f"{{{NS['w']}}}br":
            parts.append("\n")
    return "".join(parts)

with zipfile.ZipFile(DOCX) as z:
    names = set(z.namelist())
    root = etree.fromstring(z.read("word/document.xml"))
    NS.update({key: root.nsmap[key] for key in ("w", "m", "wp") if key in root.nsmap})
    body = root.find("w:body", NS)
    lines = []
    paragraphs = []
    tables = []
    p_index = 0
    t_index = 0
    for child in body:
        if child.tag == f"{{{NS['w']}}}p":
            p_index += 1
            txt = text_of(child).strip()
            style = child.find("w:pPr/w:pStyle", NS)
            style_val = style.get(f"{{{NS['w']}}}val") if style is not None else ""
            paragraphs.append({"index": p_index, "style": style_val, "text": txt})
            if txt:
                lines.append(f"[P{p_index:04d} style={style_val or 'Normal'}] {txt}")
        elif child.tag == f"{{{NS['w']}}}tbl":
            t_index += 1
            rows = []
            for tr in child.findall("w:tr", NS):
                row = [text_of(tc).strip().replace("\n", " ") for tc in tr.findall("w:tc", NS)]
                rows.append(row)
            tables.append({"index": t_index, "rows": rows})
            lines.append(f"[TABLE {t_index}]")
            for row in rows:
                lines.append(" | ".join(row))
    metadata = {
        "paragraph_count": p_index,
        "table_count": t_index,
        "image_count": len([n for n in names if n.startswith("word/media/")]),
        "equation_count": len(root.xpath(".//m:oMath", namespaces=NS)),
        "tracked_insertions": len(root.xpath(".//w:ins", namespaces=NS)),
        "tracked_deletions": len(root.xpath(".//w:del", namespaces=NS)),
        "comments_part": "word/comments.xml" in names,
        "sectPr_count": len(root.xpath(".//w:sectPr", namespaces=NS)),
        "package_files": len(names),
    }
    if "docProps/core.xml" in names:
        core = etree.fromstring(z.read("docProps/core.xml"))
        metadata["core_properties"] = {etree.QName(n).localname: n.text for n in core if n.text}
    if "word/comments.xml" in names:
        comments = etree.fromstring(z.read("word/comments.xml"))
        metadata["comments"] = [{"id": c.get(f"{{{NS['w']}}}id"), "text": text_of(c)} for c in comments]
    media = []
    for name in sorted(n for n in names if n.startswith("word/media/")):
        data = z.read(name)
        target = OUT / "media" / Path(name).name
        target.parent.mkdir(exist_ok=True)
        target.write_bytes(data)
        media.append({"name": name, "bytes": len(data), "output": str(target)})
    metadata["media"] = media

(OUT / "extracted_text.txt").write_text("\n\n".join(lines), encoding="utf-8")
(OUT / "paragraphs.json").write_text(json.dumps(paragraphs, indent=2, ensure_ascii=False), encoding="utf-8")
(OUT / "tables.json").write_text(json.dumps(tables, indent=2, ensure_ascii=False), encoding="utf-8")
(OUT / "document_metadata.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(metadata, indent=2, ensure_ascii=False))
