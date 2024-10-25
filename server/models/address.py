from server.db import db  # Importar el objeto db desde db.py

class Principal_Subdivision(db.Model):
    __tablename__ = 'Principal_Subdivision'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)

    def to_dict(self):
        return {
            'name': self.name
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

    locality = db.relationship('Locality', backref='Address')

    def to_dict(self):
        return {
            'id': self.id,
            'street': self.street,
            'number': self.number,
            'locality': self.locality.to_dict()
        }