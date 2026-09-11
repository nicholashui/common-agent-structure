# Improve `specials.psychological-recommendation-agent`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: Explainable recs, cold start, filter bubbles
Notes: Explainable recs, cold start, filter bubbles. A recommendation is incomplete without **why** (features used, trait used, what was not chosen). Cold start: no history → use stated traits and situational context (stress → lower intensity), not a fake viewing history. Diversity: optimizing only predicted rating collapses to a filter bubble. Personality-aware recsys literature reports modest accuracy 

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/specials.psychological-recommendation-agent/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: no fake history; 5–10% lift unverified unless local eval exists. Do not close with “≥95%”. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `specials.psychological-recommendation-agent`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | [2101.12153](https://arxiv.org/abs/2101.12153) |
| arXiv | [2106.03060](https://arxiv.org/abs/2106.03060) |
| arXiv | [2501.01945](https://arxiv.org/abs/2501.01945) |
| YouTube | [Trait theories lecture (Eysenck, Costa, McCrae, Cattell) — traits as rec side-features](https://www.youtube.com/watch?v=D33VOyGGib8) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/tools/overview) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

