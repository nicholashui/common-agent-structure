# Files

Companion plane for the sixteen on-disk agent configuration folders: corrigibility, docs, evals, identity, improvement, inheritance, memory, observability, plugins, prompts, protocols, rubrics, runtime, safety, skills, sources.

`GET /api/v3/agents/{id}/files` lists them. `GET`/`PUT /files/item?path=` reads or writes one confined relative path. PUT requires mutation headers. Host-owned corrigibility and generated locks are not writable. Path escape is rejected.
