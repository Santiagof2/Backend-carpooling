from datetime import datetime
from flask import Blueprint, jsonify, request
from server.models import Trip
from server.database import Database
from server.models import Vehicle, VehicleDriver
from .user import buscar_usuario_por_id

vehicle_bp = Blueprint('vehicle_bp', __name__, url_prefix='/vehicles')

def get_vehicle_por_id(id, vehicles):
    for vehicle in vehicles:
        if vehicle._id == id:
            return vehicle
    return None

#Obtener vehiculo por condutor ID
@vehicle_bp.route('/<int:id>', methods=['GET'])
def get_vehicle(id):
    vehicle = get_vehicle_por_id(id, Database.vehicles)
    if not vehicle: return jsonify({'error': 'vehiculo no encontrado'}), 404
    return vehicle.to_dict(), 200

# listar todos los vehiculos
@vehicle_bp.route('/', methods=['GET'])
def get_vehicles():
    list_vehicles = Database.vehicles
    return jsonify([vehicle.to_dict() for vehicle in list_vehicles]), 200

#Crear Vehiculo
@vehicle_bp.route('/', methods=['POST'])
def crear_vehicle():
    data = request.get_json()
    
    # Obtenemos los datos
    license_plate = data.get('license_plate')
    brand = data.get('brand')
    model = data.get('model')
    color = data.get('color')
    year  = data.get('year')
    user_id = data.get('user_id')
    
    # Validación
    if not license_plate  or not brand or not  model or not color or not year or user_id is None:
        return jsonify({'error': 'Faltan datos'}), 400
    
    driver= buscar_usuario_por_id(user_id,Database.users)
    if not driver:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    # Creción del vehiculo
    vehicle = Vehicle(
        len(Database.vehicles) + 1,
        license_plate,
        brand,
        model,
        color,
        year   
    )
    Database.vehicles.append(vehicle)

    # Crear la relación entre el usuario y el vehículo
    vehicle_driver = VehicleDriver(
        len(Database.vehicle_drivers) + 1,
        driver,
        vehicle
    )
    Database.vehicle_drivers.append(vehicle_driver)

    return jsonify({
        'mensaje': 'Vehículo creado correctamente y asociado al usuario.',
        'vehicle_id': vehicle._id,
        'vehicle_driver_id': vehicle_driver.get_id()
    }), 201    
   
    
# Actualizar un Vehiculo existente
@vehicle_bp.route('/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    vehicle = get_vehicle_por_id(id, Database.vehicles)
    
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
    vehicle = get_vehicle_por_id(id, Database.vehicles)
    
    if vehicle is None:
        return jsonify({'error': 'Vehiculo no encontrado'}), 404
    
    Database.vehicles.remove(vehicle)
    
    return jsonify({'mensaje': 'Vehiculo eliminado'}), 200