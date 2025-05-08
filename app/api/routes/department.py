from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.department import DepartmentCreate, DepartmentOut
from app.crud import department as crud

router = APIRouter()

@router.post("/", response_model=DepartmentOut, status_code=201)
def create_department(department: DepartmentCreate, db: Session = Depends(get_db)):
    return crud.create_department(db, department)

@router.get("/", response_model=list[DepartmentOut])
def list_departments(db: Session = Depends(get_db)):
    return crud.get_departments(db)
