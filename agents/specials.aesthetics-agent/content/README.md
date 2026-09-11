# Operator content — `specials.aesthetics-agent`

This folder is **operator study**. The host still loads `prompts/primary.md`, `sources/study/domain_knowledge.md`, `evals/fixtures/*.json`, and `agent_spec.json`.

Skill `casops.skill.aesthetics.dimension-vector` is **declared** and **not host-granted**. Tools, network, plugins, memory writes, and production stay off. Live vision stays off.

```
content/
  README.md
  research/sources.md
  tests/chat/               # aesthetic brief edges (paste into Chat)
  tests/api/                # /api/v3 samples
  tests/multi-agent/        # name-only bus paste-in
  test_guide.md
```

Host-loadable copies of the edge chat cases: `evals/fixtures/chat-aes-*.json`. API samples stay here (`path` enum is only `chat` | `run`).
