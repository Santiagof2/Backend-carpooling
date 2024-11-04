from server.db import db

class Trip(db.Model):
    __tablename__ = 'Trip'

    id = db.Column(db.Integer, primary_key=True)
    departure_date = db.Column(db.Date, nullable=False)
    departure_time = db.Column(db.Time, nullable=False)
    available_seats = db.Column(db.Integer, nullable=False)
    seat_price = db.Column(db.Float, nullable=False)
    creation_timestamp = db.Column(db.DateTime, nullable=False)
    departure_address_id = db.Column(db.Integer, db.ForeignKey('Address.id'), nullable=False)
    arrival_address_id = db.Column(db.Integer, db.ForeignKey('Address.id'), nullable=False)
    vehicle_driver_id = db.Column(db.Integer, db.ForeignKey('Vehicle_Driver.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='active')

    departure_address = db.relationship('Address', foreign_keys=[departure_address_id])
    arrival_address = db.relationship('Address', foreign_keys=[arrival_address_id])
    vehicle_driver = db.relationship('Vehicle_Driver', foreign_keys=[vehicle_driver_id])

    def to_dict(self):
        return {
            'id': self.id,
            'departure_date': self.departure_date.strftime('%Y-%m-%d'),
            'departure_time': self.departure_time.strftime('%H:%M:%S'),
            'available_seats': self.available_seats,
            'seat_price': self.seat_price,
            'creation_timestamp': self.creation_timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'departure_address': self.departure_address.to_dict() if self.departure_address else None,
            'arrival_address': self.arrival_address.to_dict() if self.arrival_address else None,
            'vehicle_driver': self.vehicle_driver.to_dict() if self.vehicle_driver else None,
            'status': self.status
        }

    def cancel_trip(self):
        self.status = 'cancelled'
        db.session.commit()