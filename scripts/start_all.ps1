# Start the local CASOPS operator stack: control plane (:18080) and Control UI (:15173).
# Run from anywhere:  powershell -File scripts/start_all.ps1

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$UiDir = Join-Path $Root "ui"
$VarDir = Join-Path $Root "var"
$LogDir = Join-Path $Root "logs"
$StateFile = Join-Path $VarDir "casops-servers.json"
$ControlOutLog = Join-Path $LogDir "control-plane.out.log"
$ControlErrLog = Join-Path $LogDir "control-plane.err.log"
$UiOutLog = Join-Path $LogDir "ui.out.log"
$UiErrLog = Join-Path $LogDir "ui.err.log"
$ControlPort = 18080
$UiPort = 15173

New-Item -ItemType Directory -Force -Path $VarDir, $LogDir | Out-Null

function Test-PortListen([int]$Port) {
    $hits = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue
    return [bool]$hits
}

function Wait-Http([string]$Url, [int]$Seconds = 40) {
    for ($i = 0; $i -lt $Seconds; $i++) {
        try {
            $null = Invoke-WebRequest -Uri $Url -UseBasicParsing -TimeoutSec 2
            return $true
        }
        catch {
            Start-Sleep -Seconds 1
        }
    }
    return $false
}

function Get-ListenerPid([int]$Port) {
    $hits = @(Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue)
    if ($hits.Count -eq 0) {
        return $null
    }
    return [int]$hits[0].OwningProcess
}

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

    $env:PYTHONPATH = Join-Path $Root "src"
    $env:CASOPS_AGENTS_ROOT = Join-Path $Root "agents"

    Remove-Item $ControlOutLog, $ControlErrLog -Force -ErrorAction SilentlyContinue

    $control = Start-Process -FilePath $Python -ArgumentList @(
        "-m", "uvicorn",
        "casops.api.control:create_app_from_env",
        "--factory",
        "--host", "127.0.0.1",
        "--port", "$ControlPort"
    ) -WorkingDirectory $Root -RedirectStandardOutput $ControlOutLog -RedirectStandardError $ControlErrLog -PassThru -WindowStyle Hidden

    Write-Host "Started control plane pid=$($control.Id) -> http://127.0.0.1:$ControlPort"
}

if (Test-PortListen $UiPort) {
    Write-Host "Control UI already listening on 127.0.0.1:$UiPort"
}
else {
    if (-not (Test-Path (Join-Path $UiDir "package.json"))) {
        throw "UI package.json not found at $UiDir"
    }
    if (-not (Test-Path (Join-Path $UiDir "node_modules"))) {
        Write-Host "ui/node_modules missing; running npm install..."
        Push-Location $UiDir
        try {
            npm install
            if ($LASTEXITCODE -ne 0) {
                throw "npm install failed with exit $LASTEXITCODE"
            }
        }
        finally {
            Pop-Location
        }
    }

    Remove-Item $UiOutLog, $UiErrLog -Force -ErrorAction SilentlyContinue

    $ui = Start-Process -FilePath "cmd.exe" -ArgumentList @(
        "/c", "npx vite --host 127.0.0.1 --port $UiPort"
    ) -WorkingDirectory $UiDir -RedirectStandardOutput $UiOutLog -RedirectStandardError $UiErrLog -PassThru -WindowStyle Hidden

    Write-Host "Started Control UI pid=$($ui.Id) -> http://127.0.0.1:$UiPort"
}

if (-not (Wait-Http "http://127.0.0.1:$ControlPort/health")) {
    throw "Control plane did not become ready on :$ControlPort. See $ControlErrLog"
}
if (-not (Wait-Http "http://127.0.0.1:$UiPort/")) {
    throw "Control UI did not become ready on :$UiPort. See $UiErrLog"
}

$state = [ordered]@{
    started_at         = (Get-Date).ToString("o")
    repo               = $Root
    control_plane_url  = "http://127.0.0.1:$ControlPort"
    ui_url             = "http://127.0.0.1:$UiPort"
    control_plane_pid  = Get-ListenerPid $ControlPort
    ui_pid             = Get-ListenerPid $UiPort
}
$state | ConvertTo-Json | Set-Content -Path $StateFile -Encoding utf8

Write-Host ""
Write-Host "CASOPS local stack is up."
Write-Host "  Control plane  $($state.control_plane_url)  (GET /health, /api/v3, /docs)"
Write-Host "  Control UI     $($state.ui_url)"
Write-Host "Logs: $ControlErrLog"
Write-Host "      $UiErrLog"
Write-Host "Stop with: powershell -File scripts/stop_all.ps1"
