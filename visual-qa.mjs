import { chromium } from 'playwright';
import fs from 'node:fs';

const base = 'http://127.0.0.1:4173';
const targets = [
  ['home', '/'],
  ['work', '/work/'],
  ['current', '/news/'],
  ['commissions', '/services/'],
  ['project', '/work/from-arrival-to-belonging/'],
  ['parallel', '/work/from-a-parallel-life/'],
  ['about', '/about/'],
  ['contact', '/contact/'],
  ['presentation', '/presentation/'],
  ['memory', '/opcoes/memoria/'],
];
const viewports = [
  ['desktop', { width: 1440, height: 1000 }],
  ['tablet', { width: 768, height: 1024 }],
  ['mobile', { width: 390, height: 844 }],
];

fs.mkdirSync('qa-artifacts', { recursive: true });
const browser = await chromium.launch();
const failures = [];
const results = [];

for (const [mode, viewport] of viewports) {
  const context = await browser.newContext({ viewport, deviceScaleFactor: 1 });
  for (const [name, path] of targets) {
    const page = await context.newPage();
    const badResponses = [];
    const consoleErrors = [];

    page.on('response', res => {
      if (res.status() >= 400 && res.request().resourceType() !== 'font') {
        badResponses.push({ status: res.status(), url: res.url() });
      }
    });
    page.on('console', msg => {
      if (msg.type() === 'error') consoleErrors.push(msg.text());
    });
    page.on('pageerror', err => consoleErrors.push(String(err)));

    await page.goto(base + path, { waitUntil: 'domcontentloaded', timeout: 30000 });
    await page.evaluate(() => document.fonts?.ready);
    await page.waitForTimeout(500);

    // Wait for visible images before the above-the-fold render.
    const visibleImages = page.locator('img:visible');
    for (let i = 0; i < await visibleImages.count(); i++) {
      const image = visibleImages.nth(i);
      await image.evaluate(async img => {
        if (!img.complete) {
          await Promise.race([
            new Promise(resolve => {
              img.addEventListener('load', resolve, { once: true });
              img.addEventListener('error', resolve, { once: true });
            }),
            new Promise(resolve => setTimeout(resolve, 3000)),
          ]);
        }
        if (img.complete && img.naturalWidth > 0 && img.decode) {
          try { await img.decode(); } catch {}
        }
      });
    }
    await page.screenshot({ path: `qa-artifacts/${mode}-${name}-fold.png`, fullPage: false });

    // Exercise every image position, then wait for decoded pixels before the full-page screenshot.
    const images = page.locator('img');
    for (let i = 0; i < await images.count(); i++) {
      const image = images.nth(i);
      await image.scrollIntoViewIfNeeded();
      await image.evaluate(async img => {
        if (!img.complete) {
          await Promise.race([
            new Promise(resolve => {
              img.addEventListener('load', resolve, { once: true });
              img.addEventListener('error', resolve, { once: true });
            }),
            new Promise(resolve => setTimeout(resolve, 2500)),
          ]);
        }
        if (img.complete && img.naturalWidth > 0 && img.decode) {
          try { await img.decode(); } catch {}
        }
      });
    }
    await page.evaluate(() => window.scrollTo(0, 0));
    await page.waitForTimeout(300);

    const metrics = await page.evaluate(() => {
      const root = document.documentElement;
      const body = document.body;
      const h1 = document.querySelector('h1');
      const header = document.querySelector('.site-header');
      const hero = document.querySelector('.hero-stage');
      const rect = el => el ? el.getBoundingClientRect() : null;
      const offenders = [...document.querySelectorAll('body *')].filter(el => {
        const r = el.getBoundingClientRect();
        return r.right > window.innerWidth + 1 || r.left < -1;
      }).slice(0, 10).map(el => ({
        tag: el.tagName,
        className: typeof el.className === 'string' ? el.className : '',
        left: Math.round(el.getBoundingClientRect().left),
        right: Math.round(el.getBoundingClientRect().right),
      }));

      return {
        scrollWidth: Math.max(root.scrollWidth, body.scrollWidth),
        clientWidth: root.clientWidth,
        h1Count: document.querySelectorAll('h1').length,
        h1Rect: rect(h1),
        headerRect: rect(header),
        heroRect: rect(hero),
        missingAlt: [...document.images].filter(img => !img.hasAttribute('alt')).length,
        brokenImages: [...document.images].filter(img => img.naturalWidth === 0).length,
        offenders,
      };
    });

    const overflow = metrics.scrollWidth > metrics.clientWidth + 1;
    if (overflow) failures.push(`${mode}/${name}: horizontal overflow ${metrics.scrollWidth} > ${metrics.clientWidth}`);
    if (metrics.h1Count !== 1) failures.push(`${mode}/${name}: expected 1 H1, got ${metrics.h1Count}`);
    if (metrics.missingAlt) failures.push(`${mode}/${name}: ${metrics.missingAlt} image(s) missing alt`);
    if (metrics.brokenImages) failures.push(`${mode}/${name}: ${metrics.brokenImages} image(s) failed to load`);
    if (consoleErrors.length) failures.push(`${mode}/${name}: console errors: ${consoleErrors.slice(0,2).join(' | ')}`);

    results.push({
      mode, name, path, viewport,
      ...metrics,
      overflow,
      badResponses: badResponses.slice(0, 10),
      consoleErrors: consoleErrors.slice(0, 10),
    });

    await page.screenshot({ path: `qa-artifacts/${mode}-${name}.png`, fullPage: true });
    await page.close();
  }
  await context.close();
}

