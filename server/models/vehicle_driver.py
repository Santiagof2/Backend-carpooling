from server.models.vehicle import Vehicle
from server.models.user import Driver


class VehicleDriver:
    def __init__(self, vehicle_driver_id, driver, vehicle):
        self.id = vehicle_driver_id
        self.driver = driver
        self.vehicle = vehicle

    def get_id(self):
        return self.vehicle_driver_id
