# Domain knowledge — `specials.agentic-rag-agent`

Design-time study (2026-09). Draft / data-only. No tools, network, plugins, memory writes, or production activation.

## RAG is parametric + non-parametric memory

Lewis et al. (arXiv:2005.11401, NeurIPS 2020) define RAG as a seq2seq *parametric* model plus a dense index *non-parametric* memory. Always-on retrieve-then-generate still hallucinates when the index is wrong or when the model ignores the passages.

## When retrieval should happen

**Self-RAG** (Asai et al., arXiv:2310.11511) trains reflection tokens: Retrieve / IsRel / IsSup / IsUse. The model decides *whether* to retrieve, then critiques relevance, support, and usefulness. That is the core of “agentic” RAG: retrieval is a *decision*, not a default.

**CRAG** (Yan et al., arXiv:2401.15884) classifies retrieved knowledge as Correct / Incorrect / Ambiguous and triggers correct / rewrite / fallback. Combining Self-RAG’s critic with CRAG’s corrective actions (Self-CRAG in that paper) is the usual 2024–2026 stack.

## Honesty on this host

- Do not invent retrieved passages. This folder has no live retriever (`network_access: false`, `allowed_tools: []`).
- If the operator did not supply evidence, say the index is empty rather than simulating Wikipedia.
- Citations must point at operator-provided or local `sources/` text. Unsourced fluent answers are a RAG failure, not a feature.

## Sources

- Lewis et al., RAG, arXiv:2005.11401
- Asai et al., Self-RAG, arXiv:2310.11511
- Yan et al., CRAG, arXiv:2401.15884
