"""
End-to-end workflow execution test.
"""

from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_execute_workflow():

    payload = {
        "workflow": {
            "id": "demo",
            "name": "Demo",
            "start_node": "transform",
            "nodes": {
                "transform": {
                    "id": "transform",
                    "type": "transform",
                    "config": {
                        "variables": {
                            "name": "{{request.name}}",
                            "city": "{{request.city}}",
                        }
                    },
                    "next_nodes": [
                        "return"
                    ],
                },
                "return": {
                    "id": "return",
                    "type": "return",
                    "config": {},
                    "next_nodes": [],
                },
            },
        },
        "request": {
            "name": "Navadeep",
            "city": "Hyderabad",
        },
    }

    response = client.post(
        "/executions/execute",
        json=payload,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True

    assert data["outputs"]["transform"]["name"] == "Navadeep"

    assert data["outputs"]["transform"]["city"] == "Hyderabad" 