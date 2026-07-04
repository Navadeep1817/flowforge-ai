"""
Application exception hierarchy and global exception handlers.
"""

from __future__ import annotations

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.responses import ApiResponse


class FlowForgeException(Exception):
    """Base exception for all FlowForge application errors."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class ValidationException(FlowForgeException):
    """Validation error."""


class AuthenticationException(FlowForgeException):
    """Authentication error."""


class AuthorizationException(FlowForgeException):
    """Authorization error."""


class WorkflowException(FlowForgeException):
    """Workflow execution error."""


class ConfigurationException(FlowForgeException):
    """Configuration error."""


def register_exception_handlers(app: FastAPI) -> None:
    """Register global exception handlers."""

    @app.exception_handler(FlowForgeException)
    async def flowforge_exception_handler(
        request: Request,
        exc: FlowForgeException,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content=ApiResponse(
                success=False,
                error=exc.message,
            ).model_dump(),
        )

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(
        request: Request,
        exc: Exception,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=500,
            content=ApiResponse(
                success=False,
                error="Internal Server Error",
            ).model_dump(),
        )