from flask import Flask
from server.db import init_db  # Configuración de la base de datos
from server.routes import *
from flask_socketio import SocketIO, emit, send, join_room, leave_room
from server.models.message import Message
from server.utils.functions import get_datetime_today
from server.utils.validations import is_valid_message

app = Flask(__name__)

# Inicializar la base de datos
init_db(app)

# Registrar el Blueprint de usuarios
app.register_blueprint(user_bp)
app.register_blueprint(driver_bp)
app.register_blueprint(address_bp)
app.register_blueprint(trip_join_bp)
app.register_blueprint(trip_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(role_selection)
app.register_blueprint(vehicle_bp)
app.register_blueprint(message_bp)
app.register_blueprint(vehicle_driver_bp)
app.register_blueprint(passenger_trip_bp)
app.register_blueprint(trip_filter_bp)


# --------------------------------- SOCKETIO ---------------------------------

socketio = SocketIO(app, cors_allowed_origins="*")

# Eventos de conexión
@socketio.on('connect')
def handle_connect():
    print('User connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('User disconnected')

# Crear o unirse a una sala
@socketio.on('join_room')
def handle_join_room(messageData): # recibe messageData={username: fede, room: idTrip}
    room = messageData['room']
    username = messageData['username']
    today = get_datetime_today()
    message = {
        'username': username,
        'sendedTime': today,
        'isSystem': True,
        'message': 'Se ha unido al chat'
    }
    join_room(room)
    send(message, to=room)

# Salir de una sala
@socketio.on('leave_room')
def handle_leave_room(messageData):
    room = messageData['room']
    username = messageData['username']
    today = get_datetime_today()
    message = {
        'username': username,
        'sendedTime': today,
        'isSystem': True,
        'message': 'Ha abandonado el chat'
    }
    leave_room(room)
    send(message, to=room)
# Enviar un mensaje
@socketio.on('message')
def handle_message(messageData):
    if(not is_valid_message(messageData)): return
    room = messageData['room']
    username = messageData['username']
    id_user = messageData['id_user']
    today = get_datetime_today()
    message = {
        'id_user': id_user,
        'username': username,
        'sendedTime': today,
        'isSystem': False,
        'message': messageData['message']
    }
    send(message, to=room)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    socketio.run(app, host='0.0.0.0', port=5000)
