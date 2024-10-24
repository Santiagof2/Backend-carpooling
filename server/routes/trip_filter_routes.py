from flask import request, jsonify, Blueprint
from geopy.distance import geodesic  # Para calcular la distancia geodésica entre dos puntos
import requests #New
from server.db import db
from server.models import Trip



# Función para obtener coordenadas usando Nominatim (OpenStreetMap)
def get_coordinates(street, number, city, province):
    # Construir la dirección completa
    address = f"{street} {number}, {city}, {province}"
    
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': address,
        'format': 'json',
        'limit': 1
    }
    headers = {
        'User-Agent': 'Carpu/1.0 (vamosCarpu@gmail.com)'  
    }
    
    response = requests.get(base_url, params=params, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            lat = float(data[0]['lat'])
            lon = float(data[0]['lon'])
            return lat, lon
    return None, None

trip_filter_bp = Blueprint('trip_filter_bp', __name__ ,url_prefix='/tripOD' )

@trip_filter_bp.route('/', methods=['POST'])
def filter_trips():
    # Puntos de origen y destino seleccionados por el usuario
    user_origin = request.json.get('user_origin')
    user_dest = request.json.get('user_dest')

    # Coordenadas del origen y destino del usuario
    user_origin_coords = (user_origin['coords']['latitude'], user_origin['coords']['longitude'])
    user_dest_coords = (user_dest['coords']['latitude'], user_dest['coords']['longitude'])

    # Obtener todos los viajes de la base de datos
    trips = Trip.query.all()
    filtered_trips = []

    for trip in trips:
        # Dirección de origen y destino del viaje
        origin_address = trip.departure_address  # Es dePArture_addres en codigo y BD
        dest_address = trip.arrival_address  

        # Obtener coordenadas del origen del viaje usando Nominatim
        origin_coords = get_coordinates(
            origin_address.street, origin_address.number,
            origin_address.city.name, origin_address.city.province.name
        )

        # Obtener coordenadas del destino del viaje usando Nominatim
        dest_coords = get_coordinates(
            dest_address.street, dest_address.number,
            dest_address.city.name, dest_address.city.province.name
        )

        # Si se obtienen coordenadas válidas
        if origin_coords and dest_coords:
            # Calcular la distancia usando geopy
            origin_distance = geodesic(user_origin_coords, origin_coords).kilometers
            dest_distance = geodesic(user_dest_coords, dest_coords).kilometers

            # Filtrar los viajes cercanos (ejemplo: dentro de 100 km)
            if origin_distance < 100 and dest_distance < 100:
                total_distance = origin_distance + dest_distance
                filtered_trips.append({
                    'trip_id': trip.id,
                    'origin_address': origin_address.to_dict(),
                    'dest_address': dest_address.to_dict(),
                    'total_distance': total_distance
                })

    # Ordenar los viajes por distancia total (de menor a mayor)
    filtered_trips.sort(key=lambda x: x['total_distance'])

    return jsonify(filtered_trips)
