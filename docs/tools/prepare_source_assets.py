"""Prepare selected, source-labelled educational images for the Vue portal.

This script only crops rendered pages already stored under source_material. It
does not alter the source PDFs and performs no scientific computation.
"""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_material" / "polix_handbook_2025"
OUTPUT = ROOT / "frontend" / "public" / "assets" / "mission"
OUTPUT.mkdir(parents=True, exist_ok=True)


def crop(source_name: str, output_name: str, box: tuple[int, int, int, int]) -> None:
    with Image.open(SOURCE / source_name) as image:
        region = image.crop(box)
        region.save(OUTPUT / output_name, optimize=True)


crop(
    "page-10-instrument.png",
    "polix-instrument-labelled-source.png",
    (310, 700, 920, 1195),
)
crop(
    "page-17-level2-pipeline.png",
    "polix-level2-pipeline-source.png",
    (145, 70, 1090, 835),
)
crop(
    "page-24-level2-tree.png",
    "polix-level2-tree-source.png",
    (120, 145, 1130, 1450),
)
crop(
    "page-67-weightedroll.png",
    "weightedroll-columns-source.png",
    (85, 285, 1150, 625),
)
