# from server.models.vehicle import Vehicle
# from server.models.driver import Driver

# class VehicleDriver:
#     def __init__(self, id: int, driver: Driver, vehicle: Vehicle) -> None:
#         self._id = id
#         self._driver = driver
#         self._vehicle = vehicle

#     def to_dict(self):
#         return {
#             'id': self._id,
#             'driver': self._driver.to_dict(),
#             'vehicle': self._vehicle.to_dict()
#         }

#     def get_id(self):
#         return self._id

from server.db import db

class VehicleDriver(db.Model):
    __tablename__ = 'Vehicle_driver'

    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('Driver.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('Vehicle.id'), nullable=False)

    driver = db.relationship('Driver', back_populates='vehicles')
    vehicle = db.relationship('Vehicle', back_populates='drivers')

    def to_dict(self):
        return {
            'id': self.id,
            'driver': self.driver.to_dict(),
            'vehicle': self.vehicle.to_dict()
        }

    def get_id(self):
        return self.id