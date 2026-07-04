"""
Workflow execution context.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ExecutionContext:
    """
    Shared runtime state for an executing workflow.
    """

    request: dict[str, Any] = field(default_factory=dict)

    variables: dict[str, Any] = field(default_factory=dict)

    outputs: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)

    errors: list[str] = field(default_factory=list)

    def update_request(
        self,
        payload: dict[str, Any],
    ) -> None:
        """
        Replace request payload.
        """
        self.request = payload

    def get_request_value(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Retrieve a value from the request payload.
        """
        return self.request.get(key, default)

    def set_variable(
        self,
        key: str,
        value: Any,
    ) -> None:
        self.variables[key] = value

    def get_variable(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        return self.variables.get(key, default)

    def set_output(
        self,
        node_id: str,
        value: Any,
    ) -> None:
        self.outputs[node_id] = value

    def get_output(
        self,
        node_id: str,
    ) -> Any:
        return self.outputs.get(node_id)

    def add_error(
        self,
        message: str,
    ) -> None:
        self.errors.append(message)