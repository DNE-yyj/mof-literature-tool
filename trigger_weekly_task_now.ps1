param(
    [string]$TaskName = "MOF Literature Weekly",
    [int]$WaitSeconds = 5
)

$ErrorActionPreference = "Stop"

Start-ScheduledTask -TaskName $TaskName
Start-Sleep -Seconds $WaitSeconds

$task = Get-ScheduledTask -TaskName $TaskName
$info = Get-ScheduledTaskInfo -TaskName $TaskName

[pscustomobject]@{
    TaskName = $TaskName
    State = $task.State
    LastRunTime = $info.LastRunTime
    LastTaskResult = $info.LastTaskResult
    NextRunTime = $info.NextRunTime
} | Format-List
