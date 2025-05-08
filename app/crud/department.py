from sqlalchemy.orm import Session
from app.models.department import Department
from app.schemas.department import DepartmentCreate

def create_department(db: Session, department: DepartmentCreate):
    db_department = Department(**department.dict())
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department

def get_departments(db: Session):
    return db.query(Department).all()
