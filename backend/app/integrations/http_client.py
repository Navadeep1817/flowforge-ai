"""
Reusable HTTP client.
"""

from __future__ import annotations

import httpx


class HttpClient:

    def __init__(self) -> None:
        self._client = httpx.AsyncClient(timeout=30)

    async def request(
        self,
        *,
        method: str,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        json: dict | None = None,
    ) -> httpx.Response:

        response = await self._client.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json,
        )

        response.raise_for_status()

        return response

    async def close(self) -> None:
        await self._client.aclose()