from flask import Blueprint, jsonify, request
from server.src.database import Database

trip_join_bp = Blueprint('trip_db', __name__, url_prefix='/trip_join')

@trip_join_bp.route('/', methods=['POST'])
def join_passager_trip():
    trip_id = Database.trip[+1]['id']
    data = request.get_json()
    if data.get('id_trip') is None or data.get('passenger_id') is None:
        return jsonify({'error': 'Faltan datos'}), 400
    Database.passenger_trip.append(
        {
            'id': trip_id,
            'id_trip': data.get('id_trip'),
            'passenger_id': data.get('passenger_id')
        })
    return jsonify({'message': 'Pasajero agregado exitosamente'}), 200