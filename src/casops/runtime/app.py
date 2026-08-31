"""Internal FastAPI app for runtime-service."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from fastapi import FastAPI, Header
from pydantic import BaseModel

from casops.api.http import actor_from_header, install_error_handler
from casops.compose.engine import Composer
from casops.corrigibility.store import InvariantStore
from casops.runtime.executor import Runtime


class RunBody(BaseModel):
    agent_id: str


def create_runtime_service_app(
    *,
    agents_root: Path,
    store: InvariantStore | None = None,
    runtime: Runtime | None = None,
) -> FastAPI:
    store = store or InvariantStore.with_host_defaults()
    runtime = runtime or Runtime(agents_root=agents_root, store=store)
    composer = Composer(agents_root=agents_root, store=store)
    app = FastAPI(title="runtime-service", version="0.1.0")
    install_error_handler(app)

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "service": "runtime-service"}

    @app.post("/internal/v1/runs")
    def start_run(body: RunBody, x_casops_actor: str = Header(default="host_service")) -> dict[str, Any]:
        del x_casops_actor
        return runtime.execute(body.agent_id).as_dict()

    @app.get("/internal/v1/runs/{trace_id}")
    def get_run(trace_id: str) -> dict[str, Any]:
        return runtime.runs[trace_id].as_dict()

    @app.get("/internal/v1/plan/{agent_id}")
    def plan(agent_id: str) -> dict[str, Any]:
        folder = composer.resolve_folder(agent_id)
        return {"agent_id": agent_id, "execution": (folder / "runtime" / "execution.json").read_text(encoding="utf-8")}

    return app
