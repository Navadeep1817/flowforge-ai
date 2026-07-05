"""
Merge executor.
"""

from __future__ import annotations

from app.engine.context import ExecutionContext
from app.engine.executors.base import BaseExecutor
from app.engine.result import ExecutionResult
from app.engine.workflow import WorkflowNode


class MergeExecutor(BaseExecutor):
    """
    Merges outputs from previous branches.
    """

    node_type = "merge"

    async def execute(
        self,
        node: WorkflowNode,
        context: ExecutionContext,
    ) -> ExecutionResult:

        merged = {}

        for value in context.outputs.values():
            if isinstance(value, dict):
                merged.update(value)

        return ExecutionResult(
            success=True,
            outputs=merged,
        ) 