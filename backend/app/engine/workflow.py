"""
Workflow domain models.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
@dataclass
class WorkflowNode:
    id: str
    type: str
    config: dict
    next_nodes: Any
@dataclass(slots=True)
class Workflow:
    """
    Executable workflow.
    """

    id: str

    name: str

    start_node: str

    nodes: dict[str, WorkflowNode]