# Prove Chat reaches agents/<id> through Grok Build ACP (ISSUE-0006).
# Transport only. Not an eval pass. Not ISSUE-0002 (agent-correct).
#
#   powershell -File scripts/start_all.ps1
#   powershell -File scripts/prove_grok_acp.ps1
#   powershell -File scripts/prove_grok_acp.ps1 -AgentId video.director -ForceAdapter

param(
    [string]$AgentId = "video.director",
    [string]$BaseUrl = "http://127.0.0.1:18080",
    [switch]$ForceAdapter,
    [switch]$Start,
    [switch]$StopAfter
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$ProofDir = Join-Path $Root "logs\proof"
$Profile = Join-Path $Root "var\acp\$AgentId\profile.md"
$Stamp = [DateTime]::UtcNow.AddHours(8).ToString("yyyy-MM-dd-HH-mm-ss")
$OutPath = Join-Path $ProofDir "grok-acp-$AgentId-$Stamp.json"
$Marker = "ISSUE-0006 ping-grok-acp-$Stamp"
$Failures = [System.Collections.Generic.List[string]]::new()

New-Item -ItemType Directory -Force -Path $ProofDir | Out-Null

function Add-Fail([string]$Text) {
    $script:Failures.Add($Text)
    Write-Host "FAIL  $Text" -ForegroundColor Red
}

function Get-Json([string]$Url) {
    return Invoke-RestMethod -Uri $Url -UseBasicParsing -TimeoutSec 30
}

function Test-Health {
    try {
        $h = Get-Json "$BaseUrl/health"
        return ($h.status -eq "ok")
    }
    catch {
        return $false
    }
}

if ($env:CASOPS_ACP_COMMAND) {
    Add-Fail "CASOPS_ACP_COMMAND is set; that is the pytest fake path, not Grok Build"
}

$grok = Get-Command grok -ErrorAction SilentlyContinue
if (-not $grok) {
    Add-Fail "grok is not on PATH"
}
else {
    Write-Host "grok  $($grok.Source)"
}

if (-not (Test-Path $Profile)) {
    Write-Host "profile missing; projecting $AgentId"
    $env:PYTHONPATH = Join-Path $Root "src"
    Push-Location $Root
    try {
        python tools/project_grok_profile.py --agent-id $AgentId --write-binding
        if ($LASTEXITCODE -ne 0) {
            Add-Fail "projector failed for $AgentId"
        }
    }
    finally {
        Pop-Location
    }
}
if (-not (Test-Path $Profile)) {
    Add-Fail "missing $Profile"
}
else {
    $head = Get-Content $Profile -TotalCount 8
    if (($head -join "`n") -notmatch "DO NOT EDIT") {
        Add-Fail "profile is not a generated projection"
    }
    if (($head -join "`n") -notmatch [regex]::Escape("name: $AgentId")) {
        Add-Fail "profile name is not $AgentId"
    }
}

$needStart = $Start -or -not (Test-Health)
if ($needStart) {
    Write-Host "starting local stack (scripts/start_all.ps1)"
    & (Join-Path $PSScriptRoot "start_all.ps1")
    if ($LASTEXITCODE -ne 0 -and -not (Test-Health)) {
        Add-Fail "control plane did not become ready at $BaseUrl"
    }
}

if (-not (Test-Health)) {
    Add-Fail "GET $BaseUrl/health failed. Run scripts/start_all.ps1"
}

$headers = @{
    "Content-Type"              = "application/json"
    "x-casops-actor"            = "human_operator"
    "x-casops-reason"           = "ISSUE-0006 grok_acp transport proof"
    "x-casops-expected-parent"  = "none"
    "x-casops-dry-run"          = "false"
}

if ($ForceAdapter -and (Test-Health)) {
    Write-Host "POST /api/v3/llm/settings chat_adapter=grok_acp"
    Invoke-RestMethod -Method POST -Uri "$BaseUrl/api/v3/llm/settings" -Headers $headers `
        -Body '{"chat_adapter":"grok_acp"}' -TimeoutSec 30 | Out-Null
}

$before = $null
$chat = $null
$after = $null
$proc = $null

if (Test-Health) {
    $before = Get-Json "$BaseUrl/api/v3/agents/$AgentId/runtime/adapter"
    Write-Host ("before  kind={0} grok={1} profile={2} pid={3}" -f $before.kind, $before.grok_available, $before.profile_ready, $before.pid)
    if ($before.kind -ne "grok_acp") {
        Add-Fail "adapter kind=$($before.kind) (need grok_acp). Re-run with -ForceAdapter or unset CASOPS_CHAT_ADAPTER"
    }
    if (-not $before.grok_available) {
        Add-Fail "grok_available=false"
    }
    if (-not $before.profile_ready) {
        Add-Fail "profile_ready=false"
    }

    Write-Host "POST /runtime/chat (may take a minute; Grok assigns session_id)"
    try {
        $chat = Invoke-RestMethod -Method POST -Uri "$BaseUrl/api/v3/agents/$AgentId/runtime/chat" `
            -Headers $headers -TimeoutSec 180 `
            -Body (@{ message = $Marker; history = @() } | ConvertTo-Json -Compress)
    }
    catch {
        Add-Fail "chat POST failed: $($_.Exception.Message)"
        if ($_.ErrorDetails -and $_.ErrorDetails.Message) {
            Write-Host $_.ErrorDetails.Message
        }
    }

    if ($chat) {
        Write-Host ("chat    provider={0} adapter={1} pid={2} session_id={3}" -f `
                $chat.provider, $chat.context.adapter, $chat.context.pid, $chat.context.session_id)
        if ($chat.provider -ne "grok_acp") {
            Add-Fail "chat provider=$($chat.provider) (need grok_acp)"
        }
        if ($chat.context.adapter -ne "grok_acp") {
            Add-Fail "context.adapter=$($chat.context.adapter)"
        }
        if (-not $chat.context.session_id) {
            Add-Fail "context.session_id empty — host did not get session/new from Grok"
        }
        else {
            Write-Host "ACP session_id (Grok-assigned, not chosen by you): $($chat.context.session_id)"
        }
        if (-not $chat.context.pid) {
            Add-Fail "context.pid empty"
        }
        if ($chat.memory_writes -and @($chat.memory_writes).Count -gt 0) {
            Add-Fail "memory_writes not empty"
        }
        if ($chat.plugins_executed) {
            Add-Fail "plugins_executed true"
        }
        if ($chat.t3_enabled) {
            Add-Fail "t3_enabled true"
        }
        if (-not $chat.reply) {
            Add-Fail "empty reply"
        }
        if ($chat.reply -match "SECRET_COT") {
            Add-Fail "thought chunk leaked into reply"
        }
        $after = Get-Json "$BaseUrl/api/v3/agents/$AgentId/runtime/adapter"
        $pid = $chat.context.pid
        if ($pid) {
            $proc = Get-CimInstance Win32_Process -Filter "ProcessId=$pid" -ErrorAction SilentlyContinue
            if (-not $proc) {
                Add-Fail "no OS process for pid $pid"
            }
            else {
                Write-Host ("os      name={0}" -f $proc.Name)
                Write-Host ("os      cmd={0}" -f $proc.CommandLine)
                if ($proc.Name -notmatch "(?i)grok") {
                    Add-Fail "process name $($proc.Name) is not grok"
                }
                if ($proc.CommandLine -match "fake_acp_stdio") {
                    Add-Fail "command line is the pytest fake"
                }
                if ($proc.CommandLine -notmatch "--no-leader") {
                    Add-Fail "command line missing --no-leader"
                }
                if ($proc.CommandLine -notmatch "--agent-profile") {
                    Add-Fail "command line missing --agent-profile"
                }
                if ($proc.CommandLine -notmatch [regex]::Escape($AgentId)) {
                    Add-Fail "command line does not name $AgentId"
                }
                if ($proc.CommandLine -notmatch "stdio") {
                    Add-Fail "command line missing stdio"
                }
            }
        }
    }
}

