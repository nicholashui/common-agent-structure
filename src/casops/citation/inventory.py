"""Spec §25 reference inventory. Identifiers are as written in v3a; live titles are filled by the auditor."""

from __future__ import annotations

from typing import Any

# marker, reference_id, expected_title, resolved_identifier, evidence_grade, numeric_claims
Reference = dict[str, Any]


def _ref(
    reference_id: str,
    marker: str,
    title: str,
    identifier: str,
    *,
    grade: str,
    claims: tuple[str, ...] = (),
    kind: str = "arxiv",
) -> Reference:
    return {
        "reference_id": reference_id,
        "marker_before": marker,
        "expected_title": title,
        "resolved_identifier": identifier,
        "evidence_grade": grade,
        "numeric_claims": list(claims),
        "kind": kind,
    }


def spec_references() -> list[Reference]:
    """Every [D], [C], and [K] entry from common_agent_structure.md §25."""
    return [
        # §25.1 [D]
        _ref("ref-001", "D", "Learning Agent Execution for KV-Cache Management in Agentic Serving", "arXiv:2608.14624", grade="E3"),
        _ref("ref-002", "D", "A Policy-Driven Runtime Layer for Agentic LLM Serving", "arXiv:2605.27744", grade="E3"),
        _ref("ref-003", "D", "Workload-Aware Caching for Multi-Agent Systems", "arXiv:2607.20495", grade="E3"),
        _ref("ref-004", "D", "A Survey on Memory Mechanisms in the Era of LLMs", "arXiv:2504.15965", grade="E2"),
        _ref("ref-005", "D", "Memory in the Age of AI Agents", "arXiv:2512.13564", grade="E2"),
        _ref("ref-006", "D", "A Survey of Agent Memory in the Second Half", "arXiv:2602.06052", grade="E3"),
        _ref("ref-007", "D", "Agent Memory: Mechanisms, Evaluation, and Emerging Frontiers", "arXiv:2603.07670", grade="E3"),
        _ref("ref-008", "D", "Agent Memory Evaluation: Taxonomy and Empirical Analysis of Evaluation and System Limitations", "arXiv:2602.19320", grade="E3"),
        _ref("ref-009", "D", "A Survey on the Security of Long-Term Memory in LLM Agents", "arXiv:2604.16548", grade="E3"),
        _ref("ref-010", "D", "A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve", "arXiv:2507.21046", grade="E2"),
        _ref("ref-011", "D", "A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm Bridging Foundation Models", "arXiv:2508.07407", grade="E3"),
        _ref("ref-012", "D", "Semantic Conventions for Generative AI", "https://opentelemetry.io/docs/specs/semconv/gen-ai/", grade="E2", kind="url"),
        _ref("ref-013", "D", "Inside the LLM Call: GenAI Observability with OpenTelemetry", "https://opentelemetry.io/blog/2026/genai-observability/", grade="E3", kind="url"),
        _ref("ref-014", "D", "How Jaeger is evolving to trace AI agents with OpenTelemetry", "https://www.cncf.io/blog/2026/05/26/how-jaeger-is-evolving-to-trace-ai-agents-with-opentelemetry/", grade="E3", kind="url"),
        _ref("ref-015", "D", "Model Context Protocol Versioning and Compatibility", "https://modelcontextprotocol.io/specification/versioning", grade="E2", kind="url"),
        # §25.2 [C]
        _ref("ref-016", "C", "Efficient Memory Management for Large Language Model Serving with PagedAttention", "arXiv:2309.06180", grade="E1"),
        _ref("ref-017", "C", "SGLang: Efficient Execution of Structured Language Model Programs", "arXiv:2312.07104", grade="E1"),
        _ref("ref-018", "C", "An LLM Compiler for Parallel Function Calling", "arXiv:2312.04511", grade="E2"),
        _ref("ref-019", "C", "RouteLLM: Learning to Route LLMs with Preference Data", "arXiv:2406.18665", grade="E2"),
        _ref("ref-020", "C", "AFlow: Automating Agentic Workflow Generation", "arXiv:2410.10762", grade="E2"),
        _ref("ref-021", "C", "Automated Design of Agentic Systems", "arXiv:2408.08435", grade="E2"),
        _ref("ref-022", "C", "EAGLE-3: Scaling up Inference Acceleration of Large Language Models", "arXiv:2503.01840", grade="E3"),
        _ref("ref-023", "C", "Agentic test-time compute system analysis", "knowledge:agentic-ttc", grade="E3", kind="knowledge"),
        _ref("ref-024", "C", "HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models", "arXiv:2405.14831", grade="E2"),
        _ref("ref-025", "C", "From RAG to Memory: Non-Parametric Continual Learning for Large Language Models", "arXiv:2502.14802", grade="E2"),
        _ref("ref-026", "C", "LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory", "arXiv:2410.10813", grade="E2"),
        _ref("ref-027", "C", "Evaluating Very Long-Term Conversational Memory of LLM Agents", "arXiv:2402.17753", grade="E2"),
        _ref("ref-028", "C", "A-MEM: Agentic Memory for LLM Agents", "arXiv:2502.12110", grade="E3"),
        _ref("ref-029", "C", "MIRIX: Multi-Agent Memory System for LLM-Based Agents", "arXiv:2507.07957", grade="E3"),
        _ref("ref-030", "C", "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory", "arXiv:2504.19413", grade="E3"),
        _ref("ref-031", "C", "MemoryAgentBench", "knowledge:memory-agent-bench", grade="E3", kind="knowledge"),
        _ref("ref-032", "C", "Mem2ActBench", "knowledge:mem2act-bench", grade="E3", kind="knowledge"),
        _ref("ref-033", "C", "MemGAS", "knowledge:memgas", grade="E3", kind="knowledge"),
        _ref("ref-034", "C", "Self-Refine: Iterative Refinement with Self-Feedback", "arXiv:2303.17651", grade="E1"),
        _ref("ref-035", "C", "Reflexion: Language Agents with Verbal Reinforcement Learning", "arXiv:2303.11366", grade="E1"),
        _ref("ref-036", "C", "Voyager: An Open-Ended Embodied Agent with Large Language Models", "arXiv:2305.16291", grade="E2"),
        _ref("ref-037", "C", "Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution", "arXiv:2309.16797", grade="E2"),
        _ref("ref-038", "C", "Agent Lightning: Train ANY AI Agent with Reinforcement Learning", "arXiv:2508.03680", grade="E3"),
        _ref("ref-039", "C", "Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents", "arXiv:2505.22954", grade="E3"),
        _ref("ref-040", "C", "A Self-Improving Coding Agent", "arXiv:2504.15228", grade="E3"),
        _ref("ref-041", "C", "Self-Adapting Language Models", "arXiv:2506.10943", grade="E3"),
        _ref("ref-042", "C", "W3C Trace Context", "https://www.w3.org/TR/trace-context/", grade="E1", kind="url"),
        _ref("ref-043", "C", "CloudEvents Specification", "https://github.com/cloudevents/spec", grade="E1", kind="url"),
        _ref("ref-044", "C", "Agent2Agent (A2A) Protocol", "https://github.com/a2aproject/A2A", grade="E2", kind="url"),
        _ref("ref-045", "C", "Language Models Don't Always Say What They Think", "arXiv:2305.04388", grade="E1"),
        _ref("ref-046", "C", "Measuring Faithfulness in Chain-of-Thought Reasoning", "arXiv:2307.13702", grade="E1"),
        _ref("ref-047", "C", "ToolSandbox: A Stateful, Conversational, Interactive Evaluation Benchmark", "arXiv:2408.04682", grade="E2"),
        _ref("ref-048", "C", "GAIA: a benchmark for General AI Assistants", "arXiv:2311.12983", grade="E1"),
        _ref("ref-049", "C", "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?", "arXiv:2310.06770", grade="E1"),
        _ref("ref-050", "C", "Berkeley Function Calling Leaderboard", "https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html", grade="E2", kind="url"),
        # withdrawn numeric claim — independent restore candidate only
        _ref(
            "ref-051",
            "C",
            "Agent Lightning v1.0: Towards Harnessed Agentic RL",
            "arXiv:2608.17528",
            grade="E3",
            claims=("SWE-bench Verified 41.8% to 56.4%",),
        ),
        # §25.3 [K] resolved to live identifiers where possible
        _ref("ref-052", "K", "MemGPT: Towards LLMs as Operating Systems", "arXiv:2310.08560", grade="E2"),
        _ref("ref-053", "K", "Memory operating-system architectures", "knowledge:memory-os", grade="E4", kind="knowledge"),
        _ref("ref-054", "K", "Zep: A Temporal Knowledge Graph Architecture for Agent Memory", "arXiv:2501.13956", grade="E3"),
        _ref("ref-055", "K", "Sleep-time Compute: Beyond Inference Scaling at Test-time", "arXiv:2504.13171", grade="E3"),
        _ref("ref-056", "K", "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models", "arXiv:2510.04618", grade="E3"),
        _ref("ref-057", "K", "GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning", "arXiv:2507.19457", grade="E3"),
        _ref("ref-058", "K", "AgentDojo: A Dynamic Environment to Evaluate Attacks and Defenses for LLM Agents", "arXiv:2406.13352", grade="E2"),
        _ref("ref-059", "K", "InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated LLM Agents", "arXiv:2403.02691", grade="E2"),
        _ref("ref-060", "K", "AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases", "arXiv:2407.12784", grade="E2"),
        _ref("ref-061", "K", "Why Do Multi-Agent LLM Systems Fail?", "arXiv:2503.13657", grade="E3"),
        _ref("ref-062", "K", "Defeating Nondeterminism in LLM Inference", "https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/", grade="E3", kind="url"),
        _ref("ref-063", "K", "How Many Megatokens Is Too Many? Measuring Long-Context Degradation", "knowledge:context-rot", grade="E3", kind="knowledge"),
        _ref("ref-064", "K", "Capability-based security and object-capability sandboxing", "knowledge:object-capability", grade="E1", kind="knowledge"),
    ]
