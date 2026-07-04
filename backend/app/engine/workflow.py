"""
Workflow domain models.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class WorkflowNode:
    """
    Represents a node in a workflow graph.
    """

    id: str

    type: str

    config: dict[str, Any] = field(default_factory=dict)

    # Outgoing edges in the workflow graph
    next_nodes: list[str] = field(default_factory=list)


@dataclass(slots=True)
class Workflow:
    """
    Executable workflow.
    """

    id: str

    name: str

    start_node: str

    nodes: dict[str, WorkflowNode]