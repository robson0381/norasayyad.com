#!/usr/bin/env python3
"""Four home-page CONCEPTS built from Nora's own identity, not from layout styles.

Run: python3 build_options.py  ->  opcoes/<slug>/index.html + opcoes/index.html
Earlier rounds are frozen in opcoes/v1/ (styles) and opcoes/v2/ (restyled).

Each concept starts from one thing she says about herself:
  simbolos   — her bio "🫒🕊️🧿🌊": the work lives in four rooms (olive, dove, eye, sea)
  rota       — "born in Sweden, based in Helsinki, roots in Palestine": home as a route
  visivel    — "the politics of looking", "the right to be seen", Visible Palestine:
               photos stay covered until the visitor chooses to look; voices come first
  dois-lares — "Hello · Terve · Hej · مرحبا": a bilingual mirror, Nordic and Arabic,
               meeting in the middle
"""
import re
from pathlib import Path

from build import PHOTOS, PROJECTS, EMAIL, img

ROOT = Path(__file__).parent / "opcoes"
N, PO, AR, PA = (PHOTOS[k] for k in ("notes-of-resistance", "portraits", "from-arrival-to-belonging", "parfyymin-tuulahdus"))
HERO = PHOTOS["hero"]
P = {p["slug"]: p for p in PROJECTS}

STATEMENT = ("Finnish-Palestinian photographer, artist and visual reporter whose experimental lens "
             "moves between documentary and fictional storytelling.")
PRESS = [
    ("The Washington Post", "2025", "How is ‘happiness’ measured around the world?"),
    ("The Times", "2026", "Finland’s plan to be the most financially literate nation"),
]
# Verified from her Instagram captions
VOICES = [
    ("“My father has spent his entire life searching for citizenship.”", "Mariam, about her father Abdel Rahman — <em>Letters to Mothers & Daughter–Father Relationships</em>, 2026"),
    ("“You learn how taxes work, how welfare works, how money moves through society.”", "Marika Iartym, 16, Helsinki — photographed for The Times, 2026"),
    ("“Olen monta kertaa katsellut miehitettyä Palestiinaa rajan toiselta puolelta.”", "Noor Assad, Nazareth / Helsinki, 2025 — <em>Visible Palestine</em>"),
]
POEM = ["They tell us to soften", "to fade at the edges,", "to loosen our grip on the ground", "that remembers our names."]
WORDS = ["may exist", "existential", "exposure", "exile", "exodus", "existence", "exhale"]


def strip(s):
    return re.sub(r"<[^>]+>", "", s)


def ph(label, ratio="4/5", cls=""):
    """Placeholder for a photo that exists only on Instagram (Nora to supply the original)."""
    return f'<div class="ph {cls}" style="aspect-ratio:{ratio}" role="img" aria-label="{strip(label)}"><span>{label}</span></div>'


SWITCH = ".switch{position:fixed;right:12px;bottom:12px;z-index:90;background:#111;color:#fff;font:500 13px/1 system-ui,sans-serif;padding:10px 14px;border-radius:999px;text-decoration:none;box-shadow:0 4px 18px rgba(0,0,0,.25)}"
BASE = """
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;overflow-x:hidden}
img{max-width:100%;display:block;height:auto}
a{color:inherit}
h1,h2,h3,p,figure,blockquote{margin:0}
:focus-visible{outline:2px solid currentColor;outline-offset:3px}
.skip{position:absolute;left:-999px}.skip:focus{left:8px;top:8px;z-index:99;background:#000;color:#fff;padding:8px}
.ph{display:grid;place-items:center;text-align:center;padding:12px;font-size:.72rem;line-height:1.4;background:repeating-linear-gradient(-45deg,rgba(0,0,0,.05) 0 6px,rgba(0,0,0,0) 6px 12px),rgba(127,127,127,.12);color:inherit;opacity:.75}
.ph span{max-width:18em}
"""


def doc(title, fonts, css, body, script="", lang="en"):
    return f"""<!doctype html>
<html lang="{lang}">
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
<style>{BASE}{css}{SWITCH}</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{body}
<a class="switch" href="/opcoes/">← Todas as opções</a>
{script}
</body>
</html>
"""


# Simple original line icons for her four symbols
ICONS = {
    "olive": "<svg viewBox='0 0 48 48' fill='none' stroke='currentColor' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'><path d='M8 40C16 30 24 22 40 8'/><path d='M20 26c-4-6-2-12 2-14 4 2 6 8 2 14-2 1-2 1-4 0z'/><path d='M30 18c-1-6 2-10 6-10 2 4 0 9-5 11z'/><path d='M14 32c-5-2-7-6-6-10 4 0 8 3 8 8z'/></svg>",
    "dove": "<svg viewBox='0 0 48 48' fill='none' stroke='currentColor' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'><path d='M10 28c6 2 12 0 16-4l4-4c3-3 8-2 10 1l-6 2c-2 4-6 8-12 10-4 1-8 1-12-1z'/><path d='M26 20c0-6 4-10 10-10-2 3-3 7-2 10'/><path d='M14 36l6-4'/><path d='M8 18l4 2'/></svg>",
    "eye": "<svg viewBox='0 0 48 48' fill='none' stroke='currentColor' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'><path d='M4 24c6-9 12-13 20-13s14 4 20 13c-6 9-12 13-20 13S10 33 4 24z'/><circle cx='24' cy='24' r='7'/><circle cx='24' cy='24' r='2.5' fill='currentColor'/></svg>",
    "sea": "<svg viewBox='0 0 48 48' fill='none' stroke='currentColor' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'><path d='M4 20c4 0 4-4 8-4s4 4 8 4 4-4 8-4 4 4 8 4 4-4 8-4'/><path d='M4 30c4 0 4-4 8-4s4 4 8 4 4-4 8-4 4 4 8 4 4-4 8-4'/></svg>",
}


