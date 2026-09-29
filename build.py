#!/usr/bin/env python3
"""Generate the static prototype pages with a shared header/footer.

Run: python3 build.py
Photos (with alt text) live in content/photos.json and are served from
Nora's existing Squarespace CDN. Text marked class="todo" still needs to be
written or confirmed by Nora.
"""
import json
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://www.norasayyad.com"
# Switch to a domain address (e.g. contact@norasayyad.com) once it exists.
EMAIL = "ellinorasayyad@gmail.com"
PHOTOS = json.loads((ROOT / "content/photos.json").read_text(encoding="utf-8"))

NAV = [("work", "Work"), ("news", "Current"), ("services", "Commissions"), ("about", "About")]

PROJECTS = [
    {
        "slug": "portraits",
        "title": "Portraits",
        "teaser": "Editorial and personal portraits of artists, activists, families and neighbours.",
        "intro": "<span class=todo>Short introduction: how Nora works with the people she photographs, and where these portraits were published.</span>",
        "facts": [
            ("Years", "<span class=todo>2017–2025</span>"),
            ("Location", "Finland"),
            ("Published", "Helsingin Sanomat, Plan International Finland, <span class=todo>…</span>"),
        ],
        "cover": 4,
    },
    {
        "slug": "from-arrival-to-belonging",
        "title": "From Arrival to Belonging? A Decade in Portraits",
        "teaser": "Refugee lives shaped by 2015 and 2022, and the policies and borders in between.",
        "intro": "<em>From Arrival to Belonging? A Decade in Portraits</em> traces refugee lives shaped by two moments — 2015 (Middle East) and 2022 (Ukraine) — and by the policies, borders, and double standards in between. The project honours resilience, skills, and labour, while asking who gets to belong in Finland and its workforce — and at what cost.",
        "facts": [
            ("Years", "2025–2026"),
            ("In collaboration with", "Startup Refugees"),
            ("Exhibited", "IKEA; STOA; Valkea; Revontuli, Finland"),
        ],
        "cover": 1,
    },
    {
        "slug": "parfyymin-tuulahdus",
        "title": "Parfyymin tuulahdus",
        "teaser": "Scent, memory and inheritance — a poetic series.",
        "intro": "<span class=todo>Short introduction to the series (in English, with the Finnish title explained).</span>",
        "facts": [
            ("Press", '<a href="https://www.ruskeattytot.fi/podcast-parfyymin-tuulahdus">Podcast: Parfyymin tuulahdus, Ruskeat tytöt</a>'),
        ],
        "cover": 0,
    },
    {
        "slug": "notes-of-resistance",
        "title": "Notes of Resistance",
        "teaser": "Black Lives Matter in Finland and the Palestine solidarity movement in Helsinki, from the street.",
        "intro": "<span class=todo>Draft — Nora to confirm:</span> Since the Black Lives Matter demonstrations of 2020, Nora has documented the people who take to the streets of Finland against racism and, later, in solidarity with Palestine: the signs they make, the vigils they hold and the care they show one another. Photographs from the series appeared in <em>NO JUSTICE, NO PEACE</em>, awarded Gold at Vuoden Huiput 2021.",
        "facts": [
            ("Years", "2020–<span class=todo>2025</span>"),
            ("Location", "Finland"),
            ("Book", '<a href="https://vuodenhuiput.fi/work/no-justice-no-peace/">No Justice, No Peace</a> (2021)'),
            ("Press", '<a href="https://www.ruskeattytot.fi/freepalestine-documented">#FREEPALESTINE: Documented</a>'),
        ],
        "cover": 7,
    },
]


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def img(p, sizes="100vw", cls="", lazy=True, attrs=""):
    """Responsive <img> using Squarespace's ?format= resizing."""
    widths = [w for w in (500, 750, 1000, 1500, 2500) if w <= p["w"]] or [p["w"]]
    srcset = ", ".join(f'{p["src"]}?format={w}w {w}w' for w in widths)
    default = f'{p["src"]}?format={max([w for w in widths if w <= 1500] or widths[:1])}w'
    loading = ' loading="lazy"' if lazy else ' fetchpriority="high"'
    return (f'<img src="{default}" srcset="{srcset}" sizes="{sizes}" width="{p["w"]}" height="{p["h"]}" '
            f'alt="{escape(p["alt"])}"{loading} decoding="async"{f" class={cls}" if cls else ""}{attrs}>')


