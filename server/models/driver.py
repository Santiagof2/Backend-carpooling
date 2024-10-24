from server.db import db

class Driver(db.Model):
    __tablename__ = 'Driver'

    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), primary_key=True)
    
    user = db.relationship('User', backref='driver')  # Relación con el modelo User

    def to_dict(self):
        return self.user.to_dict() if self.user else None