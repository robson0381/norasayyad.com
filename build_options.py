#!/usr/bin/env python3
"""Generate four alternative home-page directions for Nora to choose from.

Run: python3 build_options.py  ->  opcoes/<a|b|c|d>/index.html
Only the home page changes; links go to the existing inner pages.
"""
from pathlib import Path

from build import PHOTOS, PROJECTS, EMAIL, img

ROOT = Path(__file__).parent / "opcoes"
N, PO, AR, PA = (PHOTOS[k] for k in ("notes-of-resistance", "portraits", "from-arrival-to-belonging", "parfyymin-tuulahdus"))
HERO = PHOTOS["hero"]

STATEMENT = ("Finnish-Palestinian photographer, artist and visual reporter whose experimental lens "
             "moves between documentary and fictional storytelling — exploring belonging, memory and "
             "the right to be seen.")
CREDS = ["The Washington Post", "The Times", "Helsinki City Museum", "Finnish Museum of Photography",
         "HIAP", "Bristol Museum & Art Gallery", "National Library of Finland"]
VENUES = [("Montréal", "Articule · MAI"), ("United States", "Unbound Visual Arts"), ("Belfast", "The MAC"),
          ("London", "P21 Gallery"), ("Bristol", "Bristol Museum & Art Gallery")]
YEARS = {"notes-of-resistance": "2020–", "portraits": "2017–", "from-arrival-to-belonging": "2025–26",
         "parfyymin-tuulahdus": "2023"}


def cover(p):
    return PHOTOS[p["slug"]][p["cover"]]