# ================================================================ 1 · Símbolos (🫒🕊️🧿🌊)
def concept_simbolos():
    css = """
:root{--paper:#f4f1ea;--ink:#1b1b18;--olive:#5f6b35;--olive-bg:#e6e8d6;--dove:#8a8a80;--dove-bg:#f7f5ef;--eye:#1e4bd8;--eye-bg:#dfe6fb;--sea:#0f6f8c;--sea-bg:#d9ecf1}
body{background:var(--paper);color:var(--ink);font:400 16px/1.6 'Manrope',system-ui,sans-serif}
.d{font-family:'DM Serif Display',Georgia,serif;font-weight:400}
.wrap{max-width:1320px;margin:0 auto;padding:0 clamp(16px,3vw,36px)}
header{display:flex;justify-content:space-between;align-items:center;padding:18px 0}
header a{text-decoration:none}
header nav{display:flex;gap:22px;font-size:.95rem}
.brand{font-size:1.4rem}
.intro{padding:clamp(24px,5vw,56px) 0 clamp(20px,3vw,32px);display:grid;grid-template-columns:1.2fr .8fr;gap:32px;align-items:end}
.intro h1{font-size:clamp(2rem,4.6vw,3.8rem);line-height:1.05}
.intro p{color:#55554d;max-width:34rem}
.key{font-size:.85rem;color:#55554d}
.rooms{display:flex;gap:6px;min-height:clamp(480px,70vh,720px)}
.room{flex:1;display:flex;flex-direction:column;justify-content:space-between;text-decoration:none;padding:clamp(18px,2.5vw,30px);border-radius:8px;transition:flex .45s cubic-bezier(.2,.8,.2,1);position:relative;overflow:hidden;min-width:0}
.room:hover,.room:focus-within{flex:2.2}
.room .ic{width:44px;height:44px}
.room .names{margin-top:14px}
.room h2{font-size:clamp(1.6rem,2.8vw,2.6rem);line-height:1}
.room .tr{display:block;font-size:.8rem;letter-spacing:.06em;opacity:.75;margin-top:6px}
.room .tr .ar{font-family:'Amiri',serif;font-size:1.05rem;letter-spacing:0}
.room p.what{margin-top:12px;font-size:.95rem;max-width:22rem;opacity:.9}
.room ul{list-style:none;margin:18px 0 0;padding:0;font-size:.9rem;display:grid;gap:4px;opacity:.75;transition:.35s}
.room:hover ul,.room:focus-within ul{opacity:1;transform:none}
.room ul li::before{content:"→ ";opacity:.6}
.room .pic{position:absolute;right:-6%;bottom:-4%;width:52%;aspect-ratio:4/5;border-radius:6px;overflow:hidden;opacity:.55;transform:translateY(12px) rotate(2deg);transition:.45s}
.room:hover .pic,.room:focus-within .pic{opacity:1;transform:none}
.room .pic img{width:100%;height:100%;object-fit:cover}
.olive{background:var(--olive-bg);color:var(--olive)}.dove{background:var(--dove-bg);color:#3b3b36;border:1px solid #e5e2d8}.eye{background:var(--eye-bg);color:var(--eye)}.sea{background:var(--sea-bg);color:var(--sea)}
.room h2,.room p,.room ul{color:var(--ink)}
.legend{display:grid;grid-template-columns:repeat(4,1fr);gap:22px;padding:clamp(40px,6vw,72px) 0;border-bottom:1px solid #dedad0}
.legend h3{font-size:1.15rem;margin:6px 0 4px}
.legend p{font-size:.92rem;color:#55554d}
.legend .sw{width:14px;height:14px;border-radius:3px;display:inline-block;vertical-align:-1px;margin-right:6px}
.below{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,4vw,56px);padding:clamp(40px,6vw,72px) 0}
.below h2{font-size:clamp(1.6rem,3vw,2.4rem);margin-bottom:14px}
.below ul{list-style:none;margin:0;padding:0}
.below li{padding:10px 0;border-top:1px solid #dedad0;display:flex;justify-content:space-between;gap:12px}
.below li span:last-child{color:#55554d;white-space:nowrap;font-size:.9rem}
.cta{background:var(--ink);color:var(--paper);border-radius:10px;padding:clamp(28px,4vw,48px);display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;margin-bottom:64px}
.cta h2{font-size:clamp(1.6rem,3vw,2.4rem)}
.cta a{background:var(--paper);color:var(--ink);text-decoration:none;padding:12px 22px;border-radius:999px;font-weight:600}
footer{display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;padding:0 0 60px;color:#55554d;font-size:.9rem}
@media (max-width:900px){
 .intro,.below{grid-template-columns:1fr}
 .rooms{flex-direction:column;min-height:0}
 .room{min-height:220px;flex:none}
 .room:hover,.room:focus-within{flex:none}
 .room ul,.room .pic{opacity:1;transform:none}
 .room .pic{position:static;width:100%;aspect-ratio:3/2;margin-top:16px}
 .legend{grid-template-columns:1fr 1fr}
 header nav a:not(.keep){display:none}
}
"""
    rooms = [
        ("olive", "Olive", "Oliivi · Oliv", "زيتون", "Roots, land, family and inheritance.",
         ["Letters to Mothers & Daughter–Father Relationships (2026)", "Somebody’s home — Lifta (2025)", "Jordan diaries (2026)", "Parfyymin tuulahdus (2023)"], PA[0], "/work/parfyymin-tuulahdus/"),
        ("dove", "Dove", "Kyyhky · Duva", "حمامة", "Peace, resistance and solidarity, from the street.",
         ["Notes of Resistance (2020–)", "No Justice, No Peace — book, Gold at Vuoden Huiput (2021)", "BDS posters for OK11 (2025)", "Even the flowers resist — for Sumud (2024)"], N[7], "/work/notes-of-resistance/"),
        ("eye", "Eye", "Silmä · Öga", "عين", "The politics of looking: who is seen, and how.",
         ["Portraits (2017–)", "From Arrival to Belonging? A Decade in Portraits (2025–26)", "Visible Palestine — HIAP (2025)", "Being Black — Helsinki City Museum (2023)"], PO[15], "/work/portraits/"),
        ("sea", "Sea", "Meri · Hav", "بحر", "Crossings, borders and the diaspora.",
         ["Born in Sweden · based in Helsinki · roots in Palestine", "Tornio / Haparanda — a protest on the border (2026)", "The Lost Paintings — Montréal, Boston, Belfast, London, Bristol", "Tervetuloa, tervemenoa — Migration Institute of Finland (2024)"], PO[16], "/work/from-arrival-to-belonging/"),
    ]
    rooms_html = "".join(f"""<a class="room {k}" href="{link}">
  <div><div class="ic">{ICONS[k]}</div><div class="names"><h2 class="d">{en}</h2><span class="tr">{tr} · <span class="ar" lang="ar">{ar}</span></span></div><p class="what">{what}</p><ul>{''.join(f'<li>{w}</li>' for w in works)}</ul></div>
  <div class="pic">{img(photo, "(max-width:900px) 100vw, 30vw")}</div>
</a>""" for k, en, tr, ar, what, works, photo, link in rooms)
    legend = "".join(f"<div><span class='sw' style='background:var(--{k})'></span><h3 class='d'>{en}</h3><p>{what}</p></div>" for k, en, _, _, what, *_ in rooms)
    press = "".join(f"<li><span>{t}</span><span>{o} · {y}</span></li>" for o, y, t in PRESS)
    body = f"""<div class="wrap">
<header><a class="brand d" href="/opcoes/simbolos/">Nora Sayyad</a><nav aria-label="Main"><a class="keep" href="/work/">Work</a><a href="/news/">Exhibitions</a><a href="/services/">Commissions</a><a class="keep" href="/about/">About</a></nav></header>
<main id="main">
<section class="intro">
  <div><h1 class="d">Four rooms: olive, dove, eye, sea.</h1><p style="margin-top:12px">{STATEMENT} Her work is organised by what it is about, not by when it was made.</p></div>
  <p class="key">The four symbols are the ones Nora uses to describe herself — 🫒🕊️🧿🌊. Move over a room to see what lives inside; on a phone, they stack.</p>
</section>
<section class="rooms" aria-label="The four rooms">{rooms_html}</section>
<section class="legend">{legend}</section>
<section class="below">
  <div><h2 class="d">Assignments</h2><ul>{press}<li><span>Photographed and written for Selkomedia</span><span>2025</span></li></ul></div>
  <div><h2 class="d">Now showing</h2><ul><li><span>The Lost Paintings: A Prelude to Return — on tour</span><span>2025–26</span></li><li><span>From Arrival to Belonging? — touring Finland</span><span>2025–26</span></li><li><span>Visible Palestine — HIAP, Suomenlinna</span><span>2025</span></li></ul></div>
</section>
<section class="cta"><h2 class="d">Commissions, exhibitions, talks.</h2><a href="/contact/">Get in touch</a></section>
</main>
<footer><span>© Nora Sayyad · Helsinki</span><span><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="https://www.instagram.com/norasayyad/">Instagram</a></span></footer>
</div>"""
    return doc("Símbolos", "family=DM+Serif+Display&family=Manrope:wght@400;600&family=Amiri", css, body)


