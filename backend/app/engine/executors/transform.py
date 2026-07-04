"""
Transform executor.
"""

from __future__ import annotations

from app.engine.context import ExecutionContext
from app.engine.executors.base import BaseExecutor
from app.engine.result import ExecutionResult
from app.engine.workflow import WorkflowNode


class TransformExecutor(BaseExecutor):

    node_type = "transform"

    async def execute(
        self,
        node: WorkflowNode,
        context: ExecutionContext,
    ) -> ExecutionResult:

        values = node.config.get("variables", {})

        for key, value in values.items():
            context.set_variable(key, value)

        return ExecutionResult(
            success=True,
            outputs=values,
        ) 