from fastapi.testclient import TestClient
from hello_world import app  # zakładam, że to Twój główny FastAPI app

client = TestClient(app)

def test_msg_with_output():
    response = client.get("/?output=plain")
    assert response.status_code == 200
    assert "Hello" in response.text  # dostosuj, jeśli zwracasz coś innego

def test_outputs():
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello" in response.text  # lub odpowiedni klucz, np. JSON