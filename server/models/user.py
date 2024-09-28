class User:
    def __init__(self, user_id, first_name, last_name, password, email, username, registration_date, is_active):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.username = username
        self.registration_date = registration_date
        self.is_active = is_active
    def get_id(self):
        return self.user_id