# ================================================================ 2 · Rota (Sweden · Helsinki · Palestine)
def concept_rota():
    css = """
:root{--paper:#e9ebe3;--ink:#1e261e;--soft:#5d665c;--line:#c9cfc4;--route:#c0392b}
body{background:var(--paper);color:var(--ink);font:400 16px/1.6 'Space Grotesk',system-ui,sans-serif}
.s{font-family:'Instrument Serif',Georgia,serif;font-weight:400}
.wrap{max-width:1240px;margin:0 auto;padding:0 clamp(16px,3vw,36px)}
header{display:flex;justify-content:space-between;align-items:center;padding:18px 0;border-bottom:1px solid var(--line)}
header a{text-decoration:none}header nav{display:flex;gap:22px;font-size:.95rem}
.brand{font-size:1.5rem}
.homes{display:grid;grid-template-columns:repeat(3,1fr);gap:0;padding:clamp(32px,6vw,72px) 0;border-bottom:1px solid var(--line)}
.homes div{padding:0 24px 0 0}
.homes div+div{border-left:1px solid var(--line);padding-left:24px}
.homes small{display:block;font-size:.75rem;letter-spacing:.14em;text-transform:uppercase;color:var(--soft)}
.homes b{display:block;font-size:clamp(1.6rem,3.2vw,2.6rem);font-weight:400;line-height:1.05;margin:6px 0}
.homes span{color:var(--soft);font-size:.95rem}
.lede{padding:clamp(28px,5vw,60px) 0;max-width:40rem}
.lede h1{font-size:clamp(2rem,4.6vw,3.8rem);line-height:1.05}
.lede p{margin-top:14px;color:var(--soft)}
.journey{display:grid;grid-template-columns:260px 1fr;gap:clamp(24px,4vw,56px);padding-bottom:40px}
.here{position:sticky;top:20px;align-self:start;padding:18px 0}
.here small{font-size:.75rem;letter-spacing:.14em;text-transform:uppercase;color:var(--soft)}
.here .place{font-size:clamp(1.8rem,3vw,2.6rem);line-height:1.05;margin:6px 0}
.here .yr{color:var(--route);font-weight:600}
.here ol{list-style:none;margin:24px 0 0;padding:0;font-size:.85rem;color:var(--soft)}
.here ol li{padding:4px 0 4px 16px;border-left:2px solid var(--line)}
.here ol li.on{color:var(--ink);border-color:var(--route)}
.stops{position:relative;padding-left:32px}
.stops::before{content:"";position:absolute;left:8px;top:0;bottom:0;border-left:2px dashed var(--route)}
.stop{position:relative;display:grid;grid-template-columns:1fr 1fr;gap:clamp(16px,3vw,40px);align-items:center;padding:clamp(28px,4vw,48px) 0;border-bottom:1px solid var(--line);text-decoration:none}
.stop::before{content:"";position:absolute;left:-30px;top:calc(50% - 7px);width:14px;height:14px;border-radius:50%;background:var(--paper);border:3px solid var(--route)}
.stop small{font-size:.75rem;letter-spacing:.14em;text-transform:uppercase;color:var(--route)}
.stop h2{font-size:clamp(1.5rem,2.8vw,2.4rem);line-height:1.05;margin:6px 0 8px}
.stop p{color:var(--soft);font-size:.98rem}
.stop .pr{margin-top:10px;font-size:.9rem;text-decoration:underline}
.stop .pic{aspect-ratio:4/3;overflow:hidden;border-radius:4px}
.stop .pic img{width:100%;height:100%;object-fit:cover}
.stop:nth-child(even) .pic{order:-1}
.stop .ph{aspect-ratio:4/3;border-radius:4px}
.tail{padding:clamp(40px,7vw,90px) 0;text-align:center}
.tail h2{font-size:clamp(1.8rem,4vw,3.2rem)}
.tail p{color:var(--soft);margin-top:10px}
.tail a{display:inline-block;margin-top:20px;background:var(--ink);color:var(--paper);text-decoration:none;padding:12px 22px;border-radius:999px}
footer{display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;padding:20px 0 64px;border-top:1px solid var(--line);color:var(--soft);font-size:.9rem}
@media (max-width:900px){
 .homes{grid-template-columns:1fr}.homes div+div{border-left:0;padding-left:0;border-top:1px solid var(--line);padding-top:16px;margin-top:16px}
 .journey{grid-template-columns:1fr}.here{position:static}.here ol{display:none}
 .stop{grid-template-columns:1fr}.stop .pic,.stop .ph{order:-1}
 header nav a:not(.keep){display:none}
}
"""
    stops = [
        ("Turku, Finland", "2020", "Black Lives Matter", "Where <em>Notes of Resistance</em> began: the Black Lives Matter demonstrations of 2020, later the book <em>No Justice, No Peace</em>.", "/work/notes-of-resistance/", ("img", N[2])),
        ("Helsinki", "2023–", "Palestine solidarity", "Vigils, marches and candles in the snow. The Palestine chapter of <em>Notes of Resistance</em>.", "/work/notes-of-resistance/", ("img", N[11])),
        ("Helsinki · Oulu · IKEA", "2025–26", "From Arrival to Belonging?", "Refugees who arrived in 2015 and 2022, photographed for the ten years of Startup Refugees. Now touring Finland.", "/work/from-arrival-to-belonging/", ("img", AR[1])),
        ("Tornio / Haparanda", "2026", "A protest on the border", "“The most romantic border I’ve ever seen.” One of the smallest Palestine protests, at the line between Finland and Sweden — the two countries she was born in and lives in.", None, ("ph", "Photo from the Instagram post — original to be supplied")),
        ("Lifta, Palestine", "2025", "Somebody’s home", "The ruins of a Palestinian village, the cacti planted centuries ago, and a poem: <em>“the ground that remembers our names”</em>.", None, ("ph", "Photos from the Instagram post — originals to be supplied")),
        ("Amman · Petra", "2026", "Jordan diaries", "Twenty frames of streets, markets and rock, from the post pinned to the top of her profile.", None, ("ph", "Photos from the Instagram post — originals to be supplied")),
        ("Montréal · Boston · New York · Belfast · London · Bristol", "2025–26", "The Lost Paintings: A Prelude to Return", "A touring exhibition of 53 artists. Nora’s still life <em>Utopia</em> (2023) crosses the Atlantic with it, and she took up a residency in Boston.", "/news/", ("img", PA[0])),
        ("Helsinki · Suomenlinna", "2025", "Visible Palestine", "A draft, in three parts, of the exhibition she is working towards: portraits, interviews and protest photography. Back home, to begin again.", "/news/", ("img", PO[15])),
    ]
    stops_html = ""
    for i, (place, yr, title, text, link, media) in enumerate(stops):
        pic = f'<div class="pic">{img(media[1], "(max-width:900px) 100vw, 45vw")}</div>' if media[0] == "img" else ph(media[1], "4/3")
        tag = "a" if link else "div"
        href = f' href="{link}"' if link else ""
        stops_html += f"""<{tag} class="stop" data-place="{strip(place)}" data-yr="{yr}"{href}><div><small>{place} · {yr}</small><h2 class="s">{title}</h2><p>{text}</p>{'<span class="pr">Open the project →</span>' if link else ''}</div>{pic}</{tag}>"""
    steps = "".join(f"<li>{strip(place)}</li>" for place, *_ in stops)
    script = """<script>
const place = document.querySelector('.here .place'), yr = document.querySelector('.here .yr'), items = [...document.querySelectorAll('.here ol li')];
const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { const i = [...document.querySelectorAll('.stop')].indexOf(e.target); place.textContent = e.target.dataset.place; yr.textContent = e.target.dataset.yr; items.forEach((li, k) => li.classList.toggle('on', k === i)); } }), { rootMargin: '-40% 0px -50% 0px' });
document.querySelectorAll('.stop').forEach(s => io.observe(s));
</script>"""
    body = f"""<div class="wrap">
<header><a class="brand s" href="/opcoes/rota/">Nora Sayyad</a><nav aria-label="Main"><a class="keep" href="/work/">Work</a><a href="/news/">Exhibitions</a><a href="/services/">Commissions</a><a class="keep" href="/about/">About</a></nav></header>
<main id="main">
<section class="homes" aria-label="Three homes">
  <div><small>Born in</small><b class="s">Sweden</b><span>Född i Sverige</span></div>
  <div><small>Based in</small><b class="s">Helsinki</b><span>Asuu Helsingissä</span></div>
  <div><small>Roots in</small><b class="s">Palestine</b><span lang="ar" dir="rtl">جذورها في فلسطين</span></div>
</section>
<section class="lede"><h1 class="s">The work follows the road.</h1><p>{STATEMENT} Published in The Washington Post and The Times. Scroll to travel through the places where the work was made.</p></section>
<section class="journey">
  <aside class="here" aria-live="polite"><small>You are in</small><div class="place s">Turku, Finland</div><div class="yr">2020</div><ol>{steps}</ol></aside>
  <div class="stops">{stops_html}</div>
</section>
<section class="tail"><h2 class="s">Next stop: yours.</h2><p>Commissions, exhibitions and talks, in Finland and abroad.</p><a href="/contact/">Get in touch</a></section>
</main>
<footer><span>© Nora Sayyad · Helsinki</span><span><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="https://www.instagram.com/norasayyad/">Instagram</a></span></footer>
</div>"""
    return doc("Rota", "family=Instrument+Serif:ital@0;1&family=Space+Grotesk:wght@400;600", css, body, script)


