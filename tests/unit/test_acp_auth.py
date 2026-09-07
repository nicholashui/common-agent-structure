"""Headless ACP auth resolution. Live grok advertised grok.com + xai.api_key, not cached_token."""

from __future__ import annotations

import pytest

from casops.acp.client import resolve_acp_auth_method
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError


def test_empty_auth_methods_skip_authenticate() -> None:
    assert resolve_acp_auth_method(set()) is None


def test_xai_api_key_wins_when_advertised_and_env_set() -> None:
    chosen = resolve_acp_auth_method({"grok.com", "xai.api_key"}, env={"XAI_API_KEY": "not-a-secret-for-logs"})
    assert chosen == "xai.api_key"


def test_cached_token_when_no_api_key() -> None:
    chosen = resolve_acp_auth_method({"cached_token", "grok.com"}, env={})
    assert chosen == "cached_token"


def test_interactive_grok_com_without_headless_method_fails_fast() -> None:
    with pytest.raises(CasopsError) as raised:
        resolve_acp_auth_method({"grok.com", "xai.api_key"}, env={})
    assert raised.value.code == ErrorCode.PERF_ROUTE_UNAVAILABLE
    message = str(raised.value)
    assert "XAI_API_KEY" in message
    assert "cached_token" in message
    assert "not-a-secret" not in message
    assert "grok.com login is not performed" in message