def doc(title, fonts, css, body):
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
h1,h2,h3,p{{margin:0}}
:focus-visible{{outline:2px solid currentColor;outline-offset:3px}}
.skip{{position:absolute;left:-999px}}.skip:focus{{left:8px;top:8px;z-index:99;background:#000;color:#fff;padding:8px}}
{css}
</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{body}
<a class="switch" href="/opcoes/">← Todas as opções</a>
</body>
</html>
"""


SWITCH = ".switch{position:fixed;right:12px;bottom:12px;z-index:90;background:#111;color:#fff;font:500 13px/1 system-ui,sans-serif;padding:10px 14px;border-radius:999px;text-decoration:none;box-shadow:0 4px 18px rgba(0,0,0,.25)}"


# ---------------------------------------------------------------- A · Noite
def option_a():
    css = """
:root{--bg:#0d0d0c;--ink:#ecebe6;--soft:#9a988f;--line:#2a2927}
body{background:var(--bg);color:var(--ink);font:400 17px/1.65 'Inter',system-ui,sans-serif}
.serif{font-family:'Cormorant Garamond',Georgia,serif;font-weight:500}
header{position:absolute;inset:0 0 auto;z-index:5;display:flex;justify-content:space-between;align-items:center;padding:22px clamp(16px,4vw,48px)}
header nav{display:flex;gap:clamp(14px,3vw,32px);font-size:.9rem;letter-spacing:.04em}
header a{text-decoration:none}
.brand{font-size:1.1rem;letter-spacing:.18em;text-transform:uppercase}
.hero{position:relative;height:100svh;min-height:560px;overflow:hidden}
.hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.45) 0%,rgba(0,0,0,0) 30%,rgba(0,0,0,0) 45%,rgba(0,0,0,.85) 100%)}
.hero-text{position:absolute;z-index:2;left:clamp(16px,4vw,48px);right:clamp(16px,4vw,48px);bottom:clamp(28px,6vh,64px)}
.hero h1{font-size:clamp(3.4rem,11vw,9.5rem);line-height:.9;letter-spacing:-.01em}
.hero p{max-width:34rem;margin-top:18px;color:#d8d6cf;font-size:clamp(1rem,1.6vw,1.15rem)}
.wrap{max-width:1280px;margin:0 auto;padding:0 clamp(16px,4vw,48px)}
.statement{padding:clamp(80px,14vw,180px) 0;text-align:center}
.statement p{font-size:clamp(1.6rem,3.6vw,2.8rem);line-height:1.25;max-width:26em;margin:0 auto}
.creds{border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:22px 0;overflow:hidden}
.creds ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;justify-content:center;gap:10px 36px;font-size:.78rem;letter-spacing:.16em;text-transform:uppercase;color:var(--soft)}
.project{display:grid;grid-template-columns:1.5fr 1fr;gap:clamp(24px,5vw,72px);align-items:end;padding:clamp(56px,9vw,120px) 0;text-decoration:none}
.project:nth-child(even){grid-template-columns:1fr 1.5fr}
.project:nth-child(even) .pic{order:2}
.project .pic{overflow:hidden;aspect-ratio:4/3}
.project .pic img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s ease,filter .6s}
.project:hover .pic img{transform:scale(1.03)}
.num{font-size:.8rem;letter-spacing:.2em;color:var(--soft)}
.project h2{font-size:clamp(2.2rem,4.6vw,3.8rem);line-height:1;margin:12px 0 14px}
.project p{color:var(--soft);max-width:26rem}
.more{display:inline-block;margin-top:20px;font-size:.85rem;letter-spacing:.14em;text-transform:uppercase;border-bottom:1px solid;padding-bottom:3px}
.tour{padding:clamp(64px,10vw,130px) 0;border-top:1px solid var(--line)}
.tour h2{font-size:clamp(2rem,5vw,4rem);line-height:1.02;max-width:14em}
.tour .eyebrow{font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;color:#d9a441;margin-bottom:18px}
.venues{display:grid;grid-template-columns:repeat(5,1fr);gap:1px;background:var(--line);margin-top:48px;border:1px solid var(--line)}
.venues div{background:var(--bg);padding:20px}
.venues b{display:block;font-weight:500}
.venues span{color:var(--soft);font-size:.85rem}
.venues .now{box-shadow:inset 0 -3px 0 #d9a441}
.cta{padding:clamp(80px,14vw,170px) 0;text-align:center;border-top:1px solid var(--line)}
.cta h2{font-size:clamp(2.4rem,7vw,5.6rem);line-height:1}
.cta a.mail{display:inline-block;margin-top:26px;font-size:clamp(1rem,2vw,1.3rem);border-bottom:1px solid;text-decoration:none;padding-bottom:4px}
footer{display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px;padding:28px clamp(16px,4vw,48px);color:var(--soft);font-size:.85rem;border-top:1px solid var(--line)}
@media (max-width:760px){
 header nav a:not(.keep){display:none}
 .project,.project:nth-child(even){grid-template-columns:1fr}
 .project:nth-child(even) .pic{order:0}
 .venues{grid-template-columns:1fr 1fr}
}
""" + SWITCH
    projects = "".join(f"""<a class="project" href="/work/{p['slug']}/">
  <div class="pic">{img(cover(p), "(max-width:760px) 100vw, 60vw")}</div>
  <div><div class="num">0{i+1} — {YEARS[p['slug']]}</div><h2 class="serif">{p['title']}</h2><p>{p['teaser']}</p><span class="more">View story</span></div>
</a>""" for i, p in enumerate(PROJECTS))
    venues = "".join(f'<div{" class=now" if v[0]=="Bristol" else ""}><b>{v[0]}</b><span>{v[1]}</span></div>' for v in VENUES)
    body = f"""<header>
  <a class="brand" href="/opcoes/a/">Nora Sayyad</a>
  <nav aria-label="Main"><a class="keep" href="/work/">Work</a><a href="/news/">Exhibitions</a><a href="/services/">Commissions</a><a class="keep" href="/about/">About</a></nav>
</header>
<main id="main">
<section class="hero">
  {img(HERO, "100vw", lazy=False)}
  <div class="hero-text"><h1 class="serif">Nora<br>Sayyad</h1><p>Documentary photographer & visual artist · Helsinki</p></div>
</section>
<section class="statement wrap"><p class="serif">{STATEMENT}</p></section>
<div class="creds"><ul>{''.join(f'<li>{c}</li>' for c in CREDS)}</ul></div>
<div class="wrap">{projects}</div>
<section class="tour"><div class="wrap">
  <p class="eyebrow">On tour · 2025–2026</p>
  <h2 class="serif">The Lost Paintings: A Prelude to Return</h2>
  <div class="venues">{venues}</div>
</div></section>
<section class="cta wrap">
  <h2 class="serif">Commissions<br>& collaborations</h2>
  <a class="mail" href="/contact/">Start a conversation →</a>
</section>
</main>
<footer><span>© Nora Sayyad · Helsinki</span><span><a href="https://www.instagram.com/norasayyad/">Instagram</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></span></footer>"""
    return doc("Noite", "family=Cormorant+Garamond:wght@400;500&family=Inter:wght@400;500", css, body)


# ---------------------------------------------------------------- B · Jornal
def option_b():
    css = """
:root{--ink:#111;--soft:#5d5d5d;--line:#111;--accent:#e4481b}
body{background:#fff;color:var(--ink);font:400 16px/1.55 'Archivo',system-ui,sans-serif}
.wrap{max-width:1360px;margin:0 auto;padding:0 clamp(16px,3vw,36px)}
.topbar{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;border-bottom:1px solid var(--line);padding:12px 0;font-size:.78rem;text-transform:uppercase;letter-spacing:.08em}
.topbar nav{display:flex;gap:20px}
.topbar a{text-decoration:none}
.mast{padding:clamp(18px,3vw,36px) 0 clamp(10px,2vw,20px);border-bottom:6px solid var(--line)}
.mast h1{font-family:'Archivo',sans-serif;font-stretch:62%;font-weight:800;font-size:clamp(4rem,17vw,15.5rem);line-height:.82;letter-spacing:-.02em;text-transform:uppercase}
.dateline{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;padding:10px 0;border-bottom:1px solid var(--line);font-size:.82rem;text-transform:uppercase;letter-spacing:.06em}
.lead{display:grid;grid-template-columns:2fr 1fr;gap:0;border-bottom:1px solid var(--line)}
.lead figure{margin:0;padding:24px 24px 24px 0;border-right:1px solid var(--line)}
.lead figcaption{font-size:.8rem;color:var(--soft);margin-top:8px}
.lead aside{padding:24px 0 24px 24px;display:flex;flex-direction:column;gap:22px}
.kicker{font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--accent)}
.lead h2{font-stretch:75%;font-weight:700;font-size:clamp(1.8rem,3vw,2.6rem);line-height:1.02;text-transform:uppercase}
.lead p{font-family:'Source Serif 4',Georgia,serif;font-size:1.08rem}
.seen{border-top:1px solid var(--line);padding-top:14px}
.seen ul{list-style:none;margin:8px 0 0;padding:0;font-family:'Source Serif 4',Georgia,serif;font-size:1.1rem;line-height:1.45}
.btns{display:flex;gap:10px;flex-wrap:wrap}
.btn{display:inline-block;background:var(--ink);color:#fff;text-decoration:none;padding:12px 18px;font-weight:600;font-size:.9rem;text-transform:uppercase;letter-spacing:.05em}
.btn.alt{background:var(--accent)}
.sec-title{display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid var(--line);padding:36px 0 10px}
.sec-title h2{font-stretch:62%;font-weight:800;font-size:clamp(2rem,5vw,3.6rem);text-transform:uppercase;line-height:1}
.index{list-style:none;margin:0;padding:0}
.index a{display:grid;grid-template-columns:70px 1fr 220px 120px;gap:20px;align-items:center;padding:18px 0;border-bottom:1px solid var(--line);text-decoration:none}
.index a:hover{background:#f4f2ee}
.index .n{font-stretch:62%;font-weight:800;font-size:2.4rem;color:var(--accent)}
.index h3{font-stretch:75%;font-weight:700;font-size:clamp(1.3rem,2.4vw,2rem);text-transform:uppercase;line-height:1.05}
.index p{font-family:'Source Serif 4',Georgia,serif;color:var(--soft);margin-top:4px}
.index img{aspect-ratio:3/2;object-fit:cover;width:100%}
.index .y{font-size:.85rem;text-transform:uppercase;letter-spacing:.06em;text-align:right}
.now{display:grid;grid-template-columns:1fr 1fr;border-bottom:1px solid var(--line)}
.now > div{padding:28px 0}
.now > div + div{border-left:1px solid var(--line);padding-left:28px}
.now h3{font-stretch:62%;font-weight:800;font-size:clamp(2rem,4.4vw,3.4rem);line-height:.95;text-transform:uppercase;margin:10px 0}
.now ol{margin:0;padding-left:1.2em;font-family:'Source Serif 4',Georgia,serif;font-size:1.05rem;line-height:1.8}
.strip{display:grid;grid-template-columns:repeat(6,1fr);gap:8px;padding:28px 0;border-bottom:6px solid var(--line)}
.strip img{aspect-ratio:1;object-fit:cover;width:100%;filter:grayscale(1);transition:filter .3s}
.strip a:hover img{filter:none}
footer{display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;padding:18px 0 60px;font-size:.8rem;text-transform:uppercase;letter-spacing:.06em}
@media (max-width:860px){
 .lead,.now{grid-template-columns:1fr}
 .lead figure{padding-right:0;border-right:0}
 .lead aside{padding-left:0}
 .now > div + div{border-left:0;padding-left:0;border-top:1px solid var(--line)}
 .index a{grid-template-columns:44px 1fr;gap:12px}
 .index .n{font-size:1.8rem}
 .index img{grid-column:1/-1;order:-1}
 .index .y{display:none}
 .strip{grid-template-columns:repeat(3,1fr)}
 .topbar nav{display:none}
}
""" + SWITCH
    idx = "".join(f"""<li><a href="/work/{p['slug']}/"><span class="n">{i+1:02d}</span><div><h3>{p['title']}</h3><p>{p['teaser']}</p></div>{img(cover(p), "(max-width:860px) 100vw, 220px")}<span class="y">{YEARS[p['slug']]}</span></a></li>""" for i, p in enumerate(PROJECTS))
    strip_photos = [(N[2], "notes-of-resistance"), (PO[3], "portraits"), (N[11], "notes-of-resistance"), (AR[8], "from-arrival-to-belonging"), (PO[6], "portraits"), (N[23], "notes-of-resistance")]
    strip = "".join(f'<a href="/work/{s}/">{img(ph, "(max-width:860px) 33vw, 16vw")}</a>' for ph, s in strip_photos)
    body = f"""<div class="wrap">
<div class="topbar"><span>Helsinki, Finland</span><nav aria-label="Main"><a href="/work/">Work</a><a href="/news/">Exhibitions</a><a href="/services/">Commissions</a><a href="/about/">About</a><a href="/contact/">Contact</a></nav></div>
<header class="mast"><h1>Nora Sayyad</h1></header>
<div class="dateline"><span>Documentary photographer · Visual artist · Visual reporter</span><span>EN · FI · SV</span></div>
<main id="main">
<section class="lead">
  <figure>{img(N[2], "(max-width:860px) 100vw, 66vw", lazy=False)}<figcaption>From <em>Notes of Resistance</em>, 2020–</figcaption></figure>
  <aside>
    <span class="kicker">Portfolio</span>
    <h2>Belonging, memory and the right to be seen</h2>
    <p>{STATEMENT}</p>
    <div class="btns"><a class="btn" href="/work/">See the work</a><a class="btn alt" href="/services/">Commission</a></div>
    <div class="seen"><span class="kicker">As seen in</span><ul>{''.join(f'<li>{c}</li>' for c in CREDS[:5])}</ul></div>
  </aside>
</section>
<div class="sec-title"><h2>Projects</h2><a href="/work/">All →</a></div>
<ol class="index">{idx}</ol>
<section class="now">
  <div><span class="kicker">Now showing · 2025–26</span><h3>The Lost Paintings: A Prelude to Return</h3><p style="font-family:'Source Serif 4',Georgia,serif">A touring group exhibition featuring Nora's still life <em>Utopia</em> (2023).</p></div>
  <div><ol>{''.join(f'<li>{v[0]} — {v[1]}</li>' for v in VENUES)}</ol></div>
</section>
<div class="strip">{strip}</div>
</main>
<footer><span>© Nora Sayyad</span><span><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="https://www.instagram.com/norasayyad/">Instagram</a></span></footer>
</div>"""
    return doc("Jornal", "family=Archivo:wdth,wght@62..125,400..800&family=Source+Serif+4:ital,wght@0,400;1,400", css, body)


# ---------------------------------------------------------------- C · Arquivo
def option_c():
    css = """
:root{--bg:#efeee9;--ink:#1a1a18;--soft:#76746c;--line:#cfccc2}
body{background:var(--bg);color:var(--ink);font:400 14px/1.55 'IBM Plex Mono',ui-monospace,monospace}
.wrap{padding:0 clamp(16px,2.5vw,32px)}
header{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;padding:18px 0;border-bottom:1px solid var(--line)}
header a{text-decoration:none}
header nav{display:flex;flex-direction:column}
header nav a:hover{text-decoration:underline}
.name{font-family:'IBM Plex Sans',sans-serif;font-weight:500;font-size:1rem}
.soft{color:var(--soft)}
.intro{display:grid;grid-template-columns:1fr 3fr;gap:16px;padding:clamp(40px,8vw,110px) 0 clamp(28px,5vw,60px)}
.intro p{font-family:'IBM Plex Sans',sans-serif;font-size:clamp(1.4rem,2.8vw,2.3rem);line-height:1.2;max-width:24em;letter-spacing:-.01em}
.sheet{display:grid;grid-template-columns:repeat(8,1fr);gap:6px}
.sheet a{position:relative;display:block}
.sheet img{width:100%;aspect-ratio:1;object-fit:cover}
.sheet span{position:absolute;left:4px;top:3px;font-size:10px;background:var(--bg);padding:0 3px}
.label{display:flex;justify-content:space-between;padding:10px 0 0;font-size:12px;color:var(--soft)}
table{width:100%;border-collapse:collapse;margin-top:clamp(48px,8vw,100px)}
th{text-align:left;font-weight:400;color:var(--soft);font-size:12px;padding:8px 8px 8px 0;border-bottom:1px solid var(--ink)}
td{padding:14px 8px 14px 0;border-bottom:1px solid var(--line);vertical-align:top}
td a{text-decoration:none;font-family:'IBM Plex Sans',sans-serif;font-size:1.15rem;font-weight:500}
tr:hover td{background:#e6e4dd}
.cols{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:clamp(48px,8vw,100px);padding-top:16px;border-top:1px solid var(--ink)}
.cols h2{font-size:12px;font-weight:400;color:var(--soft);margin-bottom:8px;text-transform:uppercase;letter-spacing:.06em}
.cols ul{list-style:none;margin:0;padding:0}
.cols li{margin-bottom:4px}
footer{display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-top:clamp(48px,8vw,100px);padding:18px 0 70px;border-top:1px solid var(--ink)}
@media (max-width:860px){
 header{grid-template-columns:1fr 1fr}
 .intro{grid-template-columns:1fr}
 .sheet{grid-template-columns:repeat(4,1fr)}
 .cols{grid-template-columns:1fr 1fr}
 .hide-m{display:none}
}
""" + SWITCH
    picks = ([(N[i], "notes-of-resistance") for i in (0, 2, 5, 6, 7, 9, 11, 13, 15, 16, 21, 22)]
             + [(PO[i], "portraits") for i in (0, 3, 5, 6, 9, 11, 14, 18)]
             + [(AR[i], "from-arrival-to-belonging") for i in (1, 8)]
             + [(PA[i], "parfyymin-tuulahdus") for i in (0, 2)])
    sheet = "".join(f'<a href="/work/{s}/" title="{ph["alt"]}">{img(ph, "(max-width:860px) 25vw, 12vw")}<span>{i+1:02d}</span></a>' for i, (ph, s) in enumerate(picks))
    rows = "".join(f"<tr><td class=soft>{i+1:03d}</td><td><a href='/work/{p['slug']}/'>{p['title']}</a><div class='soft hide-m'>{p['teaser']}</div></td><td>{YEARS[p['slug']]}</td><td class='hide-m'>{len(PHOTOS[p['slug']])}</td></tr>" for i, p in enumerate(PROJECTS))
    body = f"""<div class="wrap">
<header>
  <a class="name" href="/opcoes/c/">Nora Sayyad</a>
  <span class="soft">Photographer, artist,<br>visual reporter</span>
  <span class="soft hide-m">Helsinki, FI<br>EN · FI · SV</span>
  <nav aria-label="Main"><a href="/work/">Index</a><a href="/news/">Exhibitions</a><a href="/services/">Commissions</a><a href="/about/">About / CV</a><a href="/contact/">Contact</a></nav>
</header>
<main id="main">
<section class="intro"><span class="soft">(About)</span><p>{STATEMENT}</p></section>
<div class="sheet">{sheet}</div>
<div class="label"><span>Contact sheet — {len(picks)} frames from 4 projects</span><span class="hide-m">Select a frame to open its project</span></div>
<table><thead><tr><th>No.</th><th>Project</th><th>Years</th><th class="hide-m">Frames</th></tr></thead><tbody>{rows}</tbody></table>
<div class="cols">
  <div><h2>Published</h2><ul><li>The Washington Post</li><li>The Times</li><li>The Sunday Times</li><li>Helsingin Sanomat</li><li>Yle</li></ul></div>
  <div><h2>Exhibited</h2><ul><li>Helsinki City Museum</li><li>Finnish Museum of Photography</li><li>HIAP</li><li>Frauen Museum, Wiesbaden</li></ul></div>
  <div><h2>Collections</h2><ul><li>National Library of Finland</li><li>Finnish Heritage Agency</li><li>Migration Institute of Finland</li></ul></div>
  <div><h2>On tour 2025–26</h2><ul><li><em>The Lost Paintings</em></li>{''.join(f'<li class=soft>{v[0]}</li>' for v in VENUES)}</ul></div>
</div>
</main>
<footer><span>© Nora Sayyad</span><a href="mailto:{EMAIL}">{EMAIL}</a><a href="https://www.instagram.com/norasayyad/">Instagram ↗</a></footer>
</div>"""
    return doc("Arquivo", "family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500", css, body)


# ---------------------------------------------------------------- D · Azul
def option_d():
    css = """
:root{--blue:#1639a8;--blue2:#0f2a80;--cream:#f5efe3;--soft:#c9d3f2}
body{background:var(--blue);color:var(--cream);font:400 17px/1.65 'DM Sans',system-ui,sans-serif}
.it{font-family:'Instrument Serif',Georgia,serif;font-weight:400}
.wrap{max-width:1240px;margin:0 auto;padding:0 clamp(16px,4vw,44px)}
header{display:flex;justify-content:space-between;align-items:center;padding:24px 0}
header a{text-decoration:none}
header nav{display:flex;gap:26px;font-size:.95rem}
.brand{font-size:1.7rem}
.hero{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,5vw,64px);align-items:center;padding:clamp(24px,6vw,80px) 0 clamp(60px,10vw,120px)}
.hero h1{font-size:clamp(3rem,7.4vw,6.6rem);line-height:.95}
.hero h1 em{color:#ffd28a}
.hero p{margin-top:24px;max-width:30rem;color:var(--soft);font-size:1.08rem}
.pill{display:inline-block;margin-top:30px;padding:14px 26px;border-radius:999px;background:var(--cream);color:var(--blue2);text-decoration:none;font-weight:500}
.pill.line{background:transparent;color:var(--cream);border:1px solid var(--cream);margin-left:8px}
.collage{position:relative;aspect-ratio:1/1.05}
.collage img{position:absolute;object-fit:cover;box-shadow:0 30px 60px rgba(0,0,20,.35)}
.c1{width:62%;height:70%;left:0;top:4%}
.c2{width:48%;height:54%;right:0;top:0;border-radius:200px 200px 0 0}
.c3{width:50%;height:42%;right:6%;bottom:0}
.band{background:var(--cream);color:var(--blue2);padding:clamp(60px,10vw,120px) 0}
.band h2{font-size:clamp(2.4rem,5vw,4.2rem);line-height:1;margin-bottom:40px}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:clamp(24px,4vw,48px)}
.card{text-decoration:none;display:block}
.card .ph{overflow:hidden;border-radius:6px;aspect-ratio:5/4}
.card:nth-child(2) .ph,.card:nth-child(3) .ph{border-radius:260px 260px 6px 6px}
.card img{width:100%;height:100%;object-fit:cover;transition:transform .8s}
.card:hover img{transform:scale(1.04)}
.card h3{font-size:clamp(1.7rem,2.8vw,2.3rem);line-height:1.05;margin-top:18px}
.card p{color:#44517d;margin-top:6px}
.quote{padding:clamp(70px,12vw,150px) 0;text-align:center}
.quote p{font-size:clamp(1.8rem,4vw,3.2rem);line-height:1.15;max-width:22em;margin:0 auto}
.quote small{display:block;margin-top:20px;color:var(--soft);font-size:.9rem}
.creds{display:flex;flex-wrap:wrap;justify-content:center;gap:10px}
.creds span{border:1px solid rgba(245,239,227,.4);border-radius:999px;padding:8px 16px;font-size:.88rem}
.tour{background:var(--blue2);padding:clamp(60px,9vw,110px) 0}
.tour-in{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}
.tour h2{font-size:clamp(2.2rem,4.4vw,3.6rem);line-height:1.02}
.tour ul{list-style:none;margin:0;padding:0}
.tour li{display:flex;justify-content:space-between;gap:12px;padding:14px 0;border-bottom:1px solid rgba(245,239,227,.25)}
.tour li span:last-child{color:var(--soft);text-align:right}
footer{padding:44px 0 80px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;color:var(--soft)}
@media (max-width:860px){
 .hero,.tour-in{grid-template-columns:1fr}
 .grid{grid-template-columns:1fr}
 header nav a:not(.keep){display:none}
 .pill.line{margin-left:0}
}
""" + SWITCH
    cards = "".join(f"""<a class="card" href="/work/{p['slug']}/"><div class="ph">{img(cover(p), "(max-width:860px) 100vw, 50vw")}</div><h3 class="it">{p['title']}</h3><p>{p['teaser']}</p></a>""" for p in PROJECTS)
    tour = "".join(f"<li><span>{v[0]}</span><span>{v[1]}</span></li>" for v in VENUES)
    body = f"""<div class="wrap">
<header><a class="brand it" href="/opcoes/d/">Nora Sayyad</a><nav aria-label="Main"><a class="keep" href="/work/">Work</a><a href="/news/">Exhibitions</a><a href="/services/">Commissions</a><a class="keep" href="/about/">About</a></nav></header>
<main id="main">
<section class="hero">
  <div>
    <h1 class="it">Between <em>documentary</em> and fiction.</h1>
    <p>{STATEMENT}</p>
    <a class="pill" href="/work/">Enter the work</a><a class="pill line" href="/contact/">Get in touch</a>
  </div>
  <div class="collage" aria-hidden="false">
    {img(PA[0], "(max-width:860px) 62vw, 30vw", "c1", lazy=False)}
    {img(AR[8], "(max-width:860px) 48vw, 24vw", "c2", lazy=False)}
    {img(PO[16], "(max-width:860px) 50vw, 25vw", "c3", lazy=False)}
  </div>
</section>
</main>
</div>
<section class="band"><div class="wrap"><h2 class="it">Selected projects</h2><div class="grid">{cards}</div></div></section>
<section class="quote wrap">
  <p class="it">“Photography can become a space for memory, dialogue and self-determination.”</p>
  <small>— from Nora's artist statement</small>
  <div class="creds" style="margin-top:44px">{''.join(f'<span>{c}</span>' for c in CREDS)}</div>
</section>
<section class="tour"><div class="wrap tour-in">
  <div><p style="color:#ffd28a;letter-spacing:.14em;text-transform:uppercase;font-size:.8rem">On tour 2025–26</p><h2 class="it">The Lost Paintings: A Prelude to Return</h2><p style="color:var(--soft);margin-top:14px">Featuring <em>Utopia</em> (2023), a still life on memory and the false promise of paradise.</p></div>
  <ul>{tour}</ul>
</div></section>
<div class="wrap"><footer><span>© Nora Sayyad · Helsinki</span><span><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="https://www.instagram.com/norasayyad/">Instagram</a></span></footer></div>"""
    return doc("Azul", "family=Instrument+Serif:ital@0;1&family=DM+Sans:wght@400;500", css, body)


# ---------------------------------------------------------------- Hub
OPTIONS = [
    ("a", "Noite", "Cinematográfico, fundo escuro", "Foto em tela cheia com o nome grande por cima, uma frase de apresentação e cada projeto como um capítulo alternado. As fotos ganham peso de cinema; pouco texto. Combina com o lado “experimental” e ficcional dela.", option_a),
    ("b", "Jornal", "Editorial, tipografia forte", "Cabeçalho de jornal com o nome gigante, foto de capa com legenda, “As seen in” e um índice numerado de projetos. Passa credibilidade jornalística (Washington Post, The Times) logo de cara.", option_b),
    ("c", "Arquivo", "Minimalista, folha de contato", "Fonte monoespaçada, uma folha de contato com 24 fotos dos 4 projetos, índice em tabela e o CV em colunas. Discreto e “de galeria”; conversa com os temas de memória e arquivo.", option_c),
    ("d", "Azul", "Poético, cor da própria obra", "Fundo no azul dos retratos de <em>From Arrival to Belonging</em> e de <em>Parfyymin tuulahdus</em>, colagem de fotos e uma fonte serifada itálica. É a opção mais autoral e calorosa.", option_d),
]


def hub():
    cards = "".join(f"""<a class="opt" href="/opcoes/{k}/">
  <div class="shots"><img src="/opcoes/shots/{k}-desk.jpg" alt="Prévia da opção {name} no computador" loading="lazy"><img class="m" src="/opcoes/shots/{k}-mob.jpg" alt="Prévia da opção {name} no celular" loading="lazy"></div>
  <div class="txt"><span class="tag">Opção {k.upper()}</span><h2>{name}</h2><p class="sub">{sub}</p><p>{desc}</p><span class="go">Abrir opção →</span></div>
</a>""" for k, name, sub, desc, _ in OPTIONS)
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
.lead{{color:#5a5850;max-width:44rem;margin:0 0 40px}}
.opt{{display:grid;grid-template-columns:1.4fr 1fr;gap:32px;align-items:center;text-decoration:none;color:inherit;background:#fff;border:1px solid #e0ddd4;border-radius:14px;padding:20px;margin-bottom:24px;transition:box-shadow .2s}}
.opt:hover{{box-shadow:0 10px 30px rgba(0,0,0,.08)}}
.shots{{position:relative}}
.shots img{{width:100%;display:block;border-radius:8px;border:1px solid #e0ddd4}}
.shots .m{{position:absolute;right:-8px;bottom:-12px;width:24%;border-radius:10px;box-shadow:0 8px 24px rgba(0,0,0,.2)}}
.tag{{font-size:.75rem;letter-spacing:.12em;text-transform:uppercase;color:#8a877c}}
h2{{margin:4px 0 2px;font-size:1.8rem}}
.sub{{margin:0 0 12px;font-weight:600}}
.go{{display:inline-block;margin-top:12px;font-weight:600;border-bottom:2px solid}}
.base{{margin-top:36px;color:#5a5850}}
@media (max-width:800px){{.opt{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
<main class="wrap">
<h1>Quatro opções de visual para a Nora</h1>
<p class="lead">Todas usam o mesmo conteúdo real (fotos, bio, CV, turnê). Só muda a cara da página inicial. Em cada opção, o botão “← Todas as opções”, no canto, volta para esta página. As páginas internas (projetos, About, contato) seguem o protótipo atual e depois são adaptadas ao estilo escolhido.</p>
{cards}
<p class="base">Referência: <a href="/">protótipo anterior (claro, clássico)</a>.</p>
</main>
</body>
</html>
"""


if __name__ == "__main__":
    for k, name, _, _, fn in OPTIONS:
        out = ROOT / k / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(fn(), encoding="utf-8")
    (ROOT / "index.html").write_text(hub(), encoding="utf-8")
    print("built options")
