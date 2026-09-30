#!/usr/bin/env python3
"""Prepare the static prototype for GitHub Pages preview hosting.

The production prototype uses root-relative URLs (/work/, /assets/...). GitHub
project Pages is served under /norasayyad.com/, so this creates an isolated
_site/ copy and prefixes only internal root-relative URLs. Source files remain
unchanged.
"""
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "_site"
RUNTIME_ITEMS = [
    "index.html", "work", "about", "services", "news", "contact", "fi",
    "presentation", "opcoes", "review", "assets",
]

def normalize_base(value: str) -> str:
    value = "/" + value.strip("/")
    return "" if value == "/" else value

def rewrite_html(text: str, base: str) -> str:
    if not base:
        return text
    # Prefix root-relative navigation/assets only; leave protocol-relative and
    # external URLs alone.
    text = re.sub(r'(?P<attr>href|src|action)="(/(?!/))', rf'\g<attr>="{base}/', text)
    # Avoid duplicated slashes after the prefix.
    text = text.replace(base + "//", base + "/")
    return text

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-path", default="/norasayyad.com")
    args = parser.parse_args()
    base = normalize_base(args.base_path)

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    for item in RUNTIME_ITEMS:
        src = ROOT / item
        if not src.exists():
            continue
        dst = OUT / item
        if src.is_dir():
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)

    for path in OUT.rglob("*.html"):
        content = path.read_text(encoding="utf-8")
        path.write_text(rewrite_html(content, base), encoding="utf-8")

    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Prepared GitHub Pages preview at {OUT} with base path {base or '/'}")

if __name__ == "__main__":
    main()
