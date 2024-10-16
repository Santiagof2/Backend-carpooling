from server.config import Config
from server.routes import *
from os import environ as env
from dotenv import load_dotenv, find_dotenv
from flask import Flask, jsonify
from authlib.integrations.flask_oauth2 import ResourceProtector
from validator import Auth0JWTBearerTokenValidator

require_auth = ResourceProtector()
validator = Auth0JWTBearerTokenValidator(
    "dev-voifjkzdk2go4y1p.us.auth0.com",
    "carpu"
)
require_auth.register_token_validator(validator)
def create_app():
    
    # Aplicacion de Flask
    app = Flask(__name__)
    # Carga de configuración
    app.config.from_object(Config)

    # Registro de Blueprints
    app.register_blueprint(address_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(trip_join_bp)
    app.register_blueprint(trip_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(role_selection)
    app.register_blueprint(vehicle_bp)
    return app

app = create_app()

@app.route("/api/public")
def public():
    """No access token required."""
    response = (
        "Hello from a public endpoint! You don't need to be"
        " authenticated to see this."
    )
    return jsonify(message=response)

@app.route("/api/private")
@require_auth(None)
def private():
    """A valid access token is required."""
    response = (
        "Hello from a private endpoint! You need to be"
        " authenticated to see this."
    )
    return jsonify(message=response)


@app.route("/api/private-scoped")
@require_auth("read:messages")
def private_scoped():
    """A valid access token and scope are required."""
    response = (
        "Hello from a private endpoint! You need to be"
        " authenticated and have a scope of read:messages to see"
        " this."
    )
    return jsonify(message=response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
