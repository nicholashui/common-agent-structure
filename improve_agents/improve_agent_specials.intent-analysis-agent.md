# Improve `specials.intent-analysis-agent`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: Owns analysis of operator text
Notes: Speech acts, not “hidden agenda” as a vibe. Austin (*How to Do Things with Words*): **locution** (what is said), **illocution** (the act performed *in* saying), **perlocution** (the effect *by* saying). Searle (*Speech Acts*, 1969) taxonomizes illocutions as **assertives, directives, commissives, expressives, declarations**. Grice’s cooperative principle and maxims (Quantity, Quality, Relation, Ma

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/specials.intent-analysis-agent/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: in-role intent-analysis-agent artifacts or wait; no invented CLIP-T/WCAG/arena numbers. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `specials.intent-analysis-agent`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | [2509.10010](https://arxiv.org/abs/2509.10010) |
| arXiv | [2507.22289](https://arxiv.org/abs/2507.22289) |
| arXiv | [2506.01881](https://arxiv.org/abs/2506.01881) |
| arXiv | [2411.14252](https://arxiv.org/abs/2411.14252) |
| YouTube | [Searle & Magee 1977 , The Philosophy of Language](https://www.youtube.com/watch?v=FItTy4yizlw) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/tools/overview) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

