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


@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()

    # Validar los datos necesarios
    if not data or not all(key in data for key in ['first_name', 'last_name', 'password', 'email', 'username']):
        return jsonify({'message': 'Missing required fields'}), 400


    now_utc = datetime.now()
    now_string = now_utc.strftime('%Y-%m-%d %H:%M:%S') 
    # Crear un nuevo usuario
    new_user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        password=data['password'],  # Asegúrate de encriptar las contraseñas antes de guardarlas
        email=data['email'],
        username=data['username'],
        creation_date = now_string,
        email_validation=data.get('email_validation', False)  # Valor por defecto en False si no se proporciona
    )

    try:
        # Agregar el nuevo usuario a la base de datos
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201  # Retorna el usuario creado y un código 201 de creación exitosa
    except Exception as e:
        db.session.rollback()  # Hacer rollback si hay un error
        return jsonify({'message': 'Error creating user', 'error': str(e)}), 500

# Actualizar un usuario existente
@user_bp.route('/<int:id>', methods=['PUT'])
def update_user(id):
    # Buscar el usuario en la base de datos por ID
    usuario = User.query.get(id)
    
    if usuario is None:
        return jsonify({'error': 'User not found'}), 404
    
    # Obtener los datos enviados en la petición
    data = request.get_json()
    
    # Actualizar los campos del usuario si están presentes en la petición
    usuario.first_name = data.get('first_name', usuario.first_name)
    usuario.last_name = data.get('last_name', usuario.last_name)
    usuario.email = data.get('email', usuario.email)
    usuario.username = data.get('username', usuario.username)
    usuario.password = data.get('password', usuario.password)
    usuario.email_validation = data.get('email_validation', usuario.email_validation)

    # Guardar los cambios en la base de datos
    db.session.commit()

    return jsonify({'message': 'User updated successfully.'}), 200

@user_bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    # Buscar el usuario en la base de datos por ID
    usuario = User.query.get(id)
    
    if usuario is None:
        return jsonify({'error': 'User not found'}), 404
    
    # Eliminar el usuario de la base de datos
    db.session.delete(usuario)
    db.session.commit()

    return jsonify({'message': 'User deleted successfully.'}), 200
