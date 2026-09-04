# ISSUE-0004 — Relocate-safe paths and self-contained external sources

**Status:** Implemented 2026-09-04  
**Severity:** High (repo cannot move; generators and tests die without sibling folders)  
**Component:** tools, tests, agent provenance JSON, user_guide, vendor copies  
**Asked:** 2026-09-04 — this project might relocate. (1) Stop hardcoding `C:\Project\common-agent-structure`; use relative paths. (2) Do not file-link external trees such as `C:\Project\common-agent-swarm-ops`; copy what this host needs into the repo so it is self-contained.

**Related:** ISSUE-0003 (characterization fixtures). Fixtures stay CHARACTERIZATION / not an eval pass.

---

## Problem

1. **This repo’s own root was hardcoded.** Operator docs and some generated book text used `C:\Project\common-agent-structure`. Moving the folder (or cloning elsewhere) makes those instructions false. Runtime already used `Path(__file__)` / `CASOPS_AGENTS_ROOT`; the defect was configuration, generators, and recorded provenance.

2. **External sources were linked by absolute path, not copied.** Live tools and tests pointed at sibling trees:

| Consumer | Hardcoded path |
|---|---|
| `tools/import_agent_testcases.py` | `C:\Project\common-agent-swarm-ops\testcases\api_test` |
| `tools/import_video_agents.py` | `C:\Project\common-agent-swarm-ops\business\video\agents` |
| `tools/import_specials_agents.py` | `C:\Project\common-agent-swarm-ops\business\specials\agents` |
| `tests/contract/test_video_agents_import.py` | same video agents path |
| `tests/contract/test_specials_agents_import.py` | same specials agents path |
| `evals/fixtures/provenance.json` and chat-tc `source.file` | absolute swarm-ops + this-repo paths |
| `identity/background.json` `source_folder` | absolute swarm-ops path |
| `sources/PROVENANCE.json` `imported_from` | absolute swarm-ops path |

Those are **path references**, not junctions. After relocate (or without the sibling checkout) import/regenerate/tests cannot find the source. The host must not require `C:\Project\...` to exist.

`va-agent-swarm` was not read by Python tools, but agent user guides listed `C:\Project\va-agent-swarm` as a corpus root. That is the same class of defect.

Media (`.mp3` etc.) in the swarm-ops source trees is **not** imported (`SKIP_SUFFIXES` already). Copying multi-GB audio is out of scope; text/json/md/svg used by import is in scope.

---

## Decision

- **Relative to repo root** for every tool default, test source, and recorded provenance field. Resolve with `Path(__file__)` / `REPO`, never `C:\Project\common-agent-structure`.
- **Copy, do not link.** Byte copies live under `vendor/`. No junctions, no git submodules, no runtime read of sibling repos.
- **Do not re-import agent folders** with `import_video_agents.py` (it `rmtree`s dest and would wipe ISSUE-0003 fixtures). Rewrite path strings in place; re-run only `import_agent_testcases.py` against the vendor copy.
- Honesty unchanged: CHARACTERIZATION fixtures, `casops-eval` `NOT_RUN`. Do not invent `va_category`. Do not enable production / T3 / network / plugins / memory writes.

---

## What landed (2026-09-04)

- `vendor/common-agent-swarm-ops/` — copies of `testcases/api_test`, `business/video/agents`, `business/specials/agents`, and `docs/special_agents_redesign` (media suffixes skipped).
- `vendor/va-agent-swarm/` — copy of the design corpus previously cited by user guides.
- `vendor/README.md` + `vendor/MANIFEST.json` — copies, not links.
- `tools/vendor_external_sources.py` — re-copy helper (reads sibling trees only when present; dest is always `vendor/`).
- `tools/reloc.py` — `repo_posix()` for recorded paths.
- Importers/tests default to `REPO / "vendor" / ...`.
- Provenance / `source.file` / `source_folder` / `imported_from` rewritten to repo-relative POSIX paths.
- `user_guide.v1.md` and book generator install snippets use “repo root” + `scripts\start_all.ps1`, not `C:\Project\...`.
- Contract test: runtime/config trees must not contain `C:\Project\`.

Re-copy (only if a sibling tree still exists on the machine):

```powershell
python tools/vendor_external_sources.py
```

Regenerate characterization fixtures from the **local** copy:

```powershell
python tools/import_agent_testcases.py
```
