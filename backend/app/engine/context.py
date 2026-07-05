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

    def get_request_value(
        self,
        key: str,
    ):
        """
        Return a value from the incoming request using dot notation.
        """
        return self._get_nested_value(self.request, key)

    def get_output_value(
        self,
        key: str,
    ):
        """
        Return a value from workflow outputs using dot notation.
        """
        return self._get_nested_value(self.outputs, key)

    def lookup(
        self,
        path: str,
    ):
        """
        Lookup values using dot notation.

        Examples:
            request.name
            transform.message
            http.json.id
        """

        parts = path.split(".")

        current = {
            "request": self.request,
            **self.outputs,
        }

        for part in parts:
            if isinstance(current, dict):
                current = current.get(part)
            else:
                return None

            if current is None:
                return None

        return current

    @staticmethod
    def _get_nested_value(
        data: dict,
        path: str,
    ):
        """
        Resolve nested dictionary values.

        Example:
            outputs.http.json.name
        """

        current = data

        for part in path.split("."):
            if not isinstance(current, dict):
                return None

            current = current.get(part)

            if current is None:
                return None

        return current