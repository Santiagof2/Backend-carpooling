from server.db import db  # Importar el objeto db desde db.py

class Vehicle(db.Model):
    __tablename__ = 'Vehicle'

    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(45), nullable=False)
    brand = db.Column(db.String(45), nullable=False)
    model = db.Column(db.String(45), nullable=False)
    color = db.Column(db.String(45), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'license_plate': self.license_plate,
            'brand': self.brand,
            'model': self.model,
            'color': self.color,
            'year': self.year
        }