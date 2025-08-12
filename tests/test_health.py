from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_route_returns_ok():
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data.get("status") == "ok"
    assert "version" in data and isinstance(data["version"], str)
