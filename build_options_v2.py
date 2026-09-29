#!/usr/bin/env python3
"""Generate four home-page directions for Nora, grounded in her own work.

Run: python3 build_options.py  ->  opcoes/<a|b|c|d>/index.html + opcoes/index.html
Only the home page changes; links go to the existing inner pages.
The previous round lives, frozen, in opcoes/v1/.

What each direction borrows from Nora's Instagram and CV:
  A Reportagem  — her press work (Washington Post, The Times, Selkomedia) as a newspaper front page
  B Cartas      — her first-person letters, diaries and poems; the refugee-route typography of
                  "Letters to Mothers" (2026)
  C Tatreez     — the palette of her bio (🫒🕊️🧿🌊) and the red cross-stitch of Palestinian embroidery
  D Sequências  — she thinks in carousels of ~10 frames; every project is a swipeable sequence
"""
import re
from pathlib import Path

from build import PHOTOS, PROJECTS, EMAIL, img

ROOT = Path(__file__).parent / "opcoes"
N, PO, AR, PA = (PHOTOS[k] for k in ("notes-of-resistance", "portraits", "from-arrival-to-belonging", "parfyymin-tuulahdus"))

STATEMENT = ("Finnish-Palestinian photographer, artist and visual reporter whose experimental lens "
             "moves between documentary and fictional storytelling.")
QUOTE = "Photography can become a space for memory, dialogue and self-determination."
PRESS = [
    ("The Washington Post", "2025", "How is ‘happiness’ measured around the world?", "Photographed in Finland, the world’s “happiest country” for the eighth time."),
    ("The Times", "2026", "Finland’s plan to be the most financially literate nation", "Assignment at Yrityskylä, where children learn how money moves through society."),
]
WRITTEN = [
    ("Selkomedia", "2025", "Lara Salous — a Palestinian artist visits Finland"),
    ("Selkomedia", "2025", "Fayez Bassalat — learning Finnish in record time"),
    ("Selkomedia", "2025", "Shadia Rask — Alumni of the Year, University of Helsinki"),
]
EXHIB = [
    ("On tour", "The Lost Paintings: A Prelude to Return", "Montréal · Boston · New York · Belfast · London · Bristol", "53 artists · Nora’s still life <em>Utopia</em> (2023)"),
    ("Touring Finland", "From Arrival to Belonging? A Decade in Portraits", "Stoa, Helsinki → Valkea, Oulu → IKEA", "With Startup Refugees, 2025–26"),
    ("Draft exhibition", "Visible Palestine", "HIAP, Suomenlinna · December 2025", "Portraits, interviews and protest photography"),
]
CREDS = ["The Washington Post", "The Times", "Helsinki City Museum", "Finnish Museum of Photography",
         "HIAP", "Bristol Museum & Art Gallery", "National Library of Finland"]
# From "Letters to Mothers & Daughter–Father Relationships" (2026): a father's search for citizenship
ROUTE = ["Gaza, Palestine", "Egypt", "Kuwait", "United Arab Emirates", "Egypt", "UAE", "Jordan",
         "Egypt", "Syria", "UAE", "Sudan", "Syria", "Finland"]
YEARS = {"notes-of-resistance": "2020–", "portraits": "2017–", "from-arrival-to-belonging": "2025–26",
         "parfyymin-tuulahdus": "2023", "from-a-parallel-life": "New project"}
NEW = ("Letters to Mothers & Daughter–Father Relationships", "2026",
       "A father who has spent his whole life searching for citizenship, and the daughter who carries his story.")


def strip(s):
    return re.sub(r"<[^>]+>", "", s)


def stitch(color, bg="transparent"):
    """Small original cross-stitch motif (tatreez-inspired) as an SVG data URI."""
    c, b = color.replace("#", "%23"), bg.replace("#", "%23")
    return ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E"
            f"%3Crect width='24' height='24' fill='{b}'/%3E"
            f"%3Cg fill='{c}'%3E%3Crect x='10' y='2' width='4' height='4'/%3E%3Crect x='6' y='6' width='4' height='4'/%3E"
            "%3Crect x='14' y='6' width='4' height='4'/%3E%3Crect x='2' y='10' width='4' height='4'/%3E%3Crect x='18' y='10' width='4' height='4'/%3E"
            "%3Crect x='6' y='14' width='4' height='4'/%3E%3Crect x='14' y='14' width='4' height='4'/%3E%3Crect x='10' y='18' width='4' height='4'/%3E"
            "%3Crect x='10' y='10' width='4' height='4'/%3E%3C/g%3E%3C/svg%3E\")")


def cover(p):
    return PHOTOS[p["slug"]][p["cover"]]


SWITCH = ".switch{position:fixed;right:12px;bottom:12px;z-index:90;background:#111;color:#fff;font:500 13px/1 system-ui,sans-serif;padding:10px 14px;border-radius:999px;text-decoration:none;box-shadow:0 4px 18px rgba(0,0,0,.25)}"


