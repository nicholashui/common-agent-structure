# Domain knowledge — `specials.techology-advisor-agent`

Design-time study (2026-09). Draft / data-only. No tools, network, plugins, memory writes, or production activation. Folder id spelling `techology` is historical; do not invent a second agent_id.

## Advice that can be reviewed

The SPEC already requires reviewing prior recommendations when an outcome is bad. Minimum:

- What was recommended, under which constraints
- What evidence was missing
- What must not be activated (vendors, keys, MCP)

Do not treat design-time model names as enabled. Fail closed on production activation, network, and credentials.

## Sources

- Host `agent_spec.json` `does_not_own`: credentials, silent production activation
- `common_agent_structure.md` §5.2 fail-closed required files
- `issues/issue0002.md` — Chat 200 ≠ agent-correct; advice is not an eval PASS
- Prefer dated vendor docs (https://x.ai/docs) over “latest model” memory; do not enable network from that mention
