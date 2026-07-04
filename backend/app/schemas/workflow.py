"""
Workflow API schemas.
"""

from __future__ import annotations

from typing import Any, Union

from pydantic import BaseModel, Field
from typing import Union

class WorkflowNodeSchema(BaseModel):
    id: str
    type: str
    config: dict = {}
    next_nodes: Union[list[str], dict[str, str]]


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