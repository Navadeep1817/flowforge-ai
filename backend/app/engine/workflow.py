"""
Workflow domain models.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class WorkflowNode:
    """
    Represents a single node in a workflow.
    """

    id: str
    type: str

    config: dict[str, Any] = field(default_factory=dict)

    # Supports:
    # ["next"]                     -> Sequential
    # {"true":"a","false":"b"}     -> Conditional
    next_nodes: list[str] | dict[str, str] = field(default_factory=list)


@dataclass(slots=True)
class Workflow:
    """
    Executable workflow.
    """

    id: str

    name: str

    start_node: str

    nodes: dict[str, WorkflowNode] = field(default_factory=dict)