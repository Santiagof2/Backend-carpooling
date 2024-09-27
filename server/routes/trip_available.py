from flask import Blueprint, request, jsonify
from datetime import datetime
from server.models import Trip
from server.src.database import Database

trip = Blueprint(' trip', __name__)

# Listar viajes Disponibles 
@ trip.route('/', methods=['GET'])
def get_travels():
    # Obtener la fecha actual para filtrar viajes pasados
    current_date = datetime.now()
    
    # Filtrar viajes con asientos disponibles y fecha de salida futura
    trips = Trip.query.filter(Trip.available_seats > 0, Trip.departure_date >= current_date).all()

    return jsonify({'viajes disponibles ': [trip.serialize() for trip in trips ]})