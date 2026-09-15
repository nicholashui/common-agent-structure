# ISSUE-0010 — Compiler dialects from video/image operation guides

**Status:** Implemented (CHARACTERIZATION). Grok dialect live; other tags preview-only fail-closed.  
**Severity:** High (vendor dialect drift vs operator CONTROL)  
**Component:** `casops.video_prompt.compile`, generator tags/profiles, Project Chat compile preview  
**Observed:** 2026-09-15  
**Operator statement:** Files `spec/*_operation_guide.md` are the video/image generation operating manuals. Learn from them. Configure related agents. Update every Project Chat to adopt them.  
**Related:** ISSUE-0009 (canonical clip + compile). ISSUE-0007 (Auto Pilot). ISSUE-0008 (Chat spine).  
**Honesty:** CHARACTERIZATION. Not an eval PASS. Not a production license. Dry-run default. Only Grok Imagine/Image are live. Other tags stay fail-closed (`request: {}`) even when a dialect **prompt** is shown for operator preview. `sample/` is read-only.

## Guides in scope

| File | Tag | Live today |
|---|---|---|
| `spec/grok_imagine_operation_guide.md` | `grok-imagine`, `grok-image` | yes (Dry-run off) |
| `spec/seedance_operation_guide.md` | `seedance` | no |
| `spec/ltx_operation_guide.md` | `ltx` | no |
| `spec/minimax_h3_operation_guide.md` | `hailuo` | no |
| `spec/gpt_image_operation_guide.md` | `gpt-image` (new declared tag) | no |

## House rules taken from the guides

1. **Parameters are not prompt words.** Duration, aspect, resolution, model, fps live in the control panel / `compiled.request`. Strip leaks from vendor prompt text.
2. **Front-load the subject** (Grok / Seedance / GPT Image). First 20–30 words are identity.
3. **I2V: still carries look; motion describes change only** (Grok §9, Seedance §13, LTX I2V). Do not rebuild the face in the motion prompt.
4. **One camera move per clip.** Stacking moves warps.
5. **Natural-language shot brief**, not tag soup (`8k`, `masterpiece`).
6. **Fail-closed engines may emit a dialect preview prompt** so the operator can read CONTROL. They must not emit a pretend vendor `request` or a 200 fake clip.
7. Citations are **design-time**. Skills declared, not live grants. No T3, network, plugins, memory writes.

## Work

- Grok compile: identity first; aspect/duration only in request fields; I2V motion uses hold-composition skeleton.
- Seedance / LTX / Hailuo / GPT Image: dialect `prompt.still` / `prompt.motion` for preview; `status: blocked`; `request: {}`.
- Add `gpt-image` generator tag + stub profile (still-only). Hailuo profile notes MiniMax H3.
- `compiled.guide` points at the operation-guide path.

**Exit:** Unit tests: Grok still does not lead with `9:16`; Seedance prompt preview non-empty and request empty; gpt-image fail-closed.
