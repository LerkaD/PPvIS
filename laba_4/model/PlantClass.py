
class MainClass:
    parameters = {
        "index": 0,
        "type_id": 0,
        "name": "",
        "symbol_on_map": "",
        "age": 0,
        "coordinates": tuple(),
        "max_age": 0,
        "life_points": 0,
        "factor_grow_up": 0,
        "factor_plants": 0,
        "factor_pests": 0,
        "hungry": True,
        "weed": False
    }

    def __init__(self, world=None):
        if world is not None:
            self.world = world

    def attack_plant(self):
        pass

    def aging(self):
        pass

    def get_position(self):
        pass

    def grow_up(self):
        pass

    def opportunity_to_live(self):
        pass



