from server.db import db  # Importar el objeto db desde db.py

class Country(db.Model):
    __tablename__ = 'Country'

    id = db.Column(db.Integer, primary_key=True)
    country  = db.Column(db.String(45), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'country': self.country,
        }

class Principal_Subdivision(db.Model):
    __tablename__ = 'Principal_Subdivision'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('Country.id'), nullable=False)

    country = db.relationship('Country', backref='Principal_Subdivision')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'country': self.country.to_dict()
        }

class Locality(db.Model):
    __tablename__ = 'Locality'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    principal_subdivision_id = db.Column(db.Integer, db.ForeignKey('Principal_Subdivision.id'), nullable=False)

    principal_subdivision = db.relationship('Principal_Subdivision', backref='Locality')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'principal_subdivision': self.principal_subdivision.to_dict()
        }

class Address(db.Model):
    __tablename__ = 'Address'

    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(45), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    locality_id = db.Column(db.Integer, db.ForeignKey('Locality.id'), nullable=False)
    longitude = db.Column(db.Double, nullable=False)
    latitude = db.Column(db.Double, nullable=False)

    locality = db.relationship('Locality', backref='Address')

    def to_dict(self):
        return {
            'id': self.id,
            'street': self.street,
            'number': self.number,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'locality': self.locality.to_dict()
        }