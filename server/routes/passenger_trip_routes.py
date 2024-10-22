from datetime import datetime
from flask import Blueprint, jsonify, request
from server.db import db
from server.models import passengerTrip

passenger_trip_bp = Blueprint('passenger_trip_bp', __name__, url_prefix='/passenger_trips')

@passenger_trip_bp.route('/', methods=['GET'])
def get_passenger_trips():
    passenger_trips = passengerTrip.query.all()
    result = [passenger_trip.to_dict() for passenger_trip in passenger_trips]
    return jsonify(result)