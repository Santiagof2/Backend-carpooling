from flask import Blueprint, jsonify, request
from server.models import Trip
from server.src.database import Database

trip_bp = Blueprint('trip_bp', __name__, url_prefix='/trip')

def get_trip_por_id(id, trips):
    for trip in trips:
        if trip._id == id:
            return trip
    return jsonify({'error': 'Viaje no encontrado'}), 404

#esta funcion no corresponde a esta BP.
def get_address(trip_address, addresses: list):
    for address in addresses:
        if address == trip_address:
            return address
    return jsonify({'error': 'Direccion no encontrada'}), 404

def get_driver_by_vehicle(vehicle_driver_id):
    for vehicle_driver in Database.vehicle_drivers:
        if vehicle_driver == vehicle_driver_id:
            driver = get_driver_from_vehicle(vehicle_driver._driver)
            return driver
    return jsonify({'error': 'Conductor no encontrado'}), 404

def get_driver_from_vehicle(_driver):
    for driver in Database.drivers:
        if driver == _driver:
            return get_user_by_driver(driver.user)
    return jsonify({'error': 'Conductor no encontrado'}), 404

def get_user_by_driver(_user):
    for user in Database.users:
        if user == _user:
            return user
    return jsonify({'error': 'Usuario no encontrado'}), 404

# listar todos los viajes
@trip_bp.route('/', methods=['GET'])
def get_trips():
    list_trips = Database.trips
    return jsonify([trip.to_dict() for trip in list_trips]), 200

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
    departure = get_address(trip._deaparture_address, Database.addresses)
    arrival = get_address(trip._arrival_address, Database.addresses)
    driver = get_driver_by_vehicle(trip._vehicle_driver)
    response = {
        'id': trip._id,
        'departure_date': trip._departure_date,
        'departure_time': trip._departure_time,
        'available_seats': trip._available_seats,
        'seat_price': trip._seat_price,
        'creation_timestamp': trip._creation_timestamp,
        'departure_address': departure.to_dict(),
        'arrival_address': arrival.to_dict(),
        'driver': driver.to_dict(),
    }
    return response, 200
