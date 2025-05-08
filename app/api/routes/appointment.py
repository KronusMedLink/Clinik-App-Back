from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.appointments import AppointmentCreate, AppointmentOut
from app.crud import appointment as crud
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=AppointmentOut)
def create_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "staff":
        raise HTTPException(status_code=403, detail="Only staff can create appointments")
    try:
        return crud.create_appointment(db, appointment)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[AppointmentOut])
def list_appointments(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud.get_appointments_for_user(db, current_user)
