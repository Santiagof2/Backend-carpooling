from datetime import datetime
from flask import Blueprint, jsonify, request
from server.models import Trip
from server.src.database import Database

trip_bp = Blueprint('trip_bp', __name__, url_prefix='/trip')


@trip_bp.route('/', methods=['GET'])
def get_trips():
    return jsonify(Database.trips)

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

