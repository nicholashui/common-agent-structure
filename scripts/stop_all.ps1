# Stop the local CASOPS operator stack started by scripts/start_all.ps1
# (control plane :8080 and Control UI :5173). Also clears leftover listeners
# on those ports.

Set-StrictMode -Version Latest
$ErrorActionPreference = "Continue"

$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$StateFile = Join-Path $Root "var\casops-servers.json"
$ControlPort = 8080
$UiPort = 5173

function Stop-PidSafe([int]$ProcessId, [string]$Label) {
    if ($ProcessId -le 0) {
        return
    }
    try {
        $proc = Get-Process -Id $ProcessId -ErrorAction Stop
        Stop-Process -Id $ProcessId -Force -ErrorAction Stop
        Write-Host "Stopped $Label pid=$ProcessId ($($proc.ProcessName))"
    }
    catch {
        Write-Host "$Label pid=$ProcessId already gone"
    }
}

function Stop-PortListener([int]$Port, [string]$Label) {
    $hits = @(Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue)
    foreach ($hit in $hits) {
        $owning = [int]$hit.OwningProcess
        if ($owning -gt 0) {
            Stop-PidSafe -ProcessId $owning -Label "$Label :$Port"
        }
    }
}

function Stop-MatchingCommand([string]$Pattern, [string]$Label) {
    Get-CimInstance Win32_Process -ErrorAction SilentlyContinue |
        Where-Object { $_.CommandLine -and ($_.CommandLine -match $Pattern) } |
        ForEach-Object { Stop-PidSafe -ProcessId ([int]$_.ProcessId) -Label $Label }
}

if (Test-Path $StateFile) {
    try {
        $state = Get-Content $StateFile -Raw | ConvertFrom-Json
        if ($state.control_plane_pid) {
            Stop-PidSafe -ProcessId ([int]$state.control_plane_pid) -Label "control-plane"
        }
        if ($state.ui_pid) {
            Stop-PidSafe -ProcessId ([int]$state.ui_pid) -Label "ui"
        }
    }
    catch {
        Write-Host "Could not read $StateFile; stopping by port instead."
    }
}

Stop-MatchingCommand -Pattern "uvicorn casops\.api\.control" -Label "uvicorn"
Stop-MatchingCommand -Pattern "vite --host 127\.0\.0\.1 --port $UiPort" -Label "vite"

Stop-PortListener -Port $ControlPort -Label "control-plane"
Stop-PortListener -Port $UiPort -Label "ui"

Start-Sleep -Seconds 1

$left = @()
if (Get-NetTCPConnection -LocalPort $ControlPort -State Listen -ErrorAction SilentlyContinue) {
    $left += $ControlPort
}
if (Get-NetTCPConnection -LocalPort $UiPort -State Listen -ErrorAction SilentlyContinue) {
    $left += $UiPort
}

if (Test-Path $StateFile) {
    Remove-Item $StateFile -Force -ErrorAction SilentlyContinue
}

if ($left.Count -gt 0) {
    Write-Host "Still listening: $($left -join ', ')"
    exit 1
}

Write-Host "CASOPS local stack is stopped (ports $ControlPort and $UiPort are free)."
