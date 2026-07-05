"""
Template resolver.

Recursively resolves expressions inside
dicts, lists and strings.
"""

from __future__ import annotations

from app.engine.context import ExecutionContext
from app.engine.expression_resolver import ExpressionResolver


class TemplateResolver:

    def __init__(self) -> None:
        self._resolver = ExpressionResolver()

    def resolve(
        self,
        value,
        context: ExecutionContext,
    ):

        if isinstance(value, dict):
            return {
                k: self.resolve(v, context)
                for k, v in value.items()
            }

        if isinstance(value, list):
            return [
                self.resolve(v, context)
                for v in value
            ]

        return self._resolver.resolve(
            value,
            context,
        ) 