const IS_FI = document.documentElement.lang === 'fi';
// Site root, so fetches and result links also work when the preview is served from a sub-path (GitHub Pages).
const BASE = (document.querySelector('link[href*="/assets/css/style.css"]')?.getAttribute('href') || '').split('/assets/')[0];

// Mobile menu: drawer from the right; a tap anywhere that is not a control closes it
const toggle = document.querySelector('.menu-toggle');
const nav = document.getElementById('nav');
if (toggle && nav) {
  const setMenu = (open) => {
    nav.classList.toggle('open', open);
    document.body.classList.toggle('menu-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    if (open) {
      window.setTimeout(() => nav.querySelector('ul a')?.focus({ preventScroll: true }), 20);
    } else if (document.activeElement && nav.contains(document.activeElement)) {
      toggle.focus();
    }
  };
  toggle.addEventListener('click', () => setMenu(!nav.classList.contains('open')));
  document.querySelectorAll('[data-nav-close]').forEach(el => el.addEventListener('click', () => setMenu(false)));
  nav.addEventListener('click', (e) => {
    if (!nav.classList.contains('open')) return;
    if (e.target.closest('a')) { setMenu(false); return; }
    if (!e.target.closest('button, input, label, .site-search, .lang')) setMenu(false);
  });
  nav.querySelectorAll('.sub-toggle').forEach(btn => btn.addEventListener('click', () => {
    const open = btn.getAttribute('aria-expanded') !== 'true';
    btn.setAttribute('aria-expanded', String(open));
    btn.closest('.has-sub').classList.toggle('sub-open', open);
  }));
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && nav.classList.contains('open')) setMenu(false); });
  window.matchMedia('(min-width: 961px)').addEventListener('change', (m) => { if (m.matches) setMenu(false); });
}

// Home header on mobile stays fixed over the hero and gains a background once the page scrolls
const homeHeader = document.querySelector('.page-home .site-header');
if (homeHeader) {
  const onScroll = () => homeHeader.classList.toggle('is-scrolled', window.scrollY > 40);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });
}

// Site search over assets/search-index.json (built by build.py)
const searchForms = [...document.querySelectorAll('[data-search]')];
if (searchForms.length) {
  let index = null;
  const fold = (t) => (t || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
  const load = () => index || (index = fetch(BASE + (IS_FI ? '/assets/search-index-fi.json' : '/assets/search-index.json')).then(r => r.json()).then(rows =>
    rows.map(r => ({ ...r, fTitle: fold(r.title), fBody: fold(r.desc + ' ' + r.text + ' ' + r.alt), raw: r.text + ' ' + r.alt }))));
  const esc = (t) => t.replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const snippet = (row, term) => {
    const at = fold(row.raw).indexOf(term);
    if (at < 0) return esc(row.desc);
    const from = Math.max(0, at - 50);
    const text = row.raw.slice(from, at + 90);
    const hit = at - from;
    return (from ? '…' : '') + esc(text.slice(0, hit)) + '<mark>' + esc(text.slice(hit, hit + term.length)) + '</mark>' + esc(text.slice(hit + term.length)) + '…';
  };
  const run = async (form) => {
    const input = form.querySelector('input');
    const list = form.querySelector('.search-results');
    const terms = fold(input.value).split(/\s+/).filter(t => t.length > 1);
    if (!terms.length) { list.replaceChildren(); form.classList.remove('has-results'); return []; }
    const rows = await load();
    const hits = rows.map(r => {
      let score = 0;
      for (const t of terms) {
        const inBody = r.fBody.split(t).length - 1;
        if (!inBody && !r.fTitle.includes(t)) return null;
        score += (r.fTitle.includes(t) ? 10 : 0) + Math.min(inBody, 6);
      }
      return { r, score };
    }).filter(Boolean).sort((a, b) => b.score - a.score).slice(0, 6);
    list.innerHTML = hits.length
      ? hits.map(({ r }) => `<li><a href="${BASE + r.url}"><b>${esc(r.title)}</b><span>${snippet(r, terms[0])}</span></a></li>`).join('')
      : `<li class="search-empty">${IS_FI ? 'Ei tuloksia' : 'No results'}</li>`;
    form.classList.add('has-results');
    return hits;
  };
  searchForms.forEach(form => {
    const input = form.querySelector('input');
    input.addEventListener('focus', load, { once: true });
    input.addEventListener('input', () => run(form));
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const hits = await run(form);
      if (hits.length) location.href = BASE + hits[0].r.url;
    });
  });

  const searchToggle = document.querySelector('.search-toggle');
  const panel = document.getElementById('search-panel');
  if (searchToggle && panel) {
    const setPanel = (open) => {
      panel.hidden = !open;
      searchToggle.setAttribute('aria-expanded', String(open));
      if (open) panel.querySelector('input').focus();
    };
    searchToggle.addEventListener('click', () => setPanel(panel.hidden));
    document.addEventListener('keydown', e => { if (e.key === 'Escape' && !panel.hidden) { setPanel(false); searchToggle.focus(); } });
    document.addEventListener('click', e => { if (!panel.hidden && !panel.contains(e.target) && !searchToggle.contains(e.target)) setPanel(false); });
  }
}

