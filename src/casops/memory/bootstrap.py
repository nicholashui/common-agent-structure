"""Bootstraps for memory-service and consolidation-worker."""

from __future__ import annotations

from fastapi import FastAPI

from casops.memory.app import create_consolidation_app, create_memory_service_app
from casops.memory.store import ConsolidationWorker, MemoryService

_MEMORY = MemoryService()
_WORKER = ConsolidationWorker(_MEMORY)


def create_memory_app_from_env() -> FastAPI:
    return create_memory_service_app(_MEMORY)


def create_consolidation_app_from_env() -> FastAPI:
    return create_consolidation_app(_WORKER)
