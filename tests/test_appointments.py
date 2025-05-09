import uuid
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_list_appointments():
    dept_name = "Cardiology-" + uuid.uuid4().hex[:6]
    client.post("/departments/", json={"name": dept_name})

    doctor_username = "doctor1-" + uuid.uuid4().hex[:6]
    client.post("/users/", json={
        "username": doctor_username,
        "email": f"{doctor_username}@clinic.com",
        "password": "docpass",
        "role": "doctor",
        "department_id": 1
    })

    staff_username = "staff1-" + uuid.uuid4().hex[:6]
    staff_email = f"{staff_username}@clinic.com"
    client.post("/users/", json={
        "username": staff_username,
        "email": staff_email,
        "password": "staffpass",
        "role": "staff"
    })
    token_res = client.post("/auth/token", data={
        "username": staff_username,
        "password": "staffpass"
    })
    token = token_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}    

    patient_res = client.post("/patients/", json={
        "name": "Patient Test",
        "age": 40,
        "gender": "female"
    }, headers=headers)
    patient_id = patient_res.json()["id"]

    appointment_res = client.post("/appointments/", json={
        "patient_id": patient_id,
        "doctor_id": 1,
        "appointment_date": "2025-05-09T14:00:00",
        "reason": "Routine check"
    }, headers=headers)

    assert appointment_res.status_code == 201
    assert appointment_res.json()["reason"] == "Routine check"