from flask import Blueprint, request, jsonify
from datetime import datetime
from server.src.database import Database  

trip_a = Blueprint('travel', __name__ ,url_prefix='/trip' )

# Listar viajes disponibles
@trip_a.route('/available', methods=['GET'])
def get_trips_available():
    # Obtener la fecha actual para filtrar viajes pasados
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Filtrar viajes con asientos disponibles y fecha de salida futura
    available_trips = [
        trip for trip in Database.trips
        if trip._available_seats > 0 and trip._departure_date >= current_date
    ]

    return jsonify({'viajes': [trip.to_dict() for trip in available_trips]})
