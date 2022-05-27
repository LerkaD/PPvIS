from model.PlantClass import MainClass

class Pests(MainClass):
    def __init__(self, coordinates, garden):
        super().__init__(garden)
        self.parameters = {
            "index": 0,
            "type_id": 2,
            "name": "pests",
            "symbol_on_map": "P",
            "age": 0,
            "coordinates": coordinates,
            "max_age": 10,
            "life_points": 100,
            "damage": 10,
            "hungry": True,
            "weed": False
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

    def attack_plant(self, plant_for_eat):
        self.parameters["hungry"] = False
        plant_for_eat.parameters["life_points"] -= self.parameters["damage"]
        if self.parameters["life_points"] == 100:
            self.parameters["life_points"] == 100
        else:
            self.parameters["life_points"] += 10
        if plant_for_eat.parameters["life_points"] <= 0:
            return plant_for_eat
        else:
            return None

    def opportunity_to_live(self):
        if self.parameters["weed"] is True:
            self.parameters["life_points"] -= 20
        if self.parameters["hungry"] is True:
            self.parameters["life_points"] -= 40
        if self.parameters["life_points"] <= 0:
            return self
        else:
            return None
        
    def kill_pest(self):
        return self
    
