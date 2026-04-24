$ErrorActionPreference = "Stop"

powershell -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot "run_weekly.ps1") -ConfigPath (Join-Path $PSScriptRoot "configs/weekly_mof_latest.json")
