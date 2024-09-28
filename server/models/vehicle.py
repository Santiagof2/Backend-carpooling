class Vehicle:
    def __init__(self, vehicle_id, license_plate, brand, model, color, year):
        self.vehicle_id = vehicle_id
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    def get_id(self):
        return self.vehicle_id