# Improve `specials.strategic-goal-achievement-agent`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: Goals that can be scored
Notes: Goals that can be scored. OKRs (Grove at Intel; Doerr, *Measure What Matters*, 2018): **Objective** (qualitative what) + **3–5 Key Results** (quantitative, yes/no at the end). Kaplan & Norton **Balanced Scorecard** (HBR 1992) supplies a strategy map; OKRs supply quarterly focus. The folder’s six self-question stages (motivation, audience, methods, emotion, execution, iteration) are a Socratic elic

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/specials.strategic-goal-achievement-agent/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: do not execute the plan; no KR → keep asking or accept qualitative stop. Do not close with “≥95%”. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `specials.strategic-goal-achievement-agent`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | [2311.16542](https://arxiv.org/abs/2311.16542) |
| arXiv | [2311.00236](https://arxiv.org/abs/2311.00236) |
| arXiv | [2511.08242](https://arxiv.org/abs/2511.08242) |
| YouTube | [John Doerr, OKRs Explained (Measure What Matters)](https://www.youtube.com/watch?v=MV4UViKjJ34) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/tools/overview) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

