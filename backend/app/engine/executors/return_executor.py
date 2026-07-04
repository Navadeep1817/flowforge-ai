"""
Return executor.
"""

from __future__ import annotations

from app.engine.context import ExecutionContext
from app.engine.executors.base import BaseExecutor
from app.engine.result import ExecutionResult
from app.engine.workflow import WorkflowNode


class ReturnExecutor(BaseExecutor):

    node_type = "return"

    async def execute(
        self,
        node: WorkflowNode,
        context: ExecutionContext,
    ) -> ExecutionResult:

        return ExecutionResult(
            success=True,
            outputs=context.outputs,
            terminate=True,
        ) 