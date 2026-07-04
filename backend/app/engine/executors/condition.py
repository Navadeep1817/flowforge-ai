"""
Condition executor.
"""

from __future__ import annotations

from app.engine.context import ExecutionContext
from app.engine.executors.base import BaseExecutor
from app.engine.result import ExecutionResult
from app.engine.workflow import WorkflowNode


class ConditionExecutor(BaseExecutor):

    node_type = "condition"

    async def execute(
        self,
        node: WorkflowNode,
        context: ExecutionContext,
    ) -> ExecutionResult:

        expression = node.config.get("condition")

        if expression is None:
            return ExecutionResult(
                success=False,
                error="Condition node requires 'condition' in config.",
            )

        try:
            value = bool(
                eval(
                    expression,
                    {},
                    context.request,
                )
            )
        except Exception as exc:
            return ExecutionResult(
                success=False,
                error=f"Condition evaluation failed: {exc}",
            )

        return ExecutionResult(
            success=True,
            branch="true" if value else "false",
        )