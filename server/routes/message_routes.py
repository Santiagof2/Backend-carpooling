from flask import Blueprint, jsonify, request
from server.db import db
from server.models import Message
from server.models.passenger_trip import PassengerTrip
from server.models.trip import Trip
from server.models.user import User
from server.routes.user_routes import send_notification
from server.utils.functions import get_datetime_today

message_bp = Blueprint('message_bp', __name__, url_prefix='/messages')

# get all messages
@message_bp.route('/', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    result = [message.to_dict() for message in messages]
    return jsonify(result)

# get messages by trip_id
@message_bp.route('/<int:id>', methods=['GET'])
def get_messages_by_id_trip(id):
    messages = (
        db.session.query(Message)
        .join(User, Message.user_id == User.id)
        .filter(Message.trip_id == id)
        .order_by(Message.created_at)
        .all()
    )
    if messages is None:
        return jsonify({'message': 'messages from trip not found '}), 404
    result = [
        {
            'id_user': message.user_id,
            'username': message.user.username,
            'room': message.trip_id,
            'message': message.message,
            'isSystem': message.is_system,
            'sendedTime': message.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        for message in messages
    ]
    return jsonify(result)

# create a message
@message_bp.route('/', methods=['POST'])
def create_message():
    data = request.get_json()
    # Validar los datos
    if not data or not all(key in data for key in ['trip_id', 'message', 'user_id']):
        return jsonify({'message': 'Missing required fields'}), 400

    now_string = get_datetime_today()
    # Crear un nuevo mensaje
    new_message = Message(
        trip_id=data['trip_id'],
        user_id=data.get('user_id', None),
        is_system=data.get('is_system', None),
        message=data['message'],
        created_at = now_string     
    )
    try:
        db.session.add(new_message)
        db.session.commit()

        # Realizando la consulta con un `select_from()` explícito
        users_to_notify = (
            db.session.query(User)
            .join(PassengerTrip, PassengerTrip.passenger_id == User.id)  # Join entre User y PassengerTrip
            .join(Message, Message.trip_id == PassengerTrip.trip_id)  # Join entre Message y PassengerTrip
            .filter(User.expo_push_token.isnot(None))  # Filtrar por usuarios con expo_push_token
            .all()
        )
        for user in users_to_notify:
            send_notification(expo_push_token=user.expo_push_token, title='Han enviado un mensaje!', body=data['message'])
        return jsonify(new_message.to_dict()), 201  # Retorna el mensaje creado y un código 201 de creación exitosa

    except Exception as e:
        print(e)
        db.session.rollback()  # Hacer rollback si hay un error
        return jsonify({'message': 'Error creating message', 'error': str(e)}), 500

# Eliminar un mensaje por id
@message_bp.route('/<int:id>', methods=['DELETE']) # delete a message by id
def delete_message(id):
    message = Message.query.get(id)
    if message is None:
        return jsonify({'error': 'message not found'}), 404
    db.session.delete(message)
    db.session.commit()
    return jsonify({'message': 'message deleted successfully.'}), 200
