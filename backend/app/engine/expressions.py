"""
Expression evaluation engine.
"""

from __future__ import annotations

from app.engine.context import ExecutionContext


class ExpressionEngine:
    """
    Resolves runtime expressions.
    """

    REQUEST_PREFIX = "$request."
    OUTPUT_PREFIX = "$outputs."

    def resolve(
        self,
        value,
        context: ExecutionContext,
    ):
        """
        Resolve one expression.
        """

        if not isinstance(value, str):
            return value

        if value.startswith(self.REQUEST_PREFIX):

            return context.get_request_value(
                value[len(self.REQUEST_PREFIX):]
            )

        if value.startswith(self.OUTPUT_PREFIX):

            return context.get_output_value(
                value[len(self.OUTPUT_PREFIX):]
            )

        return value 