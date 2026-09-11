---
description: Speech-act labelling procedure for specials.intent-analysis-agent. Omitted from Chat until host_permission AND operator_toggle resolve true. Adds no tools.
---

No live grant. `resolved_enabled` is false until the host register lists this skill_id and the operator toggle is ON.

Procedure (also packed in `prompts/primary.md` How to reply, which does not require this file):

1. Locution — what was said (keep source-language wording).
2. Illocution — Searle class plus specific act; list each intent.
3. Implicature — Grice; a maxim flout is not deception.
4. Triggerability — understood vs action-ready; wait if incomplete.
5. Scope — in-scope vs OOS; do not force a class.
6. Hidden agenda — evidence only, else `none evidenced`.
7. Next agent — name a handoff; do not absorb peer craft.
8. Refuse — tools, network, production, invented quotes, writing the deliverable.

This skill adds **no** tools. FR-SKL-005: enabling cannot add tools outside child and host grants (`allowed_tools` is `[]`).
