"""
Base workflow node.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from app.engine.context import ExecutionContext
from app.engine.result import ExecutionResult


class BaseNode(ABC):
    """
    Base class for every workflow node.
    """

    def __init__(
        self,
        node_id: str,
        config: dict[str, Any] | None = None,
    ) -> None:
        self.node_id = node_id
        self.config = config or {}

    @property
    @abstractmethod
    def node_type(self) -> str:
        """
        Unique node type identifier.
        """
        raise NotImplementedError

    def validate(self) -> None:
        """
        Validate node configuration.

        Override when a node requires validation.
        """
        return

    @abstractmethod
    async def execute(
        self,
        context: ExecutionContext,
    ) -> ExecutionResult:
        """
        Execute the node.
        """
        raise NotImplementedError

    async def cleanup(
        self,
        context: ExecutionContext,
    ) -> None:
        """
        Cleanup hook executed after node completion.
        """
        return

    def to_dict(self) -> dict[str, Any]:
        """
        Serialize node.
        """

        return {
            "id": self.node_id,
            "type": self.node_type,
            "config": self.config,
        } 