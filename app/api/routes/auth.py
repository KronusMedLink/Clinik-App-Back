from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserOut
from app.crud.user import get_user_by_username
from app.core.security import verify_password, create_access_token
from app.utils.response import success_response, error_response

router = APIRouter(tags=["auth"])

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_username(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        return error_response("Invalid credentials", 401)

    access_token = create_access_token(data={"sub": user.username, "role": user.role})
    return success_response({"access_token": access_token, "token_type": "bearer"})
