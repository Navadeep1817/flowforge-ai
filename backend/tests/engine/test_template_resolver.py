"""
Tests for the template resolver.
"""

from app.engine.context import ExecutionContext
from app.engine.template_resolver import TemplateResolver


def create_context() -> ExecutionContext:
    """
    Create a populated execution context for testing.
    """

    context = ExecutionContext()

    context.update_request(
        {
            "name": "Navadeep",
            "city": "Hyderabad",
            "age": 21,
        }
    )

    context.set_output(
        "transform",
        {
            "message": "Hello",
            "country": "India",
        },
    )

    return context


def test_string_resolution():

    resolver = TemplateResolver()

    context = create_context()

    result = resolver.resolve(
        "{{request.name}}",
        context,
    )

    assert result == "Navadeep"


def test_dictionary_resolution():

    resolver = TemplateResolver()

    context = create_context()

    result = resolver.resolve(
        {
            "username": "{{request.name}}",
            "location": "{{request.city}}",
        },
        context,
    )

    assert result == {
        "username": "Navadeep",
        "location": "Hyderabad",
    }


def test_list_resolution():

    resolver = TemplateResolver()

    context = create_context()

    result = resolver.resolve(
        [
            "{{request.name}}",
            "{{request.city}}",
            "{{request.age}}",
        ],
        context,
    )

    assert result == [
        "Navadeep",
        "Hyderabad",
        21,
    ]


def test_nested_resolution():

    resolver = TemplateResolver()

    context = create_context()

    result = resolver.resolve(
        {
            "user": {
                "name": "{{request.name}}",
                "city": "{{request.city}}",
            },
            "message": "{{transform.message}}",
            "country": "{{transform.country}}",
        },
        context,
    )

    assert result == {
        "user": {
            "name": "Navadeep",
            "city": "Hyderabad",
        },
        "message": "Hello",
        "country": "India",
    } 