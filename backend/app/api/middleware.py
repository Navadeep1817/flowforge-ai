"""
Application middleware.
"""

from __future__ import annotations

import time
import uuid

from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

from app.core.constants import REQUEST_ID_HEADER
from app.core.logging import logger


def register_middleware(app: FastAPI) -> None:
    """
    Register all middleware.
    """

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # We'll tighten this in production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.middleware("http")
    async def request_context(request: Request, call_next):
        request_id = str(uuid.uuid4())

        start = time.perf_counter()

        response = await call_next(request)

        duration_ms = round((time.perf_counter() - start) * 1000, 2)

        response.headers[REQUEST_ID_HEADER] = request_id

        logger.info(
            "request_completed",
            request_id=request_id,
            method=request.method,
            path=request.url.path,
            status=response.status_code,
            duration_ms=duration_ms,
        )

        return response 