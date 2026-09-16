# Program — spec notes

Companion `/api/v3/programs*` (not spec §19). Schema `casops.program.v1`.

- `first_called`: `video.showrunner`
- `first_agent_hop`: `specials.intent-analysis-agent`
- `phase`: `w0`…`w6`
- `locks`: logline, pages, generation_list, visual_bible, storyboard, picture, delivery
- Spawn `POST .../spawn` fails unless `generation_list` and `visual_bible` are true
- Finish `POST .../finish` with color/mix/graphics/sound fails unless `picture` is true
- `GET .../sequence` always has `fused_request: null` and `concat: post`
- Dry-run default. Honesty CHARACTERIZATION. `allowed_tools: []`. No production activation.