def page(path, title, desc, body, current=None, og=None):
    full_title = f"{title} — Nora Sayyad" if title else "Nora Sayyad — Documentary photographer & visual artist, Helsinki"
    url = SITE + ("/" + path.rsplit("index.html", 1)[0] if path != "index.html" else "/")
    og_image = (og or PHOTOS["hero"])["src"] + "?format=1500w"
    nav = "".join(
        f'<li><a href="/{slug}/"{" aria-current=page" if current == slug else ""}>{label}</a></li>'
        for slug, label in NAV
    )
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{escape(desc)}">\n<meta name="robots" content="noindex,nofollow">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://images.squarespace-cdn.com">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600&family=Newsreader:opsz,wght@6..72,400;6..72,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/">Nora Sayyad</a>
    <button class="menu-toggle" aria-label="Menu" aria-expanded="false" aria-controls="nav">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 7h18M3 12h18M3 17h18"/></svg>
    </button>
    <nav class="nav" id="nav" aria-label="Main">
      <ul>{nav}</ul>
      <div class="lang" aria-label="Language"><span aria-current="true">EN</span><span class="disabled" aria-disabled="true" title="Suomeksi — planned">FI</span></div>
      <a class="btn small" href="/contact/">Get in touch</a>
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <p>© Nora Sayyad · Helsinki, Finland · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <ul>
      <li><a href="https://www.instagram.com/norasayyad/" rel="me">Instagram</a></li>
      <li><a href="https://www.womenphotograph.com">Women Photograph</a></li>
      <li><a href="/contact/">Contact</a></li>
    </ul>
  </div>
</footer>
<script src="/assets/js/main.js" defer></script>
</body>
</html>
"""
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


def cover(p):
    return PHOTOS[p["slug"]][p["cover"]]


def card(p):
    return f"""<a class="card" href="/work/{p['slug']}/">
  <div class="frame">{img(cover(p), "(max-width: 700px) 100vw, 33vw", "cover")}</div>
  <h3>{p['title']}</h3>
  <p>{p['teaser']}</p>
  <div class="meta">{len(PHOTOS[p['slug']])} photographs</div>
</a>"""


CREDS = """<div class="creds" aria-label="Published, exhibited and collected by">
  <div class="wrap">
    <p class="eyebrow" style="margin:0">Published · exhibited · collected</p>
    <ul>
      <li>The Washington Post</li>
      <li>The Times</li>
      <li>Helsinki City Museum</li>
      <li>Finnish Museum of Photography</li>
      <li>Bristol Museum & Art Gallery</li>
      <li>National Library of Finland</li>
    </ul>
  </div>
</div>"""

TOUR = """<ul class="tour">
  <li><span>Montréal, Canada · Articule; MAI – Montréal, arts interculturels</span><span class=todo>Dates</span></li>
  <li><span>United States · Unbound Visual Arts</span><span class=todo>Dates</span></li>
  <li><span>Belfast, Northern Ireland · The MAC</span><span class=todo>Dates</span></li>
  <li><span>London, UK · P21 Gallery</span><span class=todo>Dates</span></li>
  <li><span>Bristol, UK · Bristol Museum & Art Gallery</span><span><span class="status">On now</span></span></li>
