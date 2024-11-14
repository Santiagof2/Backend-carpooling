from flask import request, jsonify, Blueprint
from server.db import db
from server.models import Trip, Rating


ratings_bp = Blueprint('ratings', __name__)

@ratings_bp.route('/rate_user', methods=['POST'])
def rate_user():
    data = request.get_json()
    user_id = data.get('user_id')
    rated_user_id = data.get('rated_user_id')
    trip_id = data.get('trip_id')
    rating_value = data.get('rating')
    comment = data.get('comment', "")

    # Verificar si el viaje existe
    trip = Trip.query.get(trip_id)
    if not trip:
        return jsonify({"error": "Trip not found"}), 404

    # Crear y guardar la calificación 
    rating = Rating(
        user_id=user_id,
        rated_user_id=rated_user_id,
        trip_id=trip_id,
        rating=rating_value,
        comment=comment
    )
    db.session.add(rating)
    db.session.commit()

    return jsonify({
        "id": rating.id,
        "user_id": user_id,
        "rated_user_id": rated_user_id,
        "trip_id": trip_id,
        "rating": rating_value,
        "comment": comment,
        "created_at": rating.created_at
    }), 201

#Obtener reputacion 

def calculate_user_reputation(user_id):
    ratings = Rating.query.filter_by(rated_user_id=user_id).all()
    if not ratings:
        return 0  # No tiene calificaciones aún

    # Calcular el promedio de las calificaciones
    average_rating = sum([r.rating for r in ratings]) / len(ratings)
    return round(average_rating, 2)


@ratings_bp.route('/user_reputation/<int:user_id>', methods=['GET'])
def user_reputation(user_id):
    reputation = calculate_user_reputation(user_id)
    return jsonify({"user_id": user_id, "reputation": reputation})
