import random

class TheWeather:
    parameters = {
        "counter_for_plants": 0,
        "counter_for_pests": 0,
        "weather_is": "",
    }

    def __init__(self, world=None):
        if world is not None:
            self.world = world

    type_of_weather = ["sun", "rain"]

    def what_weather_today(self):
        weather_today = random.choice(self.type_of_weather)
        if self.parameters["weather_is"] == "sun" and weather_today == "sun":
            weather_today = "drought"
        if self.parameters["weather_is"] == "drought" and weather_today == "sun":
            weather_today = "drought"
        self.parameters["weather_is"] = weather_today
        return self.parameters["weather_is"]
