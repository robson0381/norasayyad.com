# Visual QA matrix — Editorial / Archive in Motion

Status: **code-level responsive pass complete; rendered-browser pass still required before launch**

This checklist records what has been explicitly designed/tested in the source for the three target viewport classes. It does **not** claim pixel-perfect browser validation until the project is deployed or opened in a browser runner.

## Target viewports

| Target | Reference width | Purpose |
|---|---:|---|
| Mobile | 390 px | modern phone baseline |
| Tablet | 768 px | portrait tablet / large mobile |
| Desktop | 1440 px | primary editorial desktop composition |

## Global

| Check | 390 | 768 | 1440 |
|---|:---:|:---:|:---:|
| No hover-only navigation | ✓ | ✓ | ✓ |
| Sticky header | ✓ | ✓ | ✓ |
| Mobile menu replaces desktop nav | ✓ | ✓ | — |
| Menu can scroll vertically | ✓ | ✓ | — |
| Escape closes mobile menu | ✓ | ✓ | — |
| Focus style visible | ✓ | ✓ | ✓ |
| Skip link present | ✓ | ✓ | ✓ |
| Reduced-motion CSS present | ✓ | ✓ | ✓ |
| Footer wraps/stacks safely | ✓ | ✓ | ✓ |

## Home

| Check | 390 | 768 | 1440 |
|---|:---:|:---:|:---:|
| Hero uses safe viewport units | ✓ | ✓ | ✓ |
| Hero copy stays inside image | ✓ source rule | ✓ source rule | ✓ source rule |
| Hero controls separated from CTA | ✓ source rule | ✓ source rule | ✓ |
| Hero is manual, not forced autoplay | ✓ | ✓ | ✓ |
| Hero index is live-updated | ✓ | ✓ | ✓ |
| Selected Projects | 1 col | 2 cols | 4-col asymmetric |
| Credentials | 2 cols | 2 cols | 6 cols |
| Current block | 1 col | 1 col | 3 cols |
| Manifesto quote | bottom overlay | bottom overlay | right overlay |
| About | text first / portrait | stacked | split |
| Commissions | stacked | stacked | split |

### Remaining rendered checks

- exact face/image crop for each of the four Hero photographs;
- line breaks of “NORA SAYYAD” on Safari/iOS and Firefox;
- contrast over every Hero image after real browser rendering;
- font-loading shift between fallback and Newsreader/Manrope.

## Work

| Check | 390 | 768 | 1440 |
|---|:---:|:---:|:---:|
| Project cards usable by touch | ✓ | ✓ | ✓ |
| Layout | 1 col | 2 cols | 12-col editorial composition |
| Current-site order preserved | ✓ | ✓ | ✓ |
| Metadata consistent | ✓ | ✓ | ✓ |

### Remaining rendered checks

- crop of landscape Notes of Resistance cover at desktop;
- visual balance of rows 1 and 2 at ~1200–1500 px.

## Project pages

| Check | 390 | 768 | 1440 |
|---|:---:|:---:|:---:|
| Intro/facts stack when needed | ✓ | ✓ | split |
| Portrait images alternate alignment | full width | responsive | left/right |
| Landscape images can run wider | ✓ | ✓ | ✓ |
| Lightbox keyboard | ✓ | ✓ | ✓ |
| Lightbox swipe | ✓ | ✓ | ✓ |
| Previous/next navigation | 2 cols | 3-part where space allows | 3-part |

### Remaining rendered checks

- long project titles at 390 px;
- lightbox controls on short landscape phone screens;
- actual sequence rhythm after Nora approves captions.

## About

| Check | 390 | 768 | 1440 |
|---|:---:|:---:|:---:|
| Text appears before portrait on phone | ✓ | — | — |
| Portrait constrained on smaller screens | ✓ | ✓ | ✓ |
| CV sections collapsible | ✓ | ✓ | ✓ |
| Full CV remains accessible | ✓ | ✓ | ✓ |

## Current

| Check | 390 | 768 | 1440 |
|---|:---:|:---:|:---:|
| Tour dates do not overflow | ✓ source rule | ✓ source rule | ✓ |
| Completed tour status current as of 29/09/2026 | ✓ | ✓ | ✓ |
| Missing installation images remain explicit placeholders | ✓ | ✓ | ✓ |

## Contact

| Check | 390 | 768 | 1440 |
|---|:---:|:---:|:---:|
| Two-column form collapses | ✓ | ✓ | — |
| Contact metadata remains readable | ✓ | ✓ | ✓ |
| Topic deep-link supported | ✓ | ✓ | ✓ |
| Preview form opens structured email | ✓ | ✓ | ✓ |
| Production backend connected | ✗ | ✗ | ✗ |

## Release gate

Before the redesign can replace the live Squarespace site, perform a real rendered pass at minimum in:

- Chrome desktop, 1440×900;
- Firefox desktop, 1440×900;
- Safari/iOS or equivalent WebKit, ~390×844;
- Android Chrome, ~390×844;
- tablet portrait, ~768×1024.

Take screenshots of Home, Work, one long project, About and Contact and compare them to this matrix.
