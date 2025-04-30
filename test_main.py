from fastapi.testclient import TestClient
from hello_world import app

client = TestClient(app)

def test_json_output():
    response = client.get("/?output=json")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    data = response.json()
    assert "message" in data