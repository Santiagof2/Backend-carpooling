from server.routes.user import user_bp
from server.routes.trip_join import trip_join_bp
from server.routes.trip import trip_bp
from server.routes.address import address_bp
from server.routes.auth import auth_bp

__all__ = ['user_bp', 'trip_join_bp', 'trip_bp', 'address_bp']