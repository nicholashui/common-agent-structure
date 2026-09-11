# Improve `specials.controller-agent`

Research **this agent's craft**, not generic intent analysis / NLU.

Craft: Why Blender (or any 3D blockout) exists in an AI video loop
Notes: Why Blender (or any 3D blockout) exists in an AI video loop. Text-only camera prompts (“slow dolly in, slight handheld”) are under-specified. A 3D blockout makes **focal length, path, and timing** executable. 2026 production practice (Flick, NVIDIA RTX video guide) uses three control strengths: 1. **Motion reference** — export a blockout clip; the video model copies camera/action. 2. **Start/end f

Collect in-role papers, standards, talks, and dated vendor docs (arXiv and/or the statute/standard that actually governs the craft; one educational YouTube; one x.ai page as **non-activating**). Apply findings to `agents/specials.controller-agent/content/` and `sources/study/domain_knowledge.md`.

Build Chat edges (ambiguous, multi-intent, domain-specific, multilingual, out-of-scope), API samples on `/api/v3` only (valid, malformed, mutation/auth, rate-limit honesty, cross-domain), and paste-in multi-agent simulations. Store them under `content/tests/`. Extra host Chat JSON in `evals/fixtures/` must be `casops.testcase.v1` with honesty CHARACTERIZATION and fail-closed expects.

Write `content/test_guide.md` with three tiers: Chat, API (`/api/v3`), multi-agent paste-in. Success criteria stay CHARACTERIZATION: control map present; vendor names are design-time; no pretend Sora/Veo enabled. Do not close with “≥95%”. Do not invent ≥95% PASS. Chat HTTP 200 ≠ agent-correct (ISSUE-0002). casops-eval stays NOT_RUN.

Gated enablement of skills or tools is a separate host change (spec + permission). Declare the skill; do not resolve it live.

## Research landed (verified, 2026-09)

In-role citations for `specials.controller-agent`. CHARACTERIZATION only. Not an eval PASS. Not a live skill/tool grant.

| Leg | Citation |
|---|---|
| arXiv | [2506.17450](https://arxiv.org/abs/2506.17450) |
| arXiv | [2406.10126](https://arxiv.org/abs/2406.10126) |
| YouTube | [Camera Movements for Beginners — pan/tilt/dolly vs text-only prompts](https://www.youtube.com/watch?v=KupEY5CAwe4) |
| x.ai | [non-activating vendor doc](https://docs.x.ai/developers/model-capabilities/video/image-to-video) |

Do not paste transcripts. Do not enable Imagine, Web Search, Collections, Voice, or function calling.

