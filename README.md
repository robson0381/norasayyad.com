# norasayyad.com — redesign prototype

Static, dependency-free prototype of a redesigned portfolio for photographer Nora Sayyad. **Before contributing, read [CONTRIBUTING.md](CONTRIBUTING.md)** (in Portuguese). See **[RELATORIO.md](RELATORIO.md)** for the full evaluation and prioritized plan (in Portuguese).

- **[opcoes/](opcoes/)** — five home-page **concepts** (Editorial / Archive in Motion, Símbolos, Rota, Visível, Dois lares); earlier rounds are kept in `opcoes/v1/` (styles) and `opcoes/v2/` (restyled). `build_editorial.py` supplies the Editorial concept and `python3 build_options.py` regenerates the current options.
- **[PERFIL.md](PERFIL.md)** — public profile research (in Portuguese).

Pages: Home · Work · 4 project stories · About/CV · Commissions · News · Contact.

```sh
python3 build.py              # regenerate HTML from the shared template
python3 -m http.server 8000   # preview at http://localhost:8000
```

- Grey blocks (`.ph`) are image placeholders — replace with `<img srcset alt loading="lazy">`.
- Yellow highlighted text (`.todo`) is content to be written or confirmed.
- Forms (`action="#"`) need a backend (Squarespace forms, Formspree, etc.).
