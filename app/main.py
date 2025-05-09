import time
import sqlalchemy
from sqlalchemy.exc import OperationalError
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.database import engine, Base
from app.api.api import api_router
from app.models import user, patient, appointment, department

app = FastAPI()

# Intentar conexión a PostgreSQL (espera activa)
for _ in range(10):
    try:
        with engine.connect() as conn:
            break
    except OperationalError:
        print("PostgreSQL no está listo. Esperando 1s...")
        time.sleep(1)
else:
    print("❌ No se pudo conectar a PostgreSQL tras múltiples intentos.")
    raise RuntimeError("Database not ready")

Base.metadata.create_all(bind=engine)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
