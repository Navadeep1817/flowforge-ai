"""
Workflow execution endpoints.
"""

from __future__ import annotations

from fastapi import APIRouter

from app.schemas.workflow import (
    ExecuteWorkflowRequest,
    ExecuteWorkflowResponse,
)
from app.services.execution_service import ExecutionService

router = APIRouter(
    prefix="/executions",
    tags=["Executions"],
)

service = ExecutionService()


@router.post(
    "/execute",
    response_model=ExecuteWorkflowResponse,
)
async def execute_workflow(
    payload: ExecuteWorkflowRequest,
) -> ExecuteWorkflowResponse:
    """
    Execute a workflow.
    """

    return await service.execute(payload) 