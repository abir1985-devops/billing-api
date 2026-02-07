import os
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_ok():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_health_db_ok():
    # This test requires DATABASE_URL to be set by CI
    assert os.getenv("DATABASE_URL"), "DATABASE_URL must be set for DB health test"
    r = client.get("/health/db")
    assert r.status_code == 200
    assert r.json() == {"database": "ok"}
