# Wrapper: python tools/grok_agent.py <chat|prompt|workshop> <agent_id> ...
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [ValidateSet("chat", "prompt", "workshop")]
    [string]$Mode,
    [Parameter(Mandatory = $true, Position = 1)]
    [string]$AgentId
)
$Root = Split-Path -Parent $PSScriptRoot
$extra = $args
& python (Join-Path $Root "tools\grok_agent.py") $Mode $AgentId @extra
exit $LASTEXITCODE
