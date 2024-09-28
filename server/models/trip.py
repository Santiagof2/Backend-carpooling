class Trip:
    def __init__(self, id:int, departure_date:str, departure_time:str, seats:int, price:float, departure_address_id:int, created_at:str, arrival_address_id:int, vehicle_driver_id:int):
        self.id = id
        self.departure_date = departure_date
        self.departure_time = departure_time
        self.available_seats = seats
        self.seat_price = price
        self.creation_timestamp = created_at
        self.departure_address_id = departure_address_id
        self.arrival_address_id = arrival_address_id
        self.vehicle_driver_id = vehicle_driver_id

    def __repr__(self):
        return f"<Trip {self.id}>"