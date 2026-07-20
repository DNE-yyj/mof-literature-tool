param(
    [string]$PythonExe = "python"
)

$ErrorActionPreference = "Stop"

$repoRoot = $PSScriptRoot
$logRoot = Join-Path $repoRoot "logs"
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$logPath = Join-Path $logRoot "method_transfer_novelty_$timestamp.log"

New-Item -ItemType Directory -Path $logRoot -Force | Out-Null

function Write-RunLog {
    param([Parameter(Mandatory = $true)][string]$Message)

    $line = "[{0}] {1}" -f (Get-Date -Format "yyyy-MM-ddTHH:mm:ssK"), $Message
    $line | Tee-Object -FilePath $logPath -Append | Out-Host
}

function Resolve-PythonExecutable {
    param([Parameter(Mandatory = $true)][string]$Value)

    if (Test-Path -LiteralPath $Value -PathType Leaf) {
        return (Resolve-Path -LiteralPath $Value).Path
    }

    $command = Get-Command $Value -ErrorAction Stop
    if (-not $command.Source) {
        throw "Could not resolve Python executable from '$Value'."
    }

    return $command.Source
}

Push-Location $repoRoot
try {
    Write-RunLog "Starting method-transfer novelty workflow."
    Write-RunLog "Repository root: $repoRoot"
    Write-RunLog "Requested Python executable: $PythonExe"

    $resolvedPython = Resolve-PythonExecutable -Value $PythonExe
    Write-RunLog "Resolved Python executable: $resolvedPython"

    $pythonVersion = & $resolvedPython --version 2>&1
    Write-RunLog "Python version: $pythonVersion"

    & $resolvedPython -B "run_method_transfer_novelty.py" *>> $logPath
    $pythonExitCode = $LASTEXITCODE
    Write-RunLog "Python exit code: $pythonExitCode"

    if ($pythonExitCode -ne 0) {
        throw "Method transfer novelty workflow failed. See log: $logPath"
    }
    Write-RunLog "Method transfer novelty workflow finished successfully."
    Write-Host "Method transfer novelty workflow finished. Log: $logPath"
}
catch {
    Write-RunLog "ERROR: $($_.Exception.Message)"
    throw
}
finally {
    Pop-Location
}
