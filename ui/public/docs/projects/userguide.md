# Project — user guide

When a Project is a Program child (ISSUE-0013), it is **one segment / one clip**. Program first-called stays `video.showrunner`. This Chat Auto Pilot still starts at `specials.intent-analysis-agent` then `video.promptengineer`, with the five human locks unchanged.

1. Open **Project** (above Agent Swarm). Fill name, brief, audience, duration, outlets, risk.
2. **Suggest sub-workflow** ranks templates A–J and scales S1–S7, then asks `video.planner` which to use. That choice is the *one* workflow for the project. CHARACTERIZATION, not an eval PASS.
3. Confirm. Uncheck **Dry-run** to write `project/<name>/`. The designer opens with only **Create Project**.
4. Each node lists **Out** buses (one per declared output). A node can Out to several next agents. Click an Out (or **Next all**): the parent suggests agents on that bus. Check one or more, then **Add next**.
5. If A already points at B and B’s Out names A, **Add next** draws a **loop** edge back to the existing A node. It does not clone A. Duplicate edges on the same Out are ignored. Save graph writes `project/<slug>/project.json`.
6. **Create Project** is high-level intent only (title + short brief). If you already knew every lock, you would write `asain-beauty-prompt.txt` yourself. **Launch** asks each domain expert to show **Think**, ranked **OPTION**s, **RECOMMEND**, and **DECIDE_BY** (human, parent agent, or a lower expert who should expand options). Click an option on the node to choose; that does not re-invent the gold file. The graph ends at **Output** (no Out). `sample/` is never copied.
7. Each saved project has **Workflow** and **Chat**. Chat lists every expert **suggestion** and the **selected** option. If an **agent** selected, Chat and the matching Workflow node show the **reason**. Tags jump to the linked block. The asain-beauty instance ships a CHARACTERIZATION walkthrough of that process (not live hops, not a copy of `sample/`).
8. Chat time order is collab hops, then **Generated video-generator instruction**, then **generated clip**. Configure aspect / duration / resolution / mode on the instruction box. Click **Grok Imagine** with Dry-run unchecked to submit; the host downloads the mp4 into `project/<slug>/output/` and embeds it in the clip bubble below the instruction. Other generator tags stay declared and fail-closed. `sample/` is never written.
