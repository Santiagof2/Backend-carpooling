from flask import Blueprint, jsonify, request
from server.db import db
from server.models import PassengerTrip

trip_join_bp = Blueprint('trip_db', __name__, url_prefix='/trip_join')

@trip_join_bp.route('/', methods=['POST'])
def join_PassengerTrip():
    data = request.get_json()
    if data.get('id_trip') is None or data.get('passenger_id') is None:
        return jsonify({'error': 'Faltan datos'}), 400
    id = len(db.PassengerTrips) + 1
    descontar_cupo(data.get('id_trip'))
    passenger= get_passenger(data.get('passenger_id'))
    new_PassengerTrip = PassengerTrip(id, data['id_trip'], passenger)
    db.PassengerTrips.append(new_PassengerTrip)
    return jsonify({'message': 'Pasajero agregado exitosamente'}), 200

def descontar_cupo(id_trip: int):
    for trip in db.trips:
        if trip._id == id_trip:
            trip._available_seats -= 1
            return trip
    return jsonify({'error': 'Viaje no encontrado'}), 404

def get_passenger(id):
    for passenger in db.Passengers:
        if passenger._id == id:
            return passenger
    return jsonify({'error': 'Pasajero no encontrado'}), 404