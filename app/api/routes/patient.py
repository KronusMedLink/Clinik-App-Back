from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import patient as crud
from app.schemas.patient import Patient, PatientCreate
from app.core.deps import get_db
from app.dependencies import require_role, get_current_user

router = APIRouter(
    tags=["patients"]
)

@router.post("/", response_model=Patient)
def create_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_role("staff"))
):
    return crud.create_patient(db=db, patient=patient)

@router.get("/", response_model=list[Patient])
def read_patients(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return crud.get_patients(db=db, skip=skip, limit=limit)

@router.get("/{patient_id}", response_model=Patient)
def read_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    db_patient = crud.get_patient(db=db, patient_id=patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient
