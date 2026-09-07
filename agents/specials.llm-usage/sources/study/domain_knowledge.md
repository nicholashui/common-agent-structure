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
