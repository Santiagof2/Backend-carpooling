from server.db import db

class Message(db.Model):
    __tablename__ = 'Message'
    
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    trip_id = db.Column(db.Integer, db.ForeignKey('Trip.id'), nullable=False) 
    user_id = db.Column(db.String(28), db.ForeignKey('User.id'), default=None, nullable=True) 
    is_system = db.Column(db.Boolean, default=False, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'message': self.message,
            'user_id': self.user_id,
            'trip_id': self.trip_id,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'is_system': self.is_system,
        }
    user = db.relationship('User', backref='messages')