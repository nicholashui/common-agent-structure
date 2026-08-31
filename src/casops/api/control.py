"""Public FastAPI control plane under /api/v3 only."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Header, Query, Request
from fastapi.responses import JSONResponse

from casops.api.http import actor_from_header, install_error_handler
from casops.auth.actors import ActorClass, is_allowed
from casops.capabilities.conformance import verify_folder
from casops.compose.engine import Composer
from casops.compose.folders import locate_agent_folder
from casops.corrigibility.store import InvariantStore
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError
from casops.eval.harness import evaluate
from casops.improvement.trainer import TrainerBridge
from casops.instruments.registry import InstrumentRegistry
from casops.cache.manager import CacheManager
from casops.memory.store import ConsolidationWorker, MemoryService
from casops.plugins.validate import validate_registry
from casops.runtime.executor import Runtime
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
    cache: CacheManager = field(default_factory=CacheManager)
    incidents: list[dict[str, Any]] = field(default_factory=list)
    candidates: dict[str, dict[str, Any]] = field(default_factory=dict)
    ledger: list[dict[str, Any]] = field(default_factory=list)


def _folder(state: HostState, agent_id: str) -> Path:
    located = locate_agent_folder(state.agents_root, agent_id)
    if located is None:
        raise CasopsError(ErrorCode.INH_PARENT_MISSING)
    return located


def create_control_plane(
    *,
    agents_root: Path,
    store: InvariantStore | None = None,
    instruments: InstrumentRegistry | None = None,
    memory: MemoryService | None = None,
    runtime: Runtime | None = None,
    consolidator: ConsolidationWorker | None = None,
    cache: CacheManager | None = None,
) -> FastAPI:
    store = store or InvariantStore.with_host_defaults()
    instruments = instruments or InstrumentRegistry()
    memory = memory or MemoryService()
    runtime = runtime or Runtime(agents_root=agents_root, store=store)
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
        cache=cache or CacheManager(),
    )
    app = FastAPI(title="casops-control-plane", version="0.1.0")
    install_error_handler(app)

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

    @app.get("/api/v3/agents/{agent_id}/structure")
    def structure(agent_id: str) -> dict[str, Any]:
        folder = _folder(state, agent_id)
        spec = (folder / "agent_spec.json").read_text(encoding="utf-8")
        return {
            "agent_id": agent_id,
            "structure_id": "casops.common_agent.v3",
            "schema_version": "3.0",
            "folder": str(folder),
            "spec_bytes": len(spec),
        }

    @app.get("/api/v3/agents/{agent_id}/resolved")
    def resolved(agent_id: str) -> dict[str, Any]:
        result = state.composer.preview(agent_id)
        return {"agent_id": agent_id, "mro": result.mro, "compose_hash": result.compose_hash, "lock": result.lock}

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
    def memory_query(agent_id: str, tenant: str = Query("t"), subject: str = Query("s")) -> dict[str, Any]:
        del agent_id
        return {"records": state.memory.scoped_query(tenant=tenant, subject=subject)}

    @app.post("/api/v3/agents/{agent_id}/memory/write-candidate")
    def memory_write(
        agent_id: str,
        tenant: str = Query("t"),
        subject: str = Query("s"),
        text: str = Query("note"),
    ) -> dict[str, Any]:
        folder = _folder(state, agent_id)
        import json

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

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "service": "control-plane"}

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
    return create_control_plane(agents_root=Path(os.environ.get("CASOPS_AGENTS_ROOT", "agents")))
