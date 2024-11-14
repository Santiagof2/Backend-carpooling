
from datetime import datetime
from server.models import User, Driver
from flask import jsonify
from dotenv import load_dotenv
import os

load_dotenv()

# ------------------------- Funciones varias que se repiten en el proyecto -------------------------
def get_mp_public_key():
    MP_PUBLIC_KEY = os.getenv('MP_PUBLIC_KEY')
    return MP_PUBLIC_KEY

def get_google_client_id():
    CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    return CLIENT_ID

def get_datetime_today():
    now_utc = datetime.utcnow()
    now_string = now_utc.strftime('%Y-%m-%d %H:%M:%S')
    return now_string

def get_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    return user

def get_driver(id):
    driver = Driver.query.get(id)
    if driver is None:
        return jsonify({'message': 'Driver not found'}), 404
    return driver