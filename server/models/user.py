class User:
    def __init__(self, id: int, first_name: str, last_name: str, password: str, email: str, username: str, creation_date: str, email_validation: bool):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._password = password
        self._email = email
        self._username = username
        self._creation_date = creation_date
        self._email_validation = email_validation

class Driver(User):
    def __init__(self, id: int, User: User):
        self._id = id
        self.user = User

class Passenger(User):
    def __init__(self, id: int, User: User):
        self._id = id
        self.user = User
