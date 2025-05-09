from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login_returns_token():
    # Crear usuario staff (ignorar si ya existe)
    client.post("/users/", json={
        "username": "auth_test_user",
        "email": "auth_test_user@clinic.com",
        "password": "authpass123",
        "role": "staff"
    })

    # Login
    response = client.post("/auth/token", data={
        "username": "auth_test_user",
        "password": "authpass123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
