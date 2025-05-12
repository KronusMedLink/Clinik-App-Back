from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud.user import create_user, get_user_by_email
from app.schemas.user import UserCreate
import os

def init_admin():
    db: Session = SessionLocal()
    admin_email = os.getenv("ADMIN_EMAIL", "admin@example.com")
    admin_password = os.getenv("ADMIN_PASSWORD", "admin123")

    user = get_user_by_email(db, email=admin_email)
    if not user:
        admin_user = UserCreate(
            username="admin",             
            email=admin_email,
            password=admin_password,
            role="admin"
        )
        create_user(db=db, user=admin_user)
        print("✅ Admin user created.")
    else:
        print("ℹ️ Admin user already exists.")
    db.close()
