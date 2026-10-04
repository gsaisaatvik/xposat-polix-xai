from pathlib import Path
import runpy
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
TEMP_ROOT = ROOT / "qa_temp"
TEMP_ROOT.mkdir(parents=True, exist_ok=True)
tempfile.tempdir = str(TEMP_ROOT)

RENDERER = Path(r"C:\Users\Saatvik\.codex\plugins\cache\openai-primary-runtime\documents\26.802.11031\skills\documents\render_docx.py")
DOCX = ROOT / "MALDIVES_Part_02_IEEE_Manuscript.docx"
OUTPUT = ROOT / "qa_render"
OUTPUT.mkdir(parents=True, exist_ok=True)

sys.argv = [str(RENDERER), str(DOCX), "--output_dir", str(OUTPUT)]
runpy.run_path(str(RENDERER), run_name="__main__")
