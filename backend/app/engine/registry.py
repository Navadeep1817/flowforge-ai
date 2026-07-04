"""
Executor registry.
"""

from __future__ import annotations

from app.engine.executors.base import BaseExecutor
from app.engine.executors.http_executor import HttpExecutor
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
     self.register(ValidationExecutor())
     self.register(TransformExecutor())
     self.register(HttpExecutor())
     self.register(ReturnExecutor())

    def register(
        self,
        executor: BaseExecutor,
    ) -> None:
        """
        Register an executor.
        """
        self._executors[executor.node_type] = executor

    def get(
        self,
        node_type: str,
    ) -> BaseExecutor:
        """
        Return the executor responsible for a node type.
        """
        try:
            return self._executors[node_type]
        except KeyError as exc:
            available = ", ".join(sorted(self._executors.keys()))
            raise ValueError(
                f"Unknown node type '{node_type}'. "
                f"Available node types: {available}"
            ) from exc

    def available(self) -> list[str]:
        """
        Return all registered node types.
        """
        return sorted(self._executors.keys())