from flask import Blueprint, request, jsonify
from server.models import User, Driver, Passenger
from server.src.database import Database

role_selection = Blueprint('role_selection', __name__)

@role_selection.route('/select_role', methods=['POST'])
def select_role():
    data = request.get_json()
    user_id = data.get('user_id')  # Asumimos que el usuario ya ha iniciado sesión
    role = data.get('role')  # Puede ser passenger  o driver

    if role not in ['passenger', 'driver']:
        return jsonify({'error': 'Seleccionado de rol invalido'}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    if role == 'passenger':
        passenger = Passenger.query.filter_by(usuario_id=user_id).first()
        if not passenger:
            return jsonify({'error': 'Perfil del pasajero no encontrado'}), 404
        return jsonify({'message': ' Estas en modo pasajero', 'data': passenger.serialize()}), 200

    if role == 'driver':
        driver = Driver.query.filter_by(usuario_id=user_id).first()
        if not driver:
            return jsonify({'error': 'Perfil del conductor no encontrado'}), 404
        return jsonify({'message': 'Estas en modo conductor', 'data': driver.serialize()}), 200
