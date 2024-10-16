# config.py
import os

class Config:
    FLASK_SECRET_KEY = 'mykey'

    API_USERS = {
        'front_carpooling': 'backend_password'
    }

    # Configuración de la base de datos
    DATABASE_HOST = os.getenv('DB_HOST', 'mysql-pruebadb.alwaysdata.net')  # Cambia si es necesario
    DATABASE_USER = os.getenv('DB_USER', 'pruebadb')  # Reemplaza con tu usuario
    DATABASE_PASSWORD = os.getenv('DB_PASSWORD', 'sdklg010')  # Reemplaza con tu contraseña
    DATABASE_NAME = os.getenv('DB_NAME', 'pruebadb_db')  # Nombre de la base de datos
