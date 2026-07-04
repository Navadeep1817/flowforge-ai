"""
Health check endpoints.
"""

from __future__ import annotations

from fastapi import APIRouter

from app.core.config import get_settings
from app.core.responses import ApiResponse

router = APIRouter(tags=["Health"])

settings = get_settings()


@router.get("/health", response_model=ApiResponse)
async def health_check() -> ApiResponse:
    """
    Basic health endpoint.
    """

    return ApiResponse(
        success=True,
        data={
            "service": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "environment": settings.ENVIRONMENT,
            "status": "healthy",
        },
    ) 
@router.get("/", response_model=ApiResponse)
async def root() -> ApiResponse:
    """
    Root endpoint.
    """

    return ApiResponse(
        success=True,
        data={
            "name": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "docs": "/docs",
        },
    )