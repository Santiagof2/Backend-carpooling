from server.models.vehicle import Vehicle
from server.models.user import Driver

class VehicleDriver:
    def __init__(self, id: int, driver: Driver, vehicle: Vehicle) -> None:
        self._id = id
        self._driver = driver
        self._vehicle = vehicle

    def to_dict(self):
        return {
            'id': self._id,
            'driver': self._driver,
            'vehicle': self._vehicle
        }

    def get_id(self):
        return self._id