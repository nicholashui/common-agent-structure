# Video pack corpus (standalone)

**Imported from:** va-agent-swarm (see `SOURCE_COMMIT.txt`, `SOURCE_URL.txt`)  
**Policy:** This tree is the **in-pack source of truth** for video domain design knowledge.  
`va-agent-swarm` is optional upstream only.

## Trees

| Path | Contents |
|------|----------|
| `study/` | Full va `study/` mirror (specs, agents, workflows, UI, 68 reference chapters) |
| `plan/` | Planner agent designs v2.0 / v2.1 |
| `root/` | Root-level starters, agent_loop creators, `inital_task*` |

## Key entrypoints

| Doc | Path |
|-----|------|
| Agent roster tables | `study/agents.md` |
| System map | `study/SYSTEM_REFERENCE.md` |
| AI production workflow | `study/ai_agent_video_production_workflow.md` |
| Human production workflow | `study/human_video_production_workflow.md` |
| Agent loop v3 | `study/agent_loop_v3.md` |
| Reference chapters (68) | `study/reference/how_to_build_a_video_agent_system/` |
| UI studies | `study/ui/` |
| Workflow SVGs A–J + LQR | `study/workflows/` |
| Planner v2.1 | `plan/planner_agent_v2.1.md` |

## For coding agents

1. Open `business/video/agents/<pack_id>/SPEC.md` first (self-contained).  
2. Then open files listed under **Related local documents**.  
3. Do **not** require `C:\Project\va-agent-swarm` to exist.  
4. Design-time “Tool Access” text is **not** an automatic runtime allow-list.

## Integrity

- `MANIFEST.json` — sha256 of every copied file  
- `COPY_LOG.jsonl` — per-file actions  
- Refresh: `python scripts/business/migrate_va_corpus.py --force`  
- Check: `python scripts/business/check_video_corpus_standalone.py`
