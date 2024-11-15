from datetime import datetime
from flask import Blueprint, jsonify, request
import requests
from server.db import db
from server.models import User
from server.utils.functions import get_expo_access_token, get_user
from server.utils.validations import validate_token

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')

# Obtener todos los usuarios
@user_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    result = [user.to_dict() for user in users]
    return jsonify(result)

# Obtener un usuario por ID
@user_bp.route('/<string:id>', methods=['GET'])
def get_user_route(id):
    user = get_user(id)
    return jsonify(user.to_dict())

# Actualizar un usuario existente
@user_bp.route('/<string:id>', methods=['PUT'])
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

# Register ExpoPushToken
@user_bp.route('/notifications', methods=['PATCH'])
def set_expo_push_token():
    data = request.get_json()
    token = request.headers.get('Authorization')
    userToken = validate_token(token)
    if not userToken:
            return jsonify({"error": "Invalid token"}), 401
    if not data or not all(key in data for key in ['expo_push_token']):
        return jsonify({'message': 'Missing expo push token'}), 400
    
    user = User.query.filter_by(id=userToken.get('id')).first()
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    try:
        setattr(user, 'expo_push_token', data['expo_push_token'])
        db.session.commit()
        return jsonify(user.to_dict()), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error updating user', 'error': str(e)})
    
def send_notification(expo_push_token, title, body, data=None):

    if not title or not body: return False 
    
    url = "https://exp.host/--/api/v2/push/send"
    payload = {
        'to': expo_push_token,
        'sound': "default",
        'title': title,
        'body': body
    }
    if data: payload['data'] = data
    headers = {
    "Authorization": f"Bearer {get_expo_access_token()}",
    "Content-Type": "application/json"  # Si estás enviando JSON
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        if data: return data
    return False