"""
Workflow execution service.
"""

from __future__ import annotations

from app.engine.context import ExecutionContext
from app.engine.executor import WorkflowExecutor
from app.engine.planner import WorkflowPlanner
from app.engine.registry import ExecutorRegistry
from app.engine.runner import NodeRunner
from app.engine.workflow import Workflow, WorkflowNode
from app.schemas.workflow import (
    ExecuteWorkflowRequest,
    ExecuteWorkflowResponse,
)


class ExecutionService:
    """
    Bridge between the API layer and the workflow engine.
    """

    def __init__(self) -> None:

        registry = ExecutorRegistry()

        planner = WorkflowPlanner()

        runner = NodeRunner(registry)

        self.executor = WorkflowExecutor(
            planner,
            runner,
        )

    async def execute(
        self,
        payload: ExecuteWorkflowRequest,
    ) -> ExecuteWorkflowResponse:

        workflow = Workflow(
            id=payload.workflow.id,
            name=payload.workflow.name,
            start_node=payload.workflow.start_node,
            nodes={
                node_id: WorkflowNode(
    id=node.id,
    type=node.type,
    config=node.config,
    next_nodes=node.next_nodes,
)
                for node_id, node in payload.workflow.nodes.items()
            },
        )

        context = ExecutionContext()

        context.update_request(payload.request)

        result = await self.executor.execute(
            workflow,
            context,
        )

        return ExecuteWorkflowResponse(
            success=result.success,
            outputs=context.outputs,
            error=result.error,
        ) 