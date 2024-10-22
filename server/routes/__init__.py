from server.routes.user_routes import user_bp
from server.routes.driver_routes import driver_bp
from server.routes.trip_join_routes import trip_join_bp
from server.routes.trip_routes import trip_bp
from server.routes.address_routes import address_bp
from server.routes.auth_routes import auth_bp
from server.routes.role_selection_routes import role_selection
from server.routes.vehicle_routes import vehicle_bp
from server.routes.passenger_routes import passenger_bp
from server.routes.message_routes import message_bp


__all__ = ['user_bp', 'driver_bp', 'trip_join_bp', 'trip_bp', 'address_bp', 'auth_bp', 'role_selection','vehicle_bp', 'passenger_bp', 'message_bp', 'province_bp']