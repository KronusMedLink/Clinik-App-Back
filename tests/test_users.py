import uuid
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_staff_user():
    username = "staff_test_" + uuid.uuid4().hex[:6]
    email = f"{username}@clinic.com"
    response = client.post("/users/", json={
        "username": username,
        "email": email,
        "password": "testpassword",
        "role": "staff"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == username
    assert data["role"] == "staff"