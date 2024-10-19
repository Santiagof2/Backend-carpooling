from server.models.vehicle import Vehicle
from server.models.driver import Driver

class VehicleDriver:
    def __init__(self, id: int, driver: Driver, vehicle: Vehicle) -> None:
        self._id = id
        self._driver = driver
        self._vehicle = vehicle

    def to_dict(self):
        return {
            'id': self._id,
            'driver': self._driver.to_dict(),
            'vehicle': self._vehicle.to_dict()
        }

    def get_id(self):
        return self._id