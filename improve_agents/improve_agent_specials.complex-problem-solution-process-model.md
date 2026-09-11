# Improve `specials.complex-problem-solution-process-model`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: WHAT–WHY–HOW–DO–REVIEW vs sense-making domains
Notes: WHAT–WHY–HOW–DO–REVIEW vs sense-making domains. This folder’s five stages (WHAT frame, WHY diagnose, HOW select, DO execute, REVIEW adapt) are a *process*. They are not always the right *move*. Snowden’s **Cynefin** (HBR 2007, “A Leader’s Framework for Decision Making”) sorts situations first: | Domain | Cause–effect | Move | |---|---|---| | Clear | Known | Sense–categorize–respond (best practice)

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/specials.complex-problem-solution-process-model/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: domain named; complex → safe-to-fail probes; complicated may use Five Whys. Do not close with “≥95%”. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `specials.complex-problem-solution-process-model`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | [2204.10358](https://arxiv.org/abs/2204.10358) |
| arXiv | [2505.00018](https://arxiv.org/abs/2505.00018) |
| YouTube | [The Cynefin Company, The Cynefin Framework (official)](https://www.youtube.com/watch?v=ogtpxA6brGo) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/tools/overview) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

