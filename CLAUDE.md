# CLAUDE.md

Prototype of the new website for Nora Sayyad, a Finnish-Palestinian photographer and visual artist in Helsinki. The live site is still on Squarespace; this repo is for trying structure, copy and visual direction. The user (Robson) writes in Portuguese: reply in Portuguese; site copy is in English.

Read `CONTRIBUTING.md` first. The rules below are the ones most often broken.

## Build

- No dependencies. `python3 build.py && python3 build_options.py && python3 build_options_v2.py`, then `python3 -m http.server 8000`.
- HTML under `index.html`, `work/`, `about/`, `services/`, `news/`, `contact/` and `opcoes/*/` is **generated**. Edit the generator, re-run it, commit both.
- `opcoes/v1/` is frozen output with no generator.
- Photos and alt text live in `content/photos.json`; images are served from Nora's Squarespace CDN with `?format=` resizing through `img()` in `build.py`.

## Content rules

- Never invent facts about Nora. Sources: `PERFIL.md`, `RELATORIO.md`, her CV on norasayyad.com/about, her public Instagram captions. Unconfirmed copy goes in `<span class=todo>`.
- Never commit images downloaded from Instagram; use a placeholder (`ph()` / `.ph`) until Nora supplies the original.
- People in her photos are real (portraits, children, Mariam and her father). Don't add new images of identifiable people, or quotes from them, without saying so in the PR so Nora can confirm consent.
- Alt text describes the scene, never the filename.
- Arabic, Finnish and Swedish copy must be flagged for review by a native speaker.

## Workflow

- Work on a `claude/...` branch, open a draft PR to `main`, never merge.
- Check pages at 1440 px and 390 px wide; no horizontal scroll.
- Commit messages: imperative, one topic per commit.
