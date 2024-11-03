from datetime import datetime
from flask import Blueprint, jsonify, request
from server.models import Trip
from server.db import db
from server.models import Vehicle, Vehicle_Driver, Driver
from server.utils.functions import get_driver
from sqlalchemy.exc import IntegrityError

from server.utils.validations import validate_token

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

# Crear Vehículo
@vehicle_bp.route('/', methods=['POST'])
def create_vehicle():
    data = request.get_json()
    token = request.headers.get('Authorization')
    user = validate_token(token)
    if not user:
        return jsonify({'mensaje': 'Acceso no autorizado'}), 401
    # Validar los datos necesarios
    if not data or not all(key in data for key in ['license_plate', 'brand', 'model', 'color', 'year', 'driver_id']):
        return jsonify({'mensaje': 'Faltan campos requeridos'}), 400

    try:
        # Verificar si el vehículo ya existe
        existing_vehicle = Vehicle.query.filter_by(license_plate=data['license_plate']).first()
        if existing_vehicle:
            return jsonify({'mensaje': 'El vehículo ya existe'}), 409 # conflicy

        # Crear el nuevo vehículo
        new_vehicle = Vehicle(
            license_plate=data['license_plate'],
            brand=data['brand'],
            model=data['model'],
            color=data['color'],
            year=data['year']
        )

        # Verificar si el conductor existe
        driver = Driver.query.filter_by(user_id=data['driver_id']).first()
        if not driver:  # Si no existe, crear el conductor
            driver = Driver(user_id=data['driver_id'])
            db.session.add(driver)

        # Agregar el nuevo vehículo y la relación en Vehicle_Driver dentro de una única transacción
        db.session.add(new_vehicle)
        db.session.flush()  # Hace que `new_vehicle.id` esté disponible sin hacer commit

        # Verificar si la relación ya existe en Vehicle_Driver
        existing_vehicle_driver = Vehicle_Driver.query.filter_by(
            vehicle_id=new_vehicle.id,
            driver_id=driver.user_id
        ).first()

        if not existing_vehicle_driver:  # Si no existe, crear la relación
            new_vehicle_driver = Vehicle_Driver(
                vehicle_id=new_vehicle.id,
                driver_id=driver.user_id
            )
            db.session.add(new_vehicle_driver)

        # Confirmar la transacción
        db.session.commit()

        return jsonify(new_vehicle.to_dict()), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'mensaje': 'Error de integridad en la base de datos, revisa los campos únicos'}), 409

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