"""Process bootstrap for compose-service."""

from __future__ import annotations

from fastapi import FastAPI

from casops.compose.app import create_compose_service_app
from casops.compose.config import ComposeConfig
from casops.corrigibility.store import InvariantStore


def create_app_from_env() -> FastAPI:
    config = ComposeConfig.from_env()
    if config.corrigibility_data and config.corrigibility_key:
        store = InvariantStore.open(
            data_dir=config.corrigibility_data,
            key_path=config.corrigibility_key,
        )
    else:
        store = InvariantStore.with_host_defaults()
    return create_compose_service_app(agents_root=config.agents_root, store=store)
