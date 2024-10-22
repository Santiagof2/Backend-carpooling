from server.db import db
from server.models.passenger import Passenger
from server.models.trip import Trip

class passengerTrip(db.Model):
    __tablename__ = 'Passenger_Trip'
    
    id = db.Column(db.Integer, primary_key=True)
    passenger_id = db.Column(db.Integer, db.ForeignKey('Passenger.user_id'), nullable=False)
    trip_id = db.Column(db.Integer, db.ForeignKey('Trip.id'), nullable=False)
    accepted = db.Column(db.Boolean, default=False)

    passenger = db.relationship('Passenger', backref='passenger_trip')
    trip = db.relationship('Trip', backref='passenger_trip')

    def accept(self):
        self.accepted = "accepted"

    def reject(self):
        self._status = "rejected"

    def cancel(self):
        self._status = "cancelled"
        self._trip._available_seats += 1

    def to_dict(self):
        return {
            'id': self.id,
            'passenger': self.passenger.to_dict(),
            'trip': self.trip.to_dict(),
            'status': self.accepted
        }
