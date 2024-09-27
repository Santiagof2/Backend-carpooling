from datetime import datetime
from flask import Blueprint, jsonify, request
from server.models import Trip
from server.src.database import Database

address_bp = Blueprint('address_bp', __name__, url_prefix='/address')

@address_bp.route('/', methods=['GET'])
def get_address():
    return jsonify(Database.addresses)

@address_bp.route('/', methods=['POST'])
def create_address():
    data = request.get_json()

    