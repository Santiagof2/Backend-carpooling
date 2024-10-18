from flask import Flask
from server.db import init_db  # Configuración de la base de datos
from server.routes import *

app = Flask(__name__)

# Inicializar la base de datos
init_db(app)

# Registrar el Blueprint de usuarios
app.register_blueprint(user_bp)
app.register_blueprint(address_bp)
app.register_blueprint(trip_join_bp)
app.register_blueprint(trip_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(role_selection)
app.register_blueprint(vehicle_bp)

if __name__ == '__main__':
    app.run(debug=True)
