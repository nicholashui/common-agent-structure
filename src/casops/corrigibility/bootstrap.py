"""Process bootstrap: load env, keys, and persistent store."""

from __future__ import annotations

from fastapi import FastAPI

from casops.corrigibility.app import create_corrigibility_service_app
from casops.corrigibility.config import CorrigibilityConfig
from casops.corrigibility.signing import HostSigner
from casops.corrigibility.store import InvariantStore


def create_app_from_env() -> FastAPI:
    config = CorrigibilityConfig.from_env()
    config.data_dir.mkdir(parents=True, exist_ok=True)
    config.key_path.parent.mkdir(parents=True, exist_ok=True)
    if not config.key_path.is_file():
        HostSigner.generate().save(config.key_path)
    store = InvariantStore.open(data_dir=config.data_dir, key_path=config.key_path)
    return create_corrigibility_service_app(store=store)
