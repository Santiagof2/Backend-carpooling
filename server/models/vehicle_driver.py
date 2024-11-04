from server.db import db

class Vehicle_Driver(db.Model):
    __tablename__ = 'Vehicle_Driver'

    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.String(28), db.ForeignKey('Driver.user_id'), primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('Vehicle.id'), primary_key=True)
    
    driver = db.relationship('Driver', backref='Vehicle_Driver')
    vehicle = db.relationship('Vehicle', backref='Vehicle_Driver')

    def to_dict(self):
        return {
            'driver_id': self.driver_id,
            'vehicle_id': self.vehicle_id,
            'driver': self.driver.to_dict() if self.driver else None,
            'vehicle': self.vehicle.to_dict() if self.vehicle else None
        }