from server.db import db

class Passenger(db.Model):
    __tablename__ = 'Passenger'

    user_id = db.Column(db.String(28), db.ForeignKey('User.id'), primary_key=True)

    rating = db.Column(db.Float, nullable=False, default=0)
    rating_count = db.Column(db.Integer, nullable=False, default=0)

    user = db.relationship('User', backref='passenger')
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'user': self.user.to_dict(),
            'rating': self.rating,
            'rating_count': self.rating_count,
        }
    
    def add_rating(self, new_rating):

        if new_rating < 1 or new_rating > 5:
            raise ValueError("El rating debe estar en el rango de 1 a 5.")
    
        if self.rating_count == 0:
            # Primer rating
            self.rating = new_rating
        else:
            # Calculo el promedio ponderado
            self.rating = (self.rating * self.rating_count + new_rating) / (self.rating_count + 1)
        
        self.rating_count += 1
        db.session.commit()
