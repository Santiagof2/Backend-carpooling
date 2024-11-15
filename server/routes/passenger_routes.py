from flask import Blueprint, jsonify, request
from server.db import db
from server.models.passenger import Passenger
from server.models.trip import Trip
from server.models.passenger_trip import PassengerTrip

passenger_bp = Blueprint('passenger_bp', __name__, url_prefix='/passenger')

@passenger_bp.route('/trips/<int:trip_id>/cancel', methods=['POST'])
def cancel_trip(trip_id):
    passenger_id = request.json.get('passenger_id')
    if passenger_id is None:
        return jsonify({'error': 'bad passenger_id'}), 400

    trip = Trip.query.filter_by(id=trip_id).first()
    if trip is None:
        return jsonify({'error': 'Trip not found'}), 404

    passenger_trip = PassengerTrip.query.filter_by(trip_id=trip_id, passenger_id=passenger_id, status='accepted').first() #TODO: debe estar aceptado para cancelar?
    if passenger_trip is None:
        return jsonify({'error': 'Passenger not found or not accepted'}), 404

    passenger_trip.cancel()
    db.session.commit()
    return jsonify({'message': f'Passenger ({passenger_id}) cancelled the Trip successfully'}), 200

@passenger_bp.route('/rate/<int:passenger_id>', methods=['POST'])
def rate_passenger(passenger_id):
    rating = request.json.get('rating')

    if passenger_id is None or rating is None:
        return jsonify({'error': 'bad passenger_id or rating'}), 400

    passenger = Passenger.query.filter_by(user_id=passenger_id).first()
    if passenger is None:
        return jsonify({'error': 'Passenger not found'}), 404
    
    try:
        passenger.add_rating(rating)
        return jsonify({'message': f'Passenger ({passenger_id}) rated successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
@passenger_bp.route('/<int:passenger_id>', methods=['GET'])
def get_passenger(passenger_id):
    passenger = Passenger.query.filter_by(user_id=passenger_id).first()
    if passenger is None:
        return jsonify({'error': 'Passenger not found'}), 404
    return jsonify(passenger.to_dict()), 200