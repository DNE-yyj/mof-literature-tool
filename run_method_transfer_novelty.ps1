param(
    [string]$PythonExe = "python"
)

$ErrorActionPreference = "Stop"

$repoRoot = $PSScriptRoot
$logRoot = Join-Path $repoRoot "logs"
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$logPath = Join-Path $logRoot "method_transfer_novelty_$timestamp.log"

New-Item -ItemType Directory -Path $logRoot -Force | Out-Null

Push-Location $repoRoot
try {
    & $PythonExe "run_method_transfer_novelty.py" *>> $logPath
    if ($LASTEXITCODE -ne 0) {
        throw "Method transfer novelty workflow failed. See log: $logPath"
    }
    Write-Host "Method transfer novelty workflow finished. Log: $logPath"
}
finally {
    Pop-Location
}
