"""Shared HTTP helpers for CASOPS services."""

from __future__ import annotations

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from casops.auth.actors import ActorClass
from casops.errors.codes import ErrorCode
from casops.errors.exceptions import CasopsError


def actor_from_header(value: str) -> ActorClass:
    try:
        return ActorClass(value)
    except ValueError as exc:
        raise CasopsError(ErrorCode.IMP_CORRIGIBILITY) from exc


def install_error_handler(app: FastAPI) -> None:
    @app.exception_handler(CasopsError)
    async def casops_error_handler(_request: Request, exc: CasopsError) -> JSONResponse:
        return JSONResponse(
            status_code=exc.http_mapping,
            content={
                "error": {
                    "code": exc.code.value,
                    "message": exc.external_message,
                    "containment_required": exc.containment_required,
                }
            },
        )
