param(
    [string]$Remote = "origin",
    [string]$Branch = "automation-reports"
)

$ErrorActionPreference = "Stop"

$repoRoot = $PSScriptRoot

Push-Location $repoRoot
try {
    & git fetch $Remote $Branch
    if ($LASTEXITCODE -ne 0) {
        throw "Failed to fetch $Remote/$Branch"
    }

    & git restore --source=FETCH_HEAD --worktree -- reports latest_report_path.txt latest_report_summary.md
    if ($LASTEXITCODE -ne 0) {
        throw "Failed to restore reports from $Remote/$Branch"
    }

    $summaryPath = Join-Path $repoRoot "latest_report_summary.md"
    Write-Host "Synced method-transfer reports from $Remote/$Branch"
    if (Test-Path $summaryPath) {
        Write-Host ""
        Get-Content -Raw $summaryPath
    }
}
finally {
    Pop-Location
}
