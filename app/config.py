import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secretacontraseña")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI",
        "postgresql://postgres:postgres@localhost:5432/LuzVioleta"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    INEGI_API_KEY = os.getenv("INEGI_API_KEY")