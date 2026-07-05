"""
Tests dynamic HTTP request mapping.
"""

from __future__ import annotations

import httpx
import pytest

from app.engine.context import ExecutionContext
from app.engine.executors.http_executor import HttpExecutor
from app.engine.workflow import WorkflowNode


class MockHttpClient:
    """
    Mock HTTP client.
    """

    async def request(
        self,
        *,
        method: str,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        json: dict | None = None,
    ) -> httpx.Response:

        assert method == "POST"

        assert url == "https://example.com/users"

        assert json == {
            "name": "Navadeep",
            "city": "Hyderabad",
        }

        return httpx.Response(
            status_code=200,
            json={
                "id": 1,
                "status": "created",
            },
        )


@pytest.mark.asyncio
async def test_http_template_mapping():

    context = ExecutionContext()

    context.update_request(
        {
            "name": "Navadeep",
            "city": "Hyderabad",
        }
    )

    executor = HttpExecutor(
        client=MockHttpClient(),
    )

    node = WorkflowNode(
        id="http",
        type="http",
        config={
            "method": "POST",
            "url": "https://example.com/users",
            "body": {
                "name": "{{request.name}}",
                "city": "{{request.city}}",
            },
        },
        next_nodes=[],
    )

    result = await executor.execute(
        node,
        context,
    )

    assert result.success

    assert context.outputs["http"] == {
        "id": 1,
        "status": "created",
    } 