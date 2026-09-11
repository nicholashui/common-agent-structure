# Improve `specials.agent-loop-creator`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: Loops that are specified vs loops that spin
Notes: Loops that are specified vs loops that spin. **ReAct** (Yao et al., arXiv:2210.03629, ICLR 2023) interleaves Thought → Action → Observation. It has no cross-episode memory: the same failure repeats. **Reflexion** (Shinn et al., arXiv:2303.11366) adds Actor / Evaluator / Self-Reflection: environmental feedback becomes a *verbal* summary stored as episodic text, not a weight update. **Plan-and-Execu

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/specials.agent-loop-creator/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: Cynefin + one named shape + hop budget + gate + escalation (or wait/OOS). No qualified loop-success instrument. Do not close with “≥95%”. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `specials.agent-loop-creator`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | [2210.03629](https://arxiv.org/abs/2210.03629) |
| arXiv | [2303.11366](https://arxiv.org/abs/2303.11366) |
| arXiv | [2305.18323](https://arxiv.org/abs/2305.18323) |
| arXiv | [2509.03990](https://arxiv.org/abs/2509.03990) |
| YouTube | [Yao, LLM Agents / ReAct (Berkeley LLM Agents MOOC)](https://www.youtube.com/watch?v=RM6ZArd2nVc) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/tools/overview) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

