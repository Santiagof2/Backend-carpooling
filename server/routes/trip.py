from datetime import datetime
from pprint import pprint
from flask import Blueprint, jsonify, request
from server.models import Trip, Address, VehicleDriver, City, Vehicle, Province
from server.src.database import Database

trip_bp = Blueprint('trip_bp', __name__, url_prefix='/trip')

def get_trip_por_id(id, trips):
    for trip in trips:
        if trip._id == id:
            return trip
    trip = None
    return trip

#esta funcion no corresponde a esta BP.
def get_address(trip_address, addresses: list):
    for address in addresses:
        if address == trip_address:
            return address
    return jsonify({'error': 'Direccion no encontrada'}), 404

def get_vehicle_driver_by_id(vehicle_driver_id):
    for vehicle_driver in Database.vehicle_drivers:
        if vehicle_driver._id == vehicle_driver_id:
            vehicle_driver = vehicle_driver
            return vehicle_driver

def get_driver_by_vehicle(vehicle_driver):
    for vehicle_driver in Database.vehicle_drivers:
        if vehicle_driver == vehicle_driver:
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

def get_vehicle_by_driver(vehicle_driver_id):
    for vehicle_driver in Database.vehicle_drivers:
        if vehicle_driver == vehicle_driver_id:
            vehicle = get_vehicle_from_vehicle_driver(vehicle_driver._vehicle)
            return vehicle
    return jsonify({'error': 'Vehiculo no encontrado'}), 404

def get_vehicle_from_vehicle_driver(_vehicle):
    for vehicle in Database.vehicles:
        if vehicle == _vehicle:
            return vehicle
    return jsonify({'error': 'Vehiculo no encontrado'}), 404

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
    status = 'activo'
    departure_date = data.get('departure_date')
    departure_time = data.get('departure_time')
    available_seats = data.get('available_seats')
    seat_price = data.get('seat_price')
    creation_timestamp = datetime.now().strftime('%Y-%m-%d')
    vehicle_driver_id = data.get('vehicle_driver_id')
    departure_address_str = data.get('departure_address', '')
    arrival_address_str = data.get('arrival_address', '')

    if not departure_address_str: return {'error': 'departure_address missing.'}, 400
    split_address = departure_address_str.split(', ')
    departure_address = get_or_add_address(split_address[0], split_address[1], split_address[2], int(split_address[3]))
    
    if not arrival_address_str: return {'error': 'arrival_address missing.'}, 400
    split_address = arrival_address_str.split(', ')
    arrival_address = get_or_add_address(split_address[0], split_address[1], split_address[2], int(split_address[3]))

    vehicle_driver = get_vehicle_driver_by_id(vehicle_driver_id)
    if not vehicle_driver: return {'error': 'vehicle_driver_id not found'}, 400

    new_trip = Trip(id, status, departure_date, departure_time, available_seats, seat_price, creation_timestamp, departure_address, arrival_address, vehicle_driver)
    
    Database.trips.append(new_trip)
    return {'message': 'Trip created successfully.', 'id': new_trip._id}, 200

#Actualizar un viaje
@trip_bp.route('/<int:id>', methods=['PUT'])
def update_trip(id):
    data = request.get_json()
    if not data: return {'error': 'No data provided'}, 400
    status = data.get('status')
    departure_date = data.get('departure_date')
    departure_time = data.get('departure_time')
    available_seats = data.get('available_seats')
    seat_price = data.get('seat_price')
    creation_timestamp = data.get('creation_timestamp')
    deaparture_address_id = data.get('deaparture_address_id')
    arrival_address_id = data.get('arrival_address_id')
    vehicle_driver_id = data.get('vehicle_driver_id')

    deaparture_address = get_address(deaparture_address_id)
    if not deaparture_address: return {'error': 'deaparture_address_id not found'}, 400

    arrival_address = get_address(arrival_address_id)
    if not arrival_address: return {'error': 'arrival_address_id not found'}, 400

    vehicle_driver = get_vehicle_driver_by_id(vehicle_driver_id)
    if not vehicle_driver: return {'error': 'vehicle_driver_id not found'}, 400

    new_trip = Trip(id, status, departure_date, departure_time, available_seats, seat_price, creation_timestamp, deaparture_address, arrival_address, vehicle_driver)

    Database.trips.append(new_trip)
    return {'message': 'Trip created successfully.'}, 200

#Obtener viaje por id
@trip_bp.route('/<int:id>', methods=['GET'])
def get_trip(id):
    trip = get_trip_por_id(id, Database.trips)
    if not trip: return jsonify({'error': 'Trip not found'}), 404
    print(trip)
    return trip.to_dict(), 200


def get_or_add_address(province_name:str, city_name:str, street:str, number:int):
    for prov in Database.province:
        if prov._name == province_name:
            province = prov
        else:
            province = Province(len(Database.province) + 1, province_name)
            Database.province.append(province)
    for city in Database.cities:
        if city._name == city_name:
            city = city
        else:
            city = City(len(Database.cities) + 1, city_name, province)
            Database.cities.append(city)
    for addres in Database.addresses:
        if addres._street == street and addres._number == number:
            address = addres
        else:
            address = Address(len(Database.addresses) + 1, street, number, city)
            Database.addresses.append(address)
    return address