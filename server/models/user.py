from server.db import db  # Importar el objeto db desde db.py

class User(db.Model):
    __tablename__ = 'User'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), unique=True, nullable=False)
    username = db.Column(db.String(45), unique=True, nullable=False)
    creation_date = db.Column(db.String(45), nullable=False)
    email_validation = db.Column(db.Boolean, nullable=False, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'username': self.username,
            'creation_date': self.creation_date,
            'email_validation': self.email_validation
        }

class Driver(User):
    def __init__(self, id: int, User: User):
        self._id = id
        self.user = User
    
    def to_dict(self):
        return {
            'id': self._id,
            'user': self.user.to_dict()
        }

class Passenger(User):
    def __init__(self, id: int, User: User):
        self._id = id
        self.user = User
    
    def to_dict(self):
        return {
            'id': self._id,
            'user': self.user.to_dict()
        }
