class Vehicle:
    def __init__(self, id: int, license_plate: str, brand: str, model: str, color: str) -> None:
        self._id = id
        self._license_plate = license_plate
        self._brand = brand
        self._model = model
        self._color = color

    def to_dict(self):
        return {
            'id': self._id,
            'license_plate': self._license_plate,
            'brand': self._brand,
            'model': self._model,
            'color': self._color
        }
