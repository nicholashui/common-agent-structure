# GET characterization fixtures

```
GET /api/v3/agents/specials.intent-analysis-agent/evals/fixtures
```

No mutation headers (GET). Expect 200 JSON:

- `honesty`: `CHARACTERIZATION`
- `note` mentions CHARACTERIZATION or NOT_RUN
- `fixtures` includes `chat-tc1` … `chat-tc10`, `run-tc1`, and `chat-nlu-*`
- no top-level `pass` field
- each listed chat fixture `expect.network_granted` is false; `memory_writes` is `[]`

This endpoint **lists** cases. It does not score them. casops-eval stays NOT_RUN.
