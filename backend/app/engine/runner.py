"""
Workflow node runner.
"""

from __future__ import annotations

from app.engine.context import ExecutionContext
from app.engine.registry import ExecutorRegistry
from app.engine.result import ExecutionResult
from app.engine.workflow import WorkflowNode


class NodeRunner:
    """
    Executes a single workflow node.
    """

    def __init__(
        self,
        registry: ExecutorRegistry,
    ) -> None:
        self._registry = registry

    async def run(
        self,
        workflow_node: WorkflowNode,
        context: ExecutionContext,
    ) -> ExecutionResult:
        """
        Execute a workflow node.
        """

        executor = self._registry.get(
            workflow_node.type,
        )

        return await executor.execute(
            workflow_node,
            context,
        ) 