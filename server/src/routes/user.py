from datetime import datetime
from flask import Blueprint, jsonify, request
from server.src.database import Database

user_bp = Blueprint('user_bp', __name__, url_prefix='/usuarios')

# Contador de usuarios
id_counter = len(Database.users) + 1

def buscar_usuario_por_id(id, usuarios):
    """
    Busca un usuario por su ID en la lista de usuarios.
    
    :param id: El ID del usuario que se desea buscar.
    :param usuarios: La lista de usuarios (diccionarios).
    :return: El usuario encontrado o None si no existe.
    """
    for user in usuarios:
        if user['id'] == id:
            return user
    return None

# Obtener todos los usuarios
@user_bp.route('/', methods=['GET'])
def obtener_usuarios():
    return jsonify(Database.users), 200

# Obtener un usuario por ID
@user_bp.route('/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = buscar_usuario_por_id(id, Database.users)
    
    if usuario is None:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    return jsonify(usuario), 200

# Crear un nuevo usuario
@user_bp.route('/', methods=['POST'])
def crear_usuario():
    global id_counter
    data = request.get_json()

    # Obtenemos los datos
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    email = data.get('email')
    password = data.get('password')
    username = data.get('username')
    validacionMail = data.get('validacionMail')

    # Validación
    if not nombre or not apellido or not email or not password or not username or validacionMail is None:
        return jsonify({'error': 'Faltan datos'}), 400

    # Creción del usuario
    nuevo_usuario = {
        'id': id_counter,
        'nombre': nombre,
        'apellido': apellido,
        'password': password,
        'email': email,
        'username': username,
        'fechaCreacion': datetime.now().strftime('%Y-%m-%d'),
        'validacionMail': validacionMail
    }
    id_counter += 1
    Database.users.append(nuevo_usuario)
    
    return jsonify(nuevo_usuario), 201

# Actualizar un usuario existente
@user_bp.route('/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario = buscar_usuario_por_id(id, Database.users)
    
    if usuario is None:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    
    data = request.get_json()
    usuario['nombre'] = data.get('nombre', usuario['nombre'])
    usuario['apellido'] = data.get('apellido', usuario['apellido'])
    usuario['email'] = data.get('email', usuario['email'])
    usuario['username'] = data.get('username', usuario['username'])
    usuario['password'] = data.get('password', usuario['password'])
    usuario['validacionMail'] = data.get('validacionMail', usuario['validacionMail'])
    
    return jsonify(usuario), 200

# Eliminar un usuario
@user_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = buscar_usuario_por_id(id, Database.users)
    
    if usuario is None:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    
    Database.users.remove(usuario)
    
    return jsonify({'mensaje': 'Usuario eliminado'}), 200
