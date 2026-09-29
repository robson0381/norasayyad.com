#!/usr/bin/env python3
"""Lightweight QA checks for the generated static prototype."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).parent
HTML = [p for p in ROOT.rglob("*.html") if ".git" not in p.parts]
SKIP_DIRS = {"opcoes/v1", "opcoes/v2"}

def route_for(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[:-10]
    return "/" + rel

def should_skip(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    return any(rel.startswith(prefix + "/") for prefix in SKIP_DIRS)

routes = {route_for(p): p for p in HTML if not should_skip(p)}
issues: list[str] = []

for route, path in sorted(routes.items()):
    text = path.read_text(encoding="utf-8")
    if '<meta name="viewport"' not in text:
        issues.append(f"{route}: missing viewport")
    ids = re.findall(r'\bid="([^"]+)"', text)
    duplicate_ids = sorted({x for x in ids if ids.count(x) > 1})
    if duplicate_ids:
        issues.append(f"{route}: duplicate ids {duplicate_ids}")

    for tag in re.findall(r"<img\b[^>]*>", text, flags=re.I | re.S):
        if not re.search(r"\balt=", tag, flags=re.I):
            issues.append(f"{route}: image without alt")

    if re.search(r'class=(?:"todo"|todo)', text):
        issues.append(f"{route}: visible todo marker")

    for href in re.findall(r'href="([^"]+)"', text):
        if not href.startswith("/") or href.startswith("//"):
            continue
        clean = href.split("?", 1)[0].split("#", 1)[0]
        if clean.startswith("/assets/"):
            asset = ROOT / clean.lstrip("/")
            if not asset.exists():
                issues.append(f"{route}: missing asset {clean}")
            continue
        if clean in ("", "/"):
            continue
        if any(clean.lstrip("/").startswith(prefix + "/") or clean.lstrip("/") == prefix for prefix in SKIP_DIRS):
            continue
        normalized = clean if clean.endswith("/") else clean + "/"
        if normalized not in routes and clean not in routes:
            issues.append(f"{route}: unresolved internal link {href}")

    if route.startswith("/review/") or route.startswith("/presentation/"):
        if "noindex" not in text:
            issues.append(f"{route}: internal page missing noindex")

print(f"Checked {len(routes)} HTML routes")
if issues:
    print(f"FAIL: {len(issues)} issue(s)")
    for issue in issues:
        print(" -", issue)
    raise SystemExit(1)

print("PASS: no structural QA issues found")
