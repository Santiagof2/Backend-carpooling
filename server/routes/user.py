from datetime import datetime
from flask import Blueprint, jsonify, request
from server.src.database import Database
from server.models import User

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')



def buscar_usuario_por_id(id, usuarios: list[User]) -> User | None:
    """
    Busca un usuario por su ID en la lista de usuarios.
    
    :param id: El ID del usuario que se desea buscar.
    :param usuarios: La lista de usuarios (diccionarios).
    :return: El usuario encontrado o None si no existe.
    """
    for user in usuarios:
        if user._id == id:
            return user
    return None

# Obtener todos los usuarios
@user_bp.route('/', methods=['GET'])
def obtener_usuarios():
    return jsonify([user.to_dict() for user in  Database.users]), 200

# Obtener un usuario por ID
@user_bp.route('/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = buscar_usuario_por_id(id, Database.users)
    
    if usuario is None:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    return jsonify(usuario.to_dict()), 200

# Crear un nuevo usuario
@user_bp.route('/', methods=['POST'])
def crear_usuario():
    global id_counter
    data = request.get_json()

    # Obtenemos los datos
    name = data.get('name')
    lastname = data.get('lastname')
    email = data.get('email')
    password = data.get('password')
    username = data.get('username')
    validacionMail = data.get('validacionMail')

    # Validación
    if not name or not lastname or not email or not password or not username or validacionMail is None:
        return jsonify({'error': 'Faltan datos'}), 400

    # Creción del usuario
    user = User(
        len(Database.users) + 1,
        name,
        lastname,
        password,
        email,
        username,
        datetime.now().strftime('%Y-%m-%d'),
        validacionMail
    )
    Database.users.append(user)
    
    return jsonify({'mensaje': 'Usuario creado correctamente.', 'user_id': user._id}), 201

# Actualizar un usuario existente
@user_bp.route('/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario = buscar_usuario_por_id(id, Database.users)
    
    if usuario is None:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    
    data = request.get_json()
    usuario._first_name= data.get('first_name', usuario._first_name)
    usuario._last_name = data.get('last_name', usuario._last_name)
    usuario._email = data.get('email', usuario._email)
    usuario._username = data.get('username', usuario._username)
    usuario._password = data.get('password', usuario._password)
    usuario._email_validation = data.get('validacionMail', usuario._email_validation)

    return jsonify({'mensaje': 'Usuario modificado correctamente.'}), 200

# Eliminar un usuario
@user_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = buscar_usuario_por_id(id, Database.users)
    
    if usuario is None:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    
    Database.users.remove(usuario)
    
    return jsonify({'mensaje': 'Usuario eliminado'}), 200

