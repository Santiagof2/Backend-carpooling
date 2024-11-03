from datetime import datetime
from flask import Blueprint, jsonify, request
from server.db import db
from server.models.user import User
from server.utils.functions import get_datetime_today
from server.utils.validations import validate_token

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

# Crear un nuevo usuario
@auth_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    token = request.headers.get('Authorization')  # Se espera un header 'Authorization: Bearer <idToken>'
    user = validate_token(token)
    if not user:
        return jsonify({"error": "Invalid token"}), 401

    if not data or not all(key in data for key in ['first_name', 'last_name', 'username']):
        return jsonify({'message': 'Missing required fields'}), 400

    now = get_datetime_today()
    # Crear un nuevo usuario
    new_user = User(
        id=user['id'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        username=data['username'],
        email=user['email'],
        creation_date = now,
    )

    try:
        # Agregar el nuevo usuario a la base de datos
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'user': new_user.to_dict(), 'email_verified': user['email_verified']}), 201  # Retorna el usuario creado y un código 201 de creación exitosa
    except Exception as e:
        db.session.rollback()  # Hacer rollback si hay un error
        return jsonify({'message': 'Error creating user', 'error': str(e)}), 500

# Iniciar sesión
@auth_bp.route('/login', methods=['POST'])
def login():
    token = request.headers.get('Authorization')  # Se espera un header 'Authorization: Bearer <idToken>'
    userToken = validate_token(token)
    if not userToken:
        return jsonify({"error": "Invalid token"}), 401
    user = User.query.filter_by(id=userToken.get('id')).first()
    if not user: return jsonify({'error': 'Usuario no encontrado.'}), 404
    if (not userToken['email_verified']): return jsonify({'error': 'Email no verificado.'}), 403
    return jsonify(user.to_dict()), 200