// Editorial hero: manual, non-autoplay carousel
const hero = document.querySelector('[data-hero]');
if (hero) {
  const slides = [...hero.querySelectorAll('[data-hero-slide]')];
  const index = hero.querySelector('[data-hero-index]');
  const prev = hero.querySelector('[data-hero-prev]');
  const next = hero.querySelector('[data-hero-next]');
  let active = 0;
  const show = (n) => {
    active = (n + slides.length) % slides.length;
    slides.forEach((slide, i) => {
      const on = i === active;
      slide.classList.toggle('active', on);
      slide.setAttribute('aria-hidden', String(!on));
    });
    if (index) index.textContent = String(active + 1).padStart(2, '0') + ' / ' + String(slides.length).padStart(2, '0');
  };
  prev && prev.addEventListener('click', () => show(active - 1));
  next && next.addEventListener('click', () => show(active + 1));
  hero.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') show(active - 1);
    if (e.key === 'ArrowRight') show(active + 1);
  });
  let x0 = null;
  hero.addEventListener('touchstart', (e) => { x0 = e.touches[0].clientX; }, { passive: true });
  hero.addEventListener('touchend', (e) => {
    if (x0 === null) return;
    const dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 50) show(active + (dx < 0 ? 1 : -1));
    x0 = null;
  });

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let autoplay = null;
  const stopAutoplay = () => { if (autoplay) { clearInterval(autoplay); autoplay = null; } };
  const startAutoplay = () => {
    if (reduceMotion || slides.length < 2 || autoplay) return;
    autoplay = setInterval(() => show(active + 1), 5500);
  };
  hero.addEventListener('mouseenter', stopAutoplay);
  hero.addEventListener('mouseleave', startAutoplay);
  hero.addEventListener('focusin', stopAutoplay);
  hero.addEventListener('focusout', () => window.setTimeout(() => {
    if (!hero.contains(document.activeElement)) startAutoplay();
  }, 0));
  document.addEventListener('visibilitychange', () => document.hidden ? stopAutoplay() : startAutoplay());
  startAutoplay();
}

// Lightbox for project stories: click a photo, then arrows / swipe / Esc
const photos = [...document.querySelectorAll('.story figure')];
if (photos.length) {
  const lb = document.createElement('div');
  lb.className = 'lightbox';
  lb.setAttribute('role', 'dialog');
  lb.setAttribute('aria-modal', 'true');
  lb.setAttribute('aria-label', IS_FI ? 'Kuvakatselin' : 'Photo viewer');
  lb.innerHTML = `<button class="lb-close" aria-label="${IS_FI ? 'Sulje' : 'Close'}">×</button>` +
    `<button class="lb-prev" aria-label="${IS_FI ? 'Edellinen kuva' : 'Previous photo'}">‹</button>` +
    '<div class="lb-stage"></div>' +
    `<button class="lb-next" aria-label="${IS_FI ? 'Seuraava kuva' : 'Next photo'}">›</button>` +
    '<p class="lb-cap"></p>';
  document.body.appendChild(lb);
  const stage = lb.querySelector('.lb-stage');
  const cap = lb.querySelector('.lb-cap');
  let i = 0;
  let lastFocus = null;

  const show = (n) => {
    i = (n + photos.length) % photos.length;
    const media = photos[i].querySelector('.ph, img').cloneNode(true);
    if (media.tagName === 'IMG') { media.sizes = '92vw'; media.removeAttribute('loading'); }
    media.removeAttribute('tabindex');
    stage.replaceChildren(media);
    const fc = photos[i].querySelector('figcaption');
    cap.textContent = `${i + 1} / ${photos.length}` + (fc ? ` — ${fc.textContent}` : '');
  };
  const open = (n) => { lastFocus = document.activeElement; show(n, 0); lb.classList.add('open'); lb.querySelector('.lb-close').focus(); };
  const close = () => { lb.classList.remove('open'); lastFocus && lastFocus.focus(); };

  photos.forEach((fig, n) => {
    const media = fig.querySelector('.ph, img');
    media.tabIndex = 0;
    media.addEventListener('click', () => open(n));
    media.addEventListener('keydown', (e) => { if (e.key === 'Enter') open(n); });
  });
  lb.querySelector('.lb-close').onclick = close;
  lb.querySelector('.lb-prev').onclick = () => show(i - 1);
  lb.querySelector('.lb-next').onclick = () => show(i + 1);
  lb.addEventListener('click', (e) => { if (e.target === lb) close(); });
  document.addEventListener('keydown', (e) => {
    if (!lb.classList.contains('open')) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') show(i - 1);
    if (e.key === 'ArrowRight') show(i + 1);
  });
  let x0 = null;
  lb.addEventListener('touchstart', (e) => { x0 = e.touches[0].clientX; }, { passive: true });
  lb.addEventListener('touchend', (e) => {
    if (x0 === null) return;
    const dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 40) show(i + (dx < 0 ? 1 : -1));
    x0 = null;
  });
}


