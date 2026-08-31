"""Compose-service process entry."""

from casops.compose.bootstrap import create_app_from_env

app = create_app_from_env()
