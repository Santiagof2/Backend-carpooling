from datetime import datetime
from server.db import db

class Rating(db.Model):
    __tablename__ = 'ratings'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    rated_user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    trip_id = db.Column(db.Integer, db.ForeignKey('Trip.id'), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    comment = db.Column(db.String(100))

    user = db.relationship("User", foreign_keys=[user_id])
    rated_user = db.relationship("User", foreign_keys=[rated_user_id])
    trip = db.relationship("Trip")
    
    def to_dict(self):
        return {
                'id': self.id,
                'user': self.user_id.to_dict(),
                'rated_user_id':self.rated_user_id.to_dict(),
                'trip_id': self.trip_id.to_dict(),
                'rating': self.rating.to_dict(),
                'comment': self.comment.to_dict(),

                }