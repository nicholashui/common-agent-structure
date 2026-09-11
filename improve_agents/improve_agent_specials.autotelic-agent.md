# Improve `specials.autotelic-agent`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: Autotelic ≠ random curiosity
Notes: Autotelic ≠ random curiosity. From Greek *auto* (self) + *telos* (goal): an autotelic agent **represents, generates, selects, and masters its own goals** (Colas, Karch, Sigaud, Oudeyer, JAIR 2022, arXiv:2012.09830). It is a special case of intrinsic motivation, which is a special case of autonomy. **IMGEP** (Intrinsically Motivated Goal Exploration Processes) is the developmental-robotics family: 

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/specials.autotelic-agent/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: IMGEP vs EMGEP is labelled; stop condition present; no live training grant. Do not close with “≥95%”. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `specials.autotelic-agent`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | [2012.09830](https://arxiv.org/abs/2012.09830) |
| YouTube | [Oudeyer, Developmental Machine Learning, ICLR 2019 keynote (IMGEP)](https://www.youtube.com/watch?v=7bJ0fnvPLaA) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/tools/overview) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

