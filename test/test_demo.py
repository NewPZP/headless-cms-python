import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from framework.app.app import create_app
from fastapi.testclient import TestClient

client = TestClient(create_app())

def test_demo():
    response = client.get("/system/info")
    assert response.status_code == 200
    assert response.json() == "hello world"
    
