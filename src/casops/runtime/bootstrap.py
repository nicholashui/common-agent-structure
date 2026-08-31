"""Process bootstrap for runtime-service."""

from __future__ import annotations

import os
from pathlib import Path

from fastapi import FastAPI

from casops.corrigibility.store import InvariantStore
from casops.runtime.app import create_runtime_service_app
from casops.runtime.executor import Runtime


def create_app_from_env() -> FastAPI:
    agents_root = Path(os.environ.get("CASOPS_AGENTS_ROOT", "agents"))
    store = InvariantStore.with_host_defaults()
    runtime = Runtime(agents_root=agents_root, store=store)
    return create_runtime_service_app(agents_root=agents_root, store=store, runtime=runtime)
