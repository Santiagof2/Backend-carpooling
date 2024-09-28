from flask import Blueprint, jsonify, request
from server.src.database import Database
from server.models import Passager_trip

trip_join_bp = Blueprint('trip_db', __name__, url_prefix='/trip_join')

@trip_join_bp.route('/', methods=['POST'])
def join_passager_trip():
    data = request.get_json()
    if data.get('id_trip') is None or data.get('passenger_id') is None:
        return jsonify({'error': 'Faltan datos'}), 400
    id = len(Database.passager_trips) + 1
    descontar_cupo(data.get('id_trip'))
    new_passager_trip = Passager_trip(id, data['id_trip'], data['passenger_id'])
    Database.passager_trips.append(new_passager_trip)
    return jsonify({'message': 'Pasajero agregado exitosamente'}), 200

def descontar_cupo(id_trip):
    for trip in Database.trips:
        if trip.id == id_trip:
            trip.available_seats -= 1
            return trip
    return jsonify({'error': 'Viaje no encontrado'}), 404