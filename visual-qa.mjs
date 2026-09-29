import { chromium } from 'playwright';
import fs from 'node:fs';

const base = 'http://127.0.0.1:4173';
const targets = [
  ['home', '/'],
  ['work', '/work/'],
  ['project', '/work/from-arrival-to-belonging/'],
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

    // Above-the-fold render before any scripted scrolling.
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
  const navVisible = await page.locator('#nav').evaluate(el => {
    const s = getComputedStyle(el);
    return s.visibility === 'visible' && s.pointerEvents !== 'none' && s.opacity !== '0';
  });
  await page.screenshot({ path: 'qa-artifacts/mobile-home-menu.png', fullPage: false });

  const before = await page.locator('[data-hero-index]').textContent();
  await page.keyboard.press('Escape');
  await page.locator('[data-hero-next]').click();
  const after = await page.locator('[data-hero-index]').textContent();

  if (!navVisible) failures.push('mobile/home: menu did not become visible');
  if (before === after) failures.push('mobile/home: hero index did not advance');

  results.push({
    mode: 'mobile',
    name: 'home-interactions',
    navVisible,
    heroBefore: before,
    heroAfter: after,
  });
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
