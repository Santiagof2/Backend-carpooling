from datetime import datetime
from flask import Blueprint, jsonify, request
from server.db import db
from server.models import User
from server.utils.functions import get_user

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')

# Obtener todos los usuarios
@user_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    result = [user.to_dict() for user in users]
    return jsonify(result)

# Obtener un usuario por ID
@user_bp.route('/<int:id>', methods=['GET'])
def get_user_route(id):
    user = get_user(id)
    return jsonify(user.to_dict())

# Actualizar un usuario existente
@user_bp.route('/<int:id>', methods=['PUT'])
def update_user(id):

    # Buscar el usuario en la base de datos por ID
    user = User.query.get(id)
    
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    
    # Obtener los datos enviados en la petición
    data = request.get_json()
    
    if not data:
        return jsonify({'message': 'No data provided to update user'}), 400

    try:
        for (key, value) in data.items():
            if hasattr(user, key):
                setattr(user, key, value)

        # Guardar los cambios en la base de datos
        db.session.commit()
        return jsonify(user.to_dict()), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error updating user', 'error': str(e)}),