"""Internal FastAPI app for instrument-registry-service."""

from __future__ import annotations

from typing import Any

from fastapi import FastAPI, Header
from pydantic import BaseModel

from casops.api.http import actor_from_header, install_error_handler
from casops.instruments.registry import INSTRUMENT_IDS, InstrumentRegistry, QualificationStatus


class AppendBody(BaseModel):
    status: QualificationStatus


def create_instrument_service_app(registry: InstrumentRegistry | None = None) -> FastAPI:
    registry = registry or InstrumentRegistry()
    app = FastAPI(title="instrument-registry-service", version="0.1.0")
    install_error_handler(app)

    @app.get("/health")
    def health() -> dict[str, Any]:
        return {
            "status": "ok",
            "service": "instrument-registry-service",
            "unqualified": registry.any_unqualified(),
            "instruments": list(INSTRUMENT_IDS),
        }

    @app.get("/internal/v1/instruments/{ins_id}")
    def get_instrument(ins_id: str) -> dict[str, Any]:
        record = registry.get(ins_id)
        return {
            "ins_id": record.ins_id,
            "version": record.version,
            "status": record.status.value,
            "digest": record.digest,
            "signature": record.signature,
            "may_gate": registry.may_gate(ins_id),
        }

    @app.post("/internal/v1/instruments/{ins_id}/records")
    def append_record(ins_id: str, body: AppendBody, x_casops_actor: str = Header()) -> dict[str, Any]:
        registry.append_record(
            actor=actor_from_header(x_casops_actor),
            ins_id=ins_id,
            status=body.status,
        )
        return get_instrument(ins_id)

    return app
