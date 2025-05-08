from fastapi import FastAPI
from app.database import engine, Base
from app.api.api import api_router

from app.models import user, patient, appointment, department

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(api_router)  
