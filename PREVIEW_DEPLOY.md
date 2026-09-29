# Preview deployment

The prototype is prepared for a temporary GitHub Pages preview. This is separate from the final hosting decision and does not change `norasayyad.com`.

## What is already configured

- `build_pages_preview.py` builds an isolated `_site/` copy.
- Root-relative links are rewritten for the GitHub project Pages base path `/norasayyad.com/`.
- `.nojekyll` is added to the preview artifact.
- Source files remain unchanged.
- The preview remains `noindex,nofollow`.
- `.github/workflows/preview-pages.yml` regenerates the prototype, runs structural QA, prepares the artifact and deploys it.

## One-time repository setting

GitHub Pages must be enabled once for this repository:

1. Open **Repository → Settings → Pages**.
2. Under **Build and deployment**, set **Source** to **GitHub Actions**.
3. Return to **Actions → Preview Site** and choose **Run workflow**, or re-run the failed workflow.

Expected preview base URL after a successful deployment:

`https://robson0381.github.io/norasayyad.com/`

Useful review routes:

- `/` — Editorial / Archive in Motion
- `/work/`
- `/work/from-arrival-to-belonging/`
- `/about/`
- `/contact/`
- `/presentation/` — presentation prepared for Nora
- `/opcoes/memoria/` — secondary Archive / Memory direction

## Why Pages is only a preview

The production target remains independent. The current recommended production architecture is Astro + TypeScript + CMS + a production host such as Vercel. GitHub Pages is used here only to obtain a stable, shareable review URL without touching Nora's existing Squarespace site.

## Current deployment check

The first workflow attempt successfully:

- checked out the branch;
- regenerated all pages;
- passed the structural audit;
- built the GitHub Pages artifact.

It stopped at **Configure Pages** because Pages is not yet enabled in the repository settings.
