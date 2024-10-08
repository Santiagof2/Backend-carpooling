from flask import Blueprint, jsonify, request
from server.src.database import Database

chat_bp = Blueprint('chat_bp', __name__, url_prefix='/chat')

@chat_bp.route('/', methods=['GET'])
def get_chats():
    list_trips = Database.trips
    return jsonify([trip.to_dict() for trip in list_trips]), 200
