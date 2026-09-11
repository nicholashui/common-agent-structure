# Improve `specials.screenwriter-strategic-goal-achievement-agent`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: Screenplay goals still need Key Results
Notes: Screenplay goals still need Key Results. Same OKR spine as `specials.strategic-goal-achievement-agent`, applied to a script: pages, sequences, character-want vs need, deadline. Vague “make it more cinematic” is not a KR. Pair with craft: want/need, turning points, scene purpose. Do not activate `video.screenwriter` tools. This is a **goal coach** for screenwriting, not the pack screenwriter.

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/specials.screenwriter-strategic-goal-achievement-agent/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: “more cinematic” is not a KR; do not write the script unless analysing one. Do not close with “≥95%”. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `specials.screenwriter-strategic-goal-achievement-agent`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | [2311.16542](https://arxiv.org/abs/2311.16542) |
| arXiv | [1708.09040](https://arxiv.org/abs/1708.09040) |
| arXiv | [2107.13189](https://arxiv.org/abs/2107.13189) |
| YouTube | [John Doerr, Intel Operation Crush OKR example — KRs must be yes/no](https://www.youtube.com/watch?v=pMlBMBTtJEw) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/tools/overview) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

