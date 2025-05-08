from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    appointment_date = Column(DateTime, nullable=False)
    reason = Column(String, nullable=False)
    doctor_id = Column(Integer, ForeignKey("users.id"))
    patient_id = Column(Integer, ForeignKey("patients.id"))

    doctor = relationship("User", back_populates="appointments")
    patient = relationship("Patient", back_populates="appointments")
