from datetime import datetime
from flask import Blueprint, jsonify, request
from server.models import Trip
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

# cargar un viaje
@trip_bp.route('/', methods=['POST'])
def create_trip():
    data = request.get_json()

    # Obtenemos los datos
    id = len(Database.trips) + 1
    status = data.get('status')
    departure_date = data.get('departure_date')
    departure_time = data.get('departure_time')
    available_seats = data.get('available_seats')
    seat_price = data.get('seat_price')
    creation_timestamp = data.get('creation_timestamp')
    deaparture_address_id = data.get('deaparture_address_id')
    arrival_address_id = data.get('arrival_address_id')
    vehicle_driver_id = data.get('vehicle_driver_id')

    deaparture_address = Database.get_address(deaparture_address_id)
    if not deaparture_address: return {'error': 'deaparture_address_id not found'}, 400

    arrival_address = Database.get_address(arrival_address_id)
    if not arrival_address: return {'error': 'arrival_address_id not found'}, 400

    vehicle_driver = Database.get_vehicle_driver(vehicle_driver_id)
    if not vehicle_driver: return {'error': 'vehicle_driver_id not found'}, 400

    new_trip = Trip(id, status, departure_date, departure_time, available_seats, seat_price, creation_timestamp, deaparture_address, arrival_address, vehicle_driver)

    Database.trips.append(new_trip)
    return {'message': 'Trip created successfully.'}, 200

#Obtener viaje por id
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
