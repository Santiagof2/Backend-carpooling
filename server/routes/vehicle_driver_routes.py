from flask import Blueprint, jsonify, request
from server.db import db
from server.models import Vehicle_Driver

vehicle_driver_bp = Blueprint('vehicle_driver_bp', __name__, url_prefix='/vehicle_drivers')

@vehicle_driver_bp.route('/', methods=['GET'])
def get_vehicle_drivers():
    vehicle_drivers = Vehicle_Driver.query.all()
    result = [vehicle_driver.to_dict() for vehicle_driver in vehicle_drivers]
    return jsonify(result)