# ISI Web Application Tests

This folder contains the Robot Framework smoke tests for the ISI Central web application.

## Requirements

- Complete the repository setup in the root [README](../README.md).
- Install Google Chrome.
- Have network access to the configured ISI environment.

## Run

Run the test from the repository root in PowerShell:

```powershell
.\ISI\run-isi.ps1
```

The script automatically starts a dedicated Chrome profile if needed. If the profile is already authenticated, the test continues without asking for credentials. If ISI displays its login form, the test reads credentials from `ISI/local_credentials.ini` and submits them automatically. This file is excluded from Git; fill in its `username` and `password` values locally and never commit or share it. The test does not prompt for credentials if the file is missing or blank.

If ISI asks which verification method to use, the test selects the Email option and requests a code, then checks Outlook for the new ISI code and enters it automatically. Outlook access uses Microsoft OAuth device authorization and IMAP XOAUTH2; no Outlook password or client secret is stored. Before first use:

1. Copy `ISI/local_outlook.ini.example` to `ISI/local_outlook.ini`, then fill in the `client_id`, `tenant_id`, and `mailbox` values. Optionally set `otp_sender_contains` and `otp_subject_contains` to narrow which ISI messages are accepted. The local file is excluded from Git; keep it local and do not share it.
2. Start `.\ISI\run-isi.ps1`. On the first verification, follow the Microsoft device sign-in instructions printed in the PowerShell window and grant the approved Outlook IMAP permission. This one-time authorization can itself require MFA.
3. Later runs reuse the token cache protected by Windows. If no fresh matching verification email arrives, the test fails with a timeout rather than entering an old or ambiguous code.

The test waits up to three minutes for the post-login ISI page and, when needed, up to three minutes for the verification email. Only fresh messages with a single six-digit code and verification-related text are accepted.

After login, the test opens **Reporting → Repository**, switches into the report-tree frame, expands **My Reports**, and opens **Invoice_Lastweek**. It then uses the report toolbar's **Export** option, selects **CSV**, and exports the report. Chrome saves the completed `.csv` file in your Windows `Downloads` folder. Chrome stays open after the download. The dedicated profile is reused on later runs, though ISI may request MFA again if its session expires.

The default target is `https://www.isicentral.net/login.jsp`. To test another ISI environment or use a different localhost debugging port:

```powershell
$env:ISI_BASE_URL = "https://your-isi-environment.example/login.jsp"
$env:ISI_CHROME_DEBUGGER_ADDRESS = "127.0.0.1:9223"
.\ISI\run-isi.ps1
```

Remote debugging is bound to localhost and should not be exposed to a network. To change the authentication wait, set `ISI_AUTH_TIMEOUT` (for example, `300s`). Robot Framework output is written to `results\isi`.
