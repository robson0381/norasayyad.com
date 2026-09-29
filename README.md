# norasayyad.com — redesign prototype

Static, dependency-free prototype of a redesigned portfolio for photographer Nora Sayyad. The main prototype now uses the approved **Editorial / Archive in Motion** identity across the shared site. **Before contributing, read [CONTRIBUTING.md](CONTRIBUTING.md)** (in Portuguese). See **[RELATORIO.md](RELATORIO.md)** for the full evaluation and prioritized plan (in Portuguese).

- **[opcoes/](opcoes/)** — six visual **concepts** (the main Editorial / Archive in Motion direction, the secondary Archive / Memory alternative, Símbolos, Rota, Visível and Dois lares); earlier rounds are kept in `opcoes/v1/` (styles) and `opcoes/v2/` (restyled). `build_editorial.py` supplies the Editorial concept and `build_memory.py` supplies the Archive / Memory alternative and `python3 build_options.py` regenerates the current options.
- **[PERFIL.md](PERFIL.md)** — public profile research (in Portuguese).
- **[REFERENCE_BUNDLE.md](REFERENCE_BUNDLE.md)** — inventário resumido das 346 imagens de referência fornecidas; não envia cópias do Instagram ao repositório.
- **[SPEC.md](SPEC.md)** — especificação da direção principal, componentes, responsividade, acessibilidade, imagens e arquitetura de produção.
- **[CONTENT_STATUS.md](CONTENT_STATUS.md)** — o que ainda depende de originais/aprovação da Nora antes de produção.
- **[MIGRATION_MAP.md](MIGRATION_MAP.md)** — mapa do site Squarespace atual para as novas rotas, com o que preservar, melhorar e remover.
- **[content/current-site-inventory.json](content/current-site-inventory.json)** — inventário de migração; inclui as 86 URLs atuais de `Notes of Resistance`.
- **[content/sample-assets.json](content/sample-assets.json)** — proveniência e status dos assets provisórios usados apenas para apresentação.
- **[review/notes-of-resistance/](review/notes-of-resistance/)** — galeria interna/noindex com o arquivo atual completo para seleção visual.
- **[presentation/](presentation/)** — página privada/noindex para apresentar a proposta à Nora sem expor notas técnicas.

Pages: Home · Work · 4 project stories · About/CV · Commissions · News · Contact.

```sh
python3 build.py              # regenerate main site from the shared template
python3 build_review.py       # regenerate internal migration review gallery
python3 qa.py                 # static accessibility/link/content sanity checks
python3 -m http.server 8000   # preview at http://localhost:8000
```

- Grey blocks (`.ph`) are image placeholders — replace with `<img srcset alt loading="lazy">`.
- Yellow highlighted text (`.todo`) is content to be written or confirmed.
- Forms (`action="#"`) need a backend (Squarespace forms, Formspree, etc.).