</ul>"""

BIO_SHORT = "Finnish-Palestinian visual artist and documentary photographer, born in Sweden and based in Helsinki."


def build_home():
    slides = [
        PHOTOS["portraits"][15],
        PHOTOS["from-arrival-to-belonging"][1],
        PHOTOS["notes-of-resistance"][7],
        PHOTOS["parfyymin-tuulahdus"][0],
    ]
    slide_html = "\n".join(
        f'<figure class="hero-slide{" active" if i == 0 else ""}" data-hero-slide aria-hidden="{"false" if i == 0 else "true"}>{img(ph, "100vw", lazy=i > 0)}</figure>'
        for i, ph in enumerate(slides)
    )
    featured_projects = [
        next(p for p in PROJECTS if p["slug"] == "from-arrival-to-belonging"),
        next(p for p in PROJECTS if p["slug"] == "notes-of-resistance"),
        next(p for p in PROJECTS if p["slug"] == "parfyymin-tuulahdus"),
        next(p for p in PROJECTS if p["slug"] == "portraits"),
    ]
    featured = "\n".join(
        f"""<a class="editorial-project" href="/work/{p['slug']}/">
  <div class="editorial-project-image">{img(cover(p), "(max-width: 640px) 100vw, 25vw", "cover")}</div>
  <h3>{p['title']}</h3>
  <div class="meta">{'Ongoing' if p['slug'] == 'portraits' else strip_tags(p['facts'][0][1]) if p['facts'] else 'Project'} · {len(PHOTOS[p['slug']])} photographs</div>
</a>""" for p in featured_projects
    )
    body = f"""<section class="editorial-hero" aria-labelledby="home-title">
  <div class="wrap">
    <div class="hero-stage" data-hero>
      <div class="hero-slides">{slide_html}</div>
      <div class="hero-shade"></div>
      <div class="hero-copy">
        <p class="eyebrow light">Photographer · Artist · Visual reporter · Helsinki</p>
        <h1 id="home-title">Nora<br>Sayyad</h1>
        <p>Finnish-Palestinian photographer, artist and visual reporter whose practice moves between documentary and poetic storytelling.</p>
        <a class="btn inverse" href="/work/">Explore work →</a>
      </div>
      <div class="hero-controls" aria-label="Featured photographs">
        <span data-hero-index>01 / {len(slides):02d}</span>
        <button type="button" data-hero-prev aria-label="Previous photograph">←</button>
        <button type="button" data-hero-next aria-label="Next photograph">→</button>
      </div>
    </div>
  </div>
</section>
<section class="selected-work" aria-labelledby="featured">
  <div class="wrap">
    <div class="section-head">
      <div><p class="eyebrow">Archive in motion</p><h2 id="featured">Selected projects</h2></div>
      <a class="text-link" href="/work/">View all projects →</a>
    </div>
    <div class="editorial-projects">{featured}</div>
  </div>
</section>
{CREDS}
<section class="current-section" aria-labelledby="now">
  <div class="wrap">
    <div class="section-head">
      <div><p class="eyebrow">Current</p><h2 id="now">Exhibitions & selected press</h2></div>
      <a class="text-link" href="/news/">View current →</a>
    </div>
    <div class="current-grid">
      <div class="current-image">{img(PHOTOS['notes-of-resistance'][9], "(max-width: 820px) 100vw, 38vw")}</div>
      <article class="current-main">
        <p class="eyebrow">On tour · 2025–2026</p>
        <h3>The Lost Paintings: A Prelude to Return</h3>
        <p>A travelling group exhibition presented across Canada, the United States, Northern Ireland and the United Kingdom, including Nora Sayyad's work <em>Utopia</em>.</p>
        <a class="btn ghost" href="/news/">Exhibitions & dates →</a>
      </article>
      <article class="press-note">
        <p class="eyebrow">Selected press</p>
        <h3>The Washington Post</h3>
        <p>“How is happiness measured around the world?” — photographed in Finland.</p>
        <hr>
        <h3>The Times</h3>
        <p>Financial literacy and Yrityskylä in Finland.</p>
        <a class="text-link" href="/about/">Biography & press →</a>
      </article>
    </div>
  </div>
</section>
<section class="manifesto-band">
  <div class="wrap manifesto-frame">
    {img(PHOTOS['hero'], "100vw")}
    <div class="manifesto-shade"></div>
    <blockquote>Photography as a space for memory, dialogue and self-determination.<small>Nora Sayyad · visual practice</small></blockquote>
  </div>
