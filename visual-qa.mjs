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
  const context = await browser.newContext({ viewportSize: viewport, deviceScaleFactor: 1 });
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
    await page.waitForTimeout(800);

    const metrics = await page.evaluate(() => ({
      scrollWidth: document.documentElement.scrollWidth,
      clientWidth: document.documentElement.clientWidth,
      h1: document.querySelectorAll('h1').length,
      missingAlt: [...document.images].filter(img => !img.hasAttribute('alt')).length,
      brokenImages: [...document.images].filter(img => img.complete && img.naturalWidth === 0).length,
    }));

    const overflow = metrics.scrollWidth > metrics.clientWidth + 1;
    if (overflow) failures.push(`${mode}/${name}: horizontal overflow ${metrics.scrollWidth} > ${metrics.clientWidth}`);
    if (metrics.h1 !== 1) failures.push(`${mode}/${name}: expected 1 H1, got ${metrics.h1}`);
    if (metrics.missingAlt) failures.push(`${mode}/${name}: ${metrics.missingAlt} image(s) missing alt`);

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
