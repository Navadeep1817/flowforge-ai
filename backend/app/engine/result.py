"""
Workflow execution result.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ExecutionResult:
    """
    Result produced by a workflow node execution.
    """

    # Whether execution succeeded
    success: bool = True

    # Data produced by the node
    outputs: dict[str, Any] = field(default_factory=dict)

    # Whether the workflow should stop immediately
    terminate: bool = False

    # Error message (if any)
    error: str | None = None

    # Branch selected by control-flow nodes
    # Examples:
    # "true"
    # "false"
    # "success"
    # "failure"
    branch: str | None = None