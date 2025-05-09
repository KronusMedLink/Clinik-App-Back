import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cargar la URL de la base de datos desde la variable de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

# Crear el motor de conexión
engine = create_engine(DATABASE_URL)

# Configurar la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos ORM
Base = declarative_base()

# Dependencia para obtener la sesión en los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
