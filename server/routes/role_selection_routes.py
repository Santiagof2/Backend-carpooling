from flask import Blueprint, request, jsonify
from server.db import db
from server.models import Passenger, Driver

role_selection = Blueprint('role_selection', __name__ , url_prefix='/role')
def get_user_por_id(id):
    for user in db.users:
        if user._id == id:
            return user
    return None

@role_selection.route('/select_role', methods=['POST'])
def select_role():
    data = request.get_json()
    user_id = data.get('user_id')  # Asumimos que el usuario ya ha iniciado sesión
    role = data.get('role')  # Puede ser passenger o driver

    if role not in ['passenger', 'driver']:
        return jsonify({'error': 'Seleccionado de rol invalido'}), 400

    user = get_user_por_id(user_id)
    if not user:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    if role == 'passenger':
        passenger = next((passenger for passenger in db.Passengers if passenger._id == user_id), None) #db.passagers 
        if not passenger:
            db.Passengers.append(Passenger(db.Passengers.__len__()+1, user))
            return jsonify({'error': 'Perfil del pasajero agregado', 'data': user.to_dict()}), 200
        return jsonify({'message': 'Estas en modo pasajero', 'data': user.to_dict()}), 200

    if role == 'driver':
        driver = next((driver for driver in db.drivers if driver._id == user_id), None)
        if not driver:
            db.drivers.append(Driver(db.drivers.__len__()+1, user))
            return jsonify({'error': 'Perfil del conductor agregado', 'data': user.to_dict()}), 200
        return jsonify({'message': 'Estas en modo conductor', 'data': user.to_dict()}), 200
