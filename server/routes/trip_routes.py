from datetime import datetime
from pprint import pprint
from flask import Blueprint, jsonify, request
from server.models import Trip, Address, Vehicle_Driver, City, Vehicle, Province
from server.db import db

trip_bp = Blueprint('trip_bp', __name__, url_prefix='/trips')

@trip_bp.route('/', methods=['GET'])
def get_trips():
    trips = Trip.query.all()
    result = [trip.to_dict() for trip in trips]
    return jsonify(result)

@trip_bp.route('/<int:id>', methods=['GET'])
def get_trip(id):
    trip = Trip.query.get(id)
    if trip is None:
        return jsonify({'message': 'Trip not found'}), 404
    return jsonify(trip.to_dict())

@trip_bp.route('/<int:id>/driver', methods=['GET'])
def get_trip_driver(id):
    trip = Trip.query.get(id)
    result = trip.vehicle_driver.driver.to_dict()
    return jsonify(result)

# # cargar un viaje
# @trip_bp.route('/', methods=['POST'])
# def create_trip():
#     data = request.get_json()

#     # Obtenemos los datos
#     id = len(db.trips) + 1
#     status = 'activo'
#     departure_date = data.get('departure_date')
#     departure_time = data.get('departure_time')
#     available_seats = data.get('available_seats')
#     seat_price = data.get('seat_price')
#     creation_timestamp = datetime.now().strftime('%Y-%m-%d')
#     vehicle_driver_id = data.get('vehicle_driver_id')
#     departure_address_str = data.get('departure_address', '')
#     arrival_address_str = data.get('arrival_address', '')

#     if not departure_address_str: return {'error': 'departure_address missing.'}, 400
#     split_address = departure_address_str.split(', ')
#     departure_address = get_or_add_address(split_address[0], split_address[1], split_address[2], int(split_address[3]))
    
#     if not arrival_address_str: return {'error': 'arrival_address missing.'}, 400
#     split_address = arrival_address_str.split(', ')
#     arrival_address = get_or_add_address(split_address[0], split_address[1], split_address[2], int(split_address[3]))

#     vehicle_driver = get_vehicle_driver_by_id(vehicle_driver_id)
#     if not vehicle_driver: return {'error': 'vehicle_driver_id not found'}, 400

#     new_trip = Trip(id, status, departure_date, departure_time, available_seats, seat_price, creation_timestamp, departure_address, arrival_address, vehicle_driver)
    
#     db.trips.append(new_trip)
#     return {'message': 'Trip created successfully.', 'id': new_trip._id}, 200

# #Actualizar un viaje
# @trip_bp.route('/<int:id>', methods=['PUT'])
# def update_trip(id):
#     data = request.get_json()
#     if not data: return {'error': 'No data provided'}, 400
#     status = data.get('status')
#     departure_date = data.get('departure_date')
#     departure_time = data.get('departure_time')
#     available_seats = data.get('available_seats')
#     seat_price = data.get('seat_price')
#     creation_timestamp = data.get('creation_timestamp')
#     deaparture_address_id = data.get('deaparture_address_id')
#     arrival_address_id = data.get('arrival_address_id')
#     vehicle_driver_id = data.get('vehicle_driver_id')

#     deaparture_address = get_address(deaparture_address_id)
#     if not deaparture_address: return {'error': 'deaparture_address_id not found'}, 400

#     arrival_address = get_address(arrival_address_id)
#     if not arrival_address: return {'error': 'arrival_address_id not found'}, 400

#     vehicle_driver = get_vehicle_driver_by_id(vehicle_driver_id)
#     if not vehicle_driver: return {'error': 'vehicle_driver_id not found'}, 400

#     new_trip = Trip(id, status, departure_date, departure_time, available_seats, seat_price, creation_timestamp, deaparture_address, arrival_address, vehicle_driver)

#     db.trips.append(new_trip)
#     return {'message': 'Trip created successfully.'}, 200

# def get_or_add_address(province_name:str, city_name:str, street:str, number:int):
#     for prov in db.province:
#         if prov._name == province_name:
#             province = prov
#         else:
#             province = Province(len(db.province) + 1, province_name)
#             db.province.append(province)
#     for city in db.cities:
#         if city._name == city_name:
#             city = city
#         else:
#             city = City(len(db.cities) + 1, city_name, province)
#             db.cities.append(city)
#     for addres in db.addresses:
#         if addres._street == street and addres._number == number:
#             address = addres
#         else:
#             address = Address(len(db.addresses) + 1, street, number, city)
#             db.addresses.append(address)
#     return address
