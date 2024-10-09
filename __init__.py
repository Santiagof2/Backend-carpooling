from flask import Flask, request
from server.config import Config
from server.routes import *
from flask_socketio import SocketIO, emit

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

socketio = SocketIO(app)
# Almacena conexiones de usuarios
clients = {}

@socketio.on('connect')
def handle_connect():
    # Almacena el usuario conectado
    user_id = request.args.get('user_id')  # Por ejemplo, puedes enviar un user_id al conectarte
    print('registra')
    print(user_id)
    clients[user_id] = request.sid

@socketio.on('message')
def handle_message(messageData):
    sender_id = messageData['sender_id']
    recipient_id = messageData['recipient_id']
    message = messageData['message']
    print('message')
    print(message)
    if recipient_id in clients:
        # Envía el mensaje solo al destinatario específico
        print('envia algo')
        emit('message', messageData, room=clients[recipient_id])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    socketio.run(app, host='0.0.0.0', port=5000)

