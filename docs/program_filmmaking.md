# Program filmmaking (ISSUE-0013)

CHARACTERIZATION. Not an eval PASS.

- First Program agent hop: `specials.intent-analysis-agent`
- Program first-called: `video.showrunner` (not `video.screenwriter`, not `video.promptengineer`)
- Screenwriter is W1 after logline lock
- Spawn child Projects only when `generation_list` **and** `visual_bible` are locked
- One segment = one Project
- Stills / storyboard before motion
- Picture lock before color / mix / final graphics
- Sequence concat is post; `fused_request` is always null
- Child Auto Pilot hop order and five human locks unchanged (ISSUE-0007)
- P3: cannot lock `generation_list` if any scene has zero segments
- P4: `program/<code>/bible/`, `assets/approved/` still slots, `storyboard/<segment>.md` (Dry-run writes nothing; fail-closed still tags are not success)
- P5: spawn Start.inherit bible/board refs; no gold-body probes
- P6: chain inspect rejects a failed end frame (refresh from bible still)
- P7: cut_state assembly → rough → fine → picture_lock; concat missing tool is blocked
- P8: `program/<code>/delivery/` specifications + a11y + captions + archive-plan; no live upload; trailer is not a silent spawn
