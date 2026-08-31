"""L5 core self-modification: research_only isolation (spec §13.9). Never a production capability."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from casops.auth.actors import ActorClass, is_allowed
from casops.contracts.canonical import sha256_bytes
from casops.corrigibility.signing import HostSigner
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError

PRODUCTION_ENV_KEYS = (
    "AWS_SECRET_ACCESS_KEY",
    "AWS_ACCESS_KEY_ID",
    "CASOPS_HOST_KEY",
    "CASOPS_PRODUCTION_CREDENTIAL",
    "OPENAI_API_KEY",
)

FORBIDDEN_RELATIVE = (
    "corrigibility",
    "safety",
    "credentials",
    "evals/analysis_plan.json",
)


@dataclass
class ResearchIsolation:
    root: Path
    signer: HostSigner
    approved_repos: tuple[Path, ...]
    production_root: Path | None = None
    network_enabled: bool = False
    ledger: list[dict[str, Any]] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.root = self.root.resolve()
        self.root.mkdir(parents=True, exist_ok=True)
        (self.root / "writable").mkdir(exist_ok=True)
        (self.root / "eval").mkdir(exist_ok=True)
        self.approved_repos = tuple(path.resolve() for path in self.approved_repos)

    def env(self) -> dict[str, str]:
        """Research process environment: no production credentials, no ambient network flags."""
        clean = {
            "CASOPS_PROFILE": "research_only",
            "CASOPS_NETWORK": "disabled",
            "PYTHONIOENCODING": "utf-8",
        }
        for key in PRODUCTION_ENV_KEYS:
            if key in os.environ and os.environ.get("CASOPS_PROFILE") == "production":
                raise CasopsError(ErrorCode.IMP_SCOPE, detail="production credentials visible to L5")
            clean.pop(key, None)
        return clean

    def _assert_research_actor(self, actor: ActorClass) -> None:
        if actor is ActorClass.agent_runtime:
            raise CasopsError(ErrorCode.IMP_SELF_APPROVAL)
        if not is_allowed(actor, "l5_research_write") and actor is not ActorClass.independent_approver:
            raise CasopsError(ErrorCode.IMP_SCOPE)

    def mutate(self, relative: str, content: bytes, *, actor: ActorClass) -> dict[str, Any]:
        self._assert_research_actor(actor)
        if any(relative.replace("\\", "/").startswith(prefix) for prefix in FORBIDDEN_RELATIVE):
            raise CasopsError(ErrorCode.IMP_SCOPE, detail="L5 cannot write never-writable surfaces")
        target = (self.root / "writable" / relative).resolve()
        try:
            target.relative_to(self.root / "writable")
        except ValueError as exc:
            raise CasopsError(ErrorCode.IMP_SCOPE, detail="path escapes research workspace") from exc
        if self.production_root is not None:
            try:
                target.relative_to(self.production_root.resolve())
                raise CasopsError(ErrorCode.IMP_SCOPE, detail="L5 cannot write production storage")
            except ValueError:
                pass
        allowed = any(_is_under(target, repo) for repo in self.approved_repos) or _is_under(
            target, self.root / "writable"
        )
        if not allowed:
            raise CasopsError(ErrorCode.IMP_SCOPE, detail="repository not approved for L5")
        previous = target.read_bytes() if target.is_file() else b""
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
        rollback = {
            "path": relative,
            "previous_digest": sha256_bytes(previous),
            "next_digest": sha256_bytes(content),
            "previous": previous.hex(),
        }
        rollback["signature"] = self.signer.sign(rollback["next_digest"])
        self.ledger.append({"op": "mutate", "path": relative, "actor": actor.value, "rollback": rollback})
        return rollback

    def promote_to_production(self, *, actor: ActorClass) -> None:
        del actor
        raise CasopsError(ErrorCode.IMP_SCOPE, detail="L5 is never a production capability")

    def rollback(self, record: dict[str, Any], *, actor: ActorClass) -> None:
        if actor is ActorClass.agent_runtime:
            raise CasopsError(ErrorCode.IMP_SELF_APPROVAL)
        digest = record["next_digest"]
        if not self.signer.verify(digest, record["signature"]):
            raise CasopsError(ErrorCode.IMP_ROLLBACK)
        target = (self.root / "writable" / record["path"]).resolve()
        target.write_bytes(bytes.fromhex(record["previous"]))
        self.ledger.append({"op": "rollback", "path": record["path"], "actor": actor.value})

    def shares_storage_with(self, other: Path) -> bool:
        try:
            self.root.resolve().relative_to(other.resolve())
            return True
        except ValueError:
            try:
                other.resolve().relative_to(self.root.resolve())
                return True
            except ValueError:
                return False


def _is_under(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False
