import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_review_feedback_endpoint():
    response = client.post("/review/feedback", json={"review": "Great product!"})
    assert response.status_code == 200
    data = response.json()
    assert data["sentiment"] == "positive"
    assert isinstance(data["readability_score"], float)
    assert isinstance(data["suggestions"], list)
