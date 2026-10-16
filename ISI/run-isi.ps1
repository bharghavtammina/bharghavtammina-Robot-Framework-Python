$ErrorActionPreference = "Stop"
$projectRoot = Split-Path -Parent $PSScriptRoot
$robot = Join-Path $projectRoot ".venv\Scripts\robot.exe"

if (-not (Test-Path $robot)) {
    Write-Host "Run setup first: python -m venv .venv; pip install -r requirements.txt"
    exit 1
}

$debuggerAddress = $env:ISI_CHROME_DEBUGGER_ADDRESS
if ([string]::IsNullOrWhiteSpace($debuggerAddress)) {
    $debuggerAddress = "127.0.0.1:9222"
}

$debuggerMatch = [regex]::Match($debuggerAddress, '^127\.0\.0\.1:(?<port>\d{1,5})$')
if (-not $debuggerMatch.Success -or [int]$debuggerMatch.Groups["port"].Value -gt 65535 -or [int]$debuggerMatch.Groups["port"].Value -eq 0) {
    Write-Error "ISI_CHROME_DEBUGGER_ADDRESS must use localhost, for example 127.0.0.1:9222."
    exit 1
}

$debuggerUri = "http://$debuggerAddress/json/version"
$chromeReady = $false
try {
    Invoke-RestMethod -Uri $debuggerUri -TimeoutSec 2 -ErrorAction Stop | Out-Null
    $chromeReady = $true
}
catch {
    $chromeReady = $false
}

if (-not $chromeReady) {
    $chromeCandidates = @(
        (Join-Path $env:ProgramFiles "Google\Chrome\Application\chrome.exe"),
        (Join-Path ${env:ProgramFiles(x86)} "Google\Chrome\Application\chrome.exe"),
        (Join-Path $env:LOCALAPPDATA "Google\Chrome\Application\chrome.exe")
    )
    $chromePath = $chromeCandidates | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1
    if (-not $chromePath) {
        Write-Error "Google Chrome was not found. Install Chrome, then rerun this script."
        exit 1
    }

    $profilePath = Join-Path $env:LOCALAPPDATA "ISI-Robot-Chrome"
    $loginUrl = $env:ISI_BASE_URL
    if ([string]::IsNullOrWhiteSpace($loginUrl)) {
        $loginUrl = "https://www.isicentral.net/login.jsp"
    }

    Write-Host "Starting a dedicated Chrome profile for ISI at $debuggerAddress."
    Write-Host "If prompted, sign in to ISI in that Chrome window; configured Outlook email verification is handled by the Robot test."
    try {
        Start-Process -FilePath $chromePath -ArgumentList @(
            "--remote-debugging-port=$($debuggerMatch.Groups['port'].Value)",
            "--user-data-dir=`"$profilePath`"",
            $loginUrl
        ) | Out-Null
    }
    catch {
        Write-Error "Could not start Chrome at '$chromePath': $($_.Exception.Message)"
        exit 1
    }

    for ($attempt = 0; $attempt -lt 30 -and -not $chromeReady; $attempt++) {
        Start-Sleep -Seconds 1
        try {
            Invoke-RestMethod -Uri $debuggerUri -TimeoutSec 2 -ErrorAction Stop | Out-Null
            $chromeReady = $true
        }
        catch {
            $chromeReady = $false
        }
    }
}

if (-not $chromeReady) {
    Write-Error "Chrome did not start its debugging endpoint at $debuggerAddress. Close any other ISI Robot Chrome window and try again."
    exit 1
}

if ([string]::IsNullOrWhiteSpace($env:ISI_AUTH_TIMEOUT)) {
    $env:ISI_AUTH_TIMEOUT = "180s"
}

& $robot --outputdir (Join-Path $projectRoot "results\isi") (Join-Path $PSScriptRoot "tests")
exit $LASTEXITCODE
