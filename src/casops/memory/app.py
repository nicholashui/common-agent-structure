"""Internal FastAPI apps for memory-service and consolidation-worker."""

from __future__ import annotations

from typing import Any

from fastapi import FastAPI, Header
from pydantic import BaseModel

from casops.api.http import install_error_handler
from casops.memory.store import ConsolidationWorker, MemoryService


class WriteBody(BaseModel):
    tenant: str
    subject: str
    text: str
    mode: str = "working"


class QueryBody(BaseModel):
    tenant: str
    subject: str
    text: str | None = None


class ScopeBody(BaseModel):
    tenant: str
    subject: str


def create_memory_service_app(memory: MemoryService | None = None) -> FastAPI:
    memory = memory or MemoryService()
    app = FastAPI(title="memory-service", version="0.1.0")
    install_error_handler(app)

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "service": "memory-service"}

    @app.post("/internal/v1/memory/query")
    def query(body: QueryBody) -> dict[str, Any]:
        return {"records": memory.scoped_query(tenant=body.tenant, subject=body.subject, text=body.text)}

    @app.post("/internal/v1/memory/write-candidate")
    def write_candidate(body: WriteBody) -> dict[str, Any]:
        record = memory.write_candidate(
            tenant=body.tenant, subject=body.subject, text=body.text, mode=body.mode
        )
        return {"memory_id": record.memory_id}

    @app.delete("/internal/v1/memory/{memory_id}")
    def delete(memory_id: str, tenant: str, subject: str) -> dict[str, Any]:
        memory.delete(memory_id, tenant=tenant, subject=subject)
        return {"memory_id": memory_id, "tombstoned": True}

    @app.post("/internal/v1/memory/{memory_id}/verify-deletion")
    def verify(memory_id: str, body: ScopeBody) -> dict[str, Any]:
        return memory.verify_deletion(memory_id, tenant=body.tenant, subject=body.subject)

    return app


def create_consolidation_app(worker: ConsolidationWorker | None = None) -> FastAPI:
    worker = worker or ConsolidationWorker(MemoryService())
    app = FastAPI(title="consolidation-worker", version="0.1.0")
    install_error_handler(app)

    @app.get("/health")
    def health() -> dict[str, Any]:
        return {
            "status": "ok",
            "service": "consolidation-worker",
            "queue": len(worker.queue),
            "ran_on_serving_path": worker.ran_on_serving_path,
        }

    @app.post("/internal/v1/consolidate")
    def consolidate() -> dict[str, Any]:
        done = worker.run_offline()
        return {"processed": len(done), "ran_on_serving_path": worker.ran_on_serving_path}

    @app.post("/internal/v1/enqueue")
    def enqueue(x_casops_actor: str = Header(default="host_service")) -> dict[str, str]:
        del x_casops_actor
        worker.enqueue({"kind": "offline"})
        return {"queued": "ok"}

    return app
