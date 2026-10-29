from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_ready_structure():
    r = client.get("/ready")
    assert r.status_code in (200, 503)
    assert "status" in r.json()