// Contact preview: preselect topic from query string and open a structured email draft.
const contactForm = document.querySelector('[data-mailto-form]');
if (contactForm) {
  const params = new URLSearchParams(window.location.search);
  const requestedTopic = params.get('topic');
  const select = contactForm.querySelector('select[name="topic"]');
  if (requestedTopic && select) {
    const decoded = requestedTopic.replace(/\+/g, ' ');
    const option = [...select.options].find(o => o.value.toLowerCase() === decoded.toLowerCase());
    if (option) select.value = option.value;
  }

  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!contactForm.reportValidity()) return;
    const data = new FormData(contactForm);
    const subject = `Nora Sayyad website — ${data.get('topic') || 'Enquiry'}`;
    const lines = [
      `Name: ${data.get('name') || ''}`,
      `Email: ${data.get('email') || ''}`,
      `Organisation: ${data.get('org') || ''}`,
      `Topic: ${data.get('topic') || ''}`,
      '',
      String(data.get('message') || '')
    ];
    window.location.href = 'mailto:ellinorasayyad@gmail.com?subject=' +
      encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n'));
  });
}

// Career history: one control opens or closes every section
const cvToggle = document.querySelector('[data-cv-toggle]');
if (cvToggle) {
  const sections = [...document.querySelectorAll('.career-section details')];
  const label = cvToggle.querySelector('.cv-toggle-label');
  const sync = () => {
    const allOpen = sections.every(d => d.open);
    cvToggle.setAttribute('aria-expanded', String(allOpen));
    label.textContent = allOpen ? (IS_FI ? 'Sulje kaikki' : 'Collapse all') : (IS_FI ? 'Avaa kaikki' : 'Expand all');
  };
  cvToggle.addEventListener('click', () => {
    const open = cvToggle.getAttribute('aria-expanded') !== 'true';
    sections.forEach(d => { d.open = open; });
    sync();
  });
  sections.forEach(d => d.addEventListener('toggle', sync));
}

// Switching EN/FI keeps the reader where they were: same open sections, same spot on the page.
// Both language versions share the same structure, so blocks are matched by their order.
(() => {
  const KEY = 'nora-lang-switch';
  const blocks = () => [...document.querySelectorAll('main section, main details, main figure, main h1, main h2, main h3')];
  document.querySelectorAll('.lang a[hreflang]').forEach(a => a.addEventListener('click', () => {
    if (a.hasAttribute('aria-current')) return;
    const list = blocks();
    let i = list.findIndex(el => el.getBoundingClientRect().bottom > 80);
    if (i < 0) i = 0;
    const state = {
      to: new URL(a.href, location.href).pathname,
      open: [...document.querySelectorAll('main details')].map(d => d.open),
      i, offset: list[i] ? list[i].getBoundingClientRect().top : 0,
    };
    try { sessionStorage.setItem(KEY, JSON.stringify(state)); } catch (e) { /* storage unavailable: plain navigation */ }
  }));
  let state = null;
  try { state = JSON.parse(sessionStorage.getItem(KEY) || 'null'); sessionStorage.removeItem(KEY); } catch (e) { state = null; }
  if (!state || state.to !== location.pathname) return;
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  document.querySelectorAll('main details').forEach((d, n) => { if (state.open[n]) d.open = true; });
  document.querySelectorAll('main details').forEach(d => d.dispatchEvent(new Event('toggle')));
  const restore = () => {
    const el = blocks()[state.i];
    if (el) window.scrollTo({ top: el.getBoundingClientRect().top + window.scrollY - state.offset, behavior: 'instant' });
  };
  restore();
  window.addEventListener('load', restore, { once: true });
})();

// About: the two bio layouts alternate (prototype comparison); arrows step through them
const aboutRotator = document.querySelector('[data-about-rotator]');
if (aboutRotator) {
  const variants = [...aboutRotator.querySelectorAll('[data-about-variant]')];
  const label = aboutRotator.querySelector('[data-about-label]');
  const labels = IS_FI ? ['Vaihtoehto A · yksi palsta', 'Vaihtoehto B · kaksi palstaa'] : variants.map(v => v.dataset.label);
  let current = 0, timer = null;
  const show = (n) => {
    current = (n + variants.length) % variants.length;
    variants.forEach((v, i) => { v.classList.toggle('is-active', i === current); v.setAttribute('aria-hidden', String(i !== current)); });
    if (label) label.textContent = labels[current];
  };
  const stop = () => { if (timer) { clearInterval(timer); timer = null; } };
  const start = () => { if (!timer && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) timer = setInterval(() => show(current + 1), 7000); };
  aboutRotator.querySelector('[data-about-prev]')?.addEventListener('click', () => { show(current - 1); });
  aboutRotator.querySelector('[data-about-next]')?.addEventListener('click', () => { show(current + 1); });
  aboutRotator.addEventListener('mouseenter', stop);
  aboutRotator.addEventListener('mouseleave', start);
  aboutRotator.addEventListener('focusin', stop);
  show(0); start();
}
