"""Instrument-registry-service process entry."""

from casops.instruments.bootstrap import create_app_from_env

app = create_app_from_env()
