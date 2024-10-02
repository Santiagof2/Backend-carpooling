from server.models.user import Passenger
from server.models.trip import Trip

class PassengerTrip:
    def __init__(self, id: int, passenger: Passenger, trip: Trip):
        self._id = id
        self._passenger = passenger
        self._trip = trip

    def to_dict(self):
        return {
            'id': self._id,
            'passenger': self._passenger.to_dict(),
            'trip': self._trip.to_dict()
        }