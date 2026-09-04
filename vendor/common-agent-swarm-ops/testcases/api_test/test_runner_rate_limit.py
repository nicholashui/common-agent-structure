#!/usr/bin/env python3
"""Unit checks for rate-limit helpers (no live Host required)."""
from __future__ import annotations

import unittest

from run_all_api_tests import is_rate_limited, sleep_backoff


class RateLimitHelpersTest(unittest.TestCase):
    def test_is_rate_limited_status(self) -> None:
        self.assertTrue(is_rate_limited(429, {}))
        self.assertFalse(is_rate_limited(200, {"ok": True}))

    def test_is_rate_limited_body_code(self) -> None:
        self.assertTrue(
            is_rate_limited(200, {"error": {"code": "rate_limited", "message": "x"}})
        )

    def test_backoff_uses_retry_after(self) -> None:
        self.assertEqual(sleep_backoff(0, retry_after_header="3", base=1.0, cap=30.0), 3.0)

    def test_backoff_exponential(self) -> None:
        self.assertEqual(sleep_backoff(0, retry_after_header=None, base=1.0, cap=30.0), 1.0)
        self.assertEqual(sleep_backoff(1, retry_after_header=None, base=1.0, cap=30.0), 2.0)
        self.assertEqual(sleep_backoff(2, retry_after_header=None, base=1.0, cap=30.0), 4.0)
        self.assertEqual(sleep_backoff(10, retry_after_header=None, base=1.0, cap=5.0), 5.0)


if __name__ == "__main__":
    unittest.main()