</section>
<section class="home-about" aria-labelledby="about-h">
  <div class="wrap about-editorial">
    <div class="ph about-portrait" role="img" aria-label="Portrait of Nora Sayyad" data-label="Portrait of Nora — original photo to be selected"></div>
    <div>
      <p class="eyebrow">About</p>
      <h2 id="about-h">Documentary, poetic and conceptual.</h2>
      <p class="lead">Her practice explores belonging, memory, diaspora, representation and the politics of looking.</p>
      <p>Based in Helsinki, Nora works across photography, visual reporting, writing, teaching and public speaking.</p>
      <a class="text-link" href="/about/">Biography & CV →</a>
    </div>
  </div>
</section>
<section class="commission-band">
  <div class="wrap commission-editorial">
    <h2>Commissions<br>& editorial.</h2>
    <div>
      <p>Available for editorial, institutional and selected commissioned work in Finland and internationally.</p>
      <a class="btn inverse" href="/contact/">Discuss a project →</a>
    </div>
  </div>
</section>"""
    page("index.html", "", "Nora Sayyad is a Finnish-Palestinian photographer, artist and visual reporter based in Helsinki, working across documentary and poetic storytelling.", body)


def build_work():
    cards = "\n".join(card(p) for p in PROJECTS)
    body = f"""<section class="work-index">
  <div class="wrap">
    <p class="eyebrow">Work</p>
    <h1>Projects</h1>
    <p class="lead narrow">Long-form documentary series, portrait work and poetic projects. Each one opens with its story.</p>
    <div class="cards" style="margin-top:40px">{cards}</div>
  </div>
</section>"""
    page("work/index.html", "Work", "Documentary projects and portraits by Nora Sayyad: Notes of Resistance, From Arrival to Belonging?, Portraits and Parfyymin tuulahdus.", body, current="work")


def build_project(i):
    p = PROJECTS[i]
    prev = PROJECTS[(i - 1) % len(PROJECTS)]
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    photos = PHOTOS[p["slug"]]
    figs = []
    for n, ph in enumerate(photos):
        if ph.get("chapter"):
            figs.append(f'<div class="chapter"><p class="eyebrow">Chapter</p><h2>{ph["chapter"]}</h2></div>')
        landscape = ph["w"] > ph["h"]
        cls = "" if landscape else ("half right" if n % 2 else "half")
        sizes = "(max-width: 1200px) 100vw, 1150px" if landscape else "(max-width: 760px) 100vw, 720px"
        figs.append(f"""<figure class="{cls}">
  {img(ph, sizes, lazy=n > 0)}
  <figcaption><span class=todo>Caption: place, date.</span></figcaption>
</figure>""")
    facts = "".join(f"<li><span>{k}</span><span>{v}</span></li>" for k, v in p["facts"])
    title_txt = strip_tags(p["title"])
    body = f"""<section style="padding-bottom:40px">
  <div class="wrap">
    <p class="eyebrow"><a href="/work/">Work</a> / {title_txt}</p>
    <div class="project-intro">
      <div>
        <h1>{p['title']}</h1>
        <p class="lead">{p['teaser']}</p>
        <p>{p['intro']}</p>
      </div>
      <ul class="facts">
        {facts}
        <li><span>Photographs</span><span>{len(photos)}</span></li>
      </ul>
    </div>
  </div>
</section>
<div class="wrap story">
{chr(10).join(figs)}
</div>
<section>
  <div class="wrap">
    <nav class="pager" aria-label="Projects">
      <a class="prev" href="/work/{prev['slug']}/"><small>← Previous</small>{prev['title']}</a>
      <a class="all" href="/work/">All projects</a>
      <a class="next" href="/work/{nxt['slug']}/"><small>Next →</small>{nxt['title']}</a>
    </nav>
  </div>
