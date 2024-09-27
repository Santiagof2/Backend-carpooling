class Province:
    def __init__(self, id: int, name: str) -> None:
        self._id = id
        self._name = name

    def to_dict(self):
        return {
            'province_id': self._id,
            'name': self._name
        }
    
class City:
    def __init__(self, id: int, name: str, province: Province) -> None:
        self._id = id
        self._name = name
        self._province = province

    def to_dict(self):
        return {
            'id': self._id,
            'name': self._name,
            'province': self._province.to_dict()
        }

class Address:
    def __init__(self, id: int, street: str, number: int, city: City):
        self._id = id
        self._street = street
        self._number = number
        self._city = city

    def to_dict(self):
        return {
            'id': self._id,
            'street': self._street,
            'number': self._number,
            'city': self._city.to_dict()
        }
    
    def get_id(self):
        return self._id