# Robot Framework Automation POC

A minimal starter for **task automation** with a **local demo website** you control, plus API examples and keyword reference docs.

## What it does

| Script | Automation |
|--------|------------|
| `tests/poc/01_browse_local_site.robot` | Home page → click Login in nav |
| `tests/poc/02_fetch_api_data.robot` | Public API call (no browser, no local site) |
| `tests/poc/03_local_site_login.robot` | Login with `demo` / `secret123` → dashboard |
| `tests/poc/04_local_site_contact.robot` | Fill contact form → success message |

API examples live under `tests/examples/api/` (restful-booker.herokuapp.com).

## ISI web application

The ISI Robot Framework project is grouped in [`ISI/`](ISI/). See its [README](ISI/README.md) for requirements, run instructions, and environment configuration.

## Project layout

```
├── site/                      # Local HTML demo site (automation target)
├── tests/
│   ├── poc/                   # Main POC suites (run via run.ps1)
│   └── examples/api/          # GET/POST/PUT/PATCH/DELETE API demos
├── resources/                 # Reusable .resource files
│   ├── browser.resource
│   ├── site.resource
│   ├── common.resource        # browser + site bundle
│   └── api_booker.resource    # Shared restful-booker keywords
├── libraries/                 # Python helper keywords
├── docs/
│   ├── curated/               # Hand-written cheat sheets by Robot section
│   └── reference/             # Full libdoc exports (XML/HTML + markdown)
├── scripts/                   # Doc generators
├── results/                   # Robot output (gitignored)
├── start-site.ps1
├── ISI/                       # ISI web application test project
└── run.ps1
```

See `docs/README.md` for the keyword documentation index.

## Setup (Windows)

```powershell
cd "c:\Users\Lokesh\Documents\GitHub\Robot-Framework-Python"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

You need **Google Chrome** installed.

## Run (two terminals)

**Terminal 1 — start the local site:**

```powershell
.\start-site.ps1
```

Open **http://127.0.0.1:8080** in your browser to preview.

**Terminal 2 — run POC automations:**

```powershell
.\.venv\Scripts\Activate.ps1
.\run.ps1
```

Or one suite:

```powershell
robot --outputdir results tests/poc/03_local_site_login.robot
```

API examples:

```powershell
robot --outputdir results tests/examples/api/api_get.robot
```

Open `results/report.html` for the summary.

## Local site credentials

| Field | Value |
|-------|--------|
| Username | `demo` |
| Password | `secret123` |

## Next steps

- Edit pages in `site/` and add new `id` attributes for clicks/typing
- Copy a file in `tests/poc/` for new UI flows
- Change `${SITE_HOST}` in `resources/site.resource` if you use another port
- Browse `docs/curated/` for keyword syntax by Robot file section
