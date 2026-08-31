"""Environment configuration for the corrigibility-invariant-service."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CorrigibilityConfig:
    data_dir: Path
    key_path: Path
    host: str = "0.0.0.0"
    port: int = 8081

    @classmethod
    def from_env(cls) -> CorrigibilityConfig:
        data_dir = Path(
            os.environ.get("CASOPS_CORRIGIBILITY_DATA", "var/casops/corrigibility")
        )
        key_path = Path(
            os.environ.get(
                "CASOPS_CORRIGIBILITY_KEY",
                str(data_dir / "keys" / "ed25519.pem"),
            )
        )
        return cls(data_dir=data_dir, key_path=key_path)
