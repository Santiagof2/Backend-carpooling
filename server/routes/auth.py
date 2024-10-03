from datetime import datetime
from flask import Blueprint, jsonify, request
from server.src.database import Database

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not (data.get('username') and data.get('password')): return jsonify({'error': 'Usuario o contraseña incorrectos.'}), 400

    for user in Database.users:
        if user._username == data.get('username') and user._password == data.get('password'): return jsonify({'mensaje': 'Usuario y contraseña correctos'}), 200
        else : return jsonify({'error': 'Usuario o contraseña incorrectos.'}), 400