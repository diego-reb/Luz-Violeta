import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "secretacontraseña")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI",
        "postgresql://neondb_owner:npg_A9jkaF3plBRe@ep-polished-art-a407tamf-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    INEGI_API_KEY = os.getenv("INEGI_API_KEY")