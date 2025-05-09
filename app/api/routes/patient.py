from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import patient as crud
from app.schemas.patient import Patient, PatientCreate
from app.core.deps import get_db
from app.dependencies import require_role, get_current_user
from app.utils.response import success_response, error_response

router = APIRouter(tags=["patients"])

@router.post("/")
def create_patient(patient: PatientCreate, db: Session = Depends(get_db), current_user=Depends(require_role("staff"))):
    patient_created = crud.create_patient(db=db, patient=patient)
    return success_response(Patient.model_validate(patient_created, from_attributes=True), 201)

@router.get("/")
def read_patients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    patients = crud.get_patients(db=db, skip=skip, limit=limit)
    return success_response([Patient.model_validate(p, from_attributes=True) for p in patients])

@router.get("/{patient_id}")
def read_patient(patient_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_patient = crud.get_patient(db=db, patient_id=patient_id)
    if not db_patient:
        return error_response("Patient not found", 404)
    return success_response(Patient.model_validate(db_patient, from_attributes=True))