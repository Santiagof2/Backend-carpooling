from flask import Blueprint, jsonify, request
from server.database import Database
from server.models.trip import Trip
from server.models.passenger_trip import PassengerTrip

passager_bp = Blueprint('passager_bp', __name__, url_prefix='/passager')

@passager_bp.route('/trips/<int:trip_id>/cancel', methods=['POST'])
def cancel_trip(trip_id):
    passenger_id = request.json.get('passenger_id')
    if passenger_id is None:
        return jsonify({'error': 'bad passenger_id'}), 400
    for request in Database.trip_requests:
        if request._trip._id == trip_id and request._passenger._id == passenger_id and request._status == 'accepted':
            request.cancel()
            return jsonify({'message': f'Passager ({passenger_id}) cancelled the Trip successfully'}), 200
    return jsonify({'message': 'Trip not found or not accepted'}), 404
