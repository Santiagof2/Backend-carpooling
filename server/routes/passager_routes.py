from flask import Blueprint, jsonify, request
from server.db import db
from server.models.trip import Trip
from server.models.passager_trip import PassagerTrip

passager_bp = Blueprint('passager_bp', __name__, url_prefix='/passager')

@passager_bp.route('/trips/<int:trip_id>/cancel', methods=['POST'])
def cancel_trip(trip_id):
    passager_id = request.json.get('passager_id')
    if passager_id is None:
        return jsonify({'error': 'bad passager_id'}), 400
    for request in db.trip_requests:
        if request._trip._id == trip_id and request.passager._id == passager_id and request._status == 'accepted':
            request.cancel()
            return jsonify({'message': f'Passager ({passager_id}) cancelled the Trip successfully'}), 200
    return jsonify({'message': 'Trip not found or not accepted'}), 404
