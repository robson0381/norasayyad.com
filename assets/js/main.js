// Mobile menu
const toggle = document.querySelector('.menu-toggle');
const nav = document.getElementById('nav');
if (toggle && nav) {
  const firstLink = () => nav.querySelector('a, button, [tabindex]:not([tabindex="-1"])');
  const setMenu = (open) => {
    nav.classList.toggle('open', open);
    toggle.setAttribute('aria-expanded', String(open));
    document.body.style.overflow = open ? 'hidden' : '';
    if (open) {
      window.setTimeout(() => firstLink()?.focus(), 20);
    } else if (document.activeElement && nav.contains(document.activeElement)) {
      toggle.focus();
    }
  };
  toggle.addEventListener('click', () => setMenu(!nav.classList.contains('open')));
  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setMenu(false)));
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && nav.classList.contains('open')) setMenu(false); });
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
}

// Lightbox for project stories: click a photo, then arrows / swipe / Esc
const photos = [...document.querySelectorAll('.story figure')];
if (photos.length) {
  const lb = document.createElement('div');
  lb.className = 'lightbox';
  lb.setAttribute('role', 'dialog');
  lb.setAttribute('aria-modal', 'true');
  lb.setAttribute('aria-label', 'Photo viewer');
  lb.innerHTML = '<button class="lb-close" aria-label="Close">×</button>' +
    '<button class="lb-prev" aria-label="Previous photo">‹</button>' +
    '<div class="lb-stage"></div>' +
    '<button class="lb-next" aria-label="Next photo">›</button>' +
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
  const open = (n) => { lastFocus = document.activeElement; show(n); lb.classList.add('open'); lb.querySelector('.lb-close').focus(); };
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