// Explicit interaction checks on mobile Home.
{
  const context = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1 });
  const page = await context.newPage();
  await page.goto(base + '/', { waitUntil: 'domcontentloaded' });
  await page.evaluate(() => document.fonts?.ready);
  await page.waitForTimeout(300);

  const menu = page.locator('.menu-toggle');
  await menu.click();
  await page.waitForTimeout(250);
  const navVisible = await page.locator('#nav').evaluate(el => {
    const s = getComputedStyle(el);
    return s.visibility === 'visible' && s.pointerEvents !== 'none' && s.opacity !== '0';
  });
  await page.screenshot({ path: 'qa-artifacts/mobile-home-menu.png', fullPage: false });

  // Mobile shows the same hero copy as desktop (name, text, View Portfolio) in normal flow.
  const mobileHeroVisible = await page.locator('.hero-copy h1').evaluate(el => {
    const r = el.getBoundingClientRect();
    return r.width > 100 && getComputedStyle(el).visibility !== 'hidden';
  });
  const menuSequence = await page.locator('#nav a').evaluateAll(links =>
    // getClientRects() is empty for links inside the collapsed Work submenu.
    links.filter(a => a.getClientRects().length > 0 && getComputedStyle(a).visibility !== 'hidden')
      .map(a => a.textContent.trim())
  );
  const expectedMenu = ['Home', 'Work', 'Current', 'Commissions', 'About', 'Get in touch'];
  if (!mobileHeroVisible) failures.push('mobile/home: hero title is not visible');
  if (JSON.stringify(menuSequence) !== JSON.stringify(expectedMenu)) {
    failures.push(`mobile/home: menu sequence ${JSON.stringify(menuSequence)} != ${JSON.stringify(expectedMenu)}`);
  }

  const before = await page.locator('[data-hero-index]').textContent();
  await page.keyboard.press('Escape');
  // Mobile hides the arrow controls (swipe + autoplay remain); trigger the same handler directly.
  await page.locator('[data-hero-next]').evaluate(el => el.click());
  const after = await page.locator('[data-hero-index]').textContent();

  if (!navVisible) failures.push('mobile/home: menu did not become visible');
  if (before === after) failures.push('mobile/home: hero index did not advance');

  results.push({
    mode: 'mobile',
    name: 'home-interactions',
    navVisible,
    mobileHeroVisible,
    menuSequence,
    heroBefore: before,
    heroAfter: after,
  });
  await context.close();
}

// The supplied Parallel Life album should no longer use the tiny prototype thumbnails.
{
  const context = await browser.newContext({ viewport: { width: 1440, height: 1000 }, deviceScaleFactor: 1 });
  const page = await context.newPage();
  await page.goto(base + '/work/from-a-parallel-life/', { waitUntil: 'domcontentloaded' });
  await page.evaluate(() => document.fonts?.ready);
  await page.waitForTimeout(500);
  const overScaled = await page.locator('.story img').evaluateAll(imgs =>
    imgs.map(img => {
      const r = img.getBoundingClientRect();
      return { src: img.getAttribute('src'), naturalW: img.naturalWidth, renderedW: Math.round(r.width), ratio: img.naturalWidth ? r.width / img.naturalWidth : 999 };
    }).filter(img => img.ratio > 1.2)
  );
  if (overScaled.length) failures.push(`parallel-overscaled: ${JSON.stringify(overScaled)}`);
  results.push({ mode: 'desktop', name: 'parallel-resolution', overScaled });
  await context.close();
}

await browser.close();
fs.writeFileSync('qa-artifacts/report.json', JSON.stringify(results, null, 2));
if (failures.length) {
  fs.writeFileSync('qa-artifacts/failures.txt', failures.join('\n') + '\n');
  console.error(failures.join('\n'));
  process.exit(1);
}
console.log('Visual QA passed:', results.length, 'checks');
