"""Process bootstrap for instrument-registry-service."""

from __future__ import annotations

import os
from pathlib import Path

from fastapi import FastAPI

from casops.corrigibility.signing import HostSigner
from casops.instruments.app import create_instrument_service_app
from casops.instruments.registry import InstrumentRegistry


def create_app_from_env() -> FastAPI:
    data_dir = Path(os.environ.get("CASOPS_INSTRUMENT_DATA", "var/casops/instruments"))
    key_path = Path(os.environ.get("CASOPS_INSTRUMENT_KEY", str(data_dir / "keys" / "ed25519.pem")))
    data_dir.mkdir(parents=True, exist_ok=True)
    key_path.parent.mkdir(parents=True, exist_ok=True)
    if not key_path.is_file():
        HostSigner.generate().save(key_path)
    registry = InstrumentRegistry.open(data_dir=data_dir, key_path=key_path)
    return create_instrument_service_app(registry)
