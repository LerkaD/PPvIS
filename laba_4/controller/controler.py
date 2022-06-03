import pygame_widgets
from pygame_widgets.button import Button

from model.Gamemap import *

class Controller:
    def __init__(self):
        self.garden = None
    
    def setView(self, view):
        self.view = view
    
    def watering_in_map(self):
        self.garden.watering_in_map()
    
    def plants_info(self, x, y, z):
        self.view.plants_info(x, y, z)
        return self.garden.plants_info(x, y, z)
    
    def get_weather(self):
        return self.garden.weather.parameters["weather_is"]
    
    def get_list_of_plants(self):
        return self.garden.plants
    
    def plant_add(self, smth):
        self.garden.plants.append(smth)
        
    def get_parametr(self, i, parametr):
        return self.garden.plants[i].parameters[parametr]
    
    def garden_init(self, world: World):
        self.garden = world
    
    def add_pests_on_game_map(self):
        self.garden.add_pests_on_game_map()
        
    def add_plant_on_game_map(self):
        self.garden.add_plant_on_game_map()
        
    def add_trees_on_game_map(self):
        self.garden.add_trees_on_game_map()
        
    def step_print(self):
        self.garden.step_print()
        self.view.step_print()
        
    def commands(self, commands):
        self.garden.commands(commands)
        
    def get_count_of_global_days(self):
        return self.garden.count_of_global_days
           
    def get_harvest_of_apples(self):
        return self.garden.harvest_of_apples
    
    def get_harvest_of_apples(self):
        return self.garden.harvest_of_apples
    
    def get_harvest_of_vegetables(self):
        return self.garden.harvest_of_vegetables
    
    def get_died_from_hungry(self):
        return self.garden.died_from_hungry
    
    def get_died_from_pests(self):
        return self.garden.died_from_pests
    
    def get_died_from_hp(self):
        return self.garden.died_from_hp
    
    def get_map_size(self, i):
        return self.garden.map_size[i]
    
    def game_map_add(self, row):
        self.garden.game_map.append(row)
        
    def plants_info(self, x, y, z):
        return self.garden.plants_info(x, y, z)
        
        
        