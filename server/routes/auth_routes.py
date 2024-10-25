from datetime import datetime
from flask import Blueprint, jsonify, request
from server.db import db
from server.models.user import User

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

# Iniciar sesión
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not (data.get('username') and data.get('password')): return jsonify({'error': 'Usuario o contraseña incorrectos.'}), 400

    user = User.query.filter_by(username=data.get('username')).first()

    if not user: return jsonify({'error': 'Usuario no encontrado.'}), 400

    if data['password'] != user.password: return jsonify({'error': 'Usuario o contraseña incorrectos.'}), 400

    return jsonify({user.to_dict()}), 200