$pass = $Failures.Count -eq 0
$record = [ordered]@{
    honesty            = "CHARACTERIZATION"
    not_eval_pass      = $true
    not_issue0002      = $true
    issue              = "ISSUE-0006"
    agent_id           = $AgentId
    marker             = $Marker
    verdict            = $(if ($pass) { "PASS_TRANSPORT" } else { "FAIL" })
    failures           = @($Failures)
    grok               = $(if ($grok) { $grok.Source } else { $null })
    profile            = $Profile
    session_id         = $(if ($chat) { $chat.context.session_id } else { $null })
    session_id_note    = "Assigned by Grok Build session/new. Do not pass this on Chat POST. Not the UI logs/chat file name."
    before             = $before
    chat_provider      = $(if ($chat) { $chat.provider } else { $null })
    chat_adapter       = $(if ($chat) { $chat.context.adapter } else { $null })
    chat_pid           = $(if ($chat) { $chat.context.pid } else { $null })
    memory_writes      = $(if ($chat) { $chat.memory_writes } else { $null })
    plugins_executed   = $(if ($chat) { $chat.plugins_executed } else { $null })
    t3_enabled         = $(if ($chat) { $chat.t3_enabled } else { $null })
    reply_chars        = $(if ($chat -and $chat.reply) { $chat.reply.Length } else { 0 })
    after              = $after
    process_name       = $(if ($proc) { $proc.Name } else { $null })
    process_command    = $(if ($proc) { $proc.CommandLine } else { $null })
    artifact           = $OutPath
}
$record | ConvertTo-Json -Depth 6 | Set-Content -Path $OutPath -Encoding utf8
Write-Host ""
Write-Host "wrote $OutPath"
Write-Host "verdict $($record.verdict)  (transport only; ISSUE-0002 stays Open)"

if ($StopAfter) {
    & (Join-Path $PSScriptRoot "stop_all.ps1")
}

if (-not $pass) {
    exit 1
}
exit 0
