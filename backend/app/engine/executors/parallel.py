"""
Parallel executor.
"""

from __future__ import annotations

import asyncio

from app.engine.context import ExecutionContext
from app.engine.executors.base import BaseExecutor
from app.engine.result import ExecutionResult
from app.engine.workflow import WorkflowNode


class ParallelExecutor(BaseExecutor):

    node_type = "parallel"

    async def execute(
        self,
        node: WorkflowNode,
        context: ExecutionContext,
    ) -> ExecutionResult:
        """
        Parallel nodes don't execute work themselves.
        The WorkflowExecutor schedules their children concurrently.
        """

        return ExecutionResult(
            success=True,
            outputs={},
        ) 