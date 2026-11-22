#!/usr/bin/env python3
"""Shrink photos before committing them.

Usage:
    pip install pillow
    python tools/optimize_images.py photo1.jpg photo2.png ...      # -> assets/img/*.webp
    python tools/optimize_images.py --width 1200 --quality 75 *.jpg

Each image is resized to at most --width px wide (default 1600), EXIF rotation
is applied, metadata (incl. GPS) is stripped, and it is saved as WebP into
assets/img/. A typical 6 MB phone photo ends up around 150-300 kB.
"""
import argparse
import pathlib
import sys

from PIL import Image, ImageOps

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "img"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("images", nargs="+", type=pathlib.Path)
    ap.add_argument("--width", type=int, default=1600)
    ap.add_argument("--quality", type=int, default=80)
    args = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    for src in args.images:
        img = ImageOps.exif_transpose(Image.open(src))
        if img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGB")
        if img.width > args.width:
            img = img.resize((args.width, round(img.height * args.width / img.width)), Image.LANCZOS)
        dst = OUT / (src.stem.lower().replace(" ", "-") + ".webp")
        img.save(dst, "WEBP", quality=args.quality, method=6)
        print(f"{src.name:40s} {src.stat().st_size/1e6:6.2f} MB -> {dst.relative_to(ROOT)}  "
              f"{dst.stat().st_size/1e3:6.0f} kB  ({img.width}x{img.height})")
    print('\nIn HTML use: <img src="../assets/img/NAME.webp" alt="..." width="W" height="H" loading="lazy">')
    return 0


if __name__ == "__main__":
    sys.exit(main())
