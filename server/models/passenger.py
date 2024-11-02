from server.db import db

class Passenger(db.Model):
    __tablename__ = 'Passenger'

    user_id = db.Column(db.String(28), db.ForeignKey('User.id'), primary_key=True)

    user = db.relationship('User', backref='passenger')
    
    def to_dict(self):
        return self.user.to_dict() if self.user else None