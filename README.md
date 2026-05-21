# Robot Framework Automation POC

A minimal starter for **task automation** with a **local demo website** you control.

## What it does

| Script | Automation |
|--------|------------|
| `01_browse_local_site.robot` | Home page → click Login in nav |
| `02_fetch_api_data.robot` | Public API call (no browser, no local site) |
| `03_local_site_login.robot` | Login with `demo` / `secret123` → dashboard |
| `04_local_site_contact.robot` | Fill contact form → success message |

## Project layout

```
├── site/                 # Local HTML demo site (your automation target)
│   ├── index.html
│   ├── login.html
│   ├── dashboard.html
│   ├── contact.html
│   ├── css/
│   └── js/
├── automations/          # Robot scripts
├── resources/            # Reusable keywords
├── libraries/            # Python helpers
├── start-site.ps1        # Start local web server
└── run.ps1               # Run all automations
```

## Setup (Windows)

```powershell
cd "c:\Users\Lokesh\Desktop\Robotic Framework Python"
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

**Terminal 2 — run automations:**

```powershell
.\.venv\Scripts\Activate.ps1
.\run.ps1
```

Or one automation:

```powershell
robot --outputdir results automations/03_local_site_login.robot
```

Open `results/report.html` for the summary.

## Local site credentials

| Field | Value |
|-------|--------|
| Username | `demo` |
| Password | `secret123` |

## Next steps

- Edit pages in `site/` and add new `id` attributes for clicks/typing
- Copy an automation file in `automations/` for new flows
- Change `${SITE_HOST}` in `resources/site.resource` if you use another port
