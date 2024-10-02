from server.models.vehicle_driver import VehicleDriver
from server.models.address import Address

class Trip:
    def __init__(self, id: int, status: str, departure_date: str, departure_time: str, available_seats: int, seat_price: float, creation_timestamp: int, deaparture_address: Address, arrival_address: Address, vehicle_driver: VehicleDriver) -> None:
        self._id = id
        self._status = status
        self._departure_date = departure_date
        self._departure_time = departure_time
        self._available_seats = available_seats
        self._seat_price = seat_price
        self._creation_timestamp = creation_timestamp
        self._deaparture_address = deaparture_address
        self._arrival_address = arrival_address
        self._vehicle_driver = vehicle_driver
    
    def to_dict(self):
        return {
            'id': self._id,
            'departure_date': self._departure_date,
            'departure_time': self._departure_time,
            'available_seats': self._available_seats,
            'seat_price': self._seat_price,
            'creation_timestamp': self._creation_timestamp,
            'deaparture_address': self._deaparture_address,
            'arrival_address': self._arrival_address,
            'vehicle_driver': self._vehicle_driver
        }