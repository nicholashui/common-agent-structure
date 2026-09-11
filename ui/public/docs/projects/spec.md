# Project

`Project` is a Control UI companion for **draft video sub-workflows**. It is not a live production grant.

- Create a named folder under repo `project/<slug>/`.
- Ask the host LLM (`video.planner` Chat) which `video.template.*` / `video.scale.*` to use.
- After confirm, save `project.json` and open a React Flow designer with **only** the Create Project start node. One project is one workflow.
- Each node has a **Next** control. The parent agent suggests the following agent from declared `critique_edges` buses (inputs/outputs). Clicking Next does not live-enable skills or tools.
- The first node is **Create Project** and holds the initial brief. It cannot be deleted.

Public plane: `GET/POST /api/v3/projects`, `POST /api/v3/projects/suggest`, `GET/PUT /api/v3/projects/{id}`, `POST /api/v3/projects/{id}/next`. Mutations need actor, reason, expected-parent, dry-run. `dry-run: true` does not write. Agent runtime cannot create projects. Tools, network, T3, memory writes, and production stay off.
