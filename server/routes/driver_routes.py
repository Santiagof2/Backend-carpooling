from flask import Blueprint, jsonify, request
from server.db import db
from server.models import Driver, Vehicle, Vehicle_Driver
from server.utils.functions import get_user

driver_bp = Blueprint('driver_bp', __name__, url_prefix='/drivers')

# Obtener todos los conductores
@driver_bp.route('/', methods=['GET'])
def get_drivers():
    drivers = Driver.query.all()
    result =[driver.to_dict() for driver in drivers]
    return jsonify(result)

# Obtener un conductor por ID
@driver_bp.route('/<int:id>', methods=['GET'])
def get_driver(id):
    driver = Driver.query.get(id)
    if driver is None:
        return jsonify({'error': 'Conductor no encontrado'}), 404
    return jsonify(driver.to_dict())

# Obtener vehiculos de un conductor
@driver_bp.route('/<int:id>/vehicles', methods=['GET'])
def get_driver_vehicles(id):
    # Verificar si el conductor existe
    driver = get_user(id)
    if driver is None:
        return jsonify({'error': 'Conductor no encontrado'}), 404

    # Obtener todas las entradas en Vehicle_driver que correspondan al conductor
    vehicle_driver_entries = Vehicle_Driver.query.filter_by(driver_id=id).all()

    if not vehicle_driver_entries:
        return jsonify({'message': 'Este conductor no tiene vehículos asignados'}), 404

    # Obtener todos los vehículos asociados a esas entradas
    vehicles = []
    for entry in vehicle_driver_entries:
        vehicle = Vehicle.query.get(entry.vehicle_id)
        if vehicle:
            vehicles.append(vehicle.to_dict())  # Asumimos que el modelo Vehicle tiene un método to_dict()

    return jsonify({'driver_id': id, 'vehicles': vehicles}), 200

@driver_bp.route('/trips/<int:trip_id>/requests', methods=['GET'])
def list_passenger_requests(trip_id):
    filtered_requests = [r.to_dict() for r in db.trip_requests if r._trip._id == trip_id and r._status == 'pending']
    return jsonify(filtered_requests), 200

@driver_bp.route('/trips/<int:trip_id>/requests/<int:request_id>/accept', methods=['POST'])
def accept_passenger(trip_id, request_id):
    for request in db.trip_requests:
        if request._id == request_id and request._trip._id == trip_id:
            request.accept()
            return jsonify({'message': 'Passenger accepted successfully'}), 200
    return jsonify({'message': 'Request not found'}), 404

@driver_bp.route('/trips/<int:trip_id>/requests/<int:request_id>/reject', methods=['POST'])
def reject_passenger(trip_id, request_id):
    for request in db.trip_requests:
        if request._id == request_id and request._trip._id == trip_id:
            request.reject()
            return jsonify({'message': 'Passenger rejected successfully'}), 200
    return jsonify({'message': 'Request not found'}), 404

@driver_bp.route('/trips/<int:trip_id>/cancel', methods=['POST'])
def cancel_trip(trip_id):
    driver_id = request.json.get('driver_id')
    for trip in db.trips:
        if trip._id == trip_id and trip._vehicle_driver._id == driver_id:
            trip.cancel_trip()
            for request in db.trip_requests:
                if request._trip._id == trip_id:
                    request.cancel()
            return jsonify({'message': f'Driver ({driver_id}) cancelled the Trip successfully'}), 200
    return jsonify({'message': 'Trip not found or unauthorized'}), 404
