class Passager_trip:
    def __init__(self, id:int ,id_trip:int, passenger_id:int):
        self.id = id
        self.id_trip = id_trip
        self.passenger_id = passenger_id
    
    def get_id(self):
        return self.id
    
    def get_id_trip(self):
        return self.id_trip
    
    def get_passenger_id(self):
        return self.passenger_id