import sys
sys.path.append("..")
from framework.app.app import create_app
from fastapi.testclient import TestClient

client = TestClient(create_app())

def test_demo():
    response = client.get("/system/info")
    assert response.status_code == 200
    assert response.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }
