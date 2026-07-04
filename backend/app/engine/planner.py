"""
Workflow planner.

Responsible for determining the next node(s) to execute.
"""

from __future__ import annotations

from app.engine.result import ExecutionResult
from app.engine.workflow import Workflow, WorkflowNode


class WorkflowPlanner:
    """
    Determines workflow execution order.
    """

    def get_start_node(self, workflow: Workflow) -> WorkflowNode:
        """
        Return the workflow's starting node.
        """
        return workflow.nodes[workflow.start_node]

    def get_next_node(
        self,
        workflow: Workflow,
        current: WorkflowNode,
        result: ExecutionResult,
    ) -> WorkflowNode | None:
        """
        Determine the next node to execute.
        """

        # Node explicitly chose the next node
        if result.next_nodes:
            return workflow.nodes[result.next_nodes[0]]

        # Follow workflow graph
        if current.next_nodes:
            return workflow.nodes[current.next_nodes[0]]

        return None