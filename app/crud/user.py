# app/crud/user.py

from sqlalchemy.orm import Session, joinedload
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pw,
        role=user.role,
        department_id=user.department_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # Precargar la relación department
    return (
        db.query(User)
        .options(joinedload(User.department))
        .filter(User.id == db_user.id)
        .first()
    )

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
