import pytest

from app.engine.context import ExecutionContext
from app.engine.executor import WorkflowExecutor
from app.engine.planner import WorkflowPlanner
from app.engine.registry import ExecutorRegistry
from app.engine.runner import NodeRunner
from app.engine.workflow import Workflow, WorkflowNode


@pytest.mark.asyncio
async def test_simple_workflow():

    workflow = Workflow(
        id="1",
        name="hello",
        start_node="transform",
        nodes={
            "transform": WorkflowNode(
                id="transform",
                type="transform",
                config={
                    "variables": {
                        "message": "Hello FlowForge"
                    }
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

    result = await executor.execute(
        workflow,
        context,
    )

    assert result.success

    assert context.get_variable("message") == "Hello FlowForge" 