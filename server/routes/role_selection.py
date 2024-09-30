from flask import Blueprint, request, jsonify
from server.models import User, Driver, Passenger
from server.src.database import Database

role_selection = Blueprint('role_selection', __name__ , url_prefix='/role')

@role_selection.route('/select_role', methods=['POST'])
def select_role():
    data = request.get_json()
    user_id = data.get('user_id')  # Asumimos que el usuario ya ha iniciado sesión
    role = data.get('role')  # Puede ser passenger  o driver

    if role not in ['passenger', 'driver']:
        return jsonify({'error': 'Seleccionado de rol invalido'}), 400

    user = next((user for user in Database.users if user._id == user_id), None)
    if not user:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    if role == 'passenger':
        passenger = next((passenger for passenger in Database.passengers if passenger._id == user_id), None)
        if not passenger:
            return jsonify({'error': 'Perfil del pasajero no encontrado'}), 404
        return jsonify({'message': ' Estas en modo pasajero', 'data': passenger.to_dict()}), 200

    if role == 'driver':
        driver = next((driver for driver in Database.drivers if driver._id == user_id), None)
        if not driver:
            return jsonify({'error': 'Perfil del conductor no encontrado'}), 404
        return jsonify({'message': 'Estas en modo conductor', 'data': driver.to_dict()}), 200
