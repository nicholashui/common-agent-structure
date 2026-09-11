# Improve `specials.psychological-profile-agent`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: Prefer trait models with evidence
Notes: Prefer trait models with evidence. The **Big Five / FFM** (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism; Costa & McCrae; Goldberg) is the most replicated broad trait model. **HEXACO** (Lee & Ashton) adds Honesty–Humility and re-cuts Emotionality / Agreeableness; meta-analysis finds broader coverage and less dimension redundancy than FFM. **MBTI** is a type indicator, not a

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/specials.psychological-profile-agent/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: never diagnose; never invent a patient record. Do not close with “≥95%”. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `specials.psychological-profile-agent`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | [2510.14203](https://arxiv.org/abs/2510.14203) |
| arXiv | [2511.23101](https://arxiv.org/abs/2511.23101) |
| arXiv | [2607.02325](https://arxiv.org/abs/2607.02325) |
| YouTube | [Seeker, The Big 5 Personality Traits (Costa & McCrae)](https://www.youtube.com/watch?v=oWpRKJPCI7M) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/tools/overview) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

