# Research map — LLM usage metering

| ID | Why here |
|---|---|
| Provider pricing is vendor-specific and changes; treat any number in design text as stale unless dated. | in-role study |
| Host `agent_spec.json`: `network_access: false`, `allowed_tools: []`. | in-role study |

Full notes: `../../sources/study/domain_knowledge.md`.
## arXiv / YouTube / xAI (verified 2026-09)

### arXiv

| ID | Why here |
|---|---|
| [2606.24616](https://arxiv.org/abs/2606.24616) | Zhu, AI Tokenomics — tokens as the accounting unit (names xAI among billers) |
| [2605.30040](https://arxiv.org/abs/2605.30040) | Hoque et al., Token Inflation — per-token bills are hard to audit |
| [2504.13359](https://arxiv.org/abs/2504.13359) | Cost-of-Pass — expected cost of a correct solution, not request counts |

### YouTube

- [Karpathy, Let's build the GPT Tokenizer — meter tokens, not 'API calls'](https://www.youtube.com/watch?v=zduSFxRajkE)

### xAI (non-activating)

- [Dated xAI token / Imagine / Voice / tools prices — stale unless dated; do not store keys](https://docs.x.ai/developers/pricing)

Do not enable tools/network from these citations.
