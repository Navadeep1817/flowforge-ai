"""
Workflow planner.

Determines the next node to execute based on the current node
and the execution result.
"""

from __future__ import annotations

from app.engine.result import ExecutionResult
from app.engine.workflow import Workflow, WorkflowNode


class WorkflowPlanner:
    """
    Determines workflow execution order.
    """

    def get_start_node(
        self,
        workflow: Workflow,
    ) -> WorkflowNode:
        """
        Return the workflow's start node.
        """
        return workflow.nodes[workflow.start_node]

   

from app.engine.result import ExecutionResult
from app.engine.workflow import Workflow, WorkflowNode


class WorkflowPlanner:
    """
    Determines workflow execution order.
    """

    def get_start_node(
        self,
        workflow: Workflow,
    ) -> WorkflowNode:
        return workflow.nodes[workflow.start_node]

    def get_next_node(
        self,
        workflow: Workflow,
        current: WorkflowNode,
        result: ExecutionResult,
    ) -> WorkflowNode | None:

        # No next node
        if not current.next_nodes:
            return None

        # Branching node (Condition)
        if isinstance(current.next_nodes, dict):

            next_node_id = current.next_nodes.get(result.branch)

            if next_node_id is None:
                raise ValueError(
                    f"No branch '{result.branch}' defined for node '{current.id}'."
                )

            return workflow.nodes[next_node_id]

        # Sequential node
        next_node_id = current.next_nodes[0]

        return workflow.nodes[next_node_id]