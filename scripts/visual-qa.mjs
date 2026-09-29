import { chromium } from 'playwright';
import fs from 'node:fs';

const base = 'http://127.0.0.1:8000';
const pages = [
  ['home','/'],
  ['work','/work/'],
  ['about','/about/'],
  ['project','/work/from-arrival-to-belonging/']
];
const viewports = [
  ['mobile',390,844],
  ['tablet',768,1024],
  ['desktop',1440,1000]
];

fs.mkdirSync('visual-qa', { recursive: true });
const browser = await chromium.launch({ headless: true });
const report = [];

for (const [size, width, height] of viewports) {
  const context = await browser.newContext({ viewport: { width, height }, deviceScaleFactor: 1 });
  for (const [name, path] of pages) {
    const page = await context.newPage();
    const errors = [];
    page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
    page.on('pageerror', err => errors.push(String(err)));

    await page.goto(base + path, { waitUntil: 'networkidle', timeout: 60000 });
    await page.screenshot({ path: `visual-qa/${name}-${size}.png`, fullPage: true });

    const metrics = await page.evaluate(() => {
      const root = document.documentElement;
      const body = document.body;
      const overflow = Math.max(root.scrollWidth, body.scrollWidth) - window.innerWidth;
      const offenders = [...document.querySelectorAll('body *')].filter(el => {
        const r = el.getBoundingClientRect();
        return r.right > window.innerWidth + 1 || r.left < -1;
      }).slice(0, 12).map(el => ({
        tag: el.tagName,
        cls: el.className || '',
        left: Math.round(el.getBoundingClientRect().left),
        right: Math.round(el.getBoundingClientRect().right)
      }));
      return {
        title: document.title,
        width: window.innerWidth,
        scrollWidth: Math.max(root.scrollWidth, body.scrollWidth),
        overflow,
        offenders,
        h1: document.querySelector('h1')?.textContent?.trim() || null,
        headerHeight: Math.round(document.querySelector('.site-header')?.getBoundingClientRect().height || 0)
      };
    });

    report.push({ page: name, path, viewport: size, width, height, consoleErrors: errors, ...metrics });
    await page.close();
  }
  await context.close();
}

// Explicitly exercise mobile navigation and hero controls.
{
  const context = await browser.newContext({ viewport: { width: 390, height: 844 } });
  const page = await context.newPage();
  await page.goto(base + '/', { waitUntil: 'networkidle' });
  const menu = page.locator('.menu-toggle');
  await menu.click();
  const navVisible = await page.locator('#nav').evaluate(el => getComputedStyle(el).visibility === 'visible' && getComputedStyle(el).pointerEvents !== 'none');
  await page.screenshot({ path: 'visual-qa/home-mobile-menu.png', fullPage: false });

  const before = await page.locator('[data-hero-index]').textContent();
  await page.keyboard.press('Escape');
  await page.locator('[data-hero-next]').click();
  const after = await page.locator('[data-hero-index]').textContent();
  report.push({ interaction: 'mobile-menu-and-hero', navVisible, heroBefore: before, heroAfter: after });
  await context.close();
}

await browser.close();
fs.writeFileSync('visual-qa/report.json', JSON.stringify(report, null, 2));

const failures = report.filter(r => (r.overflow || 0) > 1 || (r.consoleErrors || []).length > 0 || (r.interaction && (!r.navVisible || r.heroBefore === r.heroAfter)));
if (failures.length) {
  console.error(JSON.stringify(failures, null, 2));
  process.exit(1);
}
console.log('Visual QA passed:', report.length, 'checks');
