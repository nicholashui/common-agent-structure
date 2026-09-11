# Improve `specials.techology-advisor-agent`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: Advice that can be reviewed
Notes: Advice that can be reviewed. The SPEC already requires reviewing prior recommendations when an outcome is bad. Minimum: - What was recommended, under which constraints - What evidence was missing - What must not be activated (vendors, keys, MCP) Do not treat design-time model names as enabled. Fail closed on production activation, network, and credentials.

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/specials.techology-advisor-agent/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: dated citations over “latest model”; vendor names are not enabled APIs. Do not close with “≥95%”. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `specials.techology-advisor-agent`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | [2510.02453](https://arxiv.org/abs/2510.02453) |
| arXiv | [2609.05385](https://arxiv.org/abs/2609.05385) |
| YouTube | [Karpathy tokenizer lecture — dated vendor internals vs 'latest model' memory](https://www.youtube.com/watch?v=zduSFxRajkE) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/pricing) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

