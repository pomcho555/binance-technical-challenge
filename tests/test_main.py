from fastapi.testclient import TestClient
from questions.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
