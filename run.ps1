# Run all automations (activate venv first if needed)
$ErrorActionPreference = "Stop"
$root = $PSScriptRoot
$robot = Join-Path $root ".venv\Scripts\robot.exe"

if (-not (Test-Path $robot)) {
    Write-Host "Run setup first: python -m venv .venv; pip install -r requirements.txt"
    exit 1
}

& $robot --outputdir (Join-Path $root "results") (Join-Path $root "tests\poc")
