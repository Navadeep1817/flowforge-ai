"""
Workflow execution state.
"""

from __future__ import annotations

from enum import Enum


class ExecutionState(str, Enum):
    CREATED = "created"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    TERMINATED = "terminated" 