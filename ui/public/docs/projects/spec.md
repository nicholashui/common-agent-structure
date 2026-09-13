# Project

`Project` is a Control UI companion for **draft video sub-workflows**. It is not a live production grant.

- Create a named folder under repo `project/<slug>/`.
- Ask the host LLM (`video.planner` Chat) which `video.template.*` / `video.scale.*` to use.
- After confirm, save `project.json` and open a React Flow designer with **only** the Create Project start node. One project is one workflow.
- Each node has **Out** buses. The parent agent suggests the following agent from declared `critique_edges` (inputs/outputs). Clicking Next does not live-enable skills or tools.
- Cycles (A→B, B→A): one node per agent. A loop-back adds a dashed **loop** edge to the existing node; it does not spawn a second copy. Self-Out (A→A) is ignored. Duplicate Out edges are ignored.
- The first node is **Create Project** and holds the initial brief. It cannot be deleted.

Public plane: `GET/POST /api/v3/projects`, `POST /api/v3/projects/suggest`, `GET/PUT /api/v3/projects/{id}`, `POST /api/v3/projects/{id}/next`, `POST /api/v3/projects/{id}/run`, `GET/POST /api/v3/projects/{id}/comms`, `GET /api/v3/projects/{id}/output`, `GET /api/v3/projects/{id}/output/file`, `POST /api/v3/projects/{id}/generate`. `POST .../run` host-mediates Chat hops and assembles live English sections into `output/`. `POST .../generate` submits the assembled instruction to a declared engine (Grok Imagine is live; others fail-closed) and writes media under `output/` only. `GET .../output/file` serves that folder inline (basename only; `sample/` and `..` are rejected). It does not copy `sample/`. Mutations need actor, reason, expected-parent, dry-run. `dry-run: true` does not write and does not call Imagine. Agent runtime cannot create projects or generate. Tools, network, T3, memory writes, and production stay off.
