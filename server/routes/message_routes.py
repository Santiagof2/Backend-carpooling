from datetime import datetime
from flask import Blueprint, jsonify, request
from server.db import db
from server.models import Message

message_bp = Blueprint('message_bp', __name__, url_prefix='/messages')


# Obtener todos los mensajes
@message_bp.route('/', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    result = [message.to_dict() for message in messages]
    return jsonify(result)

# Obtener un mensaje por id_trip
@message_bp.route('/<int:id>', methods=['GET'])
def get_messages_by_id_trip(id):
    messages = Message.query.filter_by(id_trip=id).all()
    if messages is None:
        return jsonify({'message': 'messages from trip not found '}), 404
    result = [message.to_dict() for message in messages]
    return jsonify(result)


@message_bp.route('/', methods=['POST'])
def create_message():
    data = request.get_json()

    # Validar los datos
    if not data or not all(key in data for key in ['id_trip', 'message']):
        return jsonify({'message': 'Missing required fields'}), 400

    now_utc = datetime.utcnow()
    now_string = now_utc.strftime('%Y-%m-%d %H:%M:%S') 
    # Crear un nuevo mensaje
    new_message = Message(
        id_trip=data['id_trip'],
        id_user=data.get('id_user', None),
        is_system=data.get('is_system', None),
        message=data['message'],
        created_at = now_string,     
    )

    try:
        # Agregar mensaje a la base de datos
        db.session.add(new_message)
        db.session.commit()
        return jsonify(new_message.to_dict()), 201  # Retorna el mensaje creado y un código 201 de creación exitosa
    except Exception as e:
        db.session.rollback()  # Hacer rollback si hay un error
        return jsonify({'message': 'Error creating message', 'error': str(e)}), 500


@message_bp.route('/<int:id>', methods=['DELETE'])
def delete_message(id):
    # Buscar el usuario en la base de datos por ID
    message = Message.query.get(id)
    
    if message is None:
        return jsonify({'error': 'message not found'}), 404
    
    # Eliminar el usuario de la base de datos
    db.session.delete(message)
    db.session.commit()

    return jsonify({'message': 'message deleted successfully.'}), 200