# ================================================================ 3 · Visível (the right to be seen)
def concept_visivel():
    css = """
:root{--bg:#0b0b0c;--ink:#f2f0ea;--soft:#9a988f;--blue:#1e4bd8;--line:#26262a}
body{background:var(--bg);color:var(--ink);font:400 16px/1.6 'Inter',system-ui,sans-serif}
.h{font-family:'Syne',sans-serif;font-weight:800;letter-spacing:-.02em}
.wrap{max-width:1280px;margin:0 auto;padding:0 clamp(16px,3vw,36px)}
header{display:flex;justify-content:space-between;align-items:center;padding:18px 0}
header a{text-decoration:none}header nav{display:flex;gap:22px;font-size:.95rem;color:var(--soft)}
.brand{font-size:1.2rem;letter-spacing:.06em;text-transform:uppercase}
.open{padding:clamp(48px,10vw,120px) 0 clamp(32px,6vw,72px);display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:end}
.open h1{font-size:clamp(3rem,10vw,9rem);line-height:.9}
.open h1 span{color:var(--blue)}
.open p{color:var(--soft);max-width:30rem}
.open .note{font-size:.85rem;margin-top:16px;color:var(--ink)}
.words{list-style:none;margin:0;padding:0;font-family:'Syne',sans-serif;font-weight:700;font-size:clamp(1.2rem,2.4vw,1.9rem);line-height:1.3;color:var(--soft)}
.words li:nth-child(4),.words li:nth-child(5){color:var(--ink)}
.words small{display:block;font:400 .8rem/1.4 'Inter',sans-serif;margin-top:8px;color:var(--soft)}
.look{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;padding-bottom:12px}
.tile{position:relative;aspect-ratio:4/5;overflow:hidden;background:var(--blue);cursor:pointer;border:0;padding:0;text-align:left;color:#fff;font:inherit}
.tile img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transform:scale(1.04);transition:opacity .5s,transform .8s}
.tile .cap{position:absolute;inset:0;padding:16px;display:flex;flex-direction:column;justify-content:space-between;transition:opacity .4s}
.tile .cap b{font-family:'Syne',sans-serif;font-weight:700;font-size:1rem;line-height:1.2}
.tile .cap small{font-size:.75rem;opacity:.85}
.tile.seen img,.tile:hover img,.tile:focus-visible img{opacity:1;transform:none}
.tile.seen .cap,.tile:hover .cap,.tile:focus-visible .cap{opacity:0}
.hint{display:flex;justify-content:space-between;color:var(--soft);font-size:.85rem;padding:0 0 40px;border-bottom:1px solid var(--line)}
.voices{padding:clamp(40px,7vw,90px) 0;border-bottom:1px solid var(--line)}
.voices h2{font-size:.8rem;letter-spacing:.16em;text-transform:uppercase;color:var(--blue);margin-bottom:26px}
.voice{padding:22px 0;border-top:1px solid var(--line)}
.voice blockquote{font-family:'Syne',sans-serif;font-weight:700;font-size:clamp(1.3rem,2.8vw,2.3rem);line-height:1.15;max-width:26em}
.voice p{color:var(--soft);margin-top:10px;font-size:.92rem}
.projects{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;padding:clamp(40px,6vw,72px) 0;border-bottom:1px solid var(--line)}
.projects a{text-decoration:none}
.projects small{color:var(--blue);font-size:.75rem;letter-spacing:.12em;text-transform:uppercase}
.projects h3{font-family:'Syne',sans-serif;font-weight:700;font-size:1.25rem;line-height:1.15;margin:6px 0}
.projects p{color:var(--soft);font-size:.9rem}
.strip{display:flex;flex-wrap:wrap;gap:10px 30px;padding:24px 0;color:var(--soft);font-size:.85rem;border-bottom:1px solid var(--line)}
.strip b{color:var(--ink);font-weight:500}
.end{padding:clamp(48px,8vw,100px) 0;display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap}
.end h2{font-size:clamp(2rem,5vw,4rem);line-height:.95}
.end a{background:var(--ink);color:var(--bg);text-decoration:none;padding:14px 24px;border-radius:999px;font-weight:600}
footer{display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;padding:0 0 64px;color:var(--soft);font-size:.9rem}
@media (max-width:900px){
 .open{grid-template-columns:1fr}
 .look{grid-template-columns:1fr 1fr}
 .projects{grid-template-columns:1fr 1fr}
 header nav a:not(.keep){display:none}
}
"""
    tiles_src = [PO[15], PO[3], AR[8], PO[5], N[24], PO[14], AR[4], N[40 - 26] if len(N) > 14 else N[0]]
    tiles = "".join(f"""<button class="tile" type="button" aria-pressed="false" aria-label="Reveal: {strip(p['alt'])}"><div class="cap"><b>{p['alt']}</b><small>Tap to look</small></div>{img(p, "(max-width:900px) 50vw, 25vw")}</button>""" for p in tiles_src)
    voices = "".join(f"<div class='voice'><blockquote>{q}</blockquote><p>{who}</p></div>" for q, who in VOICES)
    projects = "".join(f"<a href='/work/{p['slug']}/'><small>{len(PHOTOS[p['slug']])} photographs</small><h3>{p['title']}</h3><p>{p['teaser']}</p></a>" for p in PROJECTS)
    words = "".join(f"<li>{w}</li>" for w in WORDS)
    script = """<script>
document.querySelectorAll('.tile').forEach(t => t.addEventListener('click', () => { const on = t.classList.toggle('seen'); t.setAttribute('aria-pressed', String(on)); }));
</script>"""
    body = f"""<div class="wrap">
<header><a class="brand h" href="/opcoes/visivel/">Nora Sayyad</a><nav aria-label="Main"><a class="keep" href="/work/">Work</a><a href="/news/">Exhibitions</a><a href="/services/">Commissions</a><a class="keep" href="/about/">About</a></nav></header>
<main id="main">
<section class="open">
  <div><h1 class="h">The right<br>to be <span>seen.</span></h1><p style="margin-top:20px">{STATEMENT} Her practice is about the politics of looking: who is seen, by whom, and on whose terms.</p><p class="note">Every photograph on this page starts covered. It is shown only when you choose to look.</p></div>
  <ul class="words" aria-label="Word poem">{words}<small>— word poem from a 2026 post</small></ul>
</section>
<section class="look" aria-label="Portraits, covered until you look">{tiles}</section>
<div class="hint"><span>Each cover carries the description a screen reader would hear.</span><span>Move over, or tap, to see the person.</span></div>
<section class="voices"><h2>They speak first</h2>{voices}</section>
<section class="projects">{projects}</section>
<div class="strip"><span>Published in <b>The Washington Post</b> and <b>The Times</b></span><span>Exhibited at <b>Helsinki City Museum</b>, <b>Finnish Museum of Photography</b>, <b>HIAP</b></span><span>On tour: <b>The Lost Paintings</b></span></div>
<section class="end"><h2 class="h">Look together.</h2><a href="/contact/">Commission Nora</a></section>
</main>
<footer><span>© Nora Sayyad · Helsinki</span><span><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="https://www.instagram.com/norasayyad/">Instagram</a></span></footer>
</div>"""
    return doc("Visível", "family=Syne:wght@700;800&family=Inter:wght@400;500;600", css, body, script)


