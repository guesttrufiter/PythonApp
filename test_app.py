"""
Pytest Unit Test Suite
Validates application routes and health check response data.
"""

from app import app
import pytest

@pytest.fixture
def client():
    """Configure test client for Flask application testing."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the root home endpoint response status and message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "Welcome to the Python CI/CD App"

def test_health_check(client):
    """Test the health check endpoint response status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"