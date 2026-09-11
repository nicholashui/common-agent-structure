# Rate-limit characterization (do not invent 429)

CASOPS control plane (`:18080`) has **no** HTTP 429 handler for Chat or Run. Bursting `POST /api/v3/agents/specials.intent-analysis-agent/runtime/chat` is expected to return a mix of 200 (valid body + mutation headers) and 4xx/409 (policy), **not** 429.

xAI documents per-model RPM/TPM (example: Grok 4 at https://docs.x.ai/developers/models/grok-4). Those limits apply to **api.x.ai**, not this host. If a reverse proxy in front of CASOPS returns 429, record it as **gateway** behaviour.

## Procedure

1. Send 20 valid Chat POSTs from `01-valid-chat.json` in a tight loop.
2. Record status codes.
3. Pass if: zero invented 429 from the Python app; fail-closed fields still empty (`memory_writes`, plugins, T3).
4. Fail if the operator writes “rate limit PASS” because xAI’s 500 RPM number was copied into this pack.

This is characterization of **host behaviour**, not a load test of Grok.
