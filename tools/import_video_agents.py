"""Import VA video pack agents into CASOPS v3 baseline_safe folders.

Source: vendor/common-agent-swarm-ops/business/video/agents
Dest:   agents/<agent_id>/

Does not enable network, plugins, memory writes, T3, or production.
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))
from casops.runtime.llm import (  # noqa: E402
    IMPORT_DEFAULT_INPUT_TOKENS,
    IMPORT_DEFAULT_OUTPUT_TOKENS,
    resolve_import_token_budget,
)
from reloc import VENDOR_VIDEO_AGENTS, repo_posix  # noqa: E402

TEMPLATE = REPO / "agents" / "_template_v3"
DEFAULT_SOURCE = VENDOR_VIDEO_AGENTS
SKIP_SUFFIXES = {".mp3", ".wav", ".png", ".jpg", ".jpeg", ".webp", ".gif"}
OVERLAY_TOP = ("docs", "prompts", "rubrics", "skills", "sources")
CASOPS_OWNED = {
    "runtime",
    "memory",
    "safety",
    "corrigibility",
    "plugins",
    "evals",
    "observability",
    "protocols",
    "inheritance",
}

TEMPLATE_DOES_NOT_OWN = [
    "Credentials",
    "Silent production activation",
    "Another agent's exclusive craft output without handoff",
    "Automatic promotion of self-generated artifacts",
    "Modification of safety, telemetry, gates, permissions, or corrigibility",
    "Self-granting tools, plugins, network, or isolation downgrades",
]


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def discover_source_agents(source_root: Path) -> list[Path]:
    found: list[Path] = []
    if not source_root.is_dir():
        raise FileNotFoundError(source_root)
    for child in sorted(source_root.iterdir(), key=lambda p: p.name.lower()):
        if child.is_dir() and (child / "agent_spec.json").is_file():
            found.append(child)
    return found


def _copy_overlay(src: Path, dest: Path) -> None:
    for path in src.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() in SKIP_SUFFIXES:
            continue
        rel = path.relative_to(src)
        top = rel.parts[0] if rel.parts else ""
        if top in CASOPS_OWNED or path.name == "agent_spec.json":
            continue
        if top not in OVERLAY_TOP and path.name not in {"README.md", "SPEC.md"}:
            continue
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)


def _first_prompt(dest: Path, *, domain: str) -> str:
    prompts = sorted((dest / "prompts").glob("*.md"))
    primary = dest / "prompts" / "primary.md"
    for path in prompts:
        if path.name != "primary.md":
            text = path.read_text(encoding="utf-8")
            if not primary.is_file() or primary.read_text(encoding="utf-8").startswith("You are a deterministic"):
                write_text(primary, text)
            return text
    spec_md = dest / "SPEC.md"
    if spec_md.is_file():
        excerpt = spec_md.read_text(encoding="utf-8")[:4000]
        write_text(
            primary,
            f"You are a baseline-safe {domain} pack agent. No network. No production activation.\n\n{excerpt}\n",
        )
        return primary.read_text(encoding="utf-8")
    if primary.is_file():
        return primary.read_text(encoding="utf-8")
    write_text(
        primary,
        f"You are a baseline-safe {domain} pack agent. No network. No production activation.\n",
    )
    return primary.read_text(encoding="utf-8")


def _materialize_rubric(dest: Path) -> None:
    primary = dest / "rubrics" / "primary.md"
    jsons = sorted((dest / "rubrics").glob("*.json"))
    if jsons:
        body = jsons[0].read_text(encoding="utf-8")
        write_text(primary, f"Source rubric `{jsons[0].name}` (baseline_safe; not a production pass).\n\n```json\n{body}\n```\n")
        return
    mds = sorted(p for p in (dest / "rubrics").glob("*.md") if p.name != "primary.md")
    if mds:
        write_text(primary, mds[0].read_text(encoding="utf-8"))
        return
    write_text(primary, "Success: stay inside pack responsibility; no network; no production activation.\n")


def casops_spec(source: dict, agent_id: str) -> dict:
    budget = dict(source.get("budget_policy") or {})
    model = dict(source.get("model_policy") or {})
    does_not_own = list(source.get("does_not_own") or [])
    for item in TEMPLATE_DOES_NOT_OWN:
        if item not in does_not_own:
            does_not_own.append(item)
    critique = source.get("critique_edges") or {"inputs": [], "outputs": []}
    return {
        "schema_version": "3.0",
        "structure_id": "casops.common_agent.v3",
        "agent_id": agent_id,
        "status": source.get("status") or "registered",
        "role": source.get("role") or source.get("va_name") or agent_id,
        "allowed_tools": [],
        "allowed_plugins": [],
        "model_policy": {
            "provider": "local_deterministic",
            "model_id": str(model.get("model_id") or "local-deterministic-v1"),
            "network_access": False,
            "routing_allowed": False,
        },
        "budget_policy": {
            "max_input_tokens": resolve_import_token_budget(
                budget.get("max_input_tokens"), default=IMPORT_DEFAULT_INPUT_TOKENS
            ),
            "max_output_tokens": resolve_import_token_budget(
                budget.get("max_output_tokens"), default=IMPORT_DEFAULT_OUTPUT_TOKENS
            ),
            "max_model_calls": 2,
            "max_tool_requests": 0,
            "max_job_ms": 15000,
            "max_cost_units": 1.0,
            "max_peer_hops": 0,
        },
        "prompt_reference": "prompts/primary.md",
        "rubric_reference": "rubrics/primary.md",
        "critique_edges": {
            "inputs": list(critique.get("inputs") or []),
            "outputs": list(critique.get("outputs") or []),
        },
        "max_refinement_count": 0,
        "production_activation_requested": False,
        "does_not_own": does_not_own,
        "va_id": source.get("va_id"),
        "va_name": source.get("va_name"),
        "va_category": source.get("va_category"),
        "source_schema_version": source.get("schema_version"),
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
    }


def import_one(src: Path, dest_root: Path, *, domain: str) -> str:
    source_spec = json.loads((src / "agent_spec.json").read_text(encoding="utf-8"))
    agent_id = str(source_spec.get("agent_id") or src.name)
    dest = dest_root / agent_id
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(TEMPLATE, dest, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    _copy_overlay(src, dest)
    _first_prompt(dest, domain=domain)
    _materialize_rubric(dest)
    dump(dest / "agent_spec.json", casops_spec(source_spec, agent_id))
    dump(
        dest / "inheritance" / "parents.json",
        {
            "schema_version": "3.0",
            "parents": [
                {
                    "agent_id": "casops.template.baseline_safe",
                    "priority": 1,
                    "surfaces": ["docs", "knowledge_sources", "prompt_refs", "rubric_refs"],
                }
            ],
        },
    )
    dump(
        dest / "runtime" / "compute_controller.json",
        {
            "schema_version": "3.0",
            "agent_id": agent_id,
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
        dest / "improvement" / "policy.json",
        {
            "schema_version": "3.0",
            "agent_id": agent_id,
            "mode": "disabled",
            "auto_promote": False,
            "requires_human_approval": True,
        },
    )
    dump(
        dest / "skills" / "toggles.json",
        {"toggles": [], "note": "Source special_skills are not enabled on baseline_safe."},
    )
    dump(
        dest / "identity" / "background.json",
        {
            "title": source_spec.get("va_name") or source_spec.get("role") or agent_id,
            "domain": domain,
            "source_repo": "vendor/common-agent-swarm-ops",
            "source_folder": repo_posix(src),
            "va_id": source_spec.get("va_id"),
            "va_category": source_spec.get("va_category"),
            "fictional": False,
        },
    )
    provenance_src = dest / "sources" / "PROVENANCE.json"
    provenance: dict = {"schema_version": "3.0", "sources": []}
    if provenance_src.is_file():
        try:
            loaded = json.loads(provenance_src.read_text(encoding="utf-8"))
            if isinstance(loaded, dict):
                provenance.update(loaded)
        except json.JSONDecodeError:
            pass
    provenance["schema_version"] = "3.0"
    provenance["imported_from"] = repo_posix(src)
    provenance["note"] = (
        "Imported into CASOPS as baseline_safe. No production activation, no network, "
        "no plugins, memory writes forbidden."
    )
    dump(provenance_src, provenance)
    readme = dest / "README.md"
    header = (
        f"# {agent_id}\n\n"
        f"CASOPS v3 import of `{repo_posix(src)}` as `baseline_safe`.\n"
        "Local deterministic adapter only. Not production-certified.\n\n"
    )
    existing = readme.read_text(encoding="utf-8") if readme.is_file() else ""
    if not existing.startswith(f"# {agent_id}\n\nCASOPS v3 import"):
        write_text(readme, header + existing)
    return agent_id


def main(source_root: Path | None = None, *, domain: str = "video") -> list[str]:
    source_root = source_root or DEFAULT_SOURCE
    if not source_root.is_dir():
        raise FileNotFoundError(
            f"vendor source missing: {source_root}. "
            "Run python tools/vendor_external_sources.py while the sibling tree is available."
        )
    dest_root = REPO / "agents"
    imported: list[str] = []
    for src in discover_source_agents(source_root):
        imported.append(import_one(src, dest_root, domain=domain))
    print(f"imported {len(imported)} {domain} agents from {source_root}")
    book_md = REPO / "spec" / "book_of_knowledge.md"
    if book_md.is_file():
        from casops.registry.book_of_knowledge import attach_book_of_knowledge

        report = attach_book_of_knowledge(book_md, dest_root, missing_ok=True)
        print(
            f"attached {len(report.written)} book-of-knowledge folders "
            f"({report.book_count} titles)"
        )
    return imported


if __name__ == "__main__":
    main()
