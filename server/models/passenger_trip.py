from server.models.passenger import Passenger
from server.models.trip import Trip

class passengerTrip:
    def __init__(self, id: int, passenger: Passenger, trip: Trip, status: str = "pending"):
        self._id = id
        self._passenger = passenger
        self._trip = trip
        self._status = status

    def accept(self):
        self._status = "accepted"

    def reject(self):
        self._status = "rejected"

    def cancel(self):
        self._status = "cancelled"
        self._trip._available_seats += 1

    def to_dict(self):
        return {
            'id': self._id,
            'passenger': self._passenger.to_dict(),
            'trip': self._trip.to_dict(),
            'status': self._status
        }