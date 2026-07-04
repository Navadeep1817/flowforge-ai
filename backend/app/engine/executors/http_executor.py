"""
HTTP executor.
"""

from __future__ import annotations

from app.engine.context import ExecutionContext
from app.engine.executors.base import BaseExecutor
from app.engine.result import ExecutionResult
from app.engine.workflow import WorkflowNode
from app.integrations.http_client import HttpClient


class HttpExecutor(BaseExecutor):

    node_type = "http"

    def __init__(self) -> None:
        self.client = HttpClient()

    async def execute(
        self,
        node: WorkflowNode,
        context: ExecutionContext,
    ) -> ExecutionResult:

        config = node.config

        result = await self.client.request(
            method=config["method"],
            url=config["url"],
            headers=config.get("headers"),
            params=config.get("params"),
            json=config.get("body"),
        )

        return ExecutionResult(
            success=True,
            outputs=result,
        ) 