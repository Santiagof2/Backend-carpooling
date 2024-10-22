from server.db import db
from server.models.passenger import Passenger
from server.models.trip import Trip

class passengerTrip(db.Model):
    __tablename__ = 'Passenger_Trip'
    
    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('Trip.id'), nullable=False)
    passenger_id = db.Column(db.Integer, db.ForeignKey('Passenger.user_id'), nullable=False)
    status = db.Column(db.String(50), nullable=False, default="pending")

    passenger = db.relationship('Passenger', backref='passenger_trip')
    trip = db.relationship('Trip', backref='passenger_trip')

    def accept(self):
        self.accepted = "accepted"
        self.trip.available_seats -= 1

    def reject(self):
        self.status = "rejected"

    def cancel(self):
        self.status = "cancelled"

    def to_dict(self):
        return {
            'id': self.id,
            'passenger': self.passenger.to_dict(),
            # 'trip': self.trip.to_dict(),
            'status': self.status
        }
