from datetime import datetime
from flask import Blueprint, jsonify, request
from server.models import Trip
from server.db import db
from server.models import Vehicle, Vehicle_Driver, Driver
from server.utils.functions import get_driver

vehicle_bp = Blueprint('vehicle_bp', __name__, url_prefix='/vehicles')

# Obtener todos los vehiculos
@vehicle_bp.route('/', methods=['GET'])
def get_vehicles():
    vehicles = Vehicle.query.all()
    result = [vehicle.to_dict() for vehicle in vehicles]
    return jsonify(result)
    
# Obtener vehiculo por ID
@vehicle_bp.route('/<int:id>', methods=['GET'])
def get_vehicle(id):
    vehicle = Vehicle.query.get(id)
    if vehicle is None:
        return jsonify({'error': 'Vehiculo no encontrado'}), 404
    return jsonify(vehicle.to_dict())

# Crear Vehiculo
@vehicle_bp.route('/', methods=['POST'])
def create_vehicle():
    data = request.get_json()

    # Validar los datos necesarios
    if not data or not all(key in data for key in ['license_plate', 'brand', 'model', 'color', 'year', 'driver_id']):
        return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

    # Verificar si el conductor existe
    driver = get_driver(data['driver_id'])

    # Crear un nuevo vehículo
    new_vehicle = Vehicle(
        license_plate=data['license_plate'],
        brand=data['brand'],
        model=data['model'],
        color=data['color'],
        year=data['year']
    )

    try:
        # Agregar el nuevo vehículo a la base de datos
        db.session.add(new_vehicle)
        db.session.commit()

        # Crear una entrada en la tabla Vehicle_Driver
        new_vehicle_driver = Vehicle_Driver(
            vehicle_id=new_vehicle.id,
            driver_id=driver.user_id
        )

        db.session.add(new_vehicle_driver)
        db.session.commit()

        return jsonify(new_vehicle.to_dict()), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'mensaje': 'Error creando vehículo', 'error': str(e)}), 500
   
    
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