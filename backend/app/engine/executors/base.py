"""
Base executor for workflow nodes.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from app.engine.context import ExecutionContext
from app.engine.result import ExecutionResult
from app.engine.workflow import WorkflowNode


class BaseExecutor(ABC):
    """
    Base class for all node executors.
    """

    node_type: str

    @abstractmethod
    async def execute(
        self,
        node: WorkflowNode,
        context: ExecutionContext,
    ) -> ExecutionResult:
        """
        Execute a workflow node.
        """
        raise NotImplementedError 