def doc(title, fonts, css, body, script=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Nora Sayyad — {title}</title>
<meta name="description" content="Nora Sayyad is a Finnish-Palestinian documentary photographer and visual artist in Helsinki, published in The Washington Post and The Times.">
<meta name="robots" content="noindex">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box}}
html{{-webkit-text-size-adjust:100%}}
body{{margin:0;overflow-x:hidden}}
img{{max-width:100%;display:block;height:auto}}
a{{color:inherit}}
h1,h2,h3,p,figure{{margin:0}}
:focus-visible{{outline:2px solid currentColor;outline-offset:3px}}
.skip{{position:absolute;left:-999px}}.skip:focus{{left:8px;top:8px;z-index:99;background:#000;color:#fff;padding:8px}}
.ar{{font-family:'Noto Naskh Arabic',serif}}
{css}
{SWITCH}
</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{body}
<a class="switch" href="/opcoes/">← Todas as opções</a>
{script}
</body>
</html>
"""


# ================================================================ A · Reportagem
def option_a():
    css = """
:root{--ink:#141414;--soft:#5b5b5b;--line:#141414;--red:#b3261e}
body{background:#fff;color:var(--ink);font:400 16px/1.55 'Archivo',system-ui,sans-serif}
.serif{font-family:'Source Serif 4',Georgia,serif}
.wrap{max-width:1360px;margin:0 auto;padding:0 clamp(16px,3vw,36px)}
.top{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;border-bottom:1px solid var(--line);padding:12px 0;font-size:.78rem;text-transform:uppercase;letter-spacing:.08em}
.top nav{display:flex;gap:20px}.top a{text-decoration:none}
.mast{display:flex;align-items:flex-end;justify-content:space-between;gap:20px;padding:clamp(16px,3vw,30px) 0 clamp(8px,1.5vw,16px);border-bottom:6px solid var(--line)}
.mast h1{font-stretch:62%;font-weight:800;font-size:clamp(3.6rem,14vw,13rem);line-height:.82;letter-spacing:-.02em;text-transform:uppercase}
.mast .ar{font-size:clamp(1.6rem,4vw,3.4rem);line-height:1.2;color:var(--red);white-space:nowrap}
.dl{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;padding:10px 0;border-bottom:1px solid var(--line);font-size:.8rem;text-transform:uppercase;letter-spacing:.06em}
.kick{font-size:.74rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--red)}
.lead{display:grid;grid-template-columns:2fr 1fr;border-bottom:1px solid var(--line)}
.lead figure{padding:24px 24px 24px 0;border-right:1px solid var(--line)}
.lead figcaption{font-size:.8rem;color:var(--soft);margin-top:8px}
.lead aside{padding:24px 0 24px 24px;display:flex;flex-direction:column;gap:20px}
.lead h2{font-stretch:75%;font-weight:700;font-size:clamp(1.8rem,3vw,2.6rem);line-height:1.02;text-transform:uppercase}
.btns{display:flex;gap:10px;flex-wrap:wrap}
.btn{display:inline-block;background:var(--ink);color:#fff;text-decoration:none;padding:12px 18px;font-weight:600;font-size:.88rem;text-transform:uppercase;letter-spacing:.05em}
.btn.red{background:var(--red)}
.assign{border-top:1px solid var(--line);padding-top:14px;display:grid;gap:16px}
.assign b{display:block;font-stretch:75%;font-size:1.15rem;text-transform:uppercase;line-height:1.1;margin-top:2px}
.assign p{font-size:.98rem;color:var(--soft)}
.sec{display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid var(--line);padding:36px 0 10px}
.sec h2{font-stretch:62%;font-weight:800;font-size:clamp(2rem,5vw,3.6rem);text-transform:uppercase;line-height:1}
.index{list-style:none;margin:0;padding:0}
.index a,.index .row{display:grid;grid-template-columns:70px 1fr 200px 110px;gap:20px;align-items:center;padding:16px 0;border-bottom:1px solid var(--line);text-decoration:none}
.index a:hover{background:#f6f3ee}
.n{font-stretch:62%;font-weight:800;font-size:2.4rem;color:var(--red)}
.index h3{font-stretch:75%;font-weight:700;font-size:clamp(1.25rem,2.3vw,1.9rem);text-transform:uppercase;line-height:1.05}
.index p{color:var(--soft);margin-top:4px}
.index img{aspect-ratio:3/2;object-fit:cover;width:100%}
.y{font-size:.82rem;text-transform:uppercase;letter-spacing:.06em;text-align:right}
.new{display:inline-block;background:var(--red);color:#fff;font-size:.66rem;font-weight:700;letter-spacing:.08em;padding:2px 6px;vertical-align:middle;margin-left:8px}
.ph{aspect-ratio:3/2;background:repeating-linear-gradient(45deg,#f1eee9,#f1eee9 6px,#e6e2da 6px,#e6e2da 12px);display:grid;place-items:center;font-size:.7rem;color:#666;text-align:center;padding:6px}
.cols{display:grid;grid-template-columns:repeat(3,1fr);border-bottom:1px solid var(--line)}
.cols > div{padding:24px 24px 28px 0}
.cols > div + div{border-left:1px solid var(--line);padding-left:24px}
.cols h3{font-stretch:62%;font-weight:800;font-size:clamp(1.6rem,2.6vw,2.2rem);line-height:.98;text-transform:uppercase;margin:8px 0}
.cols p{font-size:.98rem}
.cols small{display:block;color:var(--soft);margin-top:6px;font-size:.9rem}
.byline{display:grid;grid-template-columns:1fr 2fr;gap:24px;padding:28px 0;border-bottom:6px solid var(--line)}
.byline h2{font-stretch:62%;font-weight:800;font-size:2.2rem;text-transform:uppercase;line-height:1;margin-top:8px}
.byline ul{list-style:none;margin:0;padding:0}
.byline li{display:flex;justify-content:space-between;gap:16px;padding:10px 0;border-bottom:1px solid #ddd;font-size:1.02rem}
.byline li span:last-child{color:var(--soft);white-space:nowrap;font-size:.85rem;text-transform:uppercase;letter-spacing:.04em}
footer{display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;padding:18px 0 64px;font-size:.8rem;text-transform:uppercase;letter-spacing:.06em}
@media (max-width:860px){
 .lead,.cols,.byline{grid-template-columns:1fr}
 .lead figure{padding-right:0;border-right:0}.lead aside{padding-left:0}
 .cols > div + div{border-left:0;padding-left:0;border-top:1px solid var(--line)}
 .index a,.index .row{grid-template-columns:44px 1fr;gap:12px}
 .n{font-size:1.8rem}.index img,.index .ph{grid-column:1/-1;order:-1}.y{display:none}
 .top nav{display:none}.mast{flex-direction:column;align-items:flex-start}
 .byline li{flex-direction:column;gap:2px}
}
"""
    rows = f"""<li><div class="row"><span class="n">00</span><div><h3>{NEW[0]}<span class="new">NEW</span></h3><p class="serif">{NEW[2]}</p></div><div class="ph">Photos from the 2026 essay</div><span class="y">{NEW[1]}</span></div></li>"""
    rows += "".join(f"""<li><a href="/work/{p['slug']}/"><span class="n">{i+1:02d}</span><div><h3>{p['title']}</h3><p class="serif">{p['teaser']}</p></div>{img(cover(p), "(max-width:860px) 100vw, 200px")}<span class="y">{YEARS[p['slug']]}</span></a></li>""" for i, p in enumerate(PROJECTS))
    assign = "".join(f"<div><span class='kick'>{o} · {y}</span><b>{t}</b><p class='serif'>{d}</p></div>" for o, y, t, d in PRESS)
    cols = "".join(f"<div><span class='kick'>{k}</span><h3>{t}</h3><p class='serif'>{w}</p><small>{x}</small></div>" for k, t, w, x in EXHIB)
    written = "".join(f"<li><span class='serif'>{t}</span><span>{o} · {y}</span></li>" for o, y, t in WRITTEN)
    body = f"""<div class="wrap">
<div class="top"><span>Helsinki, Finland</span><nav aria-label="Main"><a href="/work/">Work</a><a href="/news/">Exhibitions</a><a href="/services/">Commissions</a><a href="/about/">About</a><a href="/contact/">Contact</a></nav></div>
<header class="mast"><h1>Nora Sayyad</h1><span class="ar" lang="ar" dir="rtl">نورا صياد</span></header>
<div class="dl"><span>Photographer · Visual artist · Visual reporter</span><span>EN · FI · SV · AR</span></div>
<main id="main">
<section class="lead">
  <figure>{img(N[2], "(max-width:860px) 100vw, 66vw", lazy=False)}<figcaption>From <em>Notes of Resistance</em> — Black Lives Matter demonstration, Finland, 2020</figcaption></figure>
  <aside>
    <span class="kick">Portfolio</span>
    <h2>Belonging, memory and the right to be seen</h2>
    <p class="serif">{STATEMENT}</p>
    <div class="btns"><a class="btn" href="/work/">See the work</a><a class="btn red" href="/services/">Commission</a></div>
    <div class="assign"><span class="kick" style="color:var(--ink)">Recent assignments</span>{assign}</div>
  </aside>
</section>
<div class="sec"><h2>Projects</h2><a href="/work/">All →</a></div>
<ol class="index">{rows}</ol>
<div class="sec"><h2>Now showing</h2><a href="/news/">Exhibitions →</a></div>
<section class="cols">{cols}</section>
<section class="byline"><div><span class="kick">Words & pictures</span><h2>Photographed and written by Nora</h2></div><ul>{written}</ul></section>
</main>
<footer><span>© Nora Sayyad · Helsinki</span><span><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="https://www.instagram.com/norasayyad/">Instagram</a></span></footer>
</div>"""
    return doc("Reportagem", "family=Archivo:wdth,wght@62..125,400..800&family=Source+Serif+4:ital,wght@0,400;1,400&family=Noto+Naskh+Arabic:wght@500", css, body)


# ================================================================ B · Cartas
def option_b():
    css = """
:root{--paper:#f3ece0;--ink:#2a231d;--soft:#74685c;--line:#d9cdb9;--red:#a2332a;--blue:#23408e}
body{background:var(--paper);color:var(--ink);font:400 18px/1.7 'Newsreader',Georgia,serif}
.mono{font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:.78rem;letter-spacing:.02em}
.wrap{max-width:1180px;margin:0 auto;padding:0 clamp(16px,4vw,40px)}
header{display:flex;justify-content:space-between;align-items:baseline;gap:16px;padding:22px 0;border-bottom:1px solid var(--line)}
header a{text-decoration:none}
header nav{display:flex;gap:22px}
.brand{font-size:1.4rem;font-style:italic}
.hello{padding:clamp(40px,8vw,100px) 0 clamp(24px,4vw,40px)}
.greet{color:var(--soft);display:flex;gap:16px;flex-wrap:wrap;align-items:baseline}
.greet .ar{font-size:1.05rem}
.hello h1{font-weight:400;font-size:clamp(2.4rem,6vw,5.2rem);line-height:1.05;margin-top:14px;max-width:14em}
.hello h1 em{color:var(--red)}
.hello p{max-width:34rem;margin-top:22px;color:#4b4037}
.letter{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(24px,5vw,72px);align-items:start;padding:clamp(40px,7vw,90px) 0;border-top:1px solid var(--line)}
.letter blockquote{margin:12px 0 0;font-size:clamp(1.8rem,3.6vw,3rem);line-height:1.15;font-style:italic}
.letter .meta{margin-top:20px;color:var(--soft)}
.letter .body{margin-top:16px;max-width:32rem}
.route{list-style:none;margin:0;padding:24px;background:#fbf7f0;border:1px solid var(--line);display:flex;flex-direction:column-reverse;align-items:center;gap:2px;font-family:'IBM Plex Mono',monospace;font-size:.86rem;text-align:center}
.route li:not(:first-child)::after{content:"↑";display:block;color:var(--red);line-height:1.3}
.route li:first-child{font-weight:600}
.route li:last-child{font-weight:600;color:var(--blue)}
.route-cap{color:var(--soft);margin-top:10px;text-align:center}
.entries{padding:clamp(40px,7vw,90px) 0;border-top:1px solid var(--line)}
.entries h2,.post h2{font-weight:400;font-style:italic;font-size:clamp(1.8rem,3.4vw,2.6rem);margin-bottom:22px}
.entry{display:grid;grid-template-columns:140px 1fr 1.1fr;gap:clamp(16px,3vw,40px);padding:26px 0;border-top:1px dashed var(--line);text-decoration:none;align-items:start}
.entry:hover h3{color:var(--red)}
.entry h3{font-weight:500;font-size:clamp(1.4rem,2.4vw,1.9rem);line-height:1.1}
.entry p{color:#4b4037;margin-top:8px;font-size:1rem}
.entry img{width:100%;aspect-ratio:3/2;object-fit:cover}
.poem{padding:clamp(56px,10vw,120px) 0;text-align:center;border-top:1px solid var(--line)}
.poem p{font-style:italic;font-size:clamp(1.3rem,2.4vw,1.8rem);line-height:1.5}
.poem .mono{display:block;margin-top:18px;color:var(--soft)}
.post{padding:clamp(40px,6vw,70px) 0;border-top:1px solid var(--line)}
.post .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.post .grid div{background:#fbf7f0;border:1px solid var(--line);padding:22px}
.post h3{font-weight:500;font-size:1.25rem;line-height:1.2;margin:10px 0 6px}
.post p{font-size:.95rem;color:#4b4037}
.stamp{display:inline-block;border:1px solid var(--red);color:var(--red);padding:2px 8px;font:.7rem 'IBM Plex Mono',monospace;text-transform:uppercase;letter-spacing:.06em}
.sign{padding:clamp(56px,9vw,110px) 0;border-top:1px solid var(--line);text-align:center}
.sign h2{font-weight:400;font-style:italic;font-size:clamp(2rem,5vw,3.6rem)}
.sign a{display:inline-block;margin-top:18px;font-size:1.2rem}
footer{display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;padding:20px 0 64px;border-top:1px solid var(--line);color:var(--soft)}
@media (max-width:860px){
 .letter,.post .grid{grid-template-columns:1fr}
 .entry{grid-template-columns:1fr}.entry img{order:-1}
 header nav a:not(.keep){display:none}
}
"""
    entries = "".join(f"""<a class="entry" href="/work/{p['slug']}/"><span class="mono">{YEARS[p['slug']]}<br>{len(PHOTOS[p['slug']])} frames</span><div><h3>{p['title']}</h3><p>{p['teaser']}</p></div>{img(cover(p), "(max-width:860px) 100vw, 40vw")}</a>""" for p in PROJECTS)
    route = "".join(f"<li>{c}</li>" for c in ROUTE)
    post = "".join(f"<div><span class='stamp'>{k}</span><h3>{t}</h3><p>{w}</p><p class='mono' style='margin-top:10px'>{x}</p></div>" for k, t, w, x in EXHIB)
    body = f"""<div class="wrap">
<header><a class="brand" href="/opcoes/b/">Nora Sayyad</a><nav aria-label="Main"><a class="keep" href="/work/">Work</a><a href="/news/">Exhibitions</a><a href="/services/">Commissions</a><a class="keep" href="/about/">About</a></nav></header>
<main id="main">
<section class="hello">
  <p class="greet mono"><span>Hello</span><span>Terve</span><span>Hej</span><span class="ar" lang="ar">مرحبا</span></p>
  <h1>Letters, diaries and portraits about <em>belonging</em>, family and memory.</h1>
  <p>{STATEMENT} Based in Helsinki. Published in The Washington Post and The Times.</p>
</section>
<section class="letter" aria-labelledby="l-title">
  <div>
    <p class="mono" style="color:var(--red)">New essay · 2026</p>
    <blockquote id="l-title">“My father has spent his entire life searching for citizenship.”</blockquote>
    <p class="meta mono">From <em>{NEW[0]}</em></p>
    <p class="body">A photo essay with a short personal story in Finnish: portraits, letters, family photographs and the long road from Gaza to Finland.</p>
  </div>
  <div>
    <ol class="route" aria-label="The route from Gaza to Finland">{route}</ol>
    <p class="route-cap mono">The route, as drawn in the essay</p>
  </div>
</section>
<section class="entries" aria-labelledby="e-title"><h2 id="e-title">Projects</h2>{entries}</section>
<section class="poem">
  <p>They tell us to soften<br>to fade at the edges,<br>to loosen our grip on the ground<br>that remembers our names.</p>
  <span class="mono">— from <em>Somebody’s home</em>, Lifta, 2025</span>
</section>
<section class="post" aria-labelledby="x-title"><h2 id="x-title">Exhibitions</h2><div class="grid">{post}</div></section>
<section class="sign"><h2>Write to me</h2><br><a href="/contact/">Commissions, exhibitions, talks →</a></section>
</main>
<footer><span>Nora Sayyad · Helsinki</span><span><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="https://www.instagram.com/norasayyad/">Instagram</a></span></footer>
</div>"""
    return doc("Cartas", "family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=IBM+Plex+Mono:wght@400;600&family=Noto+Naskh+Arabic:wght@500", css, body)


# ================================================================ C · Tatreez
def option_c():
    css = f"""
:root{{--cream:#f7f2e8;--ink:#1f1d1a;--soft:#5f5a50;--olive:#5c6b2e;--dove:#fbfaf6;--eye:#1f4fa8;--sea:#2f8fb5;--red:#b8322a}}
body{{background:var(--cream);color:var(--ink);font:400 17px/1.65 'Inter',system-ui,sans-serif}}
.serif{{font-family:'Fraunces',Georgia,serif}}
.band{{height:24px;background:{stitch('#b8322a', '#f7f2e8')} repeat-x;background-size:24px 24px}}
.wrap{{max-width:1200px;margin:0 auto;padding:0 clamp(16px,4vw,40px)}}
header{{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:20px 0}}
header a{{text-decoration:none}}
header nav{{display:flex;gap:24px;font-size:.95rem;align-items:center}}
.brand{{font-size:1.45rem}}
.cta{{background:var(--red);color:#fff;border-radius:999px;padding:9px 16px}}
.hero{{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,5vw,64px);align-items:center;padding:clamp(24px,5vw,60px) 0 clamp(48px,7vw,90px)}}
.symbols{{display:flex;gap:10px;font-size:1.3rem;margin-bottom:18px}}
.hero h1{{font-weight:500;font-size:clamp(2.4rem,5.4vw,4.4rem);line-height:1.04}}
.hero h1 span{{color:var(--red)}}
.hero p{{margin-top:20px;max-width:32rem;color:var(--soft);font-size:1.08rem}}
.btns{{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}}
.btn{{display:inline-block;padding:13px 22px;border-radius:999px;text-decoration:none;font-weight:500;background:var(--ink);color:#fff}}
.btn.line{{background:transparent;color:var(--ink);border:1px solid var(--ink)}}
.hero-img{{position:relative;isolation:isolate}}
.hero-img img{{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:220px 220px 6px 6px}}
.hero-img::after{{content:"";position:absolute;left:-14px;bottom:-14px;width:120px;height:120px;background:{stitch('#b8322a')};background-size:24px 24px;z-index:-1}}
.creds{{background:var(--dove);border-top:1px solid #e6dfd0;border-bottom:1px solid #e6dfd0;padding:22px 0}}
.creds ul{{list-style:none;margin:0;padding:0 16px;display:flex;flex-wrap:wrap;gap:10px 34px;justify-content:center;font-family:'Fraunces',serif;font-size:1.1rem}}
section.s{{padding:clamp(56px,8vw,100px) 0}}
.head{{display:flex;justify-content:space-between;align-items:baseline;gap:16px;margin-bottom:30px}}
.head h2{{font-weight:500;font-size:clamp(1.8rem,3.4vw,2.6rem)}}
.cards{{display:grid;grid-template-columns:repeat(4,1fr);gap:22px}}
.card{{text-decoration:none;display:block}}
.card .f{{overflow:hidden;border-radius:6px;aspect-ratio:4/5}}
.card img{{width:100%;height:100%;object-fit:cover;transition:transform .6s}}
.card:hover img{{transform:scale(1.03)}}
.card h3{{font-weight:500;font-size:1.2rem;margin-top:14px;line-height:1.2}}
.card p{{font-size:.92rem;color:var(--soft);margin-top:4px}}
.dot{{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:6px;vertical-align:middle}}
.essay{{background:var(--eye);color:#fff;border-radius:10px;overflow:hidden;display:grid;grid-template-columns:1fr 1fr}}
.essay .t{{padding:clamp(28px,5vw,56px)}}
.essay .k{{text-transform:uppercase;letter-spacing:.14em;font-size:.75rem;color:#cfe0ff}}
.essay h2{{font-weight:500;font-size:clamp(1.8rem,3.4vw,2.8rem);line-height:1.08;margin:12px 0}}
.essay blockquote{{margin:18px 0 0;font-family:'Fraunces',serif;font-style:italic;font-size:1.3rem;border-left:3px solid #ff8a7a;padding-left:16px}}
.essay .pat{{background:{stitch('#b8322a', '#f7f2e8')};background-size:36px 36px;min-height:260px;display:grid;place-items:center}}
.essay .pat span{{background:var(--cream);color:var(--ink);padding:10px 14px;font-size:.8rem;border-radius:4px}}
.shows{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}}
.show{{background:var(--dove);border:1px solid #e6dfd0;border-top:4px solid var(--olive);padding:24px;border-radius:6px}}
.show:nth-child(2){{border-top-color:var(--sea)}}
.show:nth-child(3){{border-top-color:var(--red)}}
.show small{{text-transform:uppercase;letter-spacing:.1em;font-size:.72rem;color:var(--soft)}}
.show h3{{font-weight:500;font-size:1.35rem;line-height:1.15;margin:8px 0}}
.show p{{font-size:.95rem;color:var(--soft)}}
.about{{display:grid;grid-template-columns:.8fr 1.2fr;gap:clamp(24px,5vw,64px);align-items:center}}
.about img{{width:100%;aspect-ratio:1;object-fit:cover;border-radius:50%}}
.about blockquote{{margin:0;font-family:'Fraunces',serif;font-size:clamp(1.5rem,2.8vw,2.2rem);line-height:1.25}}
footer{{display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;padding:26px 0 70px;color:var(--soft)}}
@media (max-width:900px){{
 .hero,.essay,.about{{grid-template-columns:1fr}}
 .cards{{grid-template-columns:1fr 1fr}}.shows{{grid-template-columns:1fr}}
 header nav a:not(.keep){{display:none}}
 .hero-img::after{{left:-8px;bottom:-8px}}
}}
"""
    dots = ["var(--olive)", "var(--sea)", "var(--eye)", "var(--red)"]
    cards = "".join(f"""<a class="card" href="/work/{p['slug']}/"><div class="f">{img(cover(p), "(max-width:900px) 50vw, 25vw")}</div><h3 class="serif">{p['title']}</h3><p><span class="dot" style="background:{dots[i % len(dots)]}"></span>{YEARS[p['slug']]} · {p['teaser']}</p></a>""" for i, p in enumerate(PROJECTS))
    shows = "".join(f"<div class='show'><small>{k}</small><h3 class='serif'>{t}</h3><p>{w}</p><p style='margin-top:8px'>{x}</p></div>" for k, t, w, x in EXHIB)
    body = f"""<div class="band" aria-hidden="true"></div>
<div class="wrap">
<header><a class="brand serif" href="/opcoes/c/">Nora Sayyad</a><nav aria-label="Main"><a class="keep" href="/work/">Work</a><a href="/news/">Exhibitions</a><a href="/services/">Commissions</a><a href="/about/">About</a><a class="cta keep" href="/contact/">Get in touch</a></nav></header>
<main id="main">
<section class="hero">
  <div>
    <div class="symbols" role="img" aria-label="Olive, dove, evil eye, sea">🫒 🕊️ 🧿 🌊</div>
    <h1 class="serif">Portraits of <span>belonging</span>, memory and resistance.</h1>
    <p>{STATEMENT} Published in The Washington Post and The Times; held in Finnish public collections.</p>
    <div class="btns"><a class="btn" href="/work/">See the work</a><a class="btn line" href="/services/">Commission Nora</a></div>
  </div>
  <div class="hero-img">{img(PO[15], "(max-width:900px) 100vw, 50vw", lazy=False)}</div>
</section>
</main>
</div>
<div class="creds"><ul>{''.join(f'<li>{c}</li>' for c in CREDS)}</ul></div>
<div class="wrap">
<section class="s"><div class="head"><h2 class="serif">Projects</h2><a href="/work/">All projects →</a></div><div class="cards">{cards}</div></section>
<section class="essay">
  <div class="t"><p class="k">New essay · 2026</p><h2 class="serif">{NEW[0]}</h2><p>{NEW[2]}</p><blockquote>“My father has spent his entire life searching for citizenship.”</blockquote></div>
  <div class="pat"><span>Essay photos go here</span></div>
</section>
<section class="s"><div class="head"><h2 class="serif">Exhibitions</h2><a href="/news/">All exhibitions →</a></div><div class="shows">{shows}</div></section>
<section class="s about" style="padding-top:0">
  {img(PO[16], "(max-width:900px) 100vw, 40vw")}
  <div><blockquote>“{QUOTE}”</blockquote><p style="margin-top:18px;color:var(--soft)">MA in Photography and Film, Aalto University. Born in Sweden, based in Helsinki. Works in English, Finnish and Swedish.</p><p style="margin-top:14px"><a href="/about/">Biography & CV →</a></p></div>
</section>
</div>
<div class="band" aria-hidden="true"></div>
<div class="wrap"><footer><span>© Nora Sayyad · Helsinki</span><span><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="https://www.instagram.com/norasayyad/">Instagram</a></span></footer></div>"""
    return doc("Tatreez", "family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;1,9..144,400&family=Inter:wght@400;500", css, body)


# ================================================================ D · Sequências
def option_d():
    css = """
:root{--bg:#f6f4ef;--ink:#1c1b19;--soft:#6a665d;--line:#dcd8cf;--red:#b3261e}
body{background:var(--bg);color:var(--ink);font:400 16px/1.6 'Inter',system-ui,sans-serif}
.serif{font-family:'Fraunces',Georgia,serif}
.wrap{max-width:1280px;margin:0 auto;padding:0 clamp(16px,4vw,40px)}
header{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:18px 0;border-bottom:1px solid var(--line)}
header a{text-decoration:none}
header nav{display:flex;gap:24px;font-size:.95rem;align-items:center}
.pill{background:var(--ink);color:#fff;border-radius:999px;padding:9px 16px}
.intro{display:grid;grid-template-columns:1.3fr 1fr;gap:40px;align-items:end;padding:clamp(40px,7vw,90px) 0 clamp(28px,4vw,48px)}
.intro h1{font-weight:500;font-size:clamp(2.2rem,5vw,4.2rem);line-height:1.04}
.intro p{color:var(--soft)}
.seen{font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;color:var(--soft);margin-top:14px}
.seen b{color:var(--ink);font-weight:600}
.seq{padding:clamp(28px,4vw,44px) 0;border-top:1px solid var(--line)}
.seq-head{display:flex;justify-content:space-between;align-items:center;gap:16px;margin-bottom:16px}
.seq-head .ctr{display:flex;gap:8px}
.seq-head button{width:40px;height:40px;border-radius:50%;border:1px solid var(--line);background:#fff;cursor:pointer;font-size:1.1rem;color:var(--ink)}
.seq-head button:hover{border-color:var(--ink)}
.track{display:flex;gap:12px;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;padding-bottom:4px;overscroll-behavior-x:contain}
.track::-webkit-scrollbar{display:none}
.slide{flex:0 0 auto;height:clamp(300px,46vw,520px);scroll-snap-align:start;position:relative}
.slide img{height:100%;width:auto;max-width:none;object-fit:cover}
.slide.txt{width:clamp(260px,30vw,380px);background:#fff;border:1px solid var(--line);padding:clamp(20px,2.5vw,30px);display:flex;flex-direction:column;justify-content:space-between}
.slide.txt.dark{background:var(--ink);color:#fff;border-color:var(--ink)}
.slide.txt h2{font-weight:500;font-size:clamp(1.6rem,2.6vw,2.2rem);line-height:1.08}
.slide.txt p{opacity:.8;font-size:.98rem;margin-top:12px}
.slide.txt .meta{font-size:.78rem;letter-spacing:.1em;text-transform:uppercase;opacity:.7}
.slide.txt a{font-weight:600}
.count{position:absolute;right:10px;top:10px;background:rgba(0,0,0,.55);color:#fff;font-size:.72rem;padding:3px 8px;border-radius:999px}
.dots{display:flex;gap:5px;justify-content:center;margin-top:14px}
.dots i{width:6px;height:6px;border-radius:50%;background:var(--line)}
.dots i.on{background:var(--ink)}
.press{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;padding:clamp(40px,6vw,70px) 0;border-top:1px solid var(--line)}
.press div{background:#fff;border:1px solid var(--line);padding:26px}
.press small{font-size:.75rem;letter-spacing:.12em;text-transform:uppercase;color:var(--red);font-weight:600}
.press h3{font-weight:500;font-size:1.5rem;line-height:1.15;margin:10px 0 8px}
.press p{color:var(--soft)}
footer{display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;padding:24px 0 70px;border-top:1px solid var(--line);color:var(--soft)}
@media (max-width:860px){
 .intro,.press{grid-template-columns:1fr}
 header nav a:not(.keep){display:none}
 .seq-head .ctr{display:none}
}
"""

    def seq(title, meta, text, link, photos, dark=False):
        slides = f"""<div class="slide txt{' dark' if dark else ''}"><div><span class="meta">{meta}</span><h2 class="serif" style="margin-top:10px">{title}</h2><p>{text}</p></div><a href="{link}">Open the story →</a></div>"""
        for i, ph in enumerate(photos):
            slides += f'<figure class="slide">{img(ph, "(max-width:860px) 80vw, 40vw")}<span class="count">{i+1}/{len(photos)}</span></figure>'
        dots = "".join(f"<i{' class=on' if i == 0 else ''}></i>" for i in range(min(len(photos) + 1, 10)))
        return f"""<section class="seq"><div class="seq-head"><span class="serif" style="font-size:1.1rem">{strip(title)}</span><div class="ctr"><button type="button" data-dir="-1" aria-label="Previous">←</button><button type="button" data-dir="1" aria-label="Next">→</button></div></div><div class="track" tabindex="0" aria-label="{strip(title)}: swipe for more">{slides}</div><div class="dots" aria-hidden="true">{dots}</div></section>"""

    seqs = [
        seq(PROJECTS[0]["title"], "2020– · Documentary", PROJECTS[0]["teaser"], "/work/notes-of-resistance/", [N[i] for i in (7, 2, 9, 11, 13, 16, 21, 22, 24)], dark=True),
        seq(PROJECTS[2]["title"], "2025–26 · With Startup Refugees", "Refugee lives shaped by 2015 and 2022. Now touring Finland: Stoa, Valkea, IKEA.", "/work/from-arrival-to-belonging/", [AR[i] for i in (1, 0, 3, 4, 5, 7, 8, 9)]),
        seq(PROJECTS[1]["title"], "2017– · Portraits", PROJECTS[1]["teaser"], "/work/portraits/", [PO[i] for i in (4, 3, 15, 14, 6, 9, 16, 18, 2)]),
        seq(PROJECTS[3]["title"], "2023 · Poetic series", "Scent, memory and inheritance. Related: <em>Utopia</em>, on tour with The Lost Paintings.", "/work/parfyymin-tuulahdus/", PA, dark=True),
    ]
    press = "".join(f"<div><small>{o} · {y}</small><h3 class='serif'>{t}</h3><p>{d}</p></div>" for o, y, t, d in PRESS)
    script = """<script>
document.querySelectorAll('.seq').forEach(s => {
  const t = s.querySelector('.track'), dots = [...s.querySelectorAll('.dots i')];
  s.querySelectorAll('button[data-dir]').forEach(b => b.addEventListener('click', () => t.scrollBy({ left: +b.dataset.dir * t.clientWidth * 0.8, behavior: 'smooth' })));
  t.addEventListener('scroll', () => {
    const r = t.scrollLeft / Math.max(1, t.scrollWidth - t.clientWidth);
    const i = Math.round(r * (dots.length - 1));
    dots.forEach((d, k) => d.classList.toggle('on', k === i));
  }, { passive: true });
});
</script>"""
    body = f"""<div class="wrap">
<header><a class="serif" style="font-size:1.4rem" href="/opcoes/d/">Nora Sayyad</a><nav aria-label="Main"><a class="keep" href="/work/">Work</a><a href="/news/">Exhibitions</a><a href="/services/">Commissions</a><a href="/about/">About</a><a class="pill keep" href="/contact/">Get in touch</a></nav></header>
<main id="main">
<section class="intro">
  <h1 class="serif">Stories told in sequence, one frame at a time.</h1>
  <div><p>{STATEMENT}</p><p class="seen">As seen in <b>The Washington Post</b> · <b>The Times</b> · <b>Helsinki City Museum</b></p></div>
</section>
{''.join(seqs)}
<section class="press" aria-label="Recent assignments">{press}</section>
</main>
<footer><span>© Nora Sayyad · Helsinki</span><span><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="https://www.instagram.com/norasayyad/">Instagram</a></span></footer>
</div>"""
    return doc("Sequências", "family=Fraunces:opsz,wght@9..144,400;9..144,500&family=Inter:wght@400;500;600", css, body, script)


# ================================================================ Hub
OPTIONS = [
    ("a", "Reportagem", "Evolução do “Jornal”, que você gostou",
     "Primeira página de jornal com o nome em árabe ao lado (نورا صياد) e o vermelho do tatreez. Mostra as pautas reais (Washington Post: felicidade; The Times: educação financeira), o ensaio novo <em>Letters to Mothers</em> no índice e uma coluna “Fotografado e escrito por Nora” com os textos da Selkomedia.",
     "Imprensa, editores, ONGs. A opção mais forte para conseguir pautas e comissões.", option_a),
    ("b", "Cartas", "O tom pessoal dos posts dela",
     "Papel creme, fonte serifada e datas em máquina de escrever. Abre com “Hello · Terve · Hej · مرحبا”, destaca a frase do ensaio de 2026 e o mapa do percurso Gaza → Finlândia, desenhado em tipografia como no post original, além de um trecho do poema <em>Somebody’s home</em>.",
     "Curadores, editais, público de arte. É o formato que mais engaja no Instagram dela.", option_b),
    ("c", "Tatreez", "As cores da bio: 🫒🕊️🧿🌊",
     "Base clara e acolhedora, como o primeiro protótipo, com a paleta da bio dela (verde-oliva, branco, azul do olho grego, mar) e uma faixa de ponto-cruz vermelho inspirada no bordado palestino. Retratos coloridos com luz quente, como na fase atual do feed.",
     "Quem quer uma identidade forte e reconhecível sem perder o ar profissional.", option_c),
    ("d", "Sequências", "Os carrosséis dela, no site",
     "Base clara, como a página Work que você gostou. Cada projeto é um carrossel que se desliza para o lado (com o dedo no celular, com setas no computador), abrindo com um cartão de texto, do jeito que ela já monta os posts.",
     "Quem chega pelo Instagram. É o formato mais familiar para os seguidores dela.", option_d),
]


def hub():
    cards = "".join(f"""<a class="opt" href="/opcoes/{k}/">
  <div class="shots"><img src="/opcoes/shots/{k}-desk.jpg" alt="Prévia da opção {name} no computador" loading="lazy"><img class="m" src="/opcoes/shots/{k}-mob.jpg" alt="Prévia da opção {name} no celular" loading="lazy"></div>
  <div class="txt"><span class="tag">Opção {k.upper()}</span><h2>{name}</h2><p class="sub">{sub}</p><p>{desc}</p><p class="for"><b>Para:</b> {who}</p><span class="go">Abrir opção →</span></div>
</a>""" for k, name, sub, desc, who, _ in OPTIONS)
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Nora Sayyad — Opções de visual</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<style>
*,*::before,*::after{{box-sizing:border-box}}
body{{margin:0;background:#f4f3ef;color:#1b1b19;font:400 16px/1.6 system-ui,-apple-system,'Segoe UI',sans-serif}}
.wrap{{max-width:1180px;margin:0 auto;padding:48px 16px 80px}}
h1{{font-size:clamp(1.8rem,4vw,2.6rem);margin:0 0 8px;line-height:1.1}}
.lead{{color:#5a5850;max-width:46rem;margin:0 0 36px}}
.opt{{display:grid;grid-template-columns:1.4fr 1fr;gap:32px;align-items:center;text-decoration:none;color:inherit;background:#fff;border:1px solid #e0ddd4;border-radius:14px;padding:20px;margin-bottom:24px;transition:box-shadow .2s}}
.opt:hover{{box-shadow:0 10px 30px rgba(0,0,0,.08)}}
.shots{{position:relative}}
.shots img{{width:100%;display:block;border-radius:8px;border:1px solid #e0ddd4}}
.shots .m{{position:absolute;right:-8px;bottom:-12px;width:24%;border-radius:10px;box-shadow:0 8px 24px rgba(0,0,0,.2)}}
.tag{{font-size:.75rem;letter-spacing:.12em;text-transform:uppercase;color:#8a877c}}
h2{{margin:4px 0 2px;font-size:1.8rem}}
.sub{{margin:0 0 12px;font-weight:600}}
.for{{color:#5a5850}}
.go{{display:inline-block;margin-top:12px;font-weight:600;border-bottom:2px solid}}
.base{{margin-top:36px;color:#5a5850}}
@media (max-width:800px){{.opt{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
<main class="wrap">
<h1>Quatro opções de visual para a Nora (versão 2)</h1>
<p class="lead">Refeitas a partir do Instagram e do currículo dela: a bio 🫒🕊️🧿🌊, o vermelho do tatreez, os textos em primeira pessoa, os carrosséis de cerca de 10 fotos e as pautas para o Washington Post e o The Times. Todas usam o mesmo conteúdo real; só muda a página inicial. O botão “← Todas as opções”, no canto, volta para cá.</p>
{cards}
<p class="base">Anteriores: <a href="/opcoes/v1/">versão 1 (Noite, Jornal, Arquivo, Azul)</a> · <a href="/">protótipo claro original</a></p>
</main>
</body>
</html>
"""


if __name__ == "__main__":
    for k, *_, fn in OPTIONS:
        out = ROOT / k / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(fn(), encoding="utf-8")
    (ROOT / "index.html").write_text(hub(), encoding="utf-8")
    print("built options")
