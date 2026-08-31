"""Process entry apps. Public routes stay under /api/v3."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from fastapi import FastAPI

from casops.api.http import install_error_handler
from casops.compose.app import create_compose_service_app
from casops.compose.engine import Composer
from casops.corrigibility.app import create_corrigibility_service_app
from casops.corrigibility.store import InvariantStore
from casops.instruments.registry import InstrumentRegistry


def create_corrigibility_app(store: InvariantStore | None = None) -> FastAPI:
    store = store or InvariantStore.with_host_defaults()
    app = create_corrigibility_service_app(store=store)

    @app.get("/api/v3/agents/{agent_id}/corrigibility/attestation")
    def public_attestation(agent_id: str) -> dict[str, Any]:
        record = store.reference()
        return {
            "agent_id": agent_id,
            "digest": record.digest,
            "signature": record.signature,
            "status": "host_reference",
            "invariant_set_id": record.invariant_set_id,
        }

    return app


def create_compose_app(
    *,
    agents_root: Path,
    store: InvariantStore | None = None,
) -> FastAPI:
    store = store or InvariantStore.with_host_defaults()
    app = create_compose_service_app(agents_root=agents_root, store=store)
    composer = Composer(agents_root=agents_root, store=store)

    @app.post("/api/v3/agents/{agent_id}/compose-preview")
    def public_compose_preview(agent_id: str) -> dict[str, Any]:
        result = composer.preview(agent_id)
        return {
            "compose_hash": result.compose_hash,
            "mro": result.mro,
            "findings": result.findings,
            "errors": result.errors,
            "lock": result.lock,
            "wrote_locks": False,
        }

    @app.get("/api/v3/agents/{agent_id}/structure")
    def structure(agent_id: str) -> dict[str, Any]:
        folder = composer.resolve_folder(agent_id)
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
        result = composer.preview(agent_id)
        return {
            "agent_id": agent_id,
            "mro": result.mro,
            "compose_hash": result.compose_hash,
            "lock": result.lock,
        }

    return app


def create_control_plane(*, agents_root: Path, **kwargs: Any) -> FastAPI:
    """Public FastAPI plane under /api/v3 only."""
    from casops.api.control import create_control_plane as build

    return build(agents_root=agents_root, **kwargs)


def create_instrument_app(registry: InstrumentRegistry | None = None) -> FastAPI:
    from casops.instruments.app import create_instrument_service_app

    return create_instrument_service_app(registry)
