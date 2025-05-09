from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.appointments import AppointmentCreate, AppointmentOut
from app.crud import appointment as crud
from app.dependencies import get_current_user
from app.models.user import User
from app.utils.response import success_response, error_response

router = APIRouter()

@router.post("/")
def create_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role != "staff":
        return error_response("Only staff can create appointments", 403)
    try:
        created = crud.create_appointment(db, appointment)
        return success_response(
    AppointmentOut.model_validate(created, from_attributes=True).model_dump(),
    status_code=201
)
    except ValueError as e:
        return error_response(str(e), 400)

@router.get("/")
def list_appointments(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    appts = crud.get_appointments_for_user(db, current_user)
    return success_response([
    AppointmentOut.model_validate(a, from_attributes=True).model_dump() for a in appts
])
