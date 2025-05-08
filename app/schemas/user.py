# app/schemas/user.py

from pydantic import BaseModel, EmailStr, model_validator
from typing import Optional
from app.schemas.department import Department

class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: str
    department_id: Optional[int] = None

class UserCreate(UserBase):
    password: str

    @model_validator(mode="after")
    def validate_department_for_doctor(cls, values):
        role = values.role
        department_id = values.department_id

        if role == "doctor" and not department_id:
            raise ValueError("A doctor must be assigned to a department (department_id required).")
        if role in ["admin", "staff"] and department_id is not None:
            raise ValueError(f"A {role} should not have a department.")
        return values

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(UserBase):
    id: int
    department: Optional[Department] = None

    class Config:
        from_attributes = True
