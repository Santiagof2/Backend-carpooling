from server.db import db  # Importar el objeto db desde db.py

class User(db.Model):
    __tablename__ = 'User'
    
    id = db.Column(db.String(28), primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), unique=True, nullable=False)
    username = db.Column(db.String(45), unique=True, nullable=False)
    creation_date = db.Column(db.String(45), nullable=False)
    expo_push_token = db.Column(db.String(42), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'username': self.username,
            'creation_date': self.creation_date,
            'expo_push_token': self.expo_push_token
        }