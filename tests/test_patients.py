from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_patients():
    client.post("/users/", json={
        "username": "staff2",
        "email": "staff2@clinic.com",
        "password": "staffpass",
        "role": "staff"
    })

    token_res = client.post("/auth/token", data={
        "username": "staff2",
        "password": "staffpass"
    })
    token = token_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}    

    response = client.post("/patients/", json={
        "name": "John Doe",
        "age": 30,
        "gender": "male"
    }, headers=headers)

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John Doe"