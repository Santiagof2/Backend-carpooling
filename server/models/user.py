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

    def to_dict(self):
        return {
            'id': self._id,
            'first_name': self._first_name,
            'last_name': self._last_name,
            'password': self._password,
            'email': self._email,
            'username': self._username,
            'creation_date': self._creation_date,
            'email_validation': self._email_validation
        }

class Driver(User):
    def __init__(self, id: int, first_name: str, last_name: str, password: str, email: str, username: str, creation_date: str, email_validation: bool):
        super().__init__(id, first_name, last_name, password, email, username, creation_date, email_validation)

class Passenger(User):
    def __init__(self, id: int, first_name: str, last_name: str, password: str, email: str, username: str, creation_date: str, email_validation: bool):
        super().__init__(id, first_name, last_name, password, email, username, creation_date, email_validation)