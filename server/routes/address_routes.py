from datetime import datetime
from flask import Blueprint, jsonify, request
from server.models import Address
from server.db import db

address_bp = Blueprint('address_bp', __name__, url_prefix='/addresses')

# Obtener todas las direcciones
@address_bp.route('/', methods=['GET'])
def get_address():
    addresses = Address.query.all()
    result = [address.to_dict() for address in addresses]
    return jsonify(result)

# Crear una dirección
@address_bp.route('/', methods=['POST'])
def create_address():
    data = request.get_json()

    # Validar los datos necesarios
    if not data or not all(key in data for key in ['street', 'number', 'latitude', 'longitude', 'locality_id']):
        return jsonify({'message': 'Missing required fields'}), 400
    
    try:

        # Crear una nueva dirección
        new_address = Address(
            street=data['street'],
            number=data['number'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            locality_id=data['locality_id']
        )

        db.session.add(new_address)
        db.session.commit()

        return jsonify(new_address.to_dict()), 201

    except Exception as e:
        return jsonify