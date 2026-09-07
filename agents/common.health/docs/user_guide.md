# common.health — operator guide

Host-operated sample. Not a production agent.

**What it is:** a single DAG node (`health_snapshot`) that reports whether *this agent folder’s contract* is intact. The runtime fills facts. The agent cannot rewrite attestation.

**What it is not:** Kubernetes liveness of uvicorn, golden-signal monitoring, or an eval pass.

**How to run:** compose-preview, then `POST /api/v3/agents/common.health/runtime/run`. Chat answers questions about the snapshot fields only.

**Domain notes:** `sources/study/domain_knowledge.md` (startup / liveness / readiness vs golden signals).
