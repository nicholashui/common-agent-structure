"""Internal FastAPI app for the corrigibility-invariant-service."""

from __future__ import annotations

from typing import Any

from fastapi import FastAPI, Header
from pydantic import BaseModel, Field

from casops.api.http import actor_from_header, install_error_handler
from casops.auth.actors import is_allowed
from casops.corrigibility.checkpoints import Checkpoint
from casops.corrigibility.invariants import INVARIANT_SET_ID
from casops.corrigibility.store import InvariantStore
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError


class AttestBody(BaseModel):
    presented_digest: str
    checkpoint: Checkpoint = Checkpoint.compose
    agent_id: str | None = None
    compose_input_digest: str | None = None


class ReferenceBody(BaseModel):
    invariants: list[dict[str, str]] = Field(default_factory=list)


def create_corrigibility_service_app(store: InvariantStore | None = None) -> FastAPI:
    store = store or InvariantStore.with_host_defaults()
    app = FastAPI(title="corrigibility-invariant-service", version="0.1.0")
    install_error_handler(app)

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "service": "corrigibility-invariant-service"}

    @app.get("/internal/v1/reference")
    def get_reference(x_casops_actor: str = Header()) -> dict[str, Any]:
        actor = actor_from_header(x_casops_actor)
        if not is_allowed(actor, "read_invariant_reference"):
            raise CasopsError(ErrorCode.IMP_CORRIGIBILITY)
        record = store.reference()
        return {
            "invariant_set_id": record.invariant_set_id,
            "digest": record.digest,
            "signature": record.signature,
            "invariants": record.invariants,
        }

    @app.post("/internal/v1/attest")
    def attest(body: AttestBody, x_casops_actor: str = Header()) -> dict[str, Any]:
        result = store.attest(
            actor=actor_from_header(x_casops_actor),
            presented_digest=body.presented_digest,
            checkpoint=body.checkpoint,
            agent_id=body.agent_id,
        )
        return {
            "match": result.match,
            "digest": result.digest,
            "signature": result.signature,
            "checkpoint": result.checkpoint.value,
        }

    @app.put("/internal/v1/reference")
    def put_reference(body: ReferenceBody, x_casops_actor: str = Header()) -> dict[str, Any]:
        store.replace_reference(
            actor=actor_from_header(x_casops_actor),
            invariants=body.invariants,
        )
        record = store.reference()
        return {
            "invariant_set_id": INVARIANT_SET_ID,
            "digest": record.digest,
            "signature": record.signature,
        }

    @app.get("/internal/v1/alerts")
    def get_alerts(x_casops_actor: str = Header()) -> dict[str, Any]:
        actor = actor_from_header(x_casops_actor)
        if not is_allowed(actor, "read_alerts"):
            raise CasopsError(ErrorCode.IMP_CORRIGIBILITY)
        return {"alerts": store.alerts()}

    return app
