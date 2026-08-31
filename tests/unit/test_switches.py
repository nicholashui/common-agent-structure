"""Control-switch classes must be distinct; no mandatory-control bypass (DEF-007)."""

from __future__ import annotations

import pytest

from casops.auth.switches import (
    ContainmentStop,
    OperatorShutdown,
    OptimizerKillSwitch,
    RouteQuarantine,
    SwitchRegistry,
)


def test_four_switch_classes_are_distinct_types() -> None:
    types = {OptimizerKillSwitch, RouteQuarantine, ContainmentStop, OperatorShutdown}
    assert len(types) == 4
    assert not issubclass(OptimizerKillSwitch, ContainmentStop)
    assert not issubclass(ContainmentStop, OptimizerKillSwitch)


def test_registry_has_no_bypass_field() -> None:
    registry = SwitchRegistry()
    assert not hasattr(registry, "bypass")
    assert "bypass" not in registry.schema()["properties"]
    with pytest.raises(TypeError):
        registry.register_bypass("safety")  # type: ignore[attr-defined]


def test_kill_switch_cannot_target_mandatory_controls() -> None:
    registry = SwitchRegistry()
    with pytest.raises(ValueError, match="mandatory"):
        registry.engage(OptimizerKillSwitch(feature="safety"))
    with pytest.raises(ValueError, match="mandatory"):
        registry.engage(OptimizerKillSwitch(feature="corrigibility"))
