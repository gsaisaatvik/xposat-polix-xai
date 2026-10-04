from pathlib import Path
import json
import re
from difflib import SequenceMatcher

ROOT = Path(r"D:\polix_xai_webapp\research_paper_ieee\guide_approved_final_run")
FRIEND = json.loads((ROOT / "final_friend_review" / "paragraphs.json").read_text(encoding="utf-8"))
CONTROL = (ROOT / "07_SINGAPORE_DELIVERY" / "SINGAPORE_Part_00_Controlled_Manuscript.md").read_text(encoding="utf-8")

def norm(s):
    s = re.sub(r"\[@[^\]]+\]", "", s)
    s = re.sub(r"\[[0-9,;\- ]+\]", "", s)
    s = s.replace("**", "").replace("#", "")
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s

control_paras = [norm(p) for p in re.split(r"\n\s*\n", CONTROL) if norm(p)]
out = []
for p in FRIEND:
    txt = p["text"]
    if not txt or len(txt) < 35:
        continue
    nt = norm(txt)
    best = max((SequenceMatcher(None, nt, cp).ratio(), cp) for cp in control_paras)
    if best[0] < 0.965:
        out.append({"paragraph": p["index"], "style": p["style"], "similarity": round(best[0], 3), "text": txt, "best_control": best[1][:500]})

(ROOT / "final_friend_review" / "differences_from_controlled.json").write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"DIFFERENT_PARAGRAPHS={len(out)}")
for item in out:
    print(f"P{item['paragraph']} sim={item['similarity']}: {item['text'][:600]}")
