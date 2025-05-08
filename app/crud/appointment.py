from sqlalchemy.orm import Session
from app.models.appointment import Appointment
from app.models.patient import Patient
from app.models.user import User
from app.schemas.appointments import AppointmentCreate

def create_appointment(db: Session, appointment: AppointmentCreate):
    # Verificar existencia de paciente
    patient = db.query(Patient).filter(Patient.id == appointment.patient_id).first()
    if not patient:
        raise ValueError("Patient ID not found")

    # Verificar existencia de doctor y rol
    doctor = db.query(User).filter(User.id == appointment.doctor_id).first()
    if not doctor or doctor.role != "doctor":
        raise ValueError("Doctor ID invalid or not a doctor")

    db_appointment = Appointment(
        patient_id=appointment.patient_id,
        doctor_id=appointment.doctor_id,
        doctor_name=appointment.doctor_name,
        appointment_date=appointment.appointment_date,
        reason=appointment.reason
    )
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment
