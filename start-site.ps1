# Serve the local POC site on http://127.0.0.1:8080
$ErrorActionPreference = "Stop"
$siteDir = Join-Path $PSScriptRoot "site"

Write-Host "POC site: http://127.0.0.1:8080" -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop.`n"

Set-Location $siteDir
python -m http.server 8080
