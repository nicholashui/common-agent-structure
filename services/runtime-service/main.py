"""Runtime-service process entry."""

from casops.runtime.bootstrap import create_app_from_env

app = create_app_from_env()
