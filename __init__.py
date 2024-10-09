from flask import Flask, request
from server.config import Config
from server.routes import *
from flask_socketio import SocketIO, emit, send, join_room, leave_room

def create_app():
    
    # Aplicacion de Flask
    app = Flask(__name__)
    # Carga de configuración
    app.config.from_object(Config)

    # Registro de Blueprints
    app.register_blueprint(address_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(trip_join_bp)
    app.register_blueprint(trip_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(role_selection)
    app.register_blueprint(chat_bp)
    
    return app

app = create_app()






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
def handle_join_room(messageData):
    room = messageData['room']
    join_room(room)
    send(f'{messageData["username"]} has entered the room.', to=room)

# Salir de una sala
@socketio.on('leave_room')
def handle_leave_room(messageData):
    room = messageData['room']
    leave_room(room)
    send(f'{messageData["username"]} has left the room.', to=room)

# Enviar un mensaje
@socketio.on('message')
def handle_message(messageData):
    room = messageData['room']
    send(messageData, to=room)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    socketio.run(app, host='0.0.0.0', port=5000)

