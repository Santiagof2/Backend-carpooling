from flask import Blueprint, request, jsonify
from server.models import User, Driver, Passager
from server.src.database import Database
from .trip import get_driver_por_id , get_user_por_id 

role_selection = Blueprint('role_selection', __name__ , url_prefix='/role')

@role_selection.route('/select_role', methods=['POST'])
def select_role():
    data = request.get_json()
    user_id = data.get('user_id')  # Asumimos que el usuario ya ha iniciado sesión
    role = data.get('role')  # Puede ser passenger  o driver

    if role not in ['passenger', 'driver']:
        return jsonify({'error': 'Seleccionado de rol invalido'}), 400

    user = get_user_por_id(user_id)
    if not user:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    if role == 'passenger':
        passenger = next((passenger for passenger in Database.passagers if passenger.id == user_id), None) #Database.passagers 
        if not passenger:
            return jsonify({'error': 'Perfil del pasajero no encontrado'}), 404
        return jsonify({'message': ' Estas en modo pasajero', 'data': user.__dict__}), 200

    if role == 'driver':
        driver = get_driver_por_id(user_id)
        if not driver:
            return jsonify({'error': 'Perfil del conductor no encontrado'}), 404
        return jsonify({'message': 'Estas en modo conductor', 'data': user.__dict__}), 200
