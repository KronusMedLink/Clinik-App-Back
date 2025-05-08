from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.crud.user import create_user, get_user_by_username
from app.database import get_db
from app.dependencies import get_current_user, require_role
from app.models.department import Department 

router = APIRouter(
    tags=["users"]
)

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    # ✅ Validar que el departamento exista si fue enviado
    if user.department_id is not None:
        department = db.query(Department).filter(Department.id == user.department_id).first()
        if not department:
            raise HTTPException(status_code=400, detail="Department ID not found")

    return create_user(db, user)

@router.get("/me", response_model=UserOut)
def read_current_user(current_user=Depends(get_current_user)):
    return current_user
