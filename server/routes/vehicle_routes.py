from datetime import datetime
from flask import Blueprint, jsonify, request
from server.models import Trip
from server.db import db
from server.models import Vehicle, Vehicle_Driver

vehicle_bp = Blueprint('vehicle_bp', __name__, url_prefix='/vehicles')

# listar todos los vehiculos
@vehicle_bp.route('/', methods=['GET'])
def get_vehicles():
    vehicles = Vehicle.query.all()
    result = [vehicle.to_dict() for vehicle in vehicles]
    return jsonify(result)
    
#Obtener vehiculo por condutor ID
@vehicle_bp.route('/<int:id>', methods=['GET'])
def get_vehicle(id):
    vehicle = Vehicle.query.get(id)
    if vehicle is None:
        return jsonify({'error': 'Vehiculo no encontrado'}), 404
    return jsonify(vehicle.to_dict())

#Crear Vehiculo
@vehicle_bp.route('/', methods=['POST'])
def create_vehicle():
    data = request.get_json()
    
    if not license_plate or not all(key in data for key in ['license_plate', 'brand', 'model', 'color', 'year']):
        return jsonify({'error': 'Faltan datos'}), 400

    # Obtenemos los datos
    license_plate = data.get('license_plate')
    brand = data.get('brand')
    model = data.get('model')
    color = data.get('color')
    year  = data.get('year')
    
    driver= get_driver(user_id,db.users)
    if not driver:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    # Creción del vehiculo
    vehicle = Vehicle(
        len(db.vehicles) + 1,
        license_plate,
        brand,
        model,
        color,
        year   
    )
    db.vehicles.append(vehicle)

    # Crear la relación entre el usuario y el vehículo
    vehicle_driver = Vehicle_Driver(
        len(db.vehicle_drivers) + 1,
        driver,
        vehicle
    )
    db.vehicle_drivers.append(vehicle_driver)

    return jsonify({
        'mensaje': 'Vehículo creado correctamente y asociado al usuario.',
        'vehicle_id': vehicle._id,
        'vehicle_driver_id': vehicle_driver.get_id()
    }), 201    
   
    
# Actualizar un Vehiculo existente
@vehicle_bp.route('/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    vehicle = get_vehicle(id, db.vehicles)
    
    if vehicle is None:
        return jsonify({'error': 'Vehiculo no encontrado'}), 404
    
    data = request.get_json()
    vehicle._license_plate= data.get('license_plate', vehicle._license_plate)
    vehicle._brand = data.get('brand', vehicle._brand)
    vehicle._model = data.get('model', vehicle._model)
    vehicle._color = data.get('color', vehicle._color)
    vehicle._year = data.get('year', vehicle._year)
    
    return jsonify({'mensaje': 'Vehiculo modificado correctamente.'}), 200

# Eliminar un Vehiculo
@vehicle_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_vehicle(id):
    vehicle = get_vehicle(id, db.vehicles)
    
    if vehicle is None:
        return jsonify({'error': 'Vehiculo no encontrado'}), 404
    
    db.vehicles.remove(vehicle)
    
    return jsonify({'mensaje': 'Vehiculo eliminado'}), 200