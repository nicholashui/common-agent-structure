# Improve `specials.llm-usage`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: What to meter
Notes: What to meter. LLM cost is **tokens × unit price × retries**, not “API calls”. Separate: - Input vs output vs cached/prompt-prefix tokens - Provider vs model vs key - Success vs error vs timeout (errors still bill on many APIs) A dashboard that only sums “requests” will lie. Do not persist API keys in git or in this folder; keys are host/env only. This agent **describes** usage accounting. It does

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/specials.llm-usage/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: request counts are not the meter; no API keys stored. Do not close with “≥95%”. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `specials.llm-usage`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | [2606.24616](https://arxiv.org/abs/2606.24616) |
| arXiv | [2605.30040](https://arxiv.org/abs/2605.30040) |
| arXiv | [2504.13359](https://arxiv.org/abs/2504.13359) |
| YouTube | [Karpathy, Let's build the GPT Tokenizer — meter tokens, not 'API calls'](https://www.youtube.com/watch?v=zduSFxRajkE) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/pricing) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

