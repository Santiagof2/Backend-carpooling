class City:
    def __init__(self, id:int ,city_name:str, province_id:int):
        self.id = id
        self.city_name = city_name
        self.province_id = province_id

    def get_id(self):
        return self.id