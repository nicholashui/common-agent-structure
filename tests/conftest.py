"""Keep pytest offline: do not follow host .env LLM keys into live providers."""

from __future__ import annotations

from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def pin_offline_llm(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setenv("DEFAULT_LLM", "local_deterministic")
    monkeypatch.setenv("CASOPS_LLM_SETTINGS", str(tmp_path / "casops-llm-settings.json"))
