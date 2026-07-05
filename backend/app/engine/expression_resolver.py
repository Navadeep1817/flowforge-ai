"""
Expression resolver.

Supports:

{{request.name}}
{{transform.message}}
{{http.json.id}}
"""

from __future__ import annotations

import re

from app.engine.context import ExecutionContext


_PATTERN = re.compile(r"\{\{\s*(.*?)\s*\}\}")


class ExpressionResolver:

    def resolve(
        self,
        value,
        context: ExecutionContext,
    ):

        if not isinstance(value, str):
            return value

        match = _PATTERN.fullmatch(value)

        if not match:
            return value

        path = match.group(1)

        return context.lookup(path) 