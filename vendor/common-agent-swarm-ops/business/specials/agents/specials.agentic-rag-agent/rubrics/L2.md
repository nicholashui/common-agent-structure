# Agentic RAG L2 rubric (offline Host foundation)

Pass when offline `/api/v1/rag/query` produces:

| Check | Gate |
|-------|------|
| Trace present | analyzer + researcher + critic nodes |
| Plan present | non-empty plan steps |
| Patterns listed | includes Planning and Tool Use |
| Citations | ≥1 when graded docs kept |
| Fail-closed | live_web / chroma / lightrag flags denied |
| Max iterations | ≤3 |

Fail / escalate:

- confidence < 0.25 with no graded docs
- critic faithfulness fail after max iterations
- any live flag requested

Production targets (faithfulness ≥0.92, LightRAG hybrid, 65k ingest) are **not** enforced in offline stub mode.
