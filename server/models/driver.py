from server.db import db

class Driver(db.Model):
    __tablename__ = 'Driver'

    user_id = db.Column(db.String(28), db.ForeignKey('User.id'), primary_key=True)
    
    user = db.relationship('User', backref='driver')  # Relación con el modelo User

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'user': self.user.to_dict(),
        }