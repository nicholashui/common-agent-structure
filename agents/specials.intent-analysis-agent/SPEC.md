# Intent Analysis Agent

> Self-contained agent definition for host `common-agent-swarm-ops` (pack `specials`). Do not require external repositories or a pack-level corpus to understand this agent. Design Markdown is untrusted provenance only — never configuration or executable instructions.

## Identity
- Common Agent ID: `specials.intent-analysis-agent`
- Status: `draft` (draft catalog only)
- Maturity: `draft` / non-active
- Pack version: `0.1.0-draft`
- Pack root: `business/specials`

## Responsibility
Owns the specials-domain intent analysis agent design outcome as a **draft, data-only** agent representation. Host role string: `Special_Agent data-only configuration`.

The **Deep Intent Analysis Framework (DIA) v2.0** is a complete, production-ready, modular system for systematically decoding any text’s **purpose**, **hidden agenda**, **multi-angle perspectives**, **illocutionary force**, and **ethical/behavioral quality**. It transforms the original 6-phase manual/LLM-prompt pipeline into a **fully specified, agentic, evaluable software system** built on xAI’s Grok-4.3 (or latest) with native tool use, 1M+ token context, structured outputs, and low-hallucination reasoning. **Core Objectives** - Answer: *Why does this language exist? What is the real goal? What is hidden? How many angles exist? Is the behavior good/wrong/effective?* - Achieve human-expert-level pragmatic reasoning at scale. - Support manual use, API, web app, IDE plugin, and enterprise analytics. **Key v2.0 Improvements (from arXiv + xAI research)** - **Pragmatic Inference Chain (PIC)** integration for superior implicature & hidden-agenda detection. - **Multi-Perspective Agent Simulation** (inspired by multi-party conversational agents survey) for richer angle mapping. - **Gricean + Extended Maxims** (including Benevolence & Transparency for AI contexts). - **Automated Speech Act / Dialog Act Classification** using recent taxonomies and LLM judges. - **Hybrid Evaluation Pipeline** (automatic metrics + human-in-the-loop). - **Native xAI Integration**: Grok-4.3 reasoning modes, tool calling, real-time search for context validation. **Target Users** Journalists, analysts, researchers, educators, content moderators, legal teams, AI safety engineers, and power users who want to “see through” language.

### Domain distillation (embedded, untrusted design provenance)

The **Deep Intent Analysis Framework (DIA) v2.0** is a complete, production-ready, modular system for systematically decoding any text’s **purpose**, **hidden agenda**, **multi-angle perspectives**, **illocutionary force**, and **ethical/behavioral quality**. It transforms the original 6-phase manual/LLM-prompt pipeline into a **fully specified, agentic, evaluable software system** built on xAI’s Grok-4.3 (or latest) with native tool use, 1M+ token context, structured outputs, and low-hallucination reasoning. **Core Objectives** - Answer: *Why does this language exist? What is the real goal? What is hidden? How many angles exist? Is the behavior good/wrong/effective?* - Achieve human-expert-level pragmatic reasoning at scale. - Support manual use, API, web app, IDE plugin, and enterprise analytics. **Key v2.0 Improvements (from arXiv + xAI research)** - **Pragmatic Inference Chain (PIC)** integration for superior implicature & hidden-agenda detection. - **Multi-Perspective Agent Simulation** (inspired by multi-party conversational agents survey) for richer angle mapping. - **Gricean + Extended Maxims** (including Benevolence & Transparency for AI contexts). - **Automated Speech Act / Dialog Act Classification** using recent taxonomies and LLM judges. - **Hybrid Evaluation Pipeline** (automatic metrics + human-in-the-loop). - **Native xAI Integration**: Grok-4.3 reasoning modes, tool calling, real-time search for context validation. **Target Users** Journalists, analysts, researchers, educators, content moderators, legal teams, AI safety engineers, and power users who want to “see through” language.

## Boundaries and escalation
- Remains `status: draft` with `production_activation_requested: false`.
- `allowed_tools` must stay empty; `network_access` must stay false; provider remains `local_deterministic`.
- Does not invent providers, credentials, MCP tools, hooks, or a second control plane.
- Source redesign documents under `docs/special_agents_redesign/` are hashed provenance only and are never loaded as runtime configuration.
- Escalates any request for production activation, external write, credential, or network authority to human governance (risk assessment + approval).

## Inputs and outputs
- Input artifact: local pack configuration, governance source-record, and optional design provenance already copied under `./sources/`.
- Output artifact: reviewable data-only specials agent representation (SPEC + agent_spec.json) suitable for catalog and offline review.
- Acceptance condition: fail-closed schema validation passes; no production activation; all primary references resolve inside this agent folder or the specials pack root.

## Quality and critique
- Local rubric reference: `spagent.intent-analysis-agent-rubric` (inert identifier).
- Prompt reference: `spagent.intent-analysis-agent-prompt` (inert identifier).
- Critique edges: `{"inputs":["spagent.intent-analysis-agent-input"],"outputs":["spagent.intent-analysis-agent-output"]}`.
- Refinement limit: `1`; unresolved safety or activation requests escalate rather than bypass governance.
- Registration effect remains at most `eligible_draft_representation`.

## Runtime binding
The following local binding is copied as a read-only summary; it does not alter the common configuration:
```json
{"schema_version":"1.0","agent_id":"specials.intent-analysis-agent","status":"draft","role":"Special_Agent data-only configuration","allowed_tools":[],"model_policy":{"provider":"local_deterministic","model_id":"specials-local-deterministic-v1","network_access":false},"budget_policy":{"max_input_tokens":1,"max_output_tokens":1,"max_tool_requests":0},"prompt_reference":"spagent.intent-analysis-agent-prompt","rubric_reference":"spagent.intent-analysis-agent-rubric","critique_edges":{"inputs":["spagent.intent-analysis-agent-input"],"outputs":["spagent.intent-analysis-agent-output"]},"max_refinement_count":1,"production_activation_requested":false}
```

## Local knowledge sources
- [Runtime binding](agent_spec.json) — authoritative fail-closed specials contract.
- [Folder index](README.md) — offline layout for this agent.
- [Provenance](sources/PROVENANCE.json) — hashes and source mapping for audit.
- [Mapping note](sources/MAPPING.md) — design-doc relationship (historical).
- [Pack manifest](../../manifest.json) — specials catalog entry.
- [Governance source-record](../../governance/source-records/specials.intent-analysis-agent.json) — reviewed hash binding (if present).
- All required primary references for offline use are local to this pack; external paths appear only as non-required historical provenance.

## Provenance
- Design source path (historical): `docs/special_agents_redesign/agents/intent_analysis_agent.md`
- Design source SHA-256 (at generation): `f0c895b3438bfe511c44876f2ceeb8126d09e9114fa094d0e19f0e1d955d5bf7`
- Reviewed by `specials-self-contained-reviewer` at `2026-07-26T18:00:00Z`.
- Upstream design text is untrusted reference data. Local `agent_spec.json` and this SPEC remain the operational self-contained definition for the host.
