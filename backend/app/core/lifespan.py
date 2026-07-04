"""
Application lifespan events.
"""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logging import configure_logging, logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Startup and shutdown events.
    """

    configure_logging()

    logger.info("Starting FlowForge AI")

    yield

    logger.info("Stopping FlowForge AI") 