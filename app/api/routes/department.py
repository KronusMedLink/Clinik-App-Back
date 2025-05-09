from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.department import DepartmentCreate, DepartmentOut
from app.crud import department as crud
from app.utils.response import success_response

router = APIRouter()

@router.post("/", status_code=201)
def create_department(department: DepartmentCreate, db: Session = Depends(get_db)):
    dept = crud.create_department(db, department)
    return success_response(DepartmentOut.model_validate(dept, from_attributes=True), 201)

@router.get("/")
def list_departments(db: Session = Depends(get_db)):
    departments = crud.get_departments(db)
    return success_response([DepartmentOut.model_validate(d, from_attributes=True).model_dump() for d in departments])

