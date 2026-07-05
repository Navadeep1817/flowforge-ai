import pytest

from app.engine.context import ExecutionContext
from app.engine.executors.merge import MergeExecutor
from app.engine.workflow import WorkflowNode


@pytest.mark.asyncio
async def test_merge_executor():

    context = ExecutionContext()

    context.set_output(
        "http1",
        {
            "name": "Navadeep",
        },
    )

    context.set_output(
        "http2",
        {
            "city": "Hyderabad",
        },
    )

    executor = MergeExecutor()

    node = WorkflowNode(
        id="merge",
        type="merge",
        config={},
        next_nodes=[],
    )

    result = await executor.execute(
        node,
        context,
    )

    assert result.success

    assert result.outputs == {
        "name": "Navadeep",
        "city": "Hyderabad",
    } 