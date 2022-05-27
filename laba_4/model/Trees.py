from model.PlantClass import MainClass
import random

class Trees1(MainClass):
    def __init__(self, coordinates, garden):
        super().__init__(garden)
        self.parameters = {
            "type_id": 3,
            "index": 0,
            "name": "tree",
            "symbol_on_map": "T",
            "age": 0,
            "coordinates": coordinates,
            "max_age": 20,
            "life_points": 600,
            "points_to_grow_up": 20,
            "start_points": 0,
            "illness": False,
            "watered": False,
            "weed": False,
        }

    def aging(self):
        self.parameters["age"] += 1
        if self.parameters["age"] >= self.parameters["max_age"]:
            return self
        else:
            return None

    def get_position(self):
        x = self.parameters["coordinates"][0]
        y = self.parameters["coordinates"][1]
        position = (x, y)
        return position

    def grow_up(self, days):
        if self.parameters["weed"] is True:  #если есть сорняки
            if days <= 2:
                self.parameters["life_points"] -= 2
            if days > 2 and days <= 4:
                self.parameters["life_points"] -= 15
            if days > 4:
                self.parameters["life_points"] -= 30    
        if self.parameters["watered"]:  #растет только если полито
            self.parameters["start_points"] += 4
        if self.parameters["illness"]:  #если болезнь есть, то при росте отниметься 20 хп
            self.parameters["life_points"] -= 20
        if self.parameters["start_points"] >= self.parameters["points_to_grow_up"] and self.parameters["life_points"] > 100:
            self.parameters["start_points"] = 0
            return self

    def opportunity_to_live(self):
        if self.parameters["life_points"] <= 0:
            return self
        else:
            return None

    def get_illness_check(self):  #получение болезни (шанс 40%)
        self.parameters["illness"] = random.choices([True, False], weights=[40, 60], k=1)[0]
        return self

    def get_rid_of_illness_check(self):  #избавление от болезни (шанс 80%)
        self.parameters["illness"] = random.choices([True, False], weights=[60, 40], k=1)[0]
        return self

    def water(self):
        self.parameters["watered"] = True
        return self
