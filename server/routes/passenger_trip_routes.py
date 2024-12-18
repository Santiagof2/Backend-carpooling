from datetime import datetime
from flask import Blueprint, jsonify, request
from server.db import db
from server.models import PassengerTrip

passenger_trip_bp = Blueprint('passenger_trip_bp', __name__, url_prefix='/passenger_trips')

# Obtener todos los PassengerTrips
@passenger_trip_bp.route('/', methods=['GET'])
def get_passenger_trips():
    passenger_trips = PassengerTrip.query.all()
    result = [passenger_trip.to_dict() for passenger_trip in passenger_trips]
    return jsonify(result)