</section>"""
    page(f"work/{p['slug']}/index.html", title_txt, f"{title_txt} — a project by photographer Nora Sayyad. {strip_tags(p['teaser'])}", body, current="work", og=cover(p))


def cv(title, rows, open_=False):
    items = "".join(f"<li><b>{y}</b> {t}</li>" for y, t in rows)
    return f'<details{" open" if open_ else ""}><summary>{title}</summary><ul class="cv">{items}</ul></details>'


def build_about():
    body = f"""<section>
  <div class="wrap about-top">
    <div class="ph" role="img" aria-label="Portrait of Nora Sayyad" data-label="Portrait of Nora — photo needed"></div>
    <div class="narrow">
      <p class="eyebrow">About</p>
      <h1>Nora Sayyad</h1>
      <p class="lead">{BIO_SHORT}</p>
      <p>Her practice moves between documentary, poetic and conceptual approaches, exploring the politics of looking, questions of representation, and how photography can become a space for memory, dialogue and self-determination. Drawing from personal and collective histories, her work examines connection, belonging and lived experience in relation to wider social and political realities.</p>
      <p>Her work has been exhibited internationally, including as part of <em>The Lost Paintings: A Prelude to Return</em>, and presented at the Helsinki City Museum, the Finnish Museum of Photography and HIAP. Her photographs have been published by The Washington Post and The Times, and are held in the public collections of the Migration Institute of Finland, the Finnish Heritage Agency and the National Library of Finland.</p>
      <p>Alongside her artistic practice she works across visual reporting, teaching, writing, public speaking and artivism, and has collaborated with organisations including Plan International Finland. In 2021 she was assistant curator of the award-winning <em>No Justice, No Peace</em>.</p>
      <p style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn" href="#cv">View full CV</a><a class="btn ghost" href="/contact/">Contact</a></p>
    </div>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap narrow">
    <h2 id="cv">CV</h2>
    {cv("Solo exhibitions", [
        ("2025–26", "<em>From Arrival to Belonging: A Decade in Portraits</em>, with Startup Refugees — IKEA; STOA; Valkea; Revontuli, Finland"),
        ("2025", "<em>Untitled: Palestine</em> (working title / ongoing work), Pop-up HIAP, Helsinki, Finland"),
        ("2024", "<em>Tervetuloa, tervemenoa: Suomi muuttoliikkeessä</em>, with the Migration Institute of Finland — touring Finnish universities and Turku City Library"),
        ("2022", "<em>Wired This Way</em>, STOA Cultural Center, Helsinki"),
        ("2021", "<em>Voimanaisia</em>, with Plan International Finland — Vuotalo & Maunula House, Helsinki"),
        ("2017", "<em>Finding Forgiveness</em>, Logomo, Turku, with the Finnish Association for Abducted Children"),
        ("2015", "<em>Hour of Your Reality</em>, Book Café, Turku"),
    ], True)}
    {cv("Selected group exhibitions", [
        ("2025–26", '<a href="https://www.thelostpaintings.com/artist-sayyad"><em>The Lost Paintings: A Prelude to Return</em></a> — Articule; MAI Montréal; Unbound Visual Arts; The MAC; P21 Gallery; Bristol Museum & Art Gallery'),
        ("2025", "<em>Förkolnade Minnen / Muistoihin Hiiltyneet</em>, Näse Gård, Porvoo"),
        ("2023", '<a href="https://www.helsinginkaupunginmuseo.fi/2023/04/20/being-black-poimintoja-afrosuomalaisuudesta-tuo-esiin-moniaanista-helsinkia/"><em>Being Black – poimintoja afrosuomalaisuudesta</em></a>, Helsinki City Museum'),
        ("2020", "<em>Unfold</em>, The Finnish Museum of Photography, Helsinki"),
        ("2019", "<em>Finding Forgiveness</em>, Frauen Museum, Wiesbaden, Germany"),
        ("2018", "<em>Islam and I</em>, Migration Institute of Finland, Turku"),
        ("2017", "<em>Movement</em>, Kaapelitehdas, Helsinki · <em>Matkalla / På Väg</em>, Art Gallery, Vaasa"),
    ])}
    {cv("Public collections", [("", "Migration Institute of Finland"), ("", "The Finnish Heritage Agency"), ("", "The National Library of Finland")])}
    {cv("Awards & residencies", [
        ("2025", "The Lost Paintings Residency, Boston, US"),
        ("2025", '<a href="https://urbanapa.fi/events/ua-miniresidencies-nora-sayyad/">UrbanApa Miniresidencies / HIAP</a>, Helsinki'),
        ("2025", "Summer Well: Art and Activism, Saari Residence, Kone Foundation"),
        ("2021", "<em>No Justice, No Peace</em> — Vuoden Huiput, Gold; Finland's Most Beautiful Books, Special Books (assistant curator)"),
        ("2019", "Jouko Lehtola Foundation & The Finnish Institute, St. Petersburg"),
    ])}
    {cv("Selected assignments", [
        ("2026", "The Times — financial literacy in Finland (Yrityskylä)"),
        ("2025", "The Washington Post — “How is happiness measured around the world?”"),
    ])}
    {cv("Selected press", [
        ("", '<a href="https://brooklineartscenter.org/lost-paintings-project">The Lost Paintings: A Prelude to Return</a> — Brookline Arts Center'),
        ("", '<a href="https://akimbo.ca/akimblog/the-lost-paintings-at-articule-and-mai-montreal/">The Lost Paintings at articule and MAI, Montréal</a> — Akimbo'),
        ("", '<a href="https://www.ruskeattytot.fi/podcast-parfyymin-tuulahdus">Podcast: Parfyymin tuulahdus</a> — Ruskeat tytöt'),
        ("", '<a href="https://www.ruskeattytot.fi/freepalestine-documented">#FREEPALESTINE: Documented</a> — Ruskeat tytöt'),
        ("", '<a href="https://vuodenhuiput.fi/work/no-justice-no-peace/">No Justice, No Peace</a> — Vuoden Huiput'),
        ("", '<a href="https://plan.fi/plan-lehti/artikkeli/aitien-ja-tyttarien-vahva-side/">Äitien ja tyttärien vahva side</a> — Plan International'),
    ])}
    {cv("Publications & clients", [("", "The Washington Post, The Times and The Sunday Times, Helsingin Sanomat, Hufvudstadsbladet, Yle, STT, LensCulture, Kone Foundation, Plan International Finland, City of Helsinki, University of Helsinki, Ministry of Economic Affairs and Employment of Finland, Startup Refugees, Nordic Culture Point, and others")])}
    {cv("Talks, teaching & juries", [("2017–", "Plan International Finland, STOA, Espoo School of Art, Yle Kultur, Migration Institute of Finland, Nordic Migration Research, ANTI Festival, Finnish Photojournalists and others")])}
    {cv("Education", [
        ("2022", "MA, Photography and Film — Aalto University School of Arts, Design and Architecture"),
        ("2017", "BA, Culture and Arts (Photography) — Novia University of Applied Sciences"),
    ])}
    {cv("Memberships", [("", "Women Photograph (US) · Association of Photographic Artists · Kuvasto ry · GAP Creatives Database")])}
  </div>
