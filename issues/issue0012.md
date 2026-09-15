# ISSUE-0012 — Project Chat adopts operation-guide SOP

**Status:** Implemented (CHARACTERIZATION). Project Chat shows still/motion compile preview and SOP note.  
**Severity:** High (operator CONTROL view)  
**Component:** `/projects/:id/chat` generator panel  
**Related:** ISSUE-0010, ISSUE-0011, ISSUE-0009 P5.  
**Honesty:** CHARACTERIZATION. Imagine is not called automatically. Dry-run off still required for a take.

## Work

- Show compiled **still** and **motion** (Grok I2V split) from `output.compiled.prompt`.
- SOP note: still carries identity/light; motion describes change only; duration/aspect live in the engine/mode controls — not in T4 as vendor syntax.
- Show `compiled.guide` (operation-guide filename) when present.
- Fail-closed engines still show dialect preview text; clicking the tag does not invent a successful clip.
- Unique T4 source blocks stay unique (Hair ≠ Subject).
- All characterization projects (`asain-beauty`, `european-handsome`, `japanese-grandma-gta`, `hongkong-grandma-gta`) use the same panel.

**Exit:** Browser desktop + mobile: still/motion previews visible; hop counts unchanged; Dry-run generate still gated.
