# Robot Framework Documentation

Two layers: **curated cheat sheets** for learning, and **full reference** for lookup.

## Curated (hand-written)

Organized by Robot file section — maps to `docs/SECTION_MAPPING.md`.

| Folder | Contents |
|--------|----------|
| `curated/settings/` | `*** Settings ***` — Library, Resource, Suite Setup, etc. |
| `curated/variables/` | `*** Variables ***` declarations and Set Variable keywords |
| `curated/test-steps/` | `*** Test Cases ***` / `*** Tasks ***` steps (API, assertions, Selenium) |
| `curated/user-keywords/` | `*** Keywords ***` — custom reusable keywords |
| `curated/javascript/` | Snippets for `Execute Javascript` |

Quick index files: `*_commands.md` in each curated folder.

## Reference (generated from libdoc)

| Path | Purpose |
|------|---------|
| `reference/libdoc/*.xml` | Source exports from installed libraries |
| `reference/libdoc/*.html` | Same content, HTML view |
| `reference/markdown/` | Markdown per library (BuiltIn, SeleniumLibrary, …) |

Regenerate markdown after updating libdoc XML:

```powershell
python scripts/generate_full_reference_md.py
```

## Robot tests

Executable suites are **not** in `docs/` — see `tests/poc/` and `tests/examples/api/`.