</section>"""
    page("about/index.html", "About", "Biography and CV of Nora Sayyad: exhibitions, public collections, awards, press, teaching and education.", body, current="about")


def build_services():
    items = [
        ("Portraits", "Editorial and personal portraits for publications, organisations and artists."),
        ("Editorial & documentary", "Visual reporting for newspapers, magazines, NGOs and institutions, in Finland and abroad."),
        ("Talks", "Lectures on documentary photography, representation and the politics of looking."),
        ("Workshops", "Photography workshops for schools, museums and community groups."),
    ]
    topic_map = {
        "Portraits": "Commission",
        "Editorial & documentary": "Commission",
        "Talks": "Talk or workshop",
        "Workshops": "Talk or workshop",
    }
    cards = "".join(
        f'<div class="service"><h3>{t}</h3><p>{d}</p><a class="btn ghost small" href="/contact/?topic={topic_map[t].replace(" ", "+")}">Ask about {t.lower()}</a></div>'
        for t, d in items
    )
    body = f"""<section>
  <div class="wrap">
    <p class="eyebrow">Commissions</p>
    <h1>Work with Nora</h1>
    <p class="lead narrow">Available for projects and commissions in Finland and internationally. Past clients include Plan International Finland, the City of Helsinki, the University of Helsinki, Kone Foundation and Startup Refugees.</p>
    <div class="services" style="margin-top:40px">{cards}</div>
  </div>
