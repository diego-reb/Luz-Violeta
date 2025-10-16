import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secretacontraseña")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI",
        "postgresql+psycopg2://postgres:postgres@localhost:5432/LuzVioleta"
        ##"postgresql+psycopg2://postgres:lenovoblue@localhost:5432/luzvioleta"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    INEGI_API_KEY = os.getenv("INEGI_API_KEY")