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

## Triple research (design-time, 2026-09)

Design-time citations collected to complete the arXiv + YouTube + x.ai triple. **Not** live grants. `allowed_tools` stays `[]`. Network, plugins, T3, memory writes, and production stay off.

### arXiv
- [2510.02453](https://arxiv.org/abs/2510.02453) — How to Train Your Advisor — steering black-box LLMs; vendor names are not enabled APIs
- [2609.05385](https://arxiv.org/abs/2609.05385) — Necessary or Sufficient? Evaluating LLM explanations with behavioural evidence

### YouTube (educational; do not paste transcripts into Chat)
- [Karpathy tokenizer lecture — dated vendor internals vs 'latest model' memory](https://www.youtube.com/watch?v=zduSFxRajkE)

### xAI (non-activating vendor docs)
- [Prefer dated xAI pricing/docs over undated 'latest model'](https://docs.x.ai/developers/pricing)
- [Quickstart is not a live key or MCP grant](https://x.ai/docs/developers/quickstart)

