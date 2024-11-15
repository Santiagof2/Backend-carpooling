from flask import request, Blueprint, jsonify
from server.db import db
from server.models import Driver, Vehicle, Vehicle_Driver, PassengerTrip, Trip
from server.routes.user_routes import send_notification
from server.utils.functions import get_driver

driver_bp = Blueprint('driver_bp', __name__, url_prefix='/drivers')

# Obtener todos los conductores
@driver_bp.route('/', methods=['GET'])
def get_drivers():
    drivers = Driver.query.all()
    result =[driver.to_dict() for driver in drivers]
    return jsonify(result)

# Obtener un conductor por ID
@driver_bp.route('/<string:id>', methods=['GET'])
def get_driver_route(id):
    driver = get_driver(id)
    return jsonify(driver.to_dict())

# Obtener vehiculos de un conductor
@driver_bp.route('/<string:id>/vehicles', methods=['GET'])
def get_driver_vehicles(id):
    # Verificar si el conductor existe
    driver = get_driver(id)
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
            vehicles.append(vehicle.to_dict())

    return jsonify({'driver_id': id, 'vehicles': vehicles}), 200

# Crear un conductor
@driver_bp.route('/', methods=['POST'])
def create_driver():
    data = request.json
    driver = Driver(user_id=data['user_id'])
    db.session.add(driver)
    db.session.commit()
    return jsonify(driver.to_dict()), 201

@driver_bp.route('/trips/<int:trip_id>/requests', methods=['GET'])
def list_passenger_requests(trip_id):
    # Filtrar las solicitudes de pasajeros pendientes para el viaje especificado
    passenger_requests = PassengerTrip.query.filter_by(trip_id=trip_id).all()
    filtered_requests = [r.to_dict() for r in passenger_requests]
    return jsonify(filtered_requests), 200

@driver_bp.route('/trips/<int:trip_id>/requests/<string:passenger_id>/accept', methods=['POST'])
def accept_passenger(trip_id, passenger_id):
    # Buscar la solicitud de pasajero específica
    passenger_request = PassengerTrip.query.filter_by(passenger_id=passenger_id, trip_id=trip_id).first()
    if passenger_request:
        passenger_request.accept()
        db.session.commit()
        expo_token = passenger_request.passenger.user.expo_push_token
        if expo_token: 
            send_notification(expo_push_token=expo_token, title='Felicidades!', body="Su solicitud de viaje fué aceptada 🥳🥳🥳")
        return jsonify({'message': 'Passenger accepted successfully'}), 200
    return jsonify({'message': 'Request not found'}), 404

@driver_bp.route('/trips/<int:trip_id>/requests/<string:passenger_id>/reject', methods=['POST'])
def reject_passenger(trip_id, passenger_id):
    # Buscar la solicitud de pasajero específica
    passenger_request = PassengerTrip.query.filter_by(passenger_id=passenger_id, trip_id=trip_id).first()
    if passenger_request:
        passenger_request.reject()
        db.session.commit()
        expo_token = passenger_request.passenger.user.expo_push_token
        if expo_token: 
            send_notification(expo_push_token=expo_token, title='Lo sentimos...', body="Su solicitud de viaje ha sido rechazada 😞. pero puedes seguir buscando otros viajes!")
        return jsonify({'message': 'Passenger rejected successfully'}), 200
    return jsonify({'message': 'Request not found'}), 404

@driver_bp.route('/trips/<int:trip_id>/cancel', methods=['POST'])
def cancel_trip(trip_id):
    driver_id = request.json.get('driver_id')

    # Verificar si el conductor existe
    driver = Driver.query.filter_by(user_id=driver_id).first()
    if not driver:
        return jsonify({'message': 'Driver not found'}), 404
    
    # Buscar el viaje específico
    trip = Trip.query.filter_by(id=trip_id).first()
    if trip:
        trip.cancel_trip()
        # Cancelar todas las solicitudes de pasajeros asociadas al viaje
        passenger_requests = PassengerTrip.query.filter_by(trip_id=trip_id).all()
        for request_i in passenger_requests:
            request_i.reject()
        db.session.commit()
        return jsonify({'message': f'Driver ({driver_id}) cancelled the Trip successfully'}), 200
    return jsonify({'message': 'Trip not found or unauthorized'}), 404

@driver_bp.route('/trips/<int:trip_id>/complete', methods=['POST'])
def complete_trip(trip_id):
    driver_id = request.json.get('driver_id')

    # Verificar si el conductor existe
    driver = Driver.query.filter_by(user_id=driver_id).first()
    if not driver:
        return jsonify({'message': 'Driver not found'}), 404
    
    # Buscar el viaje específico
    trip = Trip.query.filter_by(id=trip_id).first()
    if trip:
        trip.complete_trip()
        db.session.commit()
        return jsonify({'message': f'Driver ({driver_id}) completed the Trip successfully'}), 200
    return jsonify({'message': 'Trip not found or unauthorized'}), 404

