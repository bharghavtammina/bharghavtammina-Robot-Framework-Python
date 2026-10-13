$ErrorActionPreference = "Stop"
$projectRoot = Split-Path -Parent $PSScriptRoot
$robot = Join-Path $projectRoot ".venv\Scripts\robot.exe"

if (-not (Test-Path $robot)) {
    Write-Host "Run setup first: python -m venv .venv; pip install -r requirements.txt"
    exit 1
}

& $robot --outputdir (Join-Path $projectRoot "results\isi") (Join-Path $PSScriptRoot "tests")
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
