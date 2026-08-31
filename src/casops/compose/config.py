"""Environment configuration for compose-service."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ComposeConfig:
    agents_root: Path
    corrigibility_data: Path | None
    corrigibility_key: Path | None

    @classmethod
    def from_env(cls) -> ComposeConfig:
        agents_root = Path(os.environ.get("CASOPS_AGENTS_ROOT", "agents"))
        data = os.environ.get("CASOPS_CORRIGIBILITY_DATA")
        key = os.environ.get("CASOPS_CORRIGIBILITY_KEY")
        return cls(
            agents_root=agents_root,
            corrigibility_data=Path(data) if data else None,
            corrigibility_key=Path(key) if key else None,
        )
