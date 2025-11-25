import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secretacontraseña")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "pool_size": 5,
        "max_overflow": 10,
        "pool_timeout": 30,
        "pool_recycle": 1800
    }

    INEGI_API_KEY = os.getenv("INEGI_API_KEY")
    MAPS_API_KEY = os.getenv("MAPS_API_KEY")