# ================================================================ 4 · Dois lares (Nordic ⇄ Arabic)
def concept_dois_lares():
    css = """
:root{--north:#eef1f4;--south:#f6e6d8;--ink:#1c1a19;--soft:#6b6661;--cold:#3d5a80;--warm:#b2402e}
body{background:#fff;color:var(--ink);font:400 17px/1.65 'Cormorant Garamond',Georgia,serif}
.ar{font-family:'Amiri',serif}
.sans{font-family:'Inter',system-ui,sans-serif}
header{display:flex;justify-content:space-between;align-items:center;padding:18px clamp(16px,3vw,36px);border-bottom:1px solid #e6e2dc}
header a{text-decoration:none}header nav{display:flex;gap:22px;font-size:.9rem}
.brand{font-size:1.5rem;font-weight:500}
.brand .ar{margin-left:10px;color:var(--warm)}
.mirror{display:grid;grid-template-columns:1fr 1fr}
.col{padding:clamp(28px,5vw,64px) clamp(16px,4vw,56px)}
.north{background:var(--north)}.south{background:var(--south);direction:rtl;text-align:right}
.row{display:contents}
.k{font-size:.75rem;letter-spacing:.14em;text-transform:uppercase;color:var(--soft);font-family:'Inter',sans-serif}
.south .k{letter-spacing:0;font-family:'Amiri',serif;font-size:.95rem;text-transform:none}
.big{font-size:clamp(2rem,5vw,4.4rem);line-height:1.02;font-weight:500;margin-top:8px}
.south .big{font-size:clamp(2.2rem,5.4vw,4.8rem);line-height:1.15}
.north .big em{color:var(--cold);font-style:italic}.south .big em{color:var(--warm);font-style:normal}
.col p.t{margin-top:14px;max-width:28rem;color:#3f3b37}
.south p.t{margin-right:0;margin-left:auto}
.col img{width:100%;aspect-ratio:4/5;object-fit:cover;margin-top:22px}
.meet{grid-column:1/-1;text-align:center;padding:clamp(28px,5vw,56px) 16px;border-top:1px solid #e6e2dc;border-bottom:1px solid #e6e2dc;background:#fff}
.meet small{display:block;font-size:.75rem;letter-spacing:.14em;text-transform:uppercase;color:var(--soft);font-family:'Inter',sans-serif}
.meet b{display:block;font-size:clamp(2rem,5vw,4rem);font-weight:500;line-height:1}
.meet p{color:var(--soft);margin-top:8px;font-size:1rem}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:0}
.pair .l{padding:clamp(18px,3vw,36px) clamp(16px,4vw,56px);border-top:1px solid #e6e2dc}
.pair .r{padding:clamp(18px,3vw,36px) clamp(16px,4vw,56px);border-top:1px solid #e6e2dc;direction:rtl;text-align:right}
.pair h3{font-weight:500;font-size:1.5rem;line-height:1.1}
.pair .r h3{font-family:'Amiri',serif;font-size:1.7rem}
.pair p{color:var(--soft);font-size:1rem;margin-top:4px}
.pair a{text-decoration:none}
.works{padding:clamp(40px,6vw,72px) clamp(16px,3vw,36px)}
.works h2{font-weight:500;font-size:clamp(1.8rem,3.6vw,2.8rem);text-align:center}
.works h2 .ar{color:var(--warm)}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:32px}
.grid a{text-decoration:none}
.grid img{aspect-ratio:4/5;object-fit:cover;width:100%}
.grid h3{font-weight:500;font-size:1.25rem;margin-top:12px;line-height:1.15}
.grid p{color:var(--soft);font-size:.95rem}
.close{display:grid;grid-template-columns:1fr 1fr}
.close div{padding:clamp(32px,6vw,72px) clamp(16px,4vw,56px)}
.close .n{background:var(--north)}.close .s{background:var(--south);direction:rtl;text-align:right}
.close b{display:block;font-size:clamp(1.6rem,3.4vw,2.6rem);font-weight:500;line-height:1.05}
.close a{display:inline-block;margin-top:16px;font-family:'Inter',sans-serif;font-size:.95rem}
footer{display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;padding:20px clamp(16px,3vw,36px) 64px;color:var(--soft);font-size:.95rem}
@media (max-width:820px){
 .mirror,.pair,.close{grid-template-columns:1fr}
 .col img{aspect-ratio:3/2}
 .grid{grid-template-columns:1fr 1fr}
 header nav a:not(.keep){display:none}
}
"""
    def col(cls, k, big, t, photo):
        return f"""<div class="col {cls}"><span class="k">{k}</span><h2 class="big">{big}</h2><p class="t">{t}</p>{img(photo, "(max-width:820px) 100vw, 50vw")}</div>"""
    def pair(l_t, l_p, r_t, r_p, link):
        return f"""<a class="l" href="{link}"><h3>{l_t}</h3><p>{l_p}</p></a><a class="r" href="{link}" lang="ar"><h3>{r_t}</h3><p>{r_p}</p></a>"""
    mirror = (
        col("north", "Syntynyt Ruotsissa · Född i Sverige", "Born in the <em>north</em>.", "Sweden, then Helsinki. Winter light, birch, snow; Finnish, Swedish, English.", PO[10])
        + f"""<div class="col south" lang="ar"><span class="k">جذورها في فلسطين</span><h2 class="big">جذور في <em>الجنوب</em>.</h2><p class="t">فلسطين: زيتون، تطريز، رسائل، بيت أحدهم. العربية لغة البيت.</p>{img(PO[15], "(max-width:820px) 100vw, 50vw")}</div>"""
        + """<div class="meet"><small>Where they meet · Missä ne kohtaavat · <span class="ar" lang="ar">حيث يلتقيان</span></small><b>Helsinki</b><p>Finnish-Palestinian photographer, artist and visual reporter. Documentary and fiction, in two directions at once.</p></div>"""
        + col("north", "Documentary · Dokumentaarinen", "What is <em>seen</em>.", "Protests, borders and portraits of people arriving: Notes of Resistance, From Arrival to Belonging?", N[11])
        + f"""<div class="col south" lang="ar"><span class="k">تجريبي · شعري</span><h2 class="big">ما <em>يُتذكَّر</em>.</h2><p class="t">الرائحة، اليوتوبيا، صور العائلة، الطريق من غزة إلى فنلندا.</p>{img(PA[0], "(max-width:820px) 100vw, 50vw")}</div>"""
    )
    pairs = (
        pair("Notes of Resistance", "Black Lives Matter and Palestine solidarity, 2020–", "ملاحظات المقاومة", "من الشارع، ٢٠٢٠–", "/work/notes-of-resistance/")
        + pair("From Arrival to Belonging?", "A decade in portraits, with Startup Refugees", "من الوصول إلى الانتماء؟", "عقد من البورتريهات", "/work/from-arrival-to-belonging/")
        + pair("Letters to Mothers", "Daughter–father relationships, 2026", "رسائل إلى الأمهات", "علاقات البنات بالآباء، ٢٠٢٦", "/work/")
        + pair("Parfyymin tuulahdus", "A poetic series on scent and inheritance", "نفحة عطر", "سلسلة شعرية عن الرائحة والإرث", "/work/parfyymin-tuulahdus/")
    )
    grid = "".join(f"<a href='/work/{p['slug']}/'>{img(PHOTOS[p['slug']][p['cover']], '(max-width:820px) 50vw, 25vw')}<h3>{p['title']}</h3><p>{p['teaser']}</p></a>" for p in PROJECTS)
    body = f"""<header><a class="brand" href="/opcoes/dois-lares/">Nora Sayyad<span class="ar" lang="ar">نورا صياد</span></a><nav class="sans" aria-label="Main"><a class="keep" href="/work/">Work</a><a href="/news/">Exhibitions</a><a href="/services/">Commissions</a><a class="keep" href="/about/">About</a></nav></header>
<main id="main">
<section class="mirror" aria-label="Two homes">{mirror}</section>
<section class="pair" aria-label="Projects in two languages">{pairs}</section>
<section class="works"><h2>The work · <span class="ar" lang="ar">الأعمال</span></h2><div class="grid">{grid}</div></section>
<section class="close">
  <div class="n"><b>Published in The Washington Post and The Times.<br>Held in Finnish public collections.</b><a href="/about/">Biography & CV →</a></div>
  <div class="s" lang="ar"><b>للتكليفات والمعارض والمحاضرات.</b><a href="/contact/" class="sans" dir="ltr">Get in touch →</a></div>
</section>
</main>
<footer><span>© Nora Sayyad · Helsinki</span><span><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="https://www.instagram.com/norasayyad/">Instagram</a></span></footer>"""
    return doc("Dois lares", "family=Cormorant+Garamond:ital,wght@0,500;1,500&family=Amiri:wght@400;700&family=Inter:wght@400;500", css, body)


