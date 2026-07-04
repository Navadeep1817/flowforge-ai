"""
Reusable async HTTP client.
"""

from __future__ import annotations

from typing import Any

import httpx


class HttpClient:
    """
    Shared async HTTP client.
    """

    def __init__(self) -> None:
        self._client = httpx.AsyncClient(
            timeout=30,
            follow_redirects=True,
        )

    async def request(
        self,
        method: str,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        response = await self._client.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json,
        )

        response.raise_for_status()

        return response.json()

    async def close(self) -> None:
        await self._client.aclose()