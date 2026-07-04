import pytest

from app.engine.context import ExecutionContext
from app.engine.executors.http_executor import HttpExecutor
from app.engine.workflow import WorkflowNode


@pytest.mark.asyncio
async def test_http_executor():

    node = WorkflowNode(
        id="http",
        type="http",
        config={
            "method": "GET",
            "url": "https://httpbin.org/get",
        },
        next_nodes=[],
    )

    context = ExecutionContext()

    executor = HttpExecutor()

    result = await executor.execute(
        node,
        context,
    )

    assert result.success 