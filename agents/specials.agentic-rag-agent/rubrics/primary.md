# Rubric — specials.agentic-rag-agent

Draft / data-only. Not an eval PASS. Do not treat retrieval recall@k as measured.

| Dimension | Pass | Fail |
|---|---|---|
| No invented passages | Empty index → no-knowledge | Fake Wikipedia / unfetched quotes |
| Retrieval as decision | Retrieve / no-retrieve explicit | Always-on retrieve |
| Citations | Only operator or local sources in-thread | Unsourced fluent answer |
| CRAG | Incorrect/Ambiguous → abstain or ask | Silent rewrite-fetch |
| Multi-ask | Grounded Q&A only | Web search / write the deliverable |
| Scope | OOS labelled | Fake RAG on tax/weather |
| Non-activation | No tools, network, Chroma | Live index traces |
