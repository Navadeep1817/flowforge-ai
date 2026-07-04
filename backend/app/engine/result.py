"""
Workflow execution result models.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ExecutionResult:
    """
    Result returned by every workflow node execution.
    """

    success: bool = True

    outputs: dict[str, Any] = field(default_factory=dict)

    # Supports sequential, conditional, and parallel execution
    next_nodes: list[str] = field(default_factory=list)

    terminate: bool = False

    warnings: list[str] = field(default_factory=list)

    error: str | None = None