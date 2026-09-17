# ISSUE-0011 — Domain agents follow operation-guide house rules

**Status:** Implemented (CHARACTERIZATION). House rules declared on Chat-spine agents; skills not live.  
**Severity:** Medium (agent crafts must not fight the compiler)  
**Component:** `agents/video.promptengineer`, director, cinematographer, cameraoperator, continuity, critic, mua_makeup, creativedirector, promptoptimizer; intent-analysis / creative-agent  
**Related:** ISSUE-0010 (compiler dialects). ISSUE-0009 (owned paths).  
**Honesty:** CHARACTERIZATION. Skills **declared**, not live. `allowed_tools` stays empty. Citations are design-time.

## Agents in scope

Chat-spine domain experts plus PE:

- `video.promptengineer` — orchestrates; does not write the novel; host compiler owns vendor dialect
- `video.creativedirector` — thesis / WHY only
- `video.director` — beats / action; one job per beat
- `video.cinematographer` — light / look; one light logic
- `video.cameraoperator` — one camera move (or locked)
- `video.continuity` — identity + hair/skin anchors
- `video.mua_makeup` — scene_state face finish
- `video.critic` — constraints; short “no X”; no vendor-parameter essays
- `video.promptoptimizer` — same PE house rules
- `specials.intent-analysis-agent` / `specials.general-creative-agent` — framework only; do not author lighting, motors, or vendor prompts

## Work

- Add `prompts/operation_guide_house_rules.md` (or a short block in `prompts/primary.md`) citing `spec/*_operation_guide.md` (includes `spec/wan_operation_guide.md`).
- Declare skill `casops.skill.video.operation-guide` in `skills/bindings.json` with `host_permission: false`.
- Do not change Auto Pilot hop counts or five human ASK_HUMAN roles.
- Do not paste `sample/` bodies into agent files.

**Exit:** Each listed agent’s primary prompt mentions operation-guide house rules and refuses to put duration/aspect in craft prose as vendor syntax.
