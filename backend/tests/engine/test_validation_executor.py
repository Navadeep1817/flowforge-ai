import pytest

from app.engine.context import ExecutionContext
from app.engine.executor import WorkflowExecutor
from app.engine.planner import WorkflowPlanner
from app.engine.registry import ExecutorRegistry
from app.engine.runner import NodeRunner
from app.engine.workflow import Workflow, WorkflowNode


@pytest.mark.asyncio
async def test_validation_workflow():

    workflow = Workflow(
        id="1",
        name="validation",
        start_node="validation",
        nodes={
            "validation": WorkflowNode(
                id="validation",
                type="validation",
                config={
                    "required": [
                        "name",
                        "email",
                    ]
                },
                next_nodes=["return"],
            ),
            "return": WorkflowNode(
                id="return",
                type="return",
            ),
        },
    )

    registry = ExecutorRegistry()

    planner = WorkflowPlanner()

    runner = NodeRunner(registry)

    executor = WorkflowExecutor(
        planner,
        runner,
    )

    context = ExecutionContext()

    context.update_request(
        {
            "name": "Navadeep",
            "email": "test@example.com",
        }
    )

    result = await executor.execute(
        workflow,
        context,
    )

    assert result.success 