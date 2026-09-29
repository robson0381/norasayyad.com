#!/usr/bin/env python3
"""Static QA for the Nora Sayyad redesign prototype.

Run after the generators:
    python3 build.py
    python3 build_options.py
    python3 build_review.py
    python3 qa.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).parent
MAIN_PAGES = [
    Path("index.html"),
    Path("work/index.html"),
    Path("work/portraits/index.html"),
    Path("work/from-arrival-to-belonging/index.html"),
    Path("work/parfyymin-tuulahdus/index.html"),
    Path("work/notes-of-resistance/index.html"),
    Path("about/index.html"),
    Path("services/index.html"),
    Path("news/index.html"),
    Path("contact/index.html"),
]
errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def internal_target_exists(href: str) -> bool:
    path = urlsplit(href).path
    if not path or path == "/":
        return (ROOT / "index.html").exists()
    if not path.startswith("/"):
        return True
    rel = path.lstrip("/")
    candidates = [
        ROOT / rel,
        ROOT / f"{rel}.html",
        ROOT / rel / "index.html",
    ]
    return any(p.is_file() for p in candidates)


for rel in MAIN_PAGES:
    path = ROOT / rel
    if not path.exists():
        err(f"{rel}: missing generated page")
        continue

    html = path.read_text(encoding="utf-8")
    if len(re.findall(r"<h1\b", html, flags=re.I)) != 1:
        err(f"{rel}: expected exactly one H1")

    if '<meta name="robots" content="noindex,nofollow">' not in html:
        err(f"{rel}: prototype must remain noindex until launch")

    ids = re.findall(r'\bid="([^"]+)"', html)
    duplicates = sorted({value for value in ids if ids.count(value) > 1})
    if duplicates:
        err(f"{rel}: duplicate ids: {', '.join(duplicates)}")

    for n, tag in enumerate(re.findall(r"<img\b[^>]*>", html, flags=re.I), 1):
        if not re.search(r"\balt=", tag):
            err(f"{rel}: image {n} missing alt")

    if re.search(r'<form\b[^>]*action="#"', html):
        err(f"{rel}: dead prototype form action=#")

    if 'data-hero-slide' in html:
        hero_tags = re.findall(r'<figure\b[^>]*data-hero-slide[^>]*>', html)
        if len(hero_tags) != 5:
            err(f"{rel}: expected 5 hero slides, found {len(hero_tags)}")
        for tag in hero_tags:
            if not re.search(r'aria-hidden="(?:true|false)"', tag):
                err(f"{rel}: malformed hero aria-hidden attribute")

    if 'href="/assets/nora-sayyad-cv.pdf"' in html:
        err(f"{rel}: references a CV PDF that is not in the repository")

    for href in re.findall(r'href="([^"]+)"', html):
        if href == "#":
            err(f"{rel}: dead href=#")
        if href.startswith("/") and not href.startswith("//") and not internal_target_exists(href):
            err(f"{rel}: broken internal link {href}")

    todos = len(re.findall(r'class=["\']?todo\b', html))
    if todos:
        warn(f"{rel}: {todos} content item(s) still need Nora's confirmation")

photos = json.loads((ROOT / "content/photos.json").read_text(encoding="utf-8"))
structured = sum(len(v) if isinstance(v, list) else 1 for v in photos.values())
if structured != 58:
    err(f"content/photos.json: expected 66 structured references, found {structured}")

inventory = json.loads((ROOT / "content/current-site-inventory.json").read_text(encoding="utf-8"))
notes = inventory["pages"]["notes_of_resistance"]["images"]
if len(notes) != 86:
    err(f"current-site-inventory.json: expected 86 Notes of Resistance entries, found {len(notes)}")

for required in [
    "SPEC.md",
    "MIGRATION_MAP.md",
    "content/redirects.json",
    "presentation/index.html",
    "opcoes/memoria/index.html",
    "review/notes-of-resistance/index.html",
]:
    if not (ROOT / required).exists():
        err(f"missing required project artifact: {required}")

print(f"QA: {len(MAIN_PAGES)} main pages · {structured} structured images · {len(notes)} Notes archive entries")
for item in warnings:
    print("WARNING:", item)
for item in errors:
    print("ERROR:", item)

if errors:
    sys.exit(1)

print("QA passed")
