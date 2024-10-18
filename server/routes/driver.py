from flask import Blueprint, jsonify, request
from server.models.trip import Trip
from server.models.passenger_trip import PassengerTrip
from server.database import Database

driver_bp = Blueprint('driver_bp', __name__, url_prefix='/driver')

@driver_bp.route('/trips/<int:trip_id>/requests', methods=['GET'])
def list_passenger_requests(trip_id):
    filtered_requests = [r.to_dict() for r in Database.trip_requests if r._trip._id == trip_id and r._status == 'pending']
    return jsonify(filtered_requests), 200

@driver_bp.route('/trips/<int:trip_id>/requests/<int:request_id>/accept', methods=['POST'])
def accept_passenger(trip_id, request_id):
    for request in Database.trip_requests:
        if request._id == request_id and request._trip._id == trip_id:
            request.accept()
            return jsonify({'message': 'Passenger accepted successfully'}), 200
    return jsonify({'message': 'Request not found'}), 404

@driver_bp.route('/trips/<int:trip_id>/requests/<int:request_id>/reject', methods=['POST'])
def reject_passenger(trip_id, request_id):
    for request in Database.trip_requests:
        if request._id == request_id and request._trip._id == trip_id:
            request.reject()
            return jsonify({'message': 'Passenger rejected successfully'}), 200
    return jsonify({'message': 'Request not found'}), 404

@driver_bp.route('/trips/<int:trip_id>/cancel', methods=['POST'])
def cancel_trip(trip_id):
    driver_id = request.json.get('driver_id')
    for trip in Database.trips:
        if trip._id == trip_id and trip._vehicle_driver._id == driver_id:
            trip.cancel_trip()
            for request in Database.trip_requests:
                if request._trip._id == trip_id:
                    request.cancel()
            return jsonify({'message': f'Driver ({driver_id}) cancelled the Trip successfully'}), 200
    return jsonify({'message': 'Trip not found or unauthorized'}), 404