# ================================================================ Hub
CONCEPTS = [
    ("simbolos", "Símbolos", "🫒🕊️🧿🌊 — a bio dela vira a estrutura do site",
     "Quatro salas: <b>Oliveira</b> (raízes, família, terra), <b>Pomba</b> (paz, resistência, solidariedade), <b>Olho</b> (olhar e ser vista) e <b>Mar</b> (travessias, fronteiras, diáspora). Cada projeto, exposição e livro mora numa sala. Os nomes aparecem em inglês, finlandês, sueco e árabe. Ao passar o mouse, a sala abre e mostra o que tem dentro.",
     "O site deixa de ser um arquivo em ordem cronológica e passa a ser organizado pelos temas que ela mesma escolheu para se apresentar.", concept_simbolos),
    ("rota", "Rota", "Nascida na Suécia · vive em Helsinque · raízes na Palestina",
     "A home é um percurso: Turku 2020 (BLM) → Helsinque (Palestina) → Stoa/Oulu/IKEA → fronteira Tornio/Haparanda → Lifta → Jordânia → Montreal/Boston/Bristol → de volta a Suomenlinna. Uma coluna fixa diz “você está em…” e muda conforme a rolagem.",
     "Deslocamento e retorno são o assunto central dela. A geografia conta a história melhor que uma lista de projetos.", concept_rota),
    ("visivel", "Visível", "“The right to be seen” · “the politics of looking” · Visible Palestine",
     "Fundo preto e azul do olho grego. Todas as fotos começam cobertas por um cartão com a descrição da pessoa; só aparecem quando o visitante escolhe olhar (mouse ou toque). Antes das fotos, as vozes: frases reais das pessoas retratadas. O poema de palavras “exile / exodus / exhale” abre a página.",
     "É a ideia mais forte da prática dela: quem é visto, por quem e em que termos. O site faz o visitante viver isso.", concept_visivel),
    ("dois-lares", "Dois lares", "Hello · Terve · Hej · مرحبا",
     "Um espelho: coluna nórdica à esquerda (finlandês/sueco, luz fria, neve) e coluna árabe à direita (da direita para a esquerda, luz quente, tatreez). Cada linha diz a mesma coisa em duas direções, e as duas se encontram no meio, em Helsinque. Os projetos aparecem em inglês e em árabe, lado a lado.",
     "Ela escreve em cinco línguas e vive entre dois mundos. O site mostra isso na própria forma, não só no texto.", concept_dois_lares),
]


