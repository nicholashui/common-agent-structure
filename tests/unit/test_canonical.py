"""Canonical JSON + SHA-256 digest (ADR-002 / RFC 8785-style)."""

from __future__ import annotations

from casops.contracts.canonical import canonical_dumps, sha256_bytes, sha256_json


def test_digest_is_stable_across_repeated_serialization() -> None:
    payload = {"b": 2, "a": {"y": 1, "x": [3, 1]}}
    first = sha256_json(payload)
    second = sha256_json(payload)
    assert first == second
    assert len(first) == 64
    assert first == first.lower()


def test_object_key_order_does_not_change_digest() -> None:
    left = sha256_json({"z": 1, "a": 2, "m": 3})
    right = sha256_json({"m": 3, "a": 2, "z": 1})
    assert left == right


def test_nested_keys_are_sorted() -> None:
    dumped = canonical_dumps({"outer": {"b": 1, "a": 2}})
    assert dumped == '{"outer":{"a":2,"b":1}}'


def test_canonical_dumps_is_compact_utf8_json() -> None:
    dumped = canonical_dumps({"msg": "ok", "n": 1})
    assert " " not in dumped
    assert dumped.startswith("{")
    encoded = dumped.encode("utf-8")
    assert sha256_bytes(encoded) == sha256_json({"n": 1, "msg": "ok"})
