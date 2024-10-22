from server.db import db
from server.models import User

class Passenger(User):
    def __init__(self, id: int, User: User):
        self._id = id
        self.user = User
    
    def to_dict(self):
        return {
            'id': self._id,
            'user': self.user.to_dict()
        }