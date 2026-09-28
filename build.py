#!/usr/bin/env python3
"""Generate the static prototype pages with a shared header/footer.

Run: python3 build.py
Text marked with class="todo" is a placeholder to confirm with Nora.
"""
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://www.norasayyad.com"
EMAIL = "contact@norasayyad.com"

NAV = [("work", "Work"), ("news", "News"), ("services", "Commissions"), ("about", "About")]

PROJECTS = [
    {
        "slug": "notes-of-resistance",
        "title": "Notes of Resistance",
        "teaser": "Protest, memory and everyday resistance in the Palestinian diaspora.",
        "year": "<span class=todo>2021–2024</span>",
        "place": "<span class=todo>Helsinki · Finland</span>",
        "count": 20,
    },
    {
        "slug": "portraits",
        "title": "Portraits",
        "teaser": "Editorial and personal portraits of artists, activists and neighbours.",
        "year": "<span class=todo>Ongoing</span>",
        "place": "<span class=todo>Finland</span>",
        "count": 15,
    },
    {
        "slug": "project-three",
        "title": "<span class=todo>Project three</span>",
        "teaser": "<span class=todo>One-line description of the project.</span>",
        "year": "<span class=todo>Year</span>",
        "place": "<span class=todo>Place</span>",
        "count": 12,
    },
    {
        "slug": "project-four",
        "title": "<span class=todo>Project four</span>",
        "teaser": "<span class=todo>One-line description of the project.</span>",
        "year": "<span class=todo>Year</span>",
        "place": "<span class=todo>Place</span>",
        "count": 12,
    },
]


def strip_tags(s):
    import re
    return re.sub(r"<[^>]+>", "", s)


