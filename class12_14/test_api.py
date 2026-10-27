import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_requests_have_different_ids(client):
    # TODO: send two GET /health requests.
    request1 = client.get("/health")
    request2 = client.get("/health")
    # Assert that their X-Request-ID header values are different.
    assert request1.headers["X-Request-ID"] != request2.headers["X-Request-ID"]