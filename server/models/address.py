class Address:
    def __init__(self, address_id, street, number, city):
        self.id = address_id
        self.street = street
        self.number = number
        self.city = city

    def get_id(self):
        return self.address_id