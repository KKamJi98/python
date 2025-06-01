from fastapi.testclient import TestClient

from app.main import app


def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_create_user(client):
    response = client.post(
        "/users/",
        json={"name": "Test User", "email": "test@example.com"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test User"
    assert data["email"] == "test@example.com"
    assert "id" in data


def test_create_user_duplicate_email(client):
    # First create a user
    client.post(
        "/users/",
        json={"name": "Test User", "email": "duplicate@example.com"},
    )

    # Try to create another user with the same email
    response = client.post(
        "/users/",
        json={"name": "Another User", "email": "duplicate@example.com"},
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"


def test_read_users(client):
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
