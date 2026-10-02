#!/usr/bin/env python3
"""Generate internal noindex review galleries from the migration inventory."""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent
INV = json.loads((ROOT / "content/current-site-inventory.json").read_text(encoding="utf-8"))

def notes_review():
    photos = INV["pages"]["notes_of_resistance"]["images"]
    cards = []
    for i, p in enumerate(photos, 1):
        loading = ' loading="lazy"' if i > 6 else ''
        cards.append(
            f'<figure><img src="{p["source_url"]}?format=1000w" alt="Notes of Resistance archival sample, image {i:02d} — description pending"{loading} decoding="async">'
            f'<figcaption><b>{i:02d}</b> {escape(p["filename"])}</figcaption></figure>'
        )
    return """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Review — Notes of Resistance full archive</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#f2efe7;color:#111;font:14px/1.45 system-ui,sans-serif}
header{position:sticky;top:0;z-index:10;background:rgba(242,239,231,.96);border-bottom:1px solid #ccc6b9;padding:16px 22px}
h1{margin:0 0 4px;font:400 28px Georgia,serif}p{margin:0;color:#5d594f}.grid{padding:22px;display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:26px 14px}
figure{margin:0}img{display:block;width:100%;height:auto;background:#ddd6c8}figcaption{padding-top:7px;font-size:12px;color:#5d594f;word-break:break-word}figcaption b{color:#111;margin-right:7px}
.notice{padding:12px 22px;background:#17345f;color:white}.notice a{color:white}
@media(max-width:600px){.grid{grid-template-columns:1fr 1fr;padding:12px;gap:18px 8px}header{padding:12px}}
</style></head><body>
<header><h1>Notes of Resistance — full current archive</h1><p>86 images captured from the live Squarespace page for migration review. This page is not part of the public navigation.</p></header>
<div class="notice">Sample CDN files only. Final production should use Nora's approved originals and proper captions / alt text.</div>
<main class="grid">""" + "\n".join(cards) + """</main></body></html>"""

if __name__ == "__main__":
    out = ROOT / "review/notes-of-resistance/index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(notes_review(), encoding="utf-8")
    print("built review gallery")
