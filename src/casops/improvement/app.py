"""Internal FastAPI app for trainer-bridge."""

from __future__ import annotations

from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

from casops.api.http import install_error_handler
from casops.improvement.trainer import TrainerBridge


class ImportBody(BaseModel):
    digest: str
    signature: str
    blob: dict[str, Any] | None = None


def create_trainer_app(bridge: TrainerBridge | None = None) -> FastAPI:
    bridge = bridge or TrainerBridge()
    app = FastAPI(title="trainer-bridge", version="0.1.0")
    install_error_handler(app)

    @app.get("/health")
    def health() -> dict[str, Any]:
        return {
            "status": "ok",
            "service": "trainer-bridge",
            "gradient_updates_in_serving": bridge.gradient_updates_in_serving,
        }

    @app.post("/internal/v1/adapters/import")
    def import_adapter(body: ImportBody) -> dict[str, Any]:
        return bridge.import_adapter(digest=body.digest, signature=body.signature, blob=body.blob)

    return app
