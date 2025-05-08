def test_create_staff_user(client):
    response = client.post("/users/", json={
        "username": "staffuser",
        "email": "staff@clinic.com",
        "password": "securepass123",
        "role": "staff"
    })
    print("DEBUG:", response.status_code, response.json())
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "staffuser"
    assert data["email"] == "staff@clinic.com"
    assert data["role"] == "staff"
