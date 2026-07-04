"""
Workflow API schemas.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class WorkflowNodeSchema(BaseModel):
    id: str
    type: str
    config: dict[str, Any] = Field(default_factory=dict)
    next_nodes: list[str] = Field(default_factory=list)


class WorkflowSchema(BaseModel):
    id: str
    name: str
    start_node: str
    nodes: dict[str, WorkflowNodeSchema]


class ExecuteWorkflowRequest(BaseModel):
    workflow: WorkflowSchema
    request: dict[str, Any] = Field(default_factory=dict)


class ExecuteWorkflowResponse(BaseModel):
    success: bool
    outputs: dict[str, Any]
    error: str | None = None