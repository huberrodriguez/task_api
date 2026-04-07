import os

class Config:
    SECRET_KEY = "mi_clave_secreta"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:159357@localhost:5432/task_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "mi_jwt_secreto"