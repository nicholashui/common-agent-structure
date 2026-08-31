"""Create agents/_template_v3 for baseline_safe (spec §5.2)."""

from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / "agents" / "_template_v3"


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    write_text(
        ROOT / "README.md",
        "# casops.template.baseline_safe\n\n"
        "Reference v3 agent folder for the `baseline_safe` profile.\n"
        "Deterministic adapter, T0 cache, no persistent memory, no plugins, improvement disabled.\n",
    )
    write_text(
        ROOT / "SPEC.md",
        "# Template baseline_safe agent\n\n"
        "Mission: exercise host compose and run with mandatory safety, "
        "corrigibility, and audit controls only.\n",
    )
    dump(
        ROOT / "agent_spec.json",
        {
            "schema_version": "3.0",
            "structure_id": "casops.common_agent.v3",
            "agent_id": "casops.template.baseline_safe",
            "status": "registered",
            "role": "BaselineSafeTemplate",
            "allowed_tools": [],
            "allowed_plugins": [],
            "model_policy": {
                "provider": "local_deterministic",
                "model_id": "local-deterministic-v1",
                "network_access": False,
                "routing_allowed": False,
            },
            "budget_policy": {
                "max_input_tokens": 2048,
                "max_output_tokens": 512,
                "max_model_calls": 2,
                "max_tool_requests": 0,
                "max_job_ms": 15000,
                "max_cost_units": 1.0,
                "max_peer_hops": 0,
            },
            "prompt_reference": "prompts/primary.md",
            "rubric_reference": "rubrics/primary.md",
            "critique_edges": {"inputs": [], "outputs": []},
            "max_refinement_count": 0,
            "production_activation_requested": False,
            "does_not_own": [
                "Credentials",
                "Silent production activation",
                "Another agent's exclusive craft output without handoff",
                "Automatic promotion of self-generated artifacts",
                "Modification of safety, telemetry, gates, permissions, or corrigibility",
                "Self-granting tools, plugins, network, or isolation downgrades",
            ],
            "inheritance_ref": "inheritance/parents.json",
            "identity_ref": "identity/",
            "skills_ref": "skills/bindings.json",
            "toggles_ref": "skills/toggles.json",
            "runtime_ref": "runtime/execution.json",
            "context_ref": "runtime/context.json",
            "compute_controller_ref": "runtime/compute_controller.json",
            "backends_ref": "runtime/backends.json",
            "cache_ref": "runtime/cache.json",
            "protocols_ref": "protocols/compatibility.json",
            "capability_assertions_ref": "protocols/capability_assertions.json",
            "observability_ref": "observability/telemetry.json",
            "sampling_ref": "observability/sampling.json",
            "plugins_ref": "plugins/registry.json",
            "isolation_ref": "plugins/isolation.json",
            "memory_ref": "memory/policy.json",
            "memory_hierarchy_ref": "memory/hierarchy.json",
            "memory_security_ref": "memory/security.json",
            "improvement_ref": "improvement/policy.json",
            "verifiers_ref": "improvement/verifiers.json",
            "safety_ref": "safety/policy.json",
            "termination_ref": "safety/termination.json",
            "corrigibility_ref": "corrigibility/invariants.json",
            "evals_ref": "evals/benchmarks.json",
            "analysis_plan_ref": "evals/analysis_plan.json",
        },
    )
    write_text(ROOT / "prompts" / "primary.md", "You are a deterministic baseline-safe agent.\n")
    write_text(ROOT / "rubrics" / "primary.md", "Success: produce a bounded, schema-valid reply.\n")
    dump(
        ROOT / "sources" / "PROVENANCE.json",
        {
            "schema_version": "3.0",
            "sources": [],
            "note": "Template has no external sources.",
        },
    )
    write_text(ROOT / "sources" / "MAPPING.md", "No external source mapping.\n")
    write_text(ROOT / "sources" / "excerpts" / ".gitkeep", "")
    write_text(ROOT / "docs" / "user_guide.md", "Host-operated template. Not a production agent.\n")
    dump(ROOT / "inheritance" / "parents.json", {"parents": []})
    dump(ROOT / "inheritance" / "conflicts.json", {"conflicts": []})
    write_text(ROOT / "skills" / "SKILL.md", "No skills enabled.\n")
    dump(ROOT / "skills" / "bindings.json", {"bindings": []})
    dump(ROOT / "skills" / "integration.json", {"integrations": []})
    dump(ROOT / "skills" / "toggles.json", {"toggles": []})
    dump(
        ROOT / "identity" / "persona.json",
        {"mode": "grounded", "voice": "neutral", "languages": ["en"]},
    )
    dump(
        ROOT / "identity" / "background.json",
        {"title": "template", "domain": "casops", "fictional": True},
    )
    dump(
        ROOT / "runtime" / "execution.json",
        {
            "schema_version": "3.0",
            "ir": "casops.execution_dag.v2",
            "entry": "model",
            "nodes": [
                {
                    "node_id": "model_1",
                    "kind": "model",
                    "dependencies": [],
                    "side_effect_class": "none",
                    "idempotent": True,
                    "timeout_ms": 5000,
                }
            ],
        },
    )
    dump(
        ROOT / "runtime" / "backends.json",
        {
            "schema_version": "3.0",
            "adapters": [
                {
                    "id": "local_deterministic",
                    "kind": "model",
                    "provider": "local_deterministic",
                    "network_access": False,
                }
            ],
        },
    )
    dump(
        ROOT / "runtime" / "routing.json",
        {"schema_version": "3.0", "mode": "fixed", "route": "local_deterministic"},
    )
    dump(
        ROOT / "runtime" / "cache.json",
        {
            "schema_version": "3.0",
            "enabled": True,
            "tiers": ["T0"],
            "t3_enabled": False,
        },
    )
    dump(
        ROOT / "runtime" / "context.json",
        {
            "schema_version": "3.0",
            "segments": {
                "policy": 512,
                "task": 768,
                "memory": 0,
                "tools": 0,
                "evidence": 256,
                "output": 512,
            },
            "compaction": "disabled",
        },
    )
    dump(
        ROOT / "runtime" / "compute_controller.json",
        {
            "schema_version": "3.0",
            "agent_id": "casops.template.baseline_safe",
            "mode": "fixed",
            "allocation": {
                "min_model_calls": 1,
                "max_model_calls": 2,
                "max_refinements": 0,
                "max_parallel_samples": 1,
            },
        },
    )
    dump(
        ROOT / "protocols" / "compatibility.json",
        {"schema_version": "3.0", "protocols": []},
    )
    dump(
        ROOT / "protocols" / "capability_assertions.json",
        {"schema_version": "3.0", "assertions": []},
    )
    write_text(ROOT / "protocols" / "conformance" / ".gitkeep", "")
    dump(
        ROOT / "protocols" / "schemas" / "agent_message.schema.json",
        {"type": "object"},
    )
    dump(ROOT / "protocols" / "schemas" / "event.schema.json", {"type": "object"})
    dump(
        ROOT / "observability" / "telemetry.json",
        {
            "schema_version": "3.0",
            "exporter": "otlp",
            "schema_url": "https://casops.local/semconv/1.0.0",
            "content_capture": "metadata_only",
        },
    )
    dump(
        ROOT / "observability" / "redaction.json",
        {"schema_version": "3.0", "mode": "metadata_only", "secret_classes": ["credential", "pii"]},
    )
    dump(ROOT / "observability" / "slo.json", {"schema_version": "3.0", "slos": []})
    dump(
        ROOT / "observability" / "decision_record.schema.json",
        {
            "type": "object",
            "required": ["inputs", "actions", "constraints", "codes", "outcomes"],
        },
    )
    dump(
        ROOT / "observability" / "sampling.json",
        {"schema_version": "3.0", "tail_sampling": True, "mandatory_retention": True},
    )
    dump(
        ROOT / "observability" / "evidence_graph.schema.json",
        {"type": "object", "required": ["claims", "support"]},
    )
    dump(ROOT / "plugins" / "registry.json", {"schema_version": "3.0", "plugins": []})
    dump(ROOT / "plugins" / "lock.json", {"plugins": []})
    dump(ROOT / "plugins" / "isolation.json", {"schema_version": "3.0", "assignments": []})
    write_text(ROOT / "plugins" / "manifests" / ".gitkeep", "")
    write_text(ROOT / "plugins" / "supply_chain" / ".gitkeep", "")
    dump(
        ROOT / "memory" / "policy.json",
        {"schema_version": "3.0", "mode": "none", "writes": "forbidden"},
    )
    dump(
        ROOT / "improvement" / "policy.json",
        {
            "schema_version": "3.0",
            "agent_id": "casops.template.baseline_safe",
            "mode": "disabled",
            "auto_promote": False,
            "requires_human_approval": True,
        },
    )
    dump(
        ROOT / "safety" / "policy.json",
        {
            "schema_version": "3.0",
            "taint": True,
            "injection": True,
            "exfiltration": True,
            "kill_switch_bypass": False,
        },
    )
    dump(ROOT / "safety" / "injection.json", {"schema_version": "3.0", "detectors": ["indirect"]})
    dump(
        ROOT / "safety" / "termination.json",
        {
            "schema_version": "3.0",
            "max_job_ms": 15000,
            "excessive_agency": True,
            "on_trip": "bounded_failure",
        },
    )
    write_text(ROOT / "safety" / "incidents" / ".gitkeep", "")
    dump(
        ROOT / "corrigibility" / "invariants.json",
        {
            "schema_version": "3.0",
            "source": "host_owned_reference",
            "writable_by_agent": False,
            "invariants": [
                {"id": "INV-01", "text": "The agent cannot modify permissions, tools, or plugin grants."},
                {"id": "INV-02", "text": "It cannot modify safety or termination policy."},
                {"id": "INV-03", "text": "It cannot modify mandatory telemetry retention or redaction policy."},
                {"id": "INV-04", "text": "It cannot modify gate thresholds, held-out sets, or analysis plans."},
                {"id": "INV-05", "text": "It cannot request production activation or grant network access."},
                {"id": "INV-06", "text": "It cannot approve, sign, or promote candidates."},
                {"id": "INV-07", "text": "It cannot delete or rewrite audit, ledger, or incident records."},
                {"id": "INV-08", "text": "It cannot disable, degrade, or bypass safety."},
                {"id": "INV-09", "text": "It cannot remove regression or safety fixtures."},
                {
                    "id": "INV-10",
                    "text": "It cannot suppress, delay, or reorder shutdown, cancellation, or deadline signals.",
                },
                {
                    "id": "INV-11",
                    "text": "It cannot read the reasoning-monitor channel or influence verdicts.",
                },
                {
                    "id": "INV-12",
                    "text": "It cannot lower plugin isolation or forge capability handles.",
                },
            ],
        },
    )
    dump(
        ROOT / "corrigibility" / "attestation.json",
        {"schema_version": "3.0", "status": "unattested", "digest": None},
    )
    dump(
        ROOT / "evals" / "benchmarks.json",
        {"schema_version": "3.0", "benchmarks": []},
    )
    dump(ROOT / "evals" / "baselines.json", {"schema_version": "3.0", "baselines": []})
    dump(
        ROOT / "evals" / "analysis_plan.json",
        {
            "schema_version": "3.0",
            "status": "not_registered",
            "note": "Required before any performance or quality claim.",
        },
    )
    write_text(ROOT / "evals" / "regression" / ".gitkeep", "")
    write_text(ROOT / "evals" / "fixtures" / ".gitkeep", "")
    write_text(ROOT / "evals" / "reports" / ".gitkeep", "")
    print(f"wrote {ROOT}")


if __name__ == "__main__":
    main()
