"""
Validation executor.
"""

from __future__ import annotations

from app.engine.context import ExecutionContext
from app.engine.executors.base import BaseExecutor
from app.engine.result import ExecutionResult
from app.engine.workflow import WorkflowNode


class ValidationExecutor(BaseExecutor):
    """
    Validates workflow input.
    """

    node_type = "validation"

    async def execute(
        self,
        node: WorkflowNode,
        context: ExecutionContext,
    ) -> ExecutionResult:

        required_fields = node.config.get("required", [])

        missing = [
            field
            for field in required_fields
            if field not in context.request
        ]

        if missing:
            return ExecutionResult(
                success=False,
                error=f"Missing required fields: {', '.join(missing)}",
            )

        return ExecutionResult(success=True)