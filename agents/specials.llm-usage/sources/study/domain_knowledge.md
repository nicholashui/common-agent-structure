# Domain knowledge — `specials.llm-usage`

Design-time study (2026-09). Draft / data-only. No tools, network, plugins, memory writes, or production activation.

## What to meter

LLM cost is **tokens × unit price × retries**, not “API calls”. Separate:

- Input vs output vs cached/prompt-prefix tokens
- Provider vs model vs key
- Success vs error vs timeout (errors still bill on many APIs)

A dashboard that only sums “requests” will lie. Do not persist API keys in git or in this folder; keys are host/env only.

This agent **describes** usage accounting. It does not call xAI, Poe, MiniMax, Kimi, or OpenRouter from CASOPS Chat.

## Sources

- Provider pricing is vendor-specific and changes; treat any number in design text as stale unless dated.
- Host `agent_spec.json`: `network_access: false`, `allowed_tools: []`.

## Triple research (design-time, 2026-09)

Design-time citations collected to complete the arXiv + YouTube + x.ai triple. **Not** live grants. `allowed_tools` stays `[]`. Network, plugins, T3, memory writes, and production stay off.

### arXiv
- [2606.24616](https://arxiv.org/abs/2606.24616) — Zhu, AI Tokenomics — tokens as the accounting unit (names xAI among billers)
- [2605.30040](https://arxiv.org/abs/2605.30040) — Hoque et al., Token Inflation — per-token bills are hard to audit
- [2504.13359](https://arxiv.org/abs/2504.13359) — Cost-of-Pass — expected cost of a correct solution, not request counts

### YouTube (educational; do not paste transcripts into Chat)
- [Karpathy, Let's build the GPT Tokenizer — meter tokens, not 'API calls'](https://www.youtube.com/watch?v=zduSFxRajkE)

### xAI (non-activating vendor docs)
- [Dated xAI token / Imagine / Voice / tools prices — stale unless dated; do not store keys](https://docs.x.ai/developers/pricing)

