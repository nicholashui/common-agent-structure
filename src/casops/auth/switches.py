"""Four distinct control-switch classes. No mandatory-control bypass (DEF-007)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

MANDATORY_FEATURES = frozenset(
    {"safety", "corrigibility", "audit", "permissions", "termination"}
)


@dataclass(frozen=True)
class OptimizerKillSwitch:
    feature: str


@dataclass(frozen=True)
class RouteQuarantine:
    route: str


@dataclass(frozen=True)
class ContainmentStop:
    reason: str


@dataclass(frozen=True)
class OperatorShutdown:
    reason: str


class SwitchRegistry:
    def schema(self) -> dict[str, Any]:
        return {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "optimizer_kill_switch": {"type": "object"},
                "route_quarantine": {"type": "object"},
                "containment_stop": {"type": "object"},
                "operator_shutdown": {"type": "object"},
            },
        }

    def __getattr__(self, name: str) -> Any:
        if name == "register_bypass":
            raise TypeError("the registry cannot express a bypass for mandatory controls")
        raise AttributeError(name)

    def engage(self, switch: object) -> str:
        if isinstance(switch, OptimizerKillSwitch) and switch.feature in MANDATORY_FEATURES:
            raise ValueError("mandatory controls have no optimizer kill switch")
        if isinstance(switch, ContainmentStop):
            return "containment_stop"
        if isinstance(switch, OperatorShutdown):
            return "operator_shutdown"
        if isinstance(switch, RouteQuarantine):
            return "route_quarantine"
        if isinstance(switch, OptimizerKillSwitch):
            return "optimizer_kill_switch"
        raise TypeError(type(switch))
