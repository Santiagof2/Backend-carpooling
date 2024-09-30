class Passager:
    def __init__(self, id:int ,user_id:int):
        self.id = id
        self.user_id = user_id
    
    def get_id(self):
        return self.id