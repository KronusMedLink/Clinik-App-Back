def test_create_and_list_departments(client):
    response = client.post("/departments/", json={"name": "Cardiología Test"})
    assert response.status_code in (200, 201)

    list_response = client.get("/departments/")
    assert list_response.status_code == 200
    assert any(dep["name"] == "Cardiología Test" for dep in list_response.json())
