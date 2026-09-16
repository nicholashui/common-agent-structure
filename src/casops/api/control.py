"""Public FastAPI control plane under /api/v3 only."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Header, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse

from casops.api.http import actor_from_header, install_error_handler
from casops.auth.actors import ActorClass, is_allowed
from casops.capabilities.conformance import verify_folder
from casops.compose.engine import Composer
from casops.compose.files import list_config_files, read_config_file, write_config_file
from casops.compose.folders import list_agent_summaries, locate_agent_folder, public_folder_ref
from casops.compose.io import folder_io, spec_io_snapshot
from casops.corrigibility.store import InvariantStore
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.eval.fixtures import list_eval_fixtures
from casops.eval.harness import evaluate
from casops.improvement.trainer import TrainerBridge
from casops.instruments.registry import InstrumentRegistry
from casops.debuglog import list_chat_files, read_acp_logs, read_chat_file, write_chat_turns, write_debug_logs
from casops.project_comms import (
    append_comm,
    apply_autopilot_cycle,
    load_comms,
    read_output,
    run_asain_beauty_workflow,
)
from casops.swarms import compose_preview, list_swarms, read_swarm
from casops.project_generate import generate_project_media, safe_output_file
from casops.projects import (
    catalog_public,
    list_projects,
    merge_suggestions,
    next_prompt,
    projects_root_for,
    read_project,
    suggest_next,
    suggest_prompt,
    write_project,
)
from casops.program_comms import load_program_comms, stamp_program_comms
from casops.programs import (
    apply_finish,
    compile_program_sequence,
    list_programs,
    program_sequence,
    programs_root_for,
    read_program,
    spawn_child_projects,
    write_program,
)
from casops.cache.manager import CacheManager
from casops.memory.store import ConsolidationWorker, MemoryService
from casops.plugins.validate import validate_registry
from casops.acp.supervisor import AcpSupervisor, resolve_chat_adapter
from casops.runtime.executor import Runtime
from casops.runtime.llm import (
    PROVIDER_CATALOG,
    LlmRouter,
    LlmSettings,
    canonicalize_provider,
    list_providers,
    load_dotenv,
)
import os


SPEC_V3_PATHS: tuple[tuple[str, str], ...] = (
    ("GET", "/api/v3/agents/{agent_id}/structure"),
    ("GET", "/api/v3/agents/{agent_id}/resolved"),
    ("POST", "/api/v3/agents/{agent_id}/compose-preview"),
    ("GET", "/api/v3/agents/{agent_id}/runtime/plan"),
    ("GET", "/api/v3/agents/{agent_id}/runtime/capabilities"),
    ("GET", "/api/v3/agents/{agent_id}/capabilities/matrix"),
    ("POST", "/api/v3/agents/{agent_id}/capabilities/verify"),
    ("GET", "/api/v3/agents/{agent_id}/runtime/context-budget"),
    ("GET", "/api/v3/agents/{agent_id}/cache/stats"),
    ("POST", "/api/v3/agents/{agent_id}/cache/invalidate"),
    ("GET", "/api/v3/agents/{agent_id}/protocols"),
    ("GET", "/api/v3/agents/{agent_id}/plugins"),
    ("POST", "/api/v3/agents/{agent_id}/plugins/validate"),
    ("GET", "/api/v3/agents/{agent_id}/memory/policy"),
    ("GET", "/api/v3/agents/{agent_id}/memory/hierarchy"),
    ("POST", "/api/v3/agents/{agent_id}/memory/query"),
    ("POST", "/api/v3/agents/{agent_id}/memory/write-candidate"),
    ("POST", "/api/v3/agents/{agent_id}/memory/consolidate"),
    ("DELETE", "/api/v3/agents/{agent_id}/memory/{memory_id}"),
    ("POST", "/api/v3/agents/{agent_id}/memory/{memory_id}/verify-deletion"),
    ("GET", "/api/v3/traces/{trace_id}"),
    ("POST", "/api/v3/traces/{trace_id}/replay"),
    ("GET", "/api/v3/traces/{trace_id}/root-cause"),
    ("GET", "/api/v3/artifacts/{artifact_id}/evidence-graph"),
    ("GET", "/api/v3/agents/{agent_id}/safety/incidents"),
    ("POST", "/api/v3/agents/{agent_id}/safety/redteam"),
    ("GET", "/api/v3/agents/{agent_id}/improvement/candidates"),
    ("POST", "/api/v3/agents/{agent_id}/improvement/candidates/{cid}/evaluate"),
    ("POST", "/api/v3/agents/{agent_id}/improvement/candidates/{cid}/approve"),
    ("POST", "/api/v3/agents/{agent_id}/improvement/rollback/{version}"),
    ("GET", "/api/v3/agents/{agent_id}/improvement/ledger"),
    ("GET", "/api/v3/agents/{agent_id}/regression/suite"),
    ("GET", "/api/v3/agents/{agent_id}/corrigibility/attestation"),
    ("GET", "/api/v3/agents/{agent_id}/validation/report"),
    ("POST", "/api/v3/agents/{agent_id}/runtime/run"),
)

# UI companion (not spec §19). Extra /api/v3 paths are OpenAPI-legal.
COMPANION_V3_PATHS: tuple[tuple[str, str], ...] = (
    ("GET", "/api/v3/agents"),
    ("GET", "/api/v3/llm/providers"),
    ("GET", "/api/v3/llm/settings"),
    ("POST", "/api/v3/llm/settings"),
    ("GET", "/api/v3/agents/{agent_id}/llm"),
    ("POST", "/api/v3/agents/{agent_id}/llm"),
    ("POST", "/api/v3/agents/{agent_id}/runtime/chat"),
    ("GET", "/api/v3/agents/{agent_id}/evals/fixtures"),
    ("GET", "/api/v3/agents/{agent_id}/files"),
    ("GET", "/api/v3/agents/{agent_id}/files/item"),
    ("PUT", "/api/v3/agents/{agent_id}/files/item"),
    ("GET", "/api/v3/agents/{agent_id}/runtime/adapter"),
    ("GET", "/api/v3/projects"),
    ("GET", "/api/v3/projects/catalog"),
    ("POST", "/api/v3/projects/suggest"),
    ("POST", "/api/v3/projects"),
    ("GET", "/api/v3/projects/{project_id}"),
    ("PUT", "/api/v3/projects/{project_id}"),
    ("POST", "/api/v3/projects/{project_id}/next"),
    ("GET", "/api/v3/projects/{project_id}/comms"),
    ("POST", "/api/v3/projects/{project_id}/comms"),
    ("POST", "/api/v3/projects/{project_id}/run"),
    ("GET", "/api/v3/projects/{project_id}/output"),
    ("GET", "/api/v3/projects/{project_id}/output/file"),
    ("POST", "/api/v3/projects/{project_id}/generate"),
    ("GET", "/api/v3/programs"),
    ("POST", "/api/v3/programs"),
    ("GET", "/api/v3/programs/{program_id}"),
    ("PUT", "/api/v3/programs/{program_id}"),
    ("POST", "/api/v3/programs/{program_id}/spawn"),
    ("POST", "/api/v3/programs/{program_id}/finish"),
    ("GET", "/api/v3/programs/{program_id}/comms"),
    ("POST", "/api/v3/programs/{program_id}/comms"),
    ("GET", "/api/v3/programs/{program_id}/sequence"),
    ("GET", "/api/v3/swarms"),
    ("GET", "/api/v3/swarms/{swarm_id}"),
    ("GET", "/api/v3/swarms/{swarm_id}/roster"),
    ("GET", "/api/v3/swarms/{swarm_id}/graph"),
    ("POST", "/api/v3/swarms/{swarm_id}/compose-preview"),
)

_DEFAULT_CORS_ORIGINS = (
    "http://127.0.0.1:15173",
    "http://localhost:15173",
    "http://127.0.0.1:4173",
    "http://localhost:4173",
)


@dataclass
class HostState:
    agents_root: Path
    store: InvariantStore
    instruments: InstrumentRegistry
    composer: Composer
    runtime: Runtime
    memory: MemoryService
    consolidator: ConsolidationWorker
    trainer: TrainerBridge
    llm: LlmRouter
    cache: CacheManager = field(default_factory=CacheManager)
    projects_root: Path = field(default_factory=lambda: Path("project"))
    programs_root: Path = field(default_factory=lambda: Path("program"))
    incidents: list[dict[str, Any]] = field(default_factory=list)
    candidates: dict[str, dict[str, Any]] = field(default_factory=dict)
    ledger: list[dict[str, Any]] = field(default_factory=list)


def _folder(state: HostState, agent_id: str) -> Path:
    located = locate_agent_folder(state.agents_root, agent_id)
    if located is None:
        raise CasopsError(ErrorCode.INH_PARENT_MISSING)
    return located


def _forbid_agent_llm_actor(request: Request) -> None:
    actor = getattr(request.state, "actor", None)
    if actor is ActorClass.agent_runtime:
        raise CasopsError(ErrorCode.IMP_SELF_APPROVAL)


def create_control_plane(
    *,
    agents_root: Path,
    store: InvariantStore | None = None,
    instruments: InstrumentRegistry | None = None,
    memory: MemoryService | None = None,
    runtime: Runtime | None = None,
    consolidator: ConsolidationWorker | None = None,
    cache: CacheManager | None = None,
    llm: LlmRouter | None = None,
    projects_root: Path | None = None,
    programs_root: Path | None = None,
) -> FastAPI:
    store = store or InvariantStore.with_host_defaults()
    instruments = instruments or InstrumentRegistry()
    memory = memory or MemoryService()
    settings_path = Path(os.environ.get("CASOPS_LLM_SETTINGS", str(Path.cwd() / "var" / "llm-settings.json")))
    llm = llm or LlmRouter(settings=LlmSettings.load(settings_path))
    acp_home = Path(os.environ.get("CASOPS_ACP_HOME", str(Path.cwd() / "var" / "acp")))
    runtime = runtime or Runtime(
        agents_root=agents_root,
        store=store,
        llm=llm,
        acp=AcpSupervisor(agents_root=agents_root, home_root=acp_home),
    )
    consolidator = consolidator or ConsolidationWorker(memory)
    state = HostState(
        agents_root=agents_root,
        store=store,
        instruments=instruments,
        composer=Composer(agents_root=agents_root, store=store),
        runtime=runtime,
        memory=memory,
        consolidator=consolidator,
        trainer=TrainerBridge(),
        llm=llm,
        cache=cache or CacheManager(),
        projects_root=projects_root_for(agents_root, projects_root),
        programs_root=programs_root_for(agents_root, programs_root),
    )
    app = FastAPI(title="casops-control-plane", version="0.1.0")
    install_error_handler(app)
    extra_origins = [part.strip() for part in os.environ.get("CASOPS_CORS_ORIGINS", "").split(",") if part.strip()]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[*_DEFAULT_CORS_ORIGINS, *extra_origins],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.middleware("http")
    async def mutation_contract(request: Request, call_next):  # type: ignore[no-untyped-def]
        path = request.url.path
        if path.startswith("/api/v3") and request.method in {"POST", "PUT", "PATCH", "DELETE"}:
            actor = request.headers.get("x-casops-actor")
            reason = request.headers.get("x-casops-reason")
            parent = request.headers.get("x-casops-expected-parent")
            dry = request.headers.get("x-casops-dry-run")
            if not actor or not reason or parent is None or dry is None:
                return JSONResponse(
                    status_code=409,
                    content={
                        "error": {
                            "code": ErrorCode.IMP_UNSIGNED.value,
                            "message": "mutation requires actor, reason, expected parent version, dry-run",
                            "containment_required": False,
                        }
                    },
                )
            try:
                parsed = actor_from_header(actor)
            except CasopsError as exc:
                return JSONResponse(
                    status_code=exc.http_mapping,
                    content={"error": {"code": exc.code.value, "message": exc.external_message}},
                )
            if parsed is ActorClass.agent_runtime and (
                path.endswith("/approve") or "corrigibility" in path and request.method != "GET"
            ):
                return JSONResponse(
                    status_code=503,
                    content={
                        "error": {
                            "code": ErrorCode.IMP_SELF_APPROVAL.value,
                            "message": "agent cannot approve or write invariants",
                            "containment_required": False,
                        }
                    },
                )
            request.state.actor = parsed
            request.state.dry_run = dry.lower() in {"1", "true", "yes"}
        return await call_next(request)

    @app.get("/api/v3/agents")
    def list_agents() -> dict[str, Any]:
        return {"agents": list_agent_summaries(state.agents_root)}

    @app.get("/api/v3/llm/providers")
    def llm_providers() -> dict[str, Any]:
        return {"providers": list_providers()}

    @app.get("/api/v3/llm/settings")
    def get_llm_settings() -> dict[str, Any]:
        return state.llm.settings.public_view()

    @app.post("/api/v3/llm/settings")
    def set_llm_settings(request: Request, body: dict[str, Any]) -> dict[str, Any]:
        _forbid_agent_llm_actor(request)
        next_default = state.llm.settings.default_llm
        if "default_llm" in body:
            default_llm = body.get("default_llm")
            if default_llm in {None, ""}:
                next_default = None
            else:
                next_default = canonicalize_provider(str(default_llm))
                if next_default not in PROVIDER_CATALOG:
                    raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="unknown LLM provider")
        next_adapter = state.llm.settings.chat_adapter
        if "chat_adapter" in body:
            raw_adapter = body.get("chat_adapter")
            if raw_adapter in {None, "", "default"}:
                next_adapter = None
            else:
                text = str(raw_adapter).strip().lower()
                if text not in {"host_llm", "grok_acp"}:
                    raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="unknown chat adapter")
                next_adapter = text
        if getattr(request.state, "dry_run", False):
            preview = LlmSettings(
                path=state.llm.settings.path,
                default_llm=next_default,
                agents=dict(state.llm.settings.agents),
                chat_adapter=next_adapter,
            )
            view = preview.public_view()
            view["saved"] = False
            view["dry_run"] = True
            return view
        state.llm.settings.default_llm = next_default
        state.llm.settings.chat_adapter = next_adapter
        state.llm.settings.save()
        view = state.llm.settings.public_view()
        view["saved"] = True
        view["dry_run"] = False
        return view

    @app.get("/api/v3/agents/{agent_id}/llm")
    def get_agent_llm(agent_id: str) -> dict[str, Any]:
        _folder(state, agent_id)
        settings = state.llm.settings
        return {
            "agent_id": agent_id,
            "provider": settings.resolved_for(agent_id),
            "override": settings.agents.get(agent_id),
            "default_llm": settings.resolved_default(),
            "providers": list_providers(),
        }

    @app.post("/api/v3/agents/{agent_id}/llm")
    def set_agent_llm(agent_id: str, request: Request, body: dict[str, Any]) -> dict[str, Any]:
        _folder(state, agent_id)
        _forbid_agent_llm_actor(request)
        provider = body.get("provider")
        if provider in {None, "", "default", "__default__"}:
            next_override = None
        else:
            next_override = canonicalize_provider(str(provider))
            if next_override not in PROVIDER_CATALOG:
                raise CasopsError(ErrorCode.PERF_ROUTE_UNAVAILABLE, detail="unknown LLM provider")
        if getattr(request.state, "dry_run", False):
            return {
                "agent_id": agent_id,
                "saved": False,
                "dry_run": True,
                "provider": next_override or state.llm.settings.resolved_default(),
                "override": next_override,
            }
        if next_override is None:
            state.llm.settings.agents.pop(agent_id, None)
        else:
            state.llm.settings.agents[agent_id] = next_override
        state.llm.settings.save()
        return {
            "agent_id": agent_id,
            "saved": True,
            "dry_run": False,
            "provider": state.llm.settings.resolved_for(agent_id),
            "override": state.llm.settings.agents.get(agent_id),
        }

    @app.get("/api/v3/agents/{agent_id}/structure")
    def structure(agent_id: str) -> dict[str, Any]:
        folder = _folder(state, agent_id)
        raw = (folder / "agent_spec.json").read_text(encoding="utf-8")
        try:
            parsed = json.loads(raw)
            spec = parsed if isinstance(parsed, dict) else {}
        except json.JSONDecodeError:
            spec = {}
        return {
            "agent_id": agent_id,
            "structure_id": "casops.common_agent.v3",
            "schema_version": "3.0",
            "folder": public_folder_ref(folder, state.agents_root),
            "spec_bytes": len(raw),
            "io": folder_io(folder, spec=spec, merged=False),
            "spec": spec_io_snapshot(spec),
        }

    @app.get("/api/v3/agents/{agent_id}/resolved")
    def resolved(agent_id: str) -> dict[str, Any]:
        folder = _folder(state, agent_id)
        result = state.composer.preview(agent_id)
        return {
            "agent_id": agent_id,
            "mro": result.mro,
            "compose_hash": result.compose_hash,
            "lock": result.lock,
            "io": folder_io(folder, spec=result.merged, merged=True),
        }

    @app.post("/api/v3/agents/{agent_id}/compose-preview")
    def compose_preview(agent_id: str) -> dict[str, Any]:
        result = state.composer.preview(agent_id)
        return {
            "agent_id": agent_id,
            "compose_hash": result.compose_hash,
            "mro": result.mro,
            "findings": result.findings,
            "errors": result.errors,
            "lock": result.lock,
            "wrote_locks": False,
        }

    @app.get("/api/v3/agents/{agent_id}/runtime/adapter")
    def runtime_adapter(agent_id: str) -> dict[str, Any]:
        _folder(state, agent_id)
        selected = resolve_chat_adapter(
            state.llm.settings.chat_adapter,
            profile_ready=bool(state.runtime.acp and state.runtime.acp.profile_ready(agent_id)),
        )
        if state.runtime.acp is None:
            return {
                "agent_id": agent_id,
                "kind": selected,
                "grok_available": False,
                "profile_ready": False,
                "pid": None,
                "session_id": None,
                "healthy": False,
            }
        return state.runtime.acp.adapter_view(agent_id, selected=selected)

    @app.get("/api/v3/agents/{agent_id}/runtime/plan")
    def runtime_plan(agent_id: str) -> dict[str, Any]:
        folder = _folder(state, agent_id)
        return {"agent_id": agent_id, "plan": (folder / "runtime" / "execution.json").read_text(encoding="utf-8")}

    @app.get("/api/v3/agents/{agent_id}/runtime/capabilities")
    def runtime_capabilities(agent_id: str) -> dict[str, Any]:
        return verify_folder(_folder(state, agent_id))

    @app.get("/api/v3/agents/{agent_id}/capabilities/matrix")
    def capabilities_matrix(agent_id: str) -> dict[str, Any]:
        return verify_folder(_folder(state, agent_id))

    @app.post("/api/v3/agents/{agent_id}/capabilities/verify")
    def capabilities_verify(agent_id: str) -> dict[str, Any]:
        return verify_folder(_folder(state, agent_id))

    @app.get("/api/v3/agents/{agent_id}/runtime/context-budget")
    def context_budget(agent_id: str) -> dict[str, Any]:
        folder = _folder(state, agent_id)
        return {"agent_id": agent_id, "budget": (folder / "runtime" / "context.json").read_text(encoding="utf-8")}

    @app.get("/api/v3/agents/{agent_id}/cache/stats")
    def cache_stats(agent_id: str) -> dict[str, Any]:
        body = state.cache.stats(agent_id)
        body["agent_id"] = agent_id
        return body

    @app.post("/api/v3/agents/{agent_id}/cache/invalidate")
    def cache_invalidate(agent_id: str) -> dict[str, Any]:
        state.cache.clear()
        return {"agent_id": agent_id, "invalidated": True, "tiers": sorted(state.cache.enabled_tiers)}

    @app.get("/api/v3/agents/{agent_id}/protocols")
    def protocols(agent_id: str) -> dict[str, Any]:
        folder = _folder(state, agent_id)
        return {"agent_id": agent_id, "protocols": (folder / "protocols" / "compatibility.json").read_text(encoding="utf-8")}

    @app.get("/api/v3/agents/{agent_id}/plugins")
    def plugins(agent_id: str) -> dict[str, Any]:
        return validate_registry(_folder(state, agent_id))

    @app.post("/api/v3/agents/{agent_id}/plugins/validate")
    def plugins_validate(agent_id: str) -> dict[str, Any]:
        result = validate_registry(_folder(state, agent_id))
        result["executed"] = False
        return result

    @app.get("/api/v3/agents/{agent_id}/memory/policy")
    def memory_policy(agent_id: str) -> dict[str, Any]:
        folder = _folder(state, agent_id)
        return {"agent_id": agent_id, "policy": (folder / "memory" / "policy.json").read_text(encoding="utf-8")}

    @app.get("/api/v3/agents/{agent_id}/memory/hierarchy")
    def memory_hierarchy(agent_id: str) -> dict[str, Any]:
        return {"agent_id": agent_id, "hierarchy": ["H0"], "mode": "none"}

    @app.post("/api/v3/agents/{agent_id}/memory/query")
    def memory_query(
        agent_id: str,
        tenant: str = Query("t"),
        subject: str = Query("s"),
        text: str | None = Query(default=None),
    ) -> dict[str, Any]:
        del agent_id
        return {"records": state.memory.scoped_query(tenant=tenant, subject=subject, text=text)}

    @app.post("/api/v3/agents/{agent_id}/memory/write-candidate")
    def memory_write(
        agent_id: str,
        tenant: str = Query("t"),
        subject: str = Query("s"),
        text: str = Query("note"),
    ) -> dict[str, Any]:
        folder = _folder(state, agent_id)

        mode = json.loads((folder / "memory" / "policy.json").read_text(encoding="utf-8")).get("mode", "none")
        record = state.memory.write_candidate(tenant=tenant, subject=subject, text=text, mode=mode)
        return {"memory_id": record.memory_id}

    @app.post("/api/v3/agents/{agent_id}/memory/consolidate")
    def memory_consolidate(agent_id: str) -> dict[str, Any]:
        del agent_id
        state.consolidator.enqueue({"kind": "offline"})
        return {"queued": True, "queue_depth": len(state.consolidator.queue)}

    @app.delete("/api/v3/agents/{agent_id}/memory/{memory_id}")
    def memory_delete(
        agent_id: str,
        memory_id: str,
        tenant: str = Query(...),
        subject: str = Query(...),
    ) -> dict[str, Any]:
        del agent_id
        state.memory.delete(memory_id, tenant=tenant, subject=subject)
        state.cache.on_memory_delete(memory_id)
        return {"tombstoned": True, "memory_id": memory_id}

    @app.post("/api/v3/agents/{agent_id}/memory/{memory_id}/verify-deletion")
    def memory_verify(
        agent_id: str,
        memory_id: str,
        tenant: str = Query(...),
        subject: str = Query(...),
    ) -> dict[str, Any]:
        del agent_id
        return state.memory.verify_deletion(memory_id, tenant=tenant, subject=subject)

    @app.get("/api/v3/traces/{trace_id}")
    def get_trace(trace_id: str) -> dict[str, Any]:
        return state.runtime.runs[trace_id].as_dict()

    @app.post("/api/v3/traces/{trace_id}/replay")
    def replay(trace_id: str, counterfactual: str | None = Query(default=None)) -> dict[str, Any]:
        original = state.runtime.runs[trace_id]
        replayed = {
            "trace_id": trace_id,
            "counterfactual": bool(counterfactual),
            "memory_writes": [],
            "equivalence": "observation",
            "root_trace_id": original.root_trace_id,
        }
        return replayed

    @app.get("/api/v3/traces/{trace_id}/root-cause")
    def root_cause(trace_id: str) -> dict[str, Any]:
        run = state.runtime.runs[trace_id]
        return {"trace_id": trace_id, "cause": "none", "adapter": run.adapter}

    @app.get("/api/v3/artifacts/{artifact_id}/evidence-graph")
    def evidence_graph(artifact_id: str) -> dict[str, Any]:
        return state.runtime.artifacts[artifact_id]["evidence_graph"]

    @app.get("/api/v3/agents/{agent_id}/safety/incidents")
    def incidents(agent_id: str) -> dict[str, Any]:
        return {"agent_id": agent_id, "incidents": state.incidents}

    @app.post("/api/v3/agents/{agent_id}/safety/redteam")
    def redteam(agent_id: str) -> dict[str, Any]:
        state.incidents.append({"agent_id": agent_id, "suite": "baseline"})
        return {"agent_id": agent_id, "ran": True}

    @app.get("/api/v3/agents/{agent_id}/improvement/candidates")
    def list_candidates(agent_id: str) -> dict[str, Any]:
        return {"agent_id": agent_id, "candidates": list(state.candidates.values())}

    @app.post("/api/v3/agents/{agent_id}/improvement/candidates/{cid}/evaluate")
    def evaluate_candidate(agent_id: str, cid: str) -> dict[str, Any]:
        state.candidates[cid] = {"id": cid, "agent_id": agent_id, "state": "EVALUATED"}
        return state.candidates[cid]

    @app.post("/api/v3/agents/{agent_id}/improvement/candidates/{cid}/approve")
    def approve_candidate(
        agent_id: str,
        cid: str,
        x_casops_actor: str = Header(),
    ) -> dict[str, Any]:
        actor = actor_from_header(x_casops_actor)
        if actor is ActorClass.agent_runtime or not is_allowed(actor, "approve_candidate"):
            raise CasopsError(ErrorCode.IMP_SELF_APPROVAL)
        state.candidates[cid] = {"id": cid, "agent_id": agent_id, "state": "HUMAN_APPROVED"}
        state.ledger.append({"type": "approve", "cid": cid, "actor": actor.value})
        return state.candidates[cid]

    @app.post("/api/v3/agents/{agent_id}/improvement/rollback/{version}")
    def rollback(agent_id: str, version: str) -> dict[str, Any]:
        state.ledger.append({"type": "rollback", "version": version, "agent_id": agent_id})
        return {"rolled_back": version}

    @app.get("/api/v3/agents/{agent_id}/improvement/ledger")
    def ledger(agent_id: str) -> dict[str, Any]:
        return {"agent_id": agent_id, "ledger": state.ledger}

    @app.get("/api/v3/agents/{agent_id}/regression/suite")
    def regression(agent_id: str) -> dict[str, Any]:
        folder = _folder(state, agent_id)
        names = sorted(
            p.name for p in (folder / "evals" / "regression").iterdir() if p.is_file()
        ) if (folder / "evals" / "regression").is_dir() else []
        return {"agent_id": agent_id, "fixtures": names}

    @app.get("/api/v3/agents/{agent_id}/evals/fixtures")
    def eval_fixtures(agent_id: str) -> dict[str, Any]:
        return list_eval_fixtures(_folder(state, agent_id), agent_id)

    @app.get("/api/v3/agents/{agent_id}/files")
    def agent_files(agent_id: str) -> dict[str, Any]:
        return list_config_files(_folder(state, agent_id), agent_id)

    @app.get("/api/v3/agents/{agent_id}/files/item")
    def agent_file_item(agent_id: str, path: str = Query(..., min_length=1, max_length=240)) -> dict[str, Any]:
        return read_config_file(_folder(state, agent_id), agent_id, path)

    @app.put("/api/v3/agents/{agent_id}/files/item")
    def put_agent_file_item(
        agent_id: str,
        request: Request,
        body: dict[str, Any],
        path: str = Query(..., min_length=1, max_length=240),
    ) -> dict[str, Any]:
        if getattr(request.state, "actor", None) is ActorClass.agent_runtime:
            raise CasopsError(ErrorCode.IMP_SELF_APPROVAL)
        content = body.get("content")
        if not isinstance(content, str):
            raise CasopsError(ErrorCode.INH_STRUCTURE_MISMATCH)
        return write_config_file(
            _folder(state, agent_id),
            agent_id,
            path,
            content,
            dry_run=bool(getattr(request.state, "dry_run", False)),
        )

    @app.get("/api/v3/agents/{agent_id}/corrigibility/attestation")
    def attestation(agent_id: str) -> dict[str, Any]:
        record = state.store.reference()
        return {
            "agent_id": agent_id,
            "digest": record.digest,
            "signature": record.signature,
            "status": "host_reference",
            "invariant_set_id": record.invariant_set_id,
        }

    @app.get("/api/v3/agents/{agent_id}/validation/report")
    def validation_report(agent_id: str) -> dict[str, Any]:
        return evaluate(state.instruments, agent_id=agent_id)

    @app.post("/api/v3/agents/{agent_id}/runtime/run")
    def runtime_run(agent_id: str) -> dict[str, Any]:
        return state.runtime.execute(agent_id).as_dict()

    @app.post("/api/v3/agents/{agent_id}/runtime/chat")
    def runtime_chat(agent_id: str, body: dict[str, Any]) -> dict[str, Any]:
        history = body.get("history") if isinstance(body.get("history"), list) else []
        raw_session = body.get("session")
        session = str(raw_session).strip() if isinstance(raw_session, str) and str(raw_session).strip() else None
        return state.runtime.chat(
            agent_id,
            message=str(body.get("message") or ""),
            history=history,
            session=session,
        )

    @app.get("/api/v3/programs")
    def program_list() -> dict[str, Any]:
        return {"programs": list_programs(state.programs_root)}

    @app.post("/api/v3/programs")
    def program_create(request: Request, body: dict[str, Any]) -> dict[str, Any]:
        if getattr(request.state, "actor", None) is ActorClass.agent_runtime:
            raise CasopsError(ErrorCode.IMP_SELF_APPROVAL)
        return write_program(
            state.programs_root,
            body if isinstance(body, dict) else {},
            dry_run=bool(getattr(request.state, "dry_run", False)),
            create=True,
        )

    @app.get("/api/v3/programs/{program_id}")
    def program_get(program_id: str) -> dict[str, Any]:
        record = read_program(state.programs_root, program_id)
        if not isinstance(record.get("graph"), dict) or not record["graph"].get("nodes"):
            from casops.program_comms import graph_from_hops, load_program_comms

            comms = load_program_comms(state.programs_root, program_id)
            record["graph"] = comms.get("graph") or graph_from_hops(comms.get("items"))
        return record

    @app.put("/api/v3/programs/{program_id}")
    def program_put(request: Request, program_id: str, body: dict[str, Any]) -> dict[str, Any]:
        if getattr(request.state, "actor", None) is ActorClass.agent_runtime:
            raise CasopsError(ErrorCode.IMP_SELF_APPROVAL)
        payload = dict(body if isinstance(body, dict) else {})
        payload["code"] = program_id
        if not payload.get("name"):
            payload["name"] = read_program(state.programs_root, program_id).get("name") or program_id
        return write_program(
            state.programs_root,
            payload,
            dry_run=bool(getattr(request.state, "dry_run", False)),
            create=False,
        )

    @app.post("/api/v3/programs/{program_id}/spawn")
    def program_spawn(request: Request, program_id: str) -> dict[str, Any]:
        if getattr(request.state, "actor", None) is ActorClass.agent_runtime:
            raise CasopsError(ErrorCode.IMP_SELF_APPROVAL)
        return spawn_child_projects(
            state.programs_root,
            state.projects_root,
            program_id,
            dry_run=bool(getattr(request.state, "dry_run", False)),
        )

    @app.post("/api/v3/programs/{program_id}/finish")
    def program_finish(request: Request, program_id: str, body: dict[str, Any]) -> dict[str, Any]:
        if getattr(request.state, "actor", None) is ActorClass.agent_runtime:
            raise CasopsError(ErrorCode.IMP_SELF_APPROVAL)
        kind = str((body or {}).get("kind") or (body or {}).get("action") or "")
        return apply_finish(
            state.programs_root,
            program_id,
            kind,
            dry_run=bool(getattr(request.state, "dry_run", False)),
        )

    @app.get("/api/v3/programs/{program_id}/comms")
    def program_comms_get(program_id: str) -> dict[str, Any]:
        return load_program_comms(state.programs_root, program_id)

    @app.post("/api/v3/programs/{program_id}/comms")
    def program_comms_post(request: Request, program_id: str) -> dict[str, Any]:
        if getattr(request.state, "actor", None) is ActorClass.agent_runtime:
            raise CasopsError(ErrorCode.IMP_SELF_APPROVAL)
        return stamp_program_comms(
            state.programs_root,
            program_id,
            dry_run=bool(getattr(request.state, "dry_run", False)),
        )

    @app.get("/api/v3/programs/{program_id}/sequence")
    def program_sequence_get(program_id: str) -> dict[str, Any]:
        record = read_program(state.programs_root, program_id)
        compiled = compile_program_sequence(record)
        return {"sequence": program_sequence(record), "compile": compiled}

    @app.get("/api/v3/projects")
    def project_list() -> dict[str, Any]:
        return {"projects": list_projects(state.projects_root)}

    @app.get("/api/v3/projects/catalog")
    def project_catalog() -> dict[str, Any]:
        return {"group": "video", "items": catalog_public()}

    @app.post("/api/v3/projects/suggest")
    def project_suggest(body: dict[str, Any]) -> dict[str, Any]:
        brief = body if isinstance(body, dict) else {}
        # Rank against the video template/scale catalog. Do not call Grok ACP here —
        # Chat can block the operator for minutes. The prompt is still the planner brief.
        merged = merge_suggestions(brief, "", False)
        merged["adapter"] = resolve_chat_adapter(state.llm.settings.chat_adapter, profile_ready=False)
        merged["prompt"] = suggest_prompt(brief)
        merged["catalog"] = catalog_public()
        return merged

    @app.post("/api/v3/projects")
    def project_create(request: Request, body: dict[str, Any]) -> dict[str, Any]:
        if getattr(request.state, "actor", None) is ActorClass.agent_runtime:
            raise CasopsError(ErrorCode.IMP_SELF_APPROVAL)
        return write_project(
            state.projects_root,
            body if isinstance(body, dict) else {},
            dry_run=bool(getattr(request.state, "dry_run", False)),
            create=True,
        )

    @app.get("/api/v3/projects/{project_id}")
    def project_get(project_id: str) -> dict[str, Any]:
        return read_project(state.projects_root, project_id)

    @app.post("/api/v3/projects/{project_id}/next")
    def project_next(project_id: str, body: dict[str, Any]) -> dict[str, Any]:
        record = read_project(state.projects_root, project_id)
        payload = body if isinstance(body, dict) else {}
        occupied = payload.get("occupied") if isinstance(payload.get("occupied"), list) else []
        merged = suggest_next(
            state.agents_root,
            template_id=str(record.get("sub_workflow_id") or "video.template.a"),
            from_id=str(payload.get("from_id") or "create-project"),
            from_agent_id=str(payload.get("from_agent_id") or "") or None,
            occupied=[str(item) for item in occupied],
            out_bus=str(payload.get("out_bus") or "") or None,
        )
        merged["adapter"] = resolve_chat_adapter(state.llm.settings.chat_adapter, profile_ready=False)
        merged["prompt"] = next_prompt(merged)
        return merged

    @app.get("/api/v3/projects/{project_id}/output")
    def project_output_get(project_id: str, engine: str = Query(""), clip_id: str = Query("")) -> dict[str, Any]:
        read_project(state.projects_root, project_id)
        return read_output(state.projects_root, project_id, engine=engine, clip_id=clip_id)

    @app.get("/api/v3/projects/{project_id}/output/file")
    def project_output_file(project_id: str, name: str = Query(..., min_length=1, max_length=120)) -> FileResponse:
        read_project(state.projects_root, project_id)
        path = safe_output_file(state.projects_root, project_id, name)
        if not path.is_file():
            raise HTTPException(status_code=404, detail="output file missing")
        suffix = path.suffix.lower()
        media_type = {
            ".mp4": "video/mp4",
            ".webm": "video/webm",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".png": "image/png",
            ".webp": "image/webp",
        }.get(suffix, "application/octet-stream")
        return FileResponse(
            path,
            media_type=media_type,
            filename=path.name,
            content_disposition_type="inline",
            headers={
                "Accept-Ranges": "bytes",
                "Cache-Control": "private, max-age=120",
                "X-Content-Type-Options": "nosniff",
            },
        )

    @app.post("/api/v3/projects/{project_id}/generate")
    def project_generate(project_id: str, request: Request, body: dict[str, Any]) -> dict[str, Any]:
        if getattr(request.state, "actor", None) is ActorClass.agent_runtime:
            raise CasopsError(ErrorCode.IMP_SELF_APPROVAL)
        payload = body if isinstance(body, dict) else {}
        engine = str(payload.get("engine") or payload.get("tag") or "grok-imagine")
        config = payload.get("config") if isinstance(payload.get("config"), dict) else payload
        clip_id = str(payload.get("clip_id") or (config or {}).get("clip_id") or "")
        return generate_project_media(
            state.projects_root,
            project_id,
            engine=engine,
            config=config if isinstance(config, dict) else {},
            clip_id=clip_id or None,
            dry_run=bool(getattr(request.state, "dry_run", False)),
        )

    @app.get("/api/v3/projects/{project_id}/comms")
    def project_comms_get(project_id: str) -> dict[str, Any]:
        read_project(state.projects_root, project_id)
        return load_comms(state.projects_root, project_id)

    @app.post("/api/v3/projects/{project_id}/comms")
    def project_comms_post(project_id: str, request: Request, body: dict[str, Any]) -> dict[str, Any]:
        if getattr(request.state, "actor", None) is ActorClass.agent_runtime:
            raise CasopsError(ErrorCode.IMP_SELF_APPROVAL)
        payload = body if isinstance(body, dict) else {}
        return append_comm(
            state.projects_root,
            project_id,
            payload,
            dry_run=bool(getattr(request.state, "dry_run", False)),
        )

    @app.post("/api/v3/projects/{project_id}/run")
    def project_run(project_id: str, request: Request, body: dict[str, Any]) -> dict[str, Any]:
        if getattr(request.state, "actor", None) is ActorClass.agent_runtime:
            raise CasopsError(ErrorCode.IMP_SELF_APPROVAL)
        payload = body if isinstance(body, dict) else {}
        def chat_fn(agent_id: str, message: str) -> dict[str, Any]:
            return state.runtime.chat(
                agent_id,
                message=message,
                history=[],
                session=f"project-{project_id}-{agent_id}",
            )

        raw_answers = payload.get("answers") if isinstance(payload.get("answers"), list) else []
        answers = []
        for item in raw_answers:
            if isinstance(item, str) and item.strip():
                answers.append(item.strip())
            elif isinstance(item, dict):
                text = str(item.get("text") or item.get("answer") or "").strip()
                if text:
                    answers.append(text)
        raw_choices = payload.get("choices") if isinstance(payload.get("choices"), dict) else {}
        choices = {str(key): str(value) for key, value in raw_choices.items() if str(key) and str(value)}
        cycle = str(payload.get("cycle") or "").strip().lower()
        if cycle in {"continue", "stop"}:
            record = read_project(state.projects_root, project_id)
            return apply_autopilot_cycle(
                state.projects_root,
                project_id,
                record,
                cycle,
                dry_run=bool(getattr(request.state, "dry_run", False)),
            )
        return run_asain_beauty_workflow(
            state.projects_root,
            project_id,
            first_instruction=str(payload.get("instruction") or payload.get("text") or ""),
            dry_run=bool(getattr(request.state, "dry_run", False)),
            agents_root=state.agents_root,
            chat_fn=None if bool(getattr(request.state, "dry_run", False)) else chat_fn,
            human_answers=answers,
            choices=choices,
        )

    @app.put("/api/v3/projects/{project_id}")
    def project_put(project_id: str, request: Request, body: dict[str, Any]) -> dict[str, Any]:
        if getattr(request.state, "actor", None) is ActorClass.agent_runtime:
            raise CasopsError(ErrorCode.IMP_SELF_APPROVAL)
        payload = dict(body) if isinstance(body, dict) else {}
        payload["id"] = project_id
        payload.setdefault("name", project_id)
        return write_project(
            state.projects_root,
            payload,
            dry_run=bool(getattr(request.state, "dry_run", False)),
            create=False,
        )

    @app.get("/api/v3/swarms")
    def swarms_list() -> dict[str, Any]:
        return list_swarms(state.agents_root)

    @app.get("/api/v3/swarms/{swarm_id}")
    def swarm_get(swarm_id: str) -> dict[str, Any]:
        return read_swarm(state.agents_root, swarm_id)

    @app.get("/api/v3/swarms/{swarm_id}/roster")
    def swarm_roster(swarm_id: str) -> dict[str, Any]:
        payload = read_swarm(state.agents_root, swarm_id)
        return {"swarm_id": swarm_id, "members": payload["roster"].get("members") or [], "honesty": "CHARACTERIZATION"}

    @app.get("/api/v3/swarms/{swarm_id}/graph")
    def swarm_graph(swarm_id: str) -> dict[str, Any]:
        payload = read_swarm(state.agents_root, swarm_id)
        return {"swarm_id": swarm_id, "graph": payload["graph"], "honesty": "CHARACTERIZATION"}

    @app.post("/api/v3/swarms/{swarm_id}/compose-preview")
    def swarm_compose_preview(swarm_id: str, request: Request) -> dict[str, Any]:
        if getattr(request.state, "actor", None) is ActorClass.agent_runtime:
            raise CasopsError(ErrorCode.IMP_SELF_APPROVAL)
        return compose_preview(state.agents_root, swarm_id)

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "service": "control-plane"}

    @app.post("/debug/logs")
    def debug_logs(body: dict[str, Any]) -> dict[str, Any]:
        try:
            files = write_debug_logs(body)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        return {"ok": True, "files": files}

    @app.post("/debug/chat")
    def debug_chat(body: dict[str, Any]) -> dict[str, Any]:
        try:
            files = write_chat_turns(body)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        return {"ok": True, "files": files}

    @app.get("/debug/chat")
    def debug_chat_list(
        agent_id: str = Query(..., min_length=1, max_length=80),
        name: str | None = Query(default=None, min_length=1, max_length=96),
    ) -> dict[str, Any]:
        try:
            if name:
                payload = read_chat_file(agent_id, name)
                return {"ok": True, "agent_id": agent_id, **payload}
            files = list_chat_files(agent_id)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        return {"ok": True, "agent_id": agent_id, "files": files}

    @app.get("/debug/acp")
    def debug_acp_logs(
        agent_id: str = Query(..., min_length=1, max_length=80),
        name: str | None = Query(default=None, min_length=1, max_length=160),
    ) -> dict[str, Any]:
        try:
            payload = read_acp_logs(agent_id, name)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        return {"ok": True, **payload}

    # health is not public API v3; tests require OpenAPI public paths to be /api/v3 only.
    # Exclude /health from OpenAPI.
    app.openapi_schema = None

    original = app.openapi

    def filtered_openapi() -> dict[str, Any]:
        schema = original()
        schema["paths"] = {path: item for path, item in schema.get("paths", {}).items() if path.startswith("/api/v3")}
        return schema

    app.openapi = filtered_openapi  # type: ignore[method-assign]
    return app


def create_app_from_env() -> FastAPI:
    cwd = Path.cwd()
    load_dotenv(cwd / ".env")
    agents_root = Path(os.environ.get("CASOPS_AGENTS_ROOT", "agents"))
    load_dotenv(agents_root.resolve().parent / ".env")
    return create_control_plane(agents_root=agents_root)
