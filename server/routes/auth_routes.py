from datetime import datetime
from flask import Blueprint, jsonify, request
from server.db import db

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not (data.get('username') and data.get('password')): return jsonify({'error': 'Usuario o contraseña incorrectos.'}), 400

    for user in db.users:
        if user._username == data.get('username') and user._password == data.get('password'):
            return jsonify({'user': user.to_dict(), 'message': 'Usuario y contraseña correctos'}), 200
    return jsonify({'error': 'Usuario o contraseña incorrectos.'}), 400