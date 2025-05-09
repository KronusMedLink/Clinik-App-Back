from pydantic import BaseModel
from datetime import datetime

class AppointmentBase(BaseModel):
    doctor_id: int
    appointment_date: datetime
    reason: str

class AppointmentCreate(AppointmentBase):
    patient_id: int
    doctor_id: int  
    appointment_date: datetime
    reason: str
class AppointmentOut(AppointmentBase):
    id: int
    patient_id: int

    class Config:
        from_attributes = True
