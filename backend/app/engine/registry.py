"""
Executor registry.
"""

from __future__ import annotations

from app.engine.executors.base import BaseExecutor
from app.engine.executors.return_executor import ReturnExecutor
from app.engine.executors.transform import TransformExecutor
from app.engine.executors.validation import ValidationExecutor

class ExecutorRegistry:
    """
    Registry of workflow executors.
    """

    def __init__(self) -> None:
        self._executors: dict[str, BaseExecutor] = {}

        self._register_defaults()

    def _register_defaults(self) -> None:
        """Register built-in executors."""
        self.register(ValidationExecutor())
        self.register(TransformExecutor())
        self.register(ReturnExecutor())

    def register(
        self,
        executor: BaseExecutor,
    ) -> None:
        """Register an executor."""

        self._executors[executor.node_type] = executor

    def get(
        self,
        node_type: str,
    ) -> BaseExecutor:
        """Return executor for a node type."""

        if node_type not in self._executors:
            raise ValueError(f"Unknown node type: {node_type}")

        return self._executors[node_type]

    def available(self) -> list[str]:
        """List registered executor types."""

        return sorted(self._executors.keys())