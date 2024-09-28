from datetime import datetime
from flask import Blueprint, jsonify, request
from server.src.database import Database

trip_bp = Blueprint('trip_bp', __name__, url_prefix='/trip')

def buscar_trip_por_id(id, trips):
    for trip in trips:
        if trip['id'] == id:
            return trip
    return None

#esta funcion no corresponde a esta BP.
def buscar_address_por_id(id, addresses):
    for address in addresses:
        if address['id'] == id:
            return address
    return None

# listar todos los viajes
@trip_bp.route('/', methods=['GET'])
def get_trips():
    list_trips = Database.trip
    return jsonify(list_trips), 200

@trip_bp.route('/<int:id>', methods=['GET'])
def get_trip(id):
    trip = buscar_trip_por_id(id, Database.trip)
    if trip is None:
        return jsonify({'error': 'Viaje no encontrado'}), 404
    departure = buscar_address_por_id(trip['deaparture_address_id'], Database.address)
    print (departure)
    arrival = buscar_address_por_id(trip['arrival_address_id'], Database.address)
    response = {
        'id': trip['id'],
        'departure_date': trip['departure_date'],
        'departure_address': departure,
        'arrival_address': arrival,
        'driver_id': trip['driver_id'],
    }
    return response, 200