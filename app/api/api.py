from fastapi import APIRouter
from app.api.routes import auth, users, patient, appointment, department

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(patient.router, prefix="/patients", tags=["patients"])
api_router.include_router(appointment.router, prefix="/appointments", tags=["appointments"])
api_router.include_router(department.router, prefix="/departments", tags=["departments"])  # <- Este importa
