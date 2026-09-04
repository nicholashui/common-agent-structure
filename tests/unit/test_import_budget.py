"""Pack import floors stub token budgets instead of copying max_output_tokens: 1."""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools"))

from import_video_agents import casops_spec  # noqa: E402


def test_casops_spec_floors_stub_specials_budget() -> None:
    spec = casops_spec(
        {
            "budget_policy": {"max_input_tokens": 1, "max_output_tokens": 1},
            "role": "Special_Agent data-only configuration",
            "critique_edges": {"inputs": [], "outputs": []},
        },
        "specials.intent-analysis-agent",
    )
    assert spec["budget_policy"]["max_output_tokens"] == 1024
    assert spec["budget_policy"]["max_input_tokens"] == 2048
    assert spec["model_policy"]["network_access"] is False
    assert spec["production_activation_requested"] is False


def test_casops_spec_keeps_usable_video_budget() -> None:
    spec = casops_spec(
        {
            "budget_policy": {"max_input_tokens": 2048, "max_output_tokens": 1024},
            "role": "Director",
            "critique_edges": {"inputs": ["video.critic"], "outputs": ["video.editor"]},
        },
        "video.director",
    )
    assert spec["budget_policy"]["max_output_tokens"] == 1024
    assert spec["budget_policy"]["max_input_tokens"] == 2048
