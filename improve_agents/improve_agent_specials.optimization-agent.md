# Improve `specials.optimization-agent`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: Optimize a *stated* objective
Notes: Optimize a *stated* objective. “Autonomous optimization” without an objective, constraints, and a measurement is just mutation. Minimum contract: 1. Objective (what improves) 2. Constraints (what must not regress: safety, cost, latency, legality) 3. Metric + window 4. Stop / rollback Process mining and digital twins are **design mentions**. This host does not attach event logs or simulators. Prefe

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/specials.optimization-agent/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: missing contract field → wait; do not evolve safety gates. Do not close with “≥95%”. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `specials.optimization-agent`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | [2503.12434](https://arxiv.org/abs/2503.12434) |
| arXiv | [2605.27630](https://arxiv.org/abs/2605.27630) |
| arXiv | [2605.27375](https://arxiv.org/abs/2605.27375) |
| YouTube | [EPM, PDCA Cycle Explained (Deming / Shewhart)](https://www.youtube.com/watch?v=bO3GpAjVvD8) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/pricing) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

