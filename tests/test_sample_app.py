"""Tests for the AppSec CI/CD demo application.

Author: chandu
"""

from app.sample_app import app


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_security_headers_are_set():
    client = app.test_client()
    response = client.get("/")
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "DENY"
    assert response.headers["Referrer-Policy"] == "no-referrer"
    assert response.headers["Content-Security-Policy"] == "default-src 'self'"


def test_profile_allows_safe_username():
    client = app.test_client()
    response = client.get("/api/profile/chandu_security")
    assert response.status_code == 200
    assert response.get_json()["username"] == "chandu_security"


def test_profile_rejects_unsafe_username():
    client = app.test_client()
    response = client.get("/api/profile/<script>")
    assert response.status_code == 400
