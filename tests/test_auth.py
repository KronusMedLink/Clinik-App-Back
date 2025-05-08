def test_login_returns_token(client):
    # Crear usuario
    client.post("/users/", json={
        "username": "auth_test_user",
        "email": "auth_test_user@clinic.com",
        "password": "authpass123",
        "role": "staff"
    })

    # Login correcto en /auth/token
    response = client.post("/auth/token", data={
        "username": "auth_test_user",
        "password": "authpass123"
    })

    assert response.status_code == 200
    assert "access_token" in response.json()
