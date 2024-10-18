from server.db import db

class Message(db.Model):
    __tablename__ = 'Message'
    
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.String(45), nullable=False) # diferente a los nombres del der
    id_user = db.Column(db.Integer, db.ForeignKey('User.id'), default=None, nullable=True) 
    id_trip = db.Column(db.Integer, nullable=False) 
    is_system = db.Column(db.Boolean, default=False, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'id_user': self.id_user,
            'id_trip': self.id_trip,
            'message': self.message,
            'created_at': self.created_at,
            'is_system': self.is_system,
        }
