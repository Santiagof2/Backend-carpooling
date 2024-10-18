from flask import Blueprint, jsonify, request
from server.database import Database

passager_bp = Blueprint('passager_bp', __name__, url_prefix='/passager')

@passager_bp.route('/trips/<int:trip_id>/cancel', methods=['POST'])
def cancel_trip(trip_id):
    passenger_id = request.get_json().get('passenger_id')
    if passenger_id is None:
        return jsonify({'error': 'bad passenger_id'}), 400
    for trip_request in Database.trip_requests:
        if trip_request._trip._id == trip_id and trip_request._passenger._id == passenger_id and trip_request._status == 'accepted':
            trip_request.cancel()
            return jsonify({'message': f'Passager ({passenger_id}) cancelled the Trip successfully'}), 200
    return jsonify({'message': 'Trip not found or not accepted'}), 404
