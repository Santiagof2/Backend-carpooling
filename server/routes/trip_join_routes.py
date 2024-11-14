from flask import Blueprint, jsonify, request
from server.db import db
from server.models.passenger_trip import PassengerTrip
from server.models.passenger import Passenger
from server.models.trip import Trip

trip_join_bp = Blueprint('trip_db', __name__, url_prefix='/trip_join')

@trip_join_bp.route('/', methods=['POST'])
def join_PassengerTrip():
    data = request.get_json()
    if data.get('id_trip') is None or data.get('passenger_id') is None:
        return jsonify({'error': 'Faltan datos'}), 400

    trip = Trip.query.filter_by(id=data.get('id_trip')).first()
    if trip is None:
        return jsonify({'error': 'Viaje no encontrado'}), 404

    passenger = get_passenger(data.get('passenger_id'))
    if passenger is None: # si pasajero no existe lo crea
        new_passenger = Passenger(user_id=data['passenger_id'])
        db.session.add(new_passenger)
        db.session.commit()
        new_passenger_trip = PassengerTrip(trip_id=data['id_trip'], passenger=new_passenger)
        db.session.add(new_passenger_trip)
        db.session.commit()
        return jsonify({'message': 'Solicitud del pasajero agregada exitosamente', 'id': new_passenger_trip.id}), 200
    
    new_passenger_trip = PassengerTrip(trip_id=data['id_trip'], passenger=passenger)
    db.session.add(new_passenger_trip)
    db.session.commit()

    return jsonify({'message': 'Solicitud del pasajero agregada exitosamente', 'id': new_passenger_trip.id}), 200

def descontar_cupo(id_trip: int):
    trip = Trip.query.filter_by(id=id_trip).first()
    if trip:
        trip.available_seats -= 1
        db.session.commit()
        return trip
    return None

def get_passenger(user_id):
    return Passenger.query.filter_by(user_id=user_id).first()