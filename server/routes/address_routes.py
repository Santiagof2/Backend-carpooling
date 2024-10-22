from datetime import datetime
from flask import Blueprint, jsonify, request
from server.models import Address
from server.db import db

address_bp = Blueprint('address_bp', __name__, url_prefix='/addresses')

@address_bp.route('/', methods=['GET'])
def get_address():
    addresses = Address.query.all()
    result = [address.to_dict() for address in addresses]
    return jsonify(result)