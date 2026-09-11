# Start the local CASOPS operator stack: control plane (:18080) and Control UI (:15173).
# Run from anywhere:  powershell -NoProfile -File scripts/start_all.ps1
# Servers are detached. This script must return the prompt (do not -Wait, do not
# RedirectStandardOutput on Start-Process — that keeps this console attached).

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"

$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$UiDir = Join-Path $Root "ui"
$SrcDir = Join-Path $Root "src"
$VarDir = Join-Path $Root "var"
$LogDir = Join-Path $Root "logs"
$StateFile = Join-Path $VarDir "casops-servers.json"
$ControlPort = 18080
$UiPort = 15173

New-Item -ItemType Directory -Force -Path $VarDir, $LogDir | Out-Null
Write-Host "CASOPS start_all from $Root"

function Test-PortListen([int]$Port) {
    $client = $null
    try {
        $client = [System.Net.Sockets.TcpClient]::new()
        $task = $client.ConnectAsync("127.0.0.1", $Port)
        if (-not $task.Wait(300)) {
            return $false
        }
        return [bool]$client.Connected
    }
    catch {
        return $false
    }
    finally {
        if ($null -ne $client) {
            try { $client.Close() } catch { }
            try { $client.Dispose() } catch { }
        }
    }
}

function Wait-Port([int]$Port, [int]$Seconds = 25) {
    Write-Host "Waiting for 127.0.0.1:$Port (max ${Seconds}s) ..."
    $started = Get-Date
    $lastReport = -5
    while (((Get-Date) - $started).TotalSeconds -lt $Seconds) {
        if (Test-PortListen $Port) {
            Write-Host "  127.0.0.1:$Port is up"
            return $true
        }
        Start-Sleep -Milliseconds 200
        $elapsed = [int]((Get-Date) - $started).TotalSeconds
        if ($elapsed -ge ($lastReport + 5)) {
            $lastReport = $elapsed
            Write-Host "  still waiting (${elapsed}s)"
        }
    }
    return $false
}

function Get-LogPair([string]$Prefix) {
    $out = Join-Path $LogDir "$Prefix.out.log"
    $err = Join-Path $LogDir "$Prefix.err.log"
    foreach ($path in @($out, $err)) {
        try {
            $fs = [System.IO.File]::Open($path, [System.IO.FileMode]::OpenOrCreate, [System.IO.FileAccess]::Write, [System.IO.FileShare]::ReadWrite)
            $fs.Close()
        }
        catch {
            $stamp = Get-Date -Format "yyyyMMdd-HHmmss"
            $out = Join-Path $LogDir "$Prefix.$stamp.out.log"
            $err = Join-Path $LogDir "$Prefix.$stamp.err.log"
            break
        }
    }
    return @{ Out = $out; Err = $err }
}

function Write-LaunchCmd([string]$Path, [string]$Body) {
    Set-Content -Path $Path -Value $Body -Encoding Ascii
}

function Start-DetachedCmd([string]$CmdPath) {
    # No -Wait. No RedirectStandard*. Hidden window. Returns immediately.
    $proc = Start-Process -FilePath $env:ComSpec -ArgumentList @("/c", "`"$CmdPath`"") -WorkingDirectory $Root -WindowStyle Hidden -PassThru
    return $proc
}

$controlPid = $null
$uiPid = $null
$controlLogs = Get-LogPair "control-plane"
$uiLogs = Get-LogPair "ui"

if (Test-PortListen $ControlPort) {
    Write-Host "Control plane already listening on 127.0.0.1:$ControlPort"
}
else {
    $venvPython = Join-Path $Root ".venv\Scripts\python.exe"
    if (Test-Path $venvPython) {
        $Python = $venvPython
    }
    else {
        $Python = (Get-Command python -ErrorAction Stop).Source
    }
    Write-Host "Starting control plane with $Python"

    $launchControl = Join-Path $VarDir "start-control-plane.cmd"
    $agentsRoot = Join-Path $Root "agents"
    Write-LaunchCmd $launchControl @"
@echo off
cd /d "$Root"
set PYTHONPATH=$SrcDir
set CASOPS_AGENTS_ROOT=$agentsRoot
set PYTHONUNBUFFERED=1
"$Python" -m uvicorn casops.api.control:create_app_from_env --factory --host 127.0.0.1 --port $ControlPort > "$($controlLogs.Out)" 2> "$($controlLogs.Err)"
"@
    $control = Start-DetachedCmd $launchControl
    $controlPid = $control.Id
    Write-Host "Started control plane wrapper pid=$controlPid -> http://127.0.0.1:$ControlPort"
    Write-Host "  stderr $($controlLogs.Err)"
    if (-not (Wait-Port $ControlPort)) {
        $tail = ""
        if (Test-Path $controlLogs.Err) {
            $tail = (Get-Content $controlLogs.Err -Tail 20 -ErrorAction SilentlyContinue) -join "`n"
        }
        throw "Control plane did not become ready on :$ControlPort.`n$tail"
    }
}

if (Test-PortListen $UiPort) {
    Write-Host "Control UI already listening on 127.0.0.1:$UiPort"
}
else {
    if (-not (Test-Path (Join-Path $UiDir "package.json"))) {
        throw "UI package.json not found at $UiDir"
    }
    if (-not (Test-Path (Join-Path $UiDir "node_modules"))) {
        throw "ui/node_modules missing. Run npm install in ui/ first (start_all will not block on npm)."
    }

    Write-Host "Starting Control UI..."
    $launchUi = Join-Path $VarDir "start-ui.cmd"
    Write-LaunchCmd $launchUi @"
@echo off
cd /d "$UiDir"
npx --no-install vite --host 127.0.0.1 --port $UiPort > "$($uiLogs.Out)" 2> "$($uiLogs.Err)"
"@
    $ui = Start-DetachedCmd $launchUi
    $uiPid = $ui.Id
    Write-Host "Started Control UI wrapper pid=$uiPid -> http://127.0.0.1:$UiPort"
    if (-not (Wait-Port $UiPort)) {
        $tail = ""
        if (Test-Path $uiLogs.Err) {
            $tail = (Get-Content $uiLogs.Err -Tail 20 -ErrorAction SilentlyContinue) -join "`n"
        }
        throw "Control UI did not become ready on :$UiPort.`n$tail"
    }
}

$state = [ordered]@{
    started_at        = [DateTime]::UtcNow.AddHours(8).ToString("yyyy-MM-ddTHH:mm:ss") + "+08:00"
    repo              = $Root
    control_plane_url = "http://127.0.0.1:$ControlPort"
    ui_url            = "http://127.0.0.1:$UiPort"
    control_plane_pid = $controlPid
    ui_pid            = $uiPid
}
$state | ConvertTo-Json | Set-Content -Path $StateFile -Encoding utf8

Write-Host ""
Write-Host "CASOPS local stack is up."
Write-Host "  Control plane  $($state.control_plane_url)  (GET /health, /api/v3, /docs)"
Write-Host "  Control UI     $($state.ui_url)"
Write-Host "Logs: $($controlLogs.Err)"
Write-Host "      $($uiLogs.Err)"
Write-Host "Stop with: powershell -NoProfile -File scripts/stop_all.ps1"
Write-Host "This window is free. Servers keep running in the background."
