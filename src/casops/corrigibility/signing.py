"""Ed25519 signatures for the host-owned invariant reference (ADR-004 / DEC-01)."""

from __future__ import annotations

from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey


class HostSigner:
    def __init__(self, private_key: Ed25519PrivateKey) -> None:
        self._key = private_key

    @classmethod
    def generate(cls) -> HostSigner:
        return cls(Ed25519PrivateKey.generate())

    @classmethod
    def load(cls, path: Path) -> HostSigner:
        loaded = serialization.load_pem_private_key(path.read_bytes(), password=None)
        if not isinstance(loaded, Ed25519PrivateKey):
            raise TypeError("corrigibility key must be Ed25519")
        return cls(loaded)

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        pem = self._key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        path.write_bytes(pem)
        try:
            path.chmod(0o600)
        except OSError:
            pass

    def sign(self, digest: str) -> str:
        return self._key.sign(digest.encode("ascii")).hex()

    def verify(self, digest: str, signature: str) -> bool:
        try:
            self._key.public_key().verify(bytes.fromhex(signature), digest.encode("ascii"))
        except Exception:
            return False
        return True
