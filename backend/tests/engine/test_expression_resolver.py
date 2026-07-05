from app.engine.context import ExecutionContext
from app.engine.expression_resolver import ExpressionResolver


def test_expression():

    context = ExecutionContext()

    context.update_request(
        {
            "name": "Navadeep"
        }
    )

    resolver = ExpressionResolver()

    assert resolver.resolve(
        "{{request.name}}",
        context,
    ) == "Navadeep" 