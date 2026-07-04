"""
Standard API response models.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class Metadata(BaseModel):
    request_id: str | None = None
    execution_time_ms: float | None = None


class ApiResponse(BaseModel):
    success: bool
    data: Any = None
    error: str | None = None
    metadata: Metadata | None = None 