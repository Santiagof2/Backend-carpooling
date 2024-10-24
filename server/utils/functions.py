
from datetime import datetime
from server.models import User
from flask import jsonify

# Funciones varias que se repiten en el proyecto
def get_datetime_today():
    now_utc = datetime.utcnow()
    now_string = now_utc.strftime('%Y-%m-%d %H:%M:%S')
    return now_string

def get_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    return user