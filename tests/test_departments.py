import uuid
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_list_departments():
    dept_name = "TestDept-" + uuid.uuid4().hex[:6]
    response = client.post("/departments/", json={"name": dept_name})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == dept_name

    response = client.get("/departments/")
    assert response.status_code == 200
    departments = response.json()
    assert any(d["name"] == dept_name for d in departments)