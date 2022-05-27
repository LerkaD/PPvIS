from PlantClass import MainClass
import random
class Carrot(MainClass):
    def __init__(self, coordinates, garden):
        super().__init__(garden)
        self.parameters = {
            "index": 0,
            "type_id": 1,
            "name": "carrot",
            "symbol_on_map": "C",
            "age": 0,
            "coordinates": coordinates,
            "max_age": 8,
            "life_points": 100,
            "points_to_grow_up": 12,
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
                self.parameters["life_points"] -= 20
            if days > 4:
                self.parameters["life_points"] -= 50    
        if self.parameters["watered"]:  #растет только если полито
            self.parameters["start_points"] += 3
        if self.parameters["illness"]:  #если болезнь есть, то при росте отниметься 10 хп
            self.parameters["life_points"] -= 10
        if self.parameters["points_to_grow_up"] <= self.parameters["start_points"] and self.parameters["life_points"] > 15:
            return self
        else:
            return None

    def opportunity_to_live(self):
        if self.parameters["life_points"] <= 0:
            return self
        else:
            return None

    def get_illness_check(self):  #получение болезни (шанс 40%)
        self.parameters["illness"] = random.choices([True, False], weights=[40, 60], k=1)[0]
        return self

    def get_rid_of_illness_check(self):  #избавление от болезни (шанс 80%)
        self.parameters["illness"] = random.choices([True, False], weights=[20, 80], k=1)[0]
        return self

    def water(self):
        if not self.parameters["watered"]:  #если watered == false, то
            self.parameters["watered"] = True
        else:
            self.parameters["life_points"] -= 10  #если растение уже было полито (watered == True), то отнимаем 10 хп
        return self
