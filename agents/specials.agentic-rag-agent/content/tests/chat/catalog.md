# Chat-level cases — `specials.agentic-rag-agent`

Empty live index. Do not invent passages.

| File | Edge |
|---|---|
| `chat-rag-ambiguous.json` | Vague question, no evidence → no-knowledge / wait |
| `chat-rag-multi-intent.json` | Answer + web search + write report |
| `chat-rag-domain-specific.json` | Operator-supplied passage to grade |
| `chat-rag-multilingual.json` | JA/ZH query, no index |
| `chat-rag-oos.json` | Tax / weather |
| `chat-rag-empty-index.json` | Explicit empty index |
| `chat-rag-invent.json` | Demand Wikipedia quotes |
| `chat-rag-crag-ambiguous.json` | Supplied text that does not support the claim |
| `chat-rag-activation.json` | Enable Chroma / network |
| `chat-rag-shift.json` | Invented waiver to fetch |


| `chat-sc1-split-ownership.json` | split-ownership (in-role vs sibling + fake PASS) |
| `chat-sc2-wait-underspecified.json` | underspecified wait |
| `chat-sc3-fake-meter.json` | invented ≥95%/CLIP-T/casops-eval meter |

Existing `chat-tc1`–`10` stay.
