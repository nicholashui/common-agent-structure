"""Bootstrap for trainer-bridge."""

from __future__ import annotations

from fastapi import FastAPI

from casops.improvement.app import create_trainer_app


def create_app_from_env() -> FastAPI:
    return create_trainer_app()
