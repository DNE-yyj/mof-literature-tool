param(
    [string]$ConfigPath = "configs/weekly_mof_latest.json",
    [string]$PythonExe = "python"
)

$ErrorActionPreference = "Stop"

$repoRoot = $PSScriptRoot
$resolvedConfig = if ([System.IO.Path]::IsPathRooted($ConfigPath)) {
    (Resolve-Path $ConfigPath).Path
} else {
    (Resolve-Path (Join-Path $repoRoot $ConfigPath)).Path
}
$logRoot = Join-Path $repoRoot "logs"
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$logPath = Join-Path $logRoot "weekly_run_$timestamp.log"

New-Item -ItemType Directory -Path $logRoot -Force | Out-Null

Push-Location $repoRoot
try {
    & $PythonExe "run.py" --config $resolvedConfig *>> $logPath
    if ($LASTEXITCODE -ne 0) {
        throw "Weekly literature run failed. See log: $logPath"
    }
    Write-Host "Weekly literature run finished. Log: $logPath"
}
finally {
    Pop-Location
}
