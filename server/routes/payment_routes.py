from flask import Blueprint, jsonify, request
from server.db import db
from server.models.user import User
from server.utils.functions import get_datetime_today, get_mp_public_key
from server.utils.validations import validate_token
import mercadopago

payment_bp = Blueprint('payment_bp', __name__, url_prefix='/payment')

access_key = get_mp_public_key()
sdk = mercadopago.SDK(access_key)

# Crear un nuevo usuario
@payment_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    token = request.headers.get('Authorization')  # Se espera un header 'Authorization: Bearer <idToken>'
    user = validate_token(token)
    if not user:
        return jsonify({"error": "Invalid token"}), 401

    if not data or not all(key in data for key in ['first_name', 'last_name', 'username']):
        return jsonify({'message': 'Missing required fields'}), 400

    now = get_datetime_today()
    # Crear un nuevo usuario
    new_user = User(
        id=user['id'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        username=data['username'],
        email=user['email'],
        creation_date = now,
    )

    try:
        # Agregar el nuevo usuario a la base de datos
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'user': new_user.to_dict(), 'email_verified': user['email_verified']}), 201  # Retorna el usuario creado y un código 201 de creación exitosa
    except Exception as e:
        db.session.rollback()  # Hacer rollback si hay un error
        return jsonify({'message': 'Error creating user', 'error': str(e)}), 500

@payment_bp.route('/create_preference', methods=['POST'])
def create_preference():
    data = request.get_json()
    preference_data = {
        "items": [
            {
                "title": data["title"],
                "quantity": data["quantity"],
                "currency_id": "ARS",
                "unit_price": data["price"],
            }
        ],
        "back_urls": {
            "success": "yourapp://success",
            "failure": "yourapp://failure",
            "pending": "yourapp://pending"
        },
        "auto_return": "approved",
    }
    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]
    return jsonify({"init_point": preference["init_point"]})