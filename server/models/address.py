from server.db import db  # Importar el objeto db desde db.py

class Province(db.Model):
    __tablename__ = 'Province'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)

    def to_dict(self):
        return {
            'name': self.name
        }

class City(db.Model):
    __tablename__ = 'City'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    province_id = db.Column(db.Integer, db.ForeignKey('Province.id'), nullable=False)

    province = db.relationship('Province', backref='City')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'province': self.province.to_dict()
        }

class Address(db.Model):
    __tablename__ = 'Address'

    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(45), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('City.id'), nullable=False)

    city = db.relationship('City', backref='Address')

    def to_dict(self):
        return {
            'id': self.id,
            'street': self.street,
            'number': self.number,
            'city': self.city.to_dict()
        }