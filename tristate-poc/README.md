# Tristate POC — Transunit

Explores [Transunit](https://transunit.traumasoft.com) after login and documents reachable pages.

## Run login test (Robot)

```powershell
robot login.robot
```

## Discover all menu pages (Python)

Creates one folder per page under `pages/` with `README.md`, `page.json`, and `screenshot.png`.

```powershell
pip install selenium
python discover_pages.py
```

Optional environment variables: `TRANSUNIT_URL`, `TRANSUNIT_USER`, `TRANSUNIT_PASS`.

Output:

- `pages/SITE_MAP.md` — overview of menu sections and folders
- `pages/site-index.json` — machine-readable index
- `pages/<page-name>/` — per-page details and sub-links found on that page

## Inspect menus only

```powershell
python inspect_menu.py
```
