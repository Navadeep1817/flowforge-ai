"""
HTTP executor.
"""

from __future__ import annotations

import httpx

from app.engine.context import ExecutionContext
from app.engine.executors.base import BaseExecutor
from app.engine.result import ExecutionResult
from app.engine.template_resolver import TemplateResolver
from app.engine.workflow import WorkflowNode
from app.integrations.http_client import HttpClient


class HttpExecutor(BaseExecutor):
    """
    Executes HTTP requests.
    """

    node_type = "http"

    def __init__(
        self,
        client: HttpClient | None = None,
    ) -> None:
        self.client = client or HttpClient()
        self.resolver = TemplateResolver()

    async def execute(
        self,
        node: WorkflowNode,
        context: ExecutionContext,
    ) -> ExecutionResult:

        url = self.resolver.resolve(
            node.config["url"],
            context,
        )

        headers = self.resolver.resolve(
            node.config.get("headers", {}),
            context,
        )

        params = self.resolver.resolve(
            node.config.get("params", {}),
            context,
        )

        body = self.resolver.resolve(
            node.config.get("body", {}),
            context,
        )

        try:

            response = await self.client.request(
                method=node.config["method"],
                url=url,
                headers=headers,
                params=params,
                json=body,
            )

            try:
                outputs = response.json()
            except Exception:
                outputs = {
                    "status_code": response.status_code,
                    "text": response.text,
                }

            context.set_output(
                node.id,
                outputs,
            )

            return ExecutionResult(
                success=True,
                outputs=outputs,
            )

        except httpx.HTTPError as exc:

            return ExecutionResult(
                success=False,
                error=str(exc),
            ) 