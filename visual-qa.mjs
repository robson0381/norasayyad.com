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
    page.on('response', res => {
      if (res.status() >= 400 && res.request().resourceType() !== 'font') {
        badResponses.push({ status: res.status(), url: res.url() });
      }
    });
    await page.goto(base + path, { waitUntil: 'domcontentloaded', timeout: 30000 });
    await page.evaluate(() => document.fonts?.ready);
    await page.waitForTimeout(500);

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

    const metrics = await page.evaluate(() => ({
      scrollWidth: document.documentElement.scrollWidth,
      clientWidth: document.documentElement.clientWidth,
      h1: document.querySelectorAll('h1').length,
      missingAlt: [...document.images].filter(img => !img.hasAttribute('alt')).length,
      brokenImages: [...document.images].filter(img => img.naturalWidth === 0).length,
    }));

    const overflow = metrics.scrollWidth > metrics.clientWidth + 1;
    if (overflow) failures.push(`${mode}/${name}: horizontal overflow ${metrics.scrollWidth} > ${metrics.clientWidth}`);
    if (metrics.h1 !== 1) failures.push(`${mode}/${name}: expected 1 H1, got ${metrics.h1}`);
    if (metrics.missingAlt) failures.push(`${mode}/${name}: ${metrics.missingAlt} image(s) missing alt`);
    if (metrics.brokenImages) failures.push(`${mode}/${name}: ${metrics.brokenImages} image(s) failed to load`);

    results.push({ mode, name, path, ...metrics, overflow, badResponses: badResponses.slice(0, 10) });
    await page.screenshot({ path: `qa-artifacts/${mode}-${name}.png`, fullPage: true });
    await page.close();
  }
  await context.close();
}

await browser.close();
fs.writeFileSync('qa-artifacts/report.json', JSON.stringify(results, null, 2));
if (failures.length) {
  console.error(failures.join('\n'));
  process.exit(1);
}
console.log('Visual QA passed:', results.length, 'page/viewport combinations');
