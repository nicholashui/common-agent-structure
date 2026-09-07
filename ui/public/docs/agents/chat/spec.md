# Chat

Direct human text to the selected agent. The host packs identity plus the operational prompt under `runtime/context.json`. Adapter `host_llm` uses `LlmRouter.complete`. Adapter `grok_acp` is UI → `/api/v3` → one Grok Build ACP stdio process per agent_id (projected profile, empty tools/skills). Chat shows `GET /api/v3/agents/{id}/runtime/adapter` before send. Does not write memory, enable plugins, T3, or network.
