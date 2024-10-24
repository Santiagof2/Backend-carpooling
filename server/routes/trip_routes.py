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

# Crear un viaje
@trip_bp.route('/', methods=['POST'])
def create_trip():
    data = request.get_json()

    # Validar los datos necesarios
    if not data or not all(key in data for key in ['departure_date', 'departure_time', 'available_seats', 'seat_price', 'departure_address_id', 'arrival_address_id', 'vehicle_driver_id']):
        return jsonify({'message': 'Missing required fields'}), 400
    
    try:

        # Obtener la fecha y hora actual
        now_utc = datetime.now()
        now_string = now_utc.strftime('%Y-%m-%d %H:%M:%S')

        # Formatear la fecha y hora de salida
        fromated_departure_date = datetime.strptime(data['departure_date'], '%Y-%m-%d')
        formated_departure_time = datetime.strptime(data['departure_time'], '%H:%M:%S').time()
        

        # Crear un nuevo viaje
        new_trip = Trip(
            departure_date=fromated_departure_date,
            departure_time=formated_departure_time,
            available_seats=data['available_seats'],
            seat_price=data['seat_price'],
            creation_timestamp=now_string,
            departure_address_id=data['departure_address_id'],
            arrival_address_id=data['arrival_address_id'],
            vehicle_driver_id=data['vehicle_driver_id']
        )

        # Agregar el nuevo viaje a la base de datos
        db.session.add(new_trip)
        db.session.commit()
        return jsonify(new_trip.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error creating trip', 'error': str(e)}), 500

# Actualizar un viaje
@trip_bp.route('/<int:id>', methods=['PUT'])
def update_trip(id):

    # Buscar el viaje en la base de datos
    trip = Trip.query.get(id)

    if trip is None:
        return jsonify({'error': 'Trip not found'}), 404
    
    # Obtener los datos enviados en la petición
    data = request.get_json()

    # Validar que al menos un dato haya sido proporcionado
    if not data:
        return jsonify({'message': 'No data provided'}), 400
    
    try:
        # Actualizar solo los campos presentes en la petición
        for (key, value) in data.items():
            if hasattr(trip, key):
                setattr(trip, key, value)

        # Guardar los cambios en la base de datos
        db.session.commit()
        return jsonify(trip.to_dict()), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error updating trip', 'error': str(e)}), 500