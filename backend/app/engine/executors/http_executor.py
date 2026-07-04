"""
HTTP executor.
"""

from __future__ import annotations

from app.engine.context import ExecutionContext
from app.engine.executors.base import BaseExecutor
from app.engine.result import ExecutionResult
from app.engine.workflow import WorkflowNode
from app.integrations.http_client import HttpClient
from app.engine.mapping import MappingEngine

class HttpExecutor(BaseExecutor):

    node_type = "http"

    def __init__(self) -> None:
        self.client = HttpClient()
        self.mapper = MappingEngine()
    async def execute(
        self,
        node: WorkflowNode,
        context: ExecutionContext,
    ) -> ExecutionResult:

        config = node.config

        result = await self.client.request(
            method=config["method"],
            url=config["url"],
            headers=self.mapper.resolve(
    config.get("headers", {}),
    context,
),

params=self.mapper.resolve(
    config.get("params", {}),
    context,
),

json=self.mapper.resolve(
    config.get("body", {}),
    context,
)
        )

        return ExecutionResult(
            success=True,
            outputs=result,
        ) 