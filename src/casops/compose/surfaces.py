"""Legal inherited surfaces (spec §6.4). Unknown surfaces fail closed."""

from __future__ import annotations

LEGAL_INHERITED_SURFACES: frozenset[str] = frozenset(
    {
        "responsibility_fragments",
        "knowledge_sources",
        "quality_criteria",
        "prompt_refs",
        "rubric_refs",
        "skill_bindings",
        "critique_edges",
        "architecture_pattern",
        "persona_defaults",
        "runtime_hints",
        "context_hints",
        "protocol_preferences",
        "plugin_requirements",
        "memory_schema_refs",
        "evaluation_dimensions",
        "verifier_refs",
        "regression_fixtures",
        "safety_fixtures",
        "failure_taxonomy",
        "observability_labels",
        "docs",
    }
)
