import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200


def test_health_endpoint(client):
    response = client.get("/health")
    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "API is running"


def test_programs_endpoint(client):
    response = client.get("/programs")

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_add_member(client):
    member_data = {
        "name": "Jatin",
        "age": 25,
        "goal": "Fat Loss"
    }

    response = client.post("/members", json=member_data)

    assert response.status_code == 200
    assert response.get_json()["member"]["name"] == "Jatin"