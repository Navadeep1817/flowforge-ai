"""
Recursive mapping engine.
"""

from __future__ import annotations

from app.engine.context import ExecutionContext
from app.engine.expressions import ExpressionEngine


class MappingEngine:

    def __init__(self):

        self._expressions = ExpressionEngine()

    def resolve(
        self,
        value,
        context: ExecutionContext,
    ):

        if isinstance(value, dict):

            return {
                key: self.resolve(val, context)
                for key, val in value.items()
            }

        if isinstance(value, list):

            return [
                self.resolve(item, context)
                for item in value
            ]

        return self._expressions.resolve(
            value,
            context,
        ) 