# Start the local CASOPS operator stack: control plane (:18080) and Control UI (:15173).
# Run from anywhere:  powershell -File scripts/start_all.ps1
# uvicorn/vite run hidden. This script must return the prompt.

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
    $client = [System.Net.Sockets.TcpClient]::new()
    try {
        $iar = $client.BeginConnect("127.0.0.1", $Port, $null, $null)
        if (-not $iar.AsyncWaitHandle.WaitOne(400)) {
            return $false
        }
        $client.EndConnect($iar)
        return $true
    }
    catch {
        return $false
    }
    finally {
        $client.Dispose()
    }
}

function Wait-Port([int]$Port, [int]$Seconds = 45) {
    Write-Host "Waiting for 127.0.0.1:$Port ..."
    $deadline = [datetime]::UtcNow.AddSeconds($Seconds)
    $lastReport = 0
    while ([datetime]::UtcNow -lt $deadline) {
        if (Test-PortListen $Port) {
            Write-Host "  127.0.0.1:$Port is up"
            return $true
        }
        Start-Sleep -Milliseconds 250
        $elapsed = [int]($Seconds - ($deadline - [datetime]::UtcNow).TotalSeconds)
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

    $env:PYTHONPATH = $SrcDir
    $env:CASOPS_AGENTS_ROOT = Join-Path $Root "agents"
    $env:PYTHONUNBUFFERED = "1"

    $control = Start-Process -FilePath $Python -ArgumentList @(
        "-m", "uvicorn",
        "casops.api.control:create_app_from_env",
        "--factory",
        "--host", "127.0.0.1",
        "--port", "$ControlPort"
    ) -WorkingDirectory $Root -RedirectStandardOutput $controlLogs.Out -RedirectStandardError $controlLogs.Err -PassThru -WindowStyle Hidden

    $controlPid = $control.Id
    Write-Host "Started control plane pid=$controlPid -> http://127.0.0.1:$ControlPort"
    Write-Host "  stderr $($controlLogs.Err)"
    if (-not (Wait-Port $ControlPort)) {
        $tail = ""
        if (Test-Path $controlLogs.Err) {
            $tail = (Get-Content $controlLogs.Err -Tail 20) -join "`n"
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
    $ui = Start-Process -FilePath "cmd.exe" -ArgumentList @(
        "/c", "npx vite --host 127.0.0.1 --port $UiPort"
    ) -WorkingDirectory $UiDir -RedirectStandardOutput $uiLogs.Out -RedirectStandardError $uiLogs.Err -PassThru -WindowStyle Hidden
    $uiPid = $ui.Id
    Write-Host "Started Control UI pid=$uiPid -> http://127.0.0.1:$UiPort"
    if (-not (Wait-Port $UiPort)) {
        $tail = ""
        if (Test-Path $uiLogs.Err) {
            $tail = (Get-Content $uiLogs.Err -Tail 20) -join "`n"
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
Write-Host "Stop with: powershell -File scripts/stop_all.ps1"
Write-Host "This window is free. Servers keep running in the background."
