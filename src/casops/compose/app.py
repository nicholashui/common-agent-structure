"""Internal FastAPI app for compose-service."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from fastapi import FastAPI, Header
from pydantic import BaseModel

from casops.api.http import actor_from_header, install_error_handler
from casops.compose.engine import Composer, ComposeResult
from casops.corrigibility.store import InvariantStore


class ComposeBody(BaseModel):
    agent_id: str


def _payload(result: ComposeResult) -> dict[str, Any]:
    return {
        "compose_hash": result.compose_hash,
        "mro": result.mro,
        "steps": result.steps,
        "findings": result.findings,
        "errors": result.errors,
        "lock": result.lock,
        "wrote_locks": result.wrote_locks,
    }


def create_compose_service_app(
    *,
    agents_root: Path,
    store: InvariantStore | None = None,
) -> FastAPI:
    store = store or InvariantStore.with_host_defaults()
    composer = Composer(agents_root=agents_root, store=store)
    app = FastAPI(title="compose-service", version="0.1.0")
    install_error_handler(app)

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "service": "compose-service"}

    @app.post("/internal/v1/compose-preview")
    def compose_preview(body: ComposeBody) -> dict[str, Any]:
        return _payload(composer.preview(body.agent_id))

    @app.post("/internal/v1/compose")
    def compose(body: ComposeBody, x_casops_actor: str = Header()) -> dict[str, Any]:
        return _payload(composer.compose(body.agent_id, actor=actor_from_header(x_casops_actor)))

    return app
