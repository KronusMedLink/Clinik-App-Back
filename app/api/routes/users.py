from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.crud.user import create_user, get_user_by_username
from app.database import get_db
from app.dependencies import get_current_user
from app.models.department import Department
from app.utils.response import success_response, error_response

router = APIRouter(tags=["users"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    if db_user:
        return error_response("Username already registered", 400)

    if user.department_id is not None:
        department = db.query(Department).filter(Department.id == user.department_id).first()
        if not department:
            return error_response("Department ID not found", 400)

    new_user = create_user(db, user)
    return success_response(UserOut.model_validate(new_user, from_attributes=True), 201)

@router.get("/me")
def read_current_user(current_user=Depends(get_current_user)):
    return success_response(UserOut.model_validate(new_user, from_attributes=True).model_dump(), 201)
