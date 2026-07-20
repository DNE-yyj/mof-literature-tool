param(
    [string]$TaskName = "MOF Method Transfer Report Sync",
    [string]$Weekday = "MON",
    [string]$Time = "15:30",
    [switch]$Force
)

$ErrorActionPreference = "Stop"

function Convert-Weekday {
    param([Parameter(Mandatory = $true)][string]$Value)

    switch ($Value.ToUpperInvariant()) {
        "MON" { return [System.DayOfWeek]::Monday }
        "TUE" { return [System.DayOfWeek]::Tuesday }
        "WED" { return [System.DayOfWeek]::Wednesday }
        "THU" { return [System.DayOfWeek]::Thursday }
        "FRI" { return [System.DayOfWeek]::Friday }
        "SAT" { return [System.DayOfWeek]::Saturday }
        "SUN" { return [System.DayOfWeek]::Sunday }
        "MONDAY" { return [System.DayOfWeek]::Monday }
        "TUESDAY" { return [System.DayOfWeek]::Tuesday }
        "WEDNESDAY" { return [System.DayOfWeek]::Wednesday }
        "THURSDAY" { return [System.DayOfWeek]::Thursday }
        "FRIDAY" { return [System.DayOfWeek]::Friday }
        "SATURDAY" { return [System.DayOfWeek]::Saturday }
        "SUNDAY" { return [System.DayOfWeek]::Sunday }
        default { throw "Unsupported weekday value: $Value" }
    }
}

$repoRoot = $PSScriptRoot
$syncScript = (Resolve-Path (Join-Path $PSScriptRoot "sync_method_transfer_reports.ps1")).Path
$actionArgs = "-ExecutionPolicy Bypass -File `"$syncScript`""
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument $actionArgs -WorkingDirectory $repoRoot
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek (Convert-Weekday -Value $Weekday) -At $Time
$settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -MultipleInstances IgnoreNew
$userId = "$env:USERDOMAIN\$env:USERNAME"
$principal = New-ScheduledTaskPrincipal -UserId $userId -LogonType Interactive -RunLevel Limited
$description = "Fetch weekly method-transfer reports from the GitHub automation-reports branch."

if ($Force -and (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue)) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
}

Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description $description | Out-Null
Write-Host "Registered scheduled task '$TaskName' for $Weekday at $Time"
