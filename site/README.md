# POC Demo Site

A small **local** website for practicing Robot Framework automations.

## Pages

| Page | URL | What to automate |
|------|-----|------------------|
| Home | `/index.html` | Links, headings, navigation |
| Login | `/login.html` | Type username/password, click Log in |
| Dashboard | `/dashboard.html` | Shown after successful login |
| Contact | `/contact.html` | Name, email, message form |

## Demo login

- **Username:** `demo`
- **Password:** `secret123`

## Start the server

From the project root:

```powershell
.\start-site.ps1
```

Or manually:

```powershell
cd site
python -m http.server 8080
```

Open in browser: **http://127.0.0.1:8080**

Keep this terminal open while running Robot automations.
