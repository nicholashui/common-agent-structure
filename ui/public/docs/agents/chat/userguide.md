# Using Chat

Type a message and Send. Requires a healthy live host and no containment. Dry-run still executes the chat path. Each agent keeps its own chat history across reloads. Transcripts are appended to timestamped files under `logs/chat/<agent_id>/`. Clear starts a new conversation file and does not delete saved transcripts.

The composer shows adapter kind, grok availability, and profile readiness before Send. Settings → Chat adapter: `host_llm` (in-process) or `grok_acp` (one Grok Build ACP process per agent). Run model nodes use the same adapter. CLI: `python tools/grok_agent.py chat <agent_id>` uses the same projected profile. `workshop` edits the folder and must not rewrite `corrigibility/`.
