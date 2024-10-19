from server.db import db
from server.models import User

class Driver(db.Model):
    __tablename__ = 'Driver'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)  # Relaciona con la tabla 'User'

    # Relación con el modelo 'User'
    user = db.relationship('User', backref='driver', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user.to_dict()  # Puedes acceder a la información del usuario
        }
