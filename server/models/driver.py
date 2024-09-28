from server.models import User

class Driver(User):
    def __init__(self, id ,user_id):
        self.id = id
        self.user_id = user_id