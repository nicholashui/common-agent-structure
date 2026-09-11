# Project — user guide

1. Open **Project** (above Agent Swarm). Fill name, brief, audience, duration, outlets, risk.
2. **Suggest sub-workflow** ranks templates A–J and scales S1–S7, then asks `video.planner` which to use. That choice is the *one* workflow for the project. CHARACTERIZATION, not an eval PASS.
3. Confirm. Uncheck **Dry-run** to write `project/<name>/`. The designer opens with only **Create Project**.
4. Each node lists **Out** buses (one per declared output). A node can Out to several next agents. Click an Out (or **Next all**): the parent suggests agents on that bus. Check one or more, then **Add next**. Save graph writes `project/<slug>/project.json`.
