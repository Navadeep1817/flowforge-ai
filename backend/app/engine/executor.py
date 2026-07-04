"""
Workflow execution engine.
"""

from __future__ import annotations

from app.engine.context import ExecutionContext
from app.engine.planner import WorkflowPlanner
from app.engine.result import ExecutionResult
from app.engine.runner import NodeRunner
from app.engine.workflow import Workflow


class WorkflowExecutor:
    """
    Coordinates workflow execution.

    The executor is responsible for:
    - Starting execution
    - Delegating node execution to the runner
    - Delegating traversal decisions to the planner
    - Updating execution context
    """

    def __init__(
        self,
        planner: WorkflowPlanner,
        runner: NodeRunner,
    ) -> None:
        self._planner = planner
        self._runner = runner

    async def execute(
        self,
        workflow: Workflow,
        context: ExecutionContext,
    ) -> ExecutionResult:
        """
        Execute a workflow from its start node until completion.
        """

        current_node = self._planner.get_start_node(workflow)

        result = ExecutionResult()

        while current_node is not None:

            result = await self._runner.run(
                current_node,
                context,
            )

            if result.outputs:
                context.set_output(
                    current_node.id,
                    result.outputs,
                )

            if not result.success:
                return result

            if result.terminate:
                return result

            current_node = self._planner.get_next_node(
                workflow=workflow,
                current=current_node,
                result=result,
            )

        return result