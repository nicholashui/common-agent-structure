"""Unforgeable, expiring, revocable capability handles (ADR-006)."""

from __future__ import annotations

import time
from dataclasses import dataclass

from casops.corrigibility.signing import HostSigner
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError


@dataclass(frozen=True)
class CapabilityHandle:
    handle_id: str
    audience: str
    scope: str
    expires_at: float
    signature: str

    def token(self) -> str:
        return "|".join(
            [self.handle_id, self.audience, self.scope, str(int(self.expires_at)), self.signature]
        )


class HandleBroker:
    def __init__(self, signer: HostSigner | None = None) -> None:
        self.signer = signer or HostSigner.generate()
        self._revoked: set[str] = set()
        self._seq = 0

    def mint(self, *, audience: str, scope: str, ttl_seconds: float = 60) -> CapabilityHandle:
        self._seq += 1
        handle_id = f"h{self._seq}"
        expires_at = time.time() + ttl_seconds
        digest = f"{handle_id}:{audience}:{scope}:{int(expires_at)}"
        handle = CapabilityHandle(
            handle_id=handle_id,
            audience=audience,
            scope=scope,
            expires_at=expires_at,
            signature=self.signer.sign(digest),
        )
        return handle

    def verify(self, handle: CapabilityHandle, *, audience: str, scope: str) -> None:
        if handle.handle_id in self._revoked:
            raise CasopsError(ErrorCode.PLG_HANDLE_FORGERY)
        if handle.audience != audience or handle.scope != scope:
            raise CasopsError(ErrorCode.PLG_HANDLE_FORGERY)
        if handle.expires_at < time.time():
            raise CasopsError(ErrorCode.PLG_HANDLE_FORGERY)
        digest = f"{handle.handle_id}:{handle.audience}:{handle.scope}:{int(handle.expires_at)}"
        if not self.signer.verify(digest, handle.signature):
            raise CasopsError(ErrorCode.PLG_HANDLE_FORGERY)

    def revoke(self, handle_id: str) -> None:
        self._revoked.add(handle_id)

    def parse(self, token: str) -> CapabilityHandle:
        parts = token.split("|")
        if len(parts) != 5:
            raise CasopsError(ErrorCode.PLG_HANDLE_FORGERY)
        return CapabilityHandle(
            handle_id=parts[0],
            audience=parts[1],
            scope=parts[2],
            expires_at=float(parts[3]),
            signature=parts[4],
        )
