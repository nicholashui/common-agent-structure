---
description: Self-RAG retrieve-decision procedure for specials.agentic-rag-agent. Omitted from Chat until host_permission AND operator_toggle resolve true. Adds no tools.
---

No live grant. Procedure (also packed in `prompts/primary.md`):

1. Query class. 2. Retrieve vs no-retrieve. 3. Grade IsRel/IsSup/IsUse on supplied text. 4. CRAG: answer, abstain, or ask — no fetch. 5. Cite only in-thread sources. 6. Empty index → no-knowledge. 7. Multi-ask: grounded Q&A only. 8. Refuse live index/tools/network.

This skill adds **no** tools. `allowed_tools` stays `[]`.