</section>
{CREDS}"""
    page("services/index.html", "Commissions", "Commission Nora Sayyad for portraits, editorial and documentary assignments, talks and photography workshops.", body, current="services")


def build_news():
    body = f"""<section>
  <div class="wrap">
    <p class="eyebrow">Exhibitions</p>
    <h1>Exhibitions & news</h1>
    <div class="news-feature" style="margin-top:32px">
      <div>
        <p><span class="status">On tour</span></p>
        <h2>The Lost Paintings: A Prelude to Return</h2>
        <p>Group exhibition, 2025–2026. <a href="https://www.thelostpaintings.com/artist-sayyad">About Nora's contribution →</a></p>
        {TOUR}
        <p>Press: <a href="https://akimbo.ca/akimblog/the-lost-paintings-at-articule-and-mai-montreal/">Akimbo</a> · <a href="https://brooklineartscenter.org/lost-paintings-project">Brookline Arts Center</a></p>
      </div>
      <div class="ph wide" role="img" aria-label="Installation view of The Lost Paintings" data-label="Installation view — photo needed"></div>
    </div>
    <h2 style="margin-top:64px">Also in 2025–2026</h2>
    <div class="cards">
      <a class="card" href="/work/from-arrival-to-belonging/"><div class="frame">{img(PHOTOS['from-arrival-to-belonging'][5], "(max-width: 700px) 100vw, 33vw", "cover")}</div><h3>From Arrival to Belonging: A Decade in Portraits</h3><p>Solo exhibition with Startup Refugees — IKEA; STOA; Valkea; Revontuli</p></a>
      <div class="card"><div class="ph land" role="img" aria-label="Untitled Palestine pop-up at HIAP" data-label="Photo needed"></div><h3>Untitled: Palestine</h3><p>Working title / ongoing work — Pop-up HIAP, Helsinki, Finland</p><div class="meta">2025</div></div>
      <div class="card"><div class="ph land" role="img" aria-label="Näse Gård, Porvoo" data-label="Photo needed"></div><h3>Förkolnade Minnen / Muistoihin Hiiltyneet</h3><p>Group exhibition, Näse Gård, Porvoo</p><div class="meta">2025</div></div>
    </div>
  </div>
</section>"""
    page("news/index.html", "Exhibitions", "Current and past exhibitions of Nora Sayyad, including the touring exhibition The Lost Paintings: A Prelude to Return.", body, current="news")


def build_contact():
    body = f"""<section class="contact-section">
  <div class="wrap contact-layout">
    <div class="contact-copy">
      <p class="eyebrow">Contact</p>
      <h1>Let's talk.</h1>
      <p class="lead">Commissions, exhibitions, press, talks and selected collaborations.</p>
      <div class="contact-meta">
        <div><span>Based in</span><b>Helsinki, Finland</b></div>
        <div><span>Email</span><a href="mailto:{EMAIL}">{EMAIL}</a></div>
        <div><span>Instagram</span><a href="https://www.instagram.com/norasayyad/">@norasayyad</a></div>
      </div>
    </div>
    <div>
      <form class="contact" action="mailto:{EMAIL}" method="post" data-mailto-form>
        <div class="two">
          <label>Name<input name="name" autocomplete="name" required></label>
          <label>Email<input type="email" name="email" autocomplete="email" required></label>
        </div>
        <div class="two">
          <label>Organisation<input name="org" autocomplete="organization"></label>
          <label>Topic<select name="topic"><option>Commission</option><option>Exhibition / curatorial</option><option>Press</option><option>Talk or workshop</option><option>Prints</option><option>Other</option></select></label>
        </div>
        <label>Message<textarea name="message" required></textarea></label>
        <div><button class="btn" type="submit">Open email draft</button></div>
        <p class="form-note">Preview mode: this opens your email application with the message filled in. A direct web form will be connected before launch.</p>
      </form>
    </div>
  </div>
</section>"""
    page("contact/index.html", "Contact", "Contact photographer Nora Sayyad for commissions, exhibitions, press, talks and prints.", body)




if __name__ == "__main__":
    build_home()
    build_work()
    for i in range(len(PROJECTS)):
        build_project(i)
    build_about()
    build_services()
    build_news()
    build_contact()
    print("built")
