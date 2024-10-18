from datetime import datetime
from flask import Blueprint, jsonify, request
from server.db import db
from server.models import User

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')