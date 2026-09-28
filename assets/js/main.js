// Mobile menu
const toggle = document.querySelector('.menu-toggle');
const nav = document.getElementById('nav');
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
    document.body.style.overflow = open ? 'hidden' : '';
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