def hub():
    cards = "".join(f"""<a class="opt" href="/opcoes/{k}/">
  <div class="shots"><img src="/opcoes/shots/{k}-desk.jpg" alt="Prévia do conceito {name} no computador" loading="lazy"><img class="m" src="/opcoes/shots/{k}-mob.jpg" alt="Prévia do conceito {name} no celular" loading="lazy"></div>
  <div class="txt"><span class="tag">Conceito</span><h2>{name}</h2><p class="sub">{sub}</p><p>{desc}</p><p class="why"><b>Por quê:</b> {why}</p><span class="go">Abrir →</span></div>
</a>""" for k, name, sub, desc, why, _ in CONCEPTS)
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Nora Sayyad — Conceitos para o site</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<style>
*,*::before,*::after{{box-sizing:border-box}}
body{{margin:0;background:#f4f3ef;color:#1b1b19;font:400 16px/1.6 system-ui,-apple-system,'Segoe UI',sans-serif}}
.wrap{{max-width:1180px;margin:0 auto;padding:48px 16px 80px}}
h1{{font-size:clamp(1.8rem,4vw,2.6rem);margin:0 0 8px;line-height:1.1}}
.lead{{color:#5a5850;max-width:48rem;margin:0 0 36px}}
.opt{{display:grid;grid-template-columns:1.4fr 1fr;gap:32px;align-items:center;text-decoration:none;color:inherit;background:#fff;border:1px solid #e0ddd4;border-radius:14px;padding:20px;margin-bottom:24px;transition:box-shadow .2s}}
.opt:hover{{box-shadow:0 10px 30px rgba(0,0,0,.08)}}
.shots{{position:relative}}
.shots img{{width:100%;display:block;border-radius:8px;border:1px solid #e0ddd4}}
.shots .m{{position:absolute;right:-8px;bottom:-12px;width:24%;border-radius:10px;box-shadow:0 8px 24px rgba(0,0,0,.2)}}
.tag{{font-size:.75rem;letter-spacing:.12em;text-transform:uppercase;color:#8a877c}}
h2{{margin:4px 0 2px;font-size:1.8rem}}
.sub{{margin:0 0 12px;font-weight:600}}
.why{{color:#5a5850}}
.go{{display:inline-block;margin-top:12px;font-weight:600;border-bottom:2px solid}}
.more{{margin-top:48px;padding-top:24px;border-top:1px solid #e0ddd4;color:#5a5850}}
.more a{{margin-right:18px}}
@media (max-width:800px){{.opt{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
<main class="wrap">
<h1>Quatro conceitos para o site da Nora</h1>
<p class="lead">Cada um parte de uma coisa que ela mesma diz sobre quem é: os símbolos da bio, os três lugares da vida dela, o direito de ser vista e as línguas em que escreve. Não são estilos: são estruturas diferentes para o mesmo conteúdo. O botão “← Todas as opções”, no canto, volta para cá.</p>
{cards}
<p class="more"><b>Opções adicionais:</b> <a href="/opcoes/v2/">versão 2 (Reportagem, Cartas, Tatreez, Sequências)</a> <a href="/opcoes/v1/">versão 1 (Noite, Jornal, Arquivo, Azul)</a> <a href="/">protótipo claro original</a></p>
</main>
</body>
</html>
"""


if __name__ == "__main__":
    for k, *_, fn in CONCEPTS:
        out = ROOT / k / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(fn(), encoding="utf-8")
    (ROOT / "index.html").write_text(hub(), encoding="utf-8")
    print("built concepts")
