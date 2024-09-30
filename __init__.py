from flask import Flask
from server.config import Config
from server.routes import user_bp, role_selection, trip_a 



def create_app():
    
    # Aplicacion de Flask
    app = Flask(__name__)
    # Carga de configuración
    app.config.from_object(Config)

    # Registro de Blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(role_selection)
    app.register_blueprint(trip_a)
  

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)