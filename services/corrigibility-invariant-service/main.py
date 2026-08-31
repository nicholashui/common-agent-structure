"""Corrigibility-invariant-service process entry."""

from casops.corrigibility.bootstrap import create_app_from_env

app = create_app_from_env()
