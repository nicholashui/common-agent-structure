# Program — user guide

A **Program** is the film. A **Project** is one generated segment (one clip). The host orchestrates. CHARACTERIZATION, not an eval PASS.

## New program

1. Open **Program** (above Project). First item is **New program**.
2. Fill **Program Code** (lowercase English, no spaces) and **Program Name** only.
3. Dry-run is default. Uncheck Dry-run to write `program/<code>/`.

## Filmmaking order (ISSUE-0013)

```text
W0 Development   intent-analysis → creative-agent → video.showrunner   LOCK logline
W1 Literary      video.screenwriter (treatment → screenplay)           LOCK pages
W2 Pre-prod      generation list + visual bible + storyboard           LOCK list + bible
W3 Spawn         host: one Project per segment
W4 Production    child Auto Pilot (intent-analysis → PE + five locks)
W5 Post / NLE    editor cut → picture lock → then color/mix/graphics
W6 Delivery      captions / archive plan — no live upload
```

- First **agent hop** is `specials.intent-analysis-agent`.
- Program **first-called** is `video.showrunner`, not `video.screenwriter` and not `video.promptengineer`.
- Spawn stays disabled until **generation_list** and **visual_bible** are locked.
- One scene may have many segments. One segment = one child Project.
- Stills and storyboard before motion.
- Picture lock before color, mix, or final graphics.
- Sequence concat is post. `fused_request` stays null.
- Child Project Chat hop order and the five human locks are unchanged (ISSUE-0007).
- Paths on this page are repo-relative (`program/<code>/…`). `sample/` is never written.