def page(path, title, desc, body, current=None, og_image="/assets/og-image.jpg"):
    depth = path.count("/")
    full_title = f"{title} — Nora Sayyad" if title else "Nora Sayyad — Documentary photographer & visual artist"
    url = SITE + ("/" + path.rsplit("index.html", 1)[0] if path != "index.html" else "/")
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
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}{og_image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="alternate" hreflang="en" href="{url}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
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
      <div class="lang" aria-label="Language"><a href="#" aria-current="true">EN</a><a href="#" title="Suomeksi (coming soon)">FI</a><a href="#" title="På svenska (coming soon)">SV</a></div>
      <a class="btn small" href="/contact/">Get in touch</a>
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<section class="newsletter" aria-labelledby="nl-title">
  <div class="wrap narrow">
    <h2 id="nl-title">Exhibitions & new work, a few times a year</h2>
    <p>No spam — just openings, talks and new projects.</p>
    <form action="#" method="post">
      <label class="sr" style="position:absolute;left:-999px" for="nl-email">Email</label>
      <input id="nl-email" type="email" name="email" placeholder="your@email.com" required>
      <button class="btn" type="submit">Subscribe</button>
    </form>
  </div>
</section>
<footer class="site-footer">
  <div class="wrap">
    <p>© Nora Sayyad · Helsinki · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <ul>
      <li><a href="https://www.instagram.com/norasayyad/" rel="me">Instagram</a></li>
      <li><a href="#" rel="me"><span class=todo>LinkedIn</span></a></li>
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


def card(p, n):
    return f"""<a class="card" href="/work/{p['slug']}/">
  <div class="ph" role="img" aria-label="Cover photo: {strip_tags(p['title'])}" data-label="Cover — {strip_tags(p['title'])}"></div>
  <h3>{p['title']}</h3>
  <p>{p['teaser']}</p>
  <div class="meta">{p['year']} · {p['count']} photographs</div>
</a>"""


CREDS = """<div class="creds" aria-label="Published and exhibited in">
  <div class="wrap">
    <p class="eyebrow" style="margin:0">Published & exhibited</p>
    <ul>
      <li>The Washington Post</li>
      <li>The Times</li>
      <li>Helsinki City Museum</li>
      <li>Bristol Museums</li>
      <li><span class=todo>Public collection</span></li>
    </ul>
  </div>
</div>"""

TOUR = """<ul class="tour">
  <li><span>Canada · <span class=todo>Venue</span></span><span class=todo>Dates</span></li>
  <li><span>United States · <span class=todo>Venue</span></span><span class=todo>Dates</span></li>
  <li><span>United Kingdom · Bristol Museums</span><span><span class="status">On now</span></span></li>
</ul>"""


def build_home():
    featured = "\n".join(card(p, i) for i, p in enumerate(PROJECTS[:3]))
    body = f"""<div class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Documentary photographer · Visual artist · Helsinki</p>
      <h1>Nora Sayyad photographs resistance, belonging and the people who carry them.</h1>
      <p class="lead">Finnish-Palestinian documentary photographer published in The Washington Post and The Times, with work held in Finnish public collections.</p>
      <div class="actions">
        <a class="btn" href="/work/">See the work</a>
        <a class="btn ghost" href="/services/">Commission Nora</a>
      </div>
    </div>
    <div class="ph" role="img" aria-label="Signature photograph (high-resolution, not the Instagram export)" data-label="Hero photo — min. 2400px wide, WebP/AVIF"></div>
  </div>
</div>
{CREDS}
<section aria-labelledby="featured">
  <div class="wrap">
    <div class="section-head"><h2 id="featured">Selected projects</h2><a href="/work/">All projects →</a></div>
    <div class="cards">{featured}</div>
  </div>
</section>
<section aria-labelledby="now" style="padding-top:0">
  <div class="wrap">
    <div class="news-feature">
      <div>
        <p class="eyebrow">On tour now</p>
        <h2 id="now">The Lost Paintings</h2>
        <p>An exhibition travelling through Canada, the United States and the United Kingdom.</p>
        {TOUR}
        <a class="btn ghost" href="/news/">Exhibitions & news</a>
      </div>
      <div class="ph wide" role="img" aria-label="Installation view of The Lost Paintings" data-label="Installation view"></div>
    </div>
  </div>
</section>
<section aria-labelledby="about-h" style="padding-top:0">
  <div class="wrap about-top">
    <div class="ph" role="img" aria-label="Portrait of Nora Sayyad" data-label="Professional portrait of Nora"></div>
    <div class="narrow">
      <p class="eyebrow">About</p>
      <h2 id="about-h">Stories told from inside the community, not from the outside looking in.</h2>
      <p><span class=todo>Two or three sentences in Nora's voice: what she photographs, why, and how she works with the people in front of her camera.</span></p>
      <p><a href="/about/">Full biography & CV →</a></p>
    </div>
  </div>
</section>"""
    page("index.html", "", "Nora Sayyad is a Finnish-Palestinian documentary photographer and visual artist in Helsinki, published in The Washington Post and The Times. Available for commissions.", body)


def build_work():
    cards = "\n".join(card(p, i) for i, p in enumerate(PROJECTS))
    body = f"""<section>
  <div class="wrap">
    <p class="eyebrow">Work</p>
    <h1>Projects</h1>
    <p class="lead narrow">Long-form documentary series and portrait work. Each project opens with its story; photos include captions, place and date.</p>
    <div class="cards" style="margin-top:40px">{cards}</div>
  </div>
</section>"""
    page("work/index.html", "Work", "Documentary projects and portraits by photographer Nora Sayyad, including Notes of Resistance.", body, current="work")


def build_project(i):
    p = PROJECTS[i]
    prev = PROJECTS[(i - 1) % len(PROJECTS)]
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    figs = []
    for n in range(1, p["count"] + 1):
        cls = "" if n % 3 == 1 else ("half right" if n % 3 == 2 else "half")
        ratio = "wide" if n % 3 == 1 else ""
        figs.append(f"""<figure class="{cls}">
  <div class="ph {ratio}" role="img" aria-label="Describe what the photo shows ({n})" data-label="Photo {n} — alt text describes the scene, not the filename"></div>
  <figcaption><span class=todo>Caption: who / what, place, date.</span></figcaption>
</figure>""")
        if n == 6 or n == 13:
            figs.append('<div class="chapter wrap narrow" style="padding:0"><h2>Chapter title</h2><p><span class=todo>A short paragraph that moves the story forward between groups of images.</span></p></div>')
    title_txt = strip_tags(p["title"])
    body = f"""<section style="padding-bottom:40px">
  <div class="wrap">
    <p class="eyebrow"><a href="/work/">Work</a> / {title_txt}</p>
    <div class="project-intro">
      <div>
        <h1>{p['title']}</h1>
        <p class="lead">{p['teaser']}</p>
        <p><span class=todo>Opening text (150–250 words): the context, why Nora made this work, who is in it.</span></p>
      </div>
      <ul class="facts">
        <li><span>Year</span><span>{p['year']}</span></li>
        <li><span>Location</span><span>{p['place']}</span></li>
        <li><span>Photographs</span><span>{p['count']}</span></li>
        <li><span>Press</span><span><a href="#"><span class=todo>Published in …</span></a></span></li>
        <li><span>Exhibited</span><span><span class=todo>Venue, year</span></span></li>
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
    page(f"work/{p['slug']}/index.html", title_txt, f"{title_txt} — a documentary photography project by Nora Sayyad. {strip_tags(p['teaser'])}", body, current="work")


def build_about():
    body = """<section>
  <div class="wrap about-top">
    <div class="ph" role="img" aria-label="Portrait of Nora Sayyad" data-label="Portrait of Nora"></div>
    <div class="narrow">
      <p class="eyebrow">About</p>
      <h1>Nora Sayyad</h1>
      <p class="lead">Finnish-Palestinian documentary photographer and visual artist based in Helsinki.</p>
      <p><span class=todo>Short bio (80–120 words), third person, ready to be copied by press and curators.</span></p>
      <p style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn" href="/assets/nora-sayyad-cv.pdf" download>Download CV (PDF)</a><a class="btn ghost" href="/contact/">Contact</a></p>
    </div>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap narrow">
    <h2>CV</h2>
    <details open><summary>Selected publications</summary><ul>
      <li>The Washington Post — <span class=todo>story, year</span></li>
      <li>The Times — <span class=todo>story, year</span></li>
    </ul></details>
    <details><summary>Exhibitions</summary><ul>
      <li>The Lost Paintings — touring exhibition, Canada / USA / UK (incl. Bristol Museums) — <span class=todo>year</span></li>
      <li>Helsinki City Museum — <span class=todo>title, year</span></li>
    </ul></details>
    <details><summary>Public collections</summary><ul><li><span class=todo>Collection name, city</span></li></ul></details>
    <details><summary>Awards & grants</summary><ul><li><span class=todo>—</span></li></ul></details>
    <details><summary>Talks & workshops</summary><ul><li><span class=todo>—</span></li></ul></details>
    <details><summary>Education</summary><ul><li><span class=todo>—</span></li></ul></details>
  </div>
</section>"""
    page("about/index.html", "About", "Biography and CV of Nora Sayyad: publications, exhibitions, public collections, talks and education.", body, current="about")


def build_services():
    items = [
        ("Portraits", "Editorial and personal portraits for publications, organisations and artists."),
        ("Editorial & documentary", "Assignments for newspapers, magazines and NGOs, in Finland and abroad."),
        ("Talks", "Talks on documentary photography, representation and the Palestinian diaspora."),
        ("Workshops", "Photography workshops for schools, museums and community groups."),
    ]
    cards = "".join(
        f'<div class="service"><h3>{t}</h3><p>{d}</p><a class="btn ghost small" href="/contact/?topic={t.split()[0].lower()}">Ask about {t.lower()}</a></div>'
        for t, d in items
    )
    body = f"""<section>
  <div class="wrap">
    <p class="eyebrow">Commissions</p>
    <h1>Work with Nora</h1>
    <p class="lead narrow">Available for assignments in Finland and internationally. Clients include <span class=todo>client names</span>.</p>
    <div class="services" style="margin-top:40px">{cards}</div>
  </div>
</section>
{CREDS}"""
    page("services/index.html", "Commissions", "Commission Nora Sayyad for portraits, editorial and documentary assignments, talks and photography workshops.", body, current="services")


def build_news():
    body = f"""<section>
  <div class="wrap">
    <p class="eyebrow">News</p>
    <h1>Exhibitions & news</h1>
    <div class="news-feature" style="margin-top:32px">
      <div>
        <p><span class="status">On tour</span></p>
        <h2>The Lost Paintings</h2>
        <p><span class=todo>Short description of the exhibition and Nora's role.</span></p>
        {TOUR}
      </div>
      <div class="ph wide" role="img" aria-label="Installation view of The Lost Paintings" data-label="Installation view"></div>
    </div>
    <h2 style="margin-top:64px">Earlier</h2>
    <div class="cards">
      <div class="card"><div class="ph land" role="img" aria-label="Exhibition at Helsinki City Museum" data-label="Helsinki City Museum"></div><h3>Helsinki City Museum</h3><p><span class=todo>Exhibition title</span></p><div class="meta"><span class=todo>Year</span></div></div>
      <div class="card"><div class="ph land" role="img" aria-label="Press feature" data-label="Press"></div><h3>The Washington Post</h3><p><span class=todo>Story title</span></p><div class="meta"><span class=todo>Year</span></div></div>
    </div>
  </div>
</section>"""
    page("news/index.html", "News", "Current and past exhibitions of Nora Sayyad, including the touring exhibition The Lost Paintings.", body, current="news")


def build_contact():
    body = f"""<section>
  <div class="wrap">
    <p class="eyebrow">Contact</p>
    <h1>Let's talk</h1>
    <p class="lead narrow">Commissions, exhibitions, press and print enquiries. I usually reply within <span class=todo>2 working days</span>.</p>
    <form class="contact" action="#" method="post" style="margin-top:32px">
      <div class="two">
        <label>Name<input name="name" autocomplete="name" required></label>
        <label>Email<input type="email" name="email" autocomplete="email" required></label>
      </div>
      <div class="two">
        <label>Organisation<input name="org" autocomplete="organization"></label>
        <label>Topic<select name="topic"><option>Commission</option><option>Exhibition / curatorial</option><option>Press</option><option>Talk or workshop</option><option>Prints</option><option>Other</option></select></label>
      </div>
      <label>Message<textarea name="message" required></textarea></label>
      <div><button class="btn" type="submit">Send message</button></div>
    </form>
    <p style="margin-top:32px">Or email <a href="mailto:{EMAIL}">{EMAIL}</a></p>
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
