# ISI Web Application Tests

This folder contains the Robot Framework smoke tests for the ISI Central web application.

## Requirements

- Complete the repository setup in the root [README](../README.md).
- Install Google Chrome.
- Have network access to the configured ISI environment.

## Run

From the repository root in PowerShell:

```powershell
.\ISI\run-isi.ps1
```

The default target is `https://www.isicentral.net/login.jsp`. To test another ISI environment:

```powershell
$env:ISI_BASE_URL = "https://your-isi-environment.example/login.jsp"
.\ISI\run-isi.ps1
```

The anonymous smoke test checks the page title and email/password form fields. It does not submit credentials. Robot Framework output is written to `results\isi`.
