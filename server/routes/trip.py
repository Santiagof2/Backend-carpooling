from datetime import datetime
from flask import Blueprint, jsonify, request
from server.src.database import Database

trip_bp = Blueprint('trip_bp', __name__, url_prefix='/trip')

def get_trip_por_id(id, trips):
    for trip in trips:
        if trip.id == id:
            return trip
    return jsonify({'error': 'Viaje no encontrado'}), 404

#esta funcion no corresponde a esta BP.
def get_address_por_id(id, addresses):
    for address in addresses:
        if address.id == id:
            return address
    return jsonify({'error': 'Direccion no encontrada'}), 404

def get_driver_by_vehicle_id(vehicle_driver_id):
    for vehicle_driver in Database.vehicle_drivers:
        if vehicle_driver.id == vehicle_driver_id:
            driver = get_driver_por_id(vehicle_driver.driver)
            return driver
    return jsonify({'error': 'Conductor no encontrado'}), 404

def get_driver_por_id(id):
    for driver in Database.drivers:
        if driver.id == id:
            return get_user_por_id(driver.user_id)
    return jsonify({'error': 'Conductor no encontrado'}), 404

def get_user_por_id(id):
    for user in Database.users:
        if user.user_id == id:
            return user
    return jsonify({'error': 'Usuario no encontrado'}), 404

# listar todos los viajes
@trip_bp.route('/', methods=['GET'])
def get_trips():
    list_trips = Database.trips
    return jsonify([trip.__dict__ for trip in list_trips]), 200

@trip_bp.route('/<int:id>', methods=['GET'])
def get_trip(id):
    trip = get_trip_por_id(id, Database.trips)
    departure = get_address_por_id(trip.departure_address_id, Database.addresses)
    arrival = get_address_por_id(trip.arrival_address_id, Database.addresses)
    driver = get_driver_by_vehicle_id(trip.vehicle_driver_id)
    response = {
        'id': trip.id,
        'departure_date': trip.departure_date,
        'departure_address': departure.__dict__,
        'arrival_address': arrival.__dict__,
        'driver': driver.__dict__,
    }
    return response, 200