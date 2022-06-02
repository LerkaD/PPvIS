from calendar import c
from itertools import count
from model.Trees import Trees1
from model.Vegetables import Carrot
from model.PestsClass import Pests
from model.TheWeatherClass import TheWeather
import random
import pickle


class World:
    class Cell:
        coordinates = tuple()
        all_in_cell = list()#не только растения
        list_for_print = list()
        new_list = list()

        def __init__(self, coordinates) :
            self._coordinates = coordinates
            self.all_in_cell = list()
            self.list_for_print = list()

        def add_plant_on_cell(self, plant):# любая сущность
            if len(self.all_in_cell) < 4:
                self.all_in_cell.append(plant)
                self.list_for_print.append(plant.parameters["symbol_on_map"])
            else:
                return
  
           
        def add_weed_on_cell(self, count, plant):
            if self.all_in_cell[count].parameters["type_id"] == 1:
                d = "C!"
            if self.all_in_cell[count].parameters["type_id"] == 2:
                d = "P!"
            if self.all_in_cell[count].parameters["type_id"] == 3:
                d = "T!"
            self.list_for_print.pop(count)
            self.list_for_print.insert(count, d)
            return d
            
        def delete_weed_from_cell(self,count, plant):
            self.list_for_print.pop(count)
            self.list_for_print.insert(count, plant.parameters["symbol_on_map"])
               
        def check_to_add_in_cell(self):
            if len(self.all_in_cell) < 4:
                return True
            else:
                return False

        def print_cell(self):
            if len(self.list_for_print) != 0:
                return self.list_for_print
            else:
                return "*"                

        def get_cell_position(self, smth, index):
            count = 0
            for plant in self.all_in_cell:
                if plant.parameters["type_id"] == smth.parameters["type_id"] and plant.parameters["index"] == index :
                    return count
                else:
                    count += 1

        def remove_smth_from_cell(self, smth):
            for i in  self.all_in_cell:
                if i.parameters["index"] ==  smth.parameters["index"]:
                    self.all_in_cell.remove(i)
                    self.list_for_print.remove(i.parameters["symbol_on_map"])
    
    game_map = list()
    map_size = tuple()
    plants = list()
    weather = TheWeather()
    step = 0
    harvest_of_vegetables = 0
    harvest_of_apples = 0
    died_from_pests = 0
    died_from_hungry = 0
    died_from_illness = 0
    died_from_hp = 0
    weather_today_is = ""  # погодка
    index = 0#уникальный для каждой сущности(показывает порядковый номер добавления в сад)
    count_of_days = 0
    count_of_global_days = 0

    def __init__(self, map_size: list = [1, 2]):
        self.map_size = map_size
        for i in range(0, map_size[0]):
            row = list()
            for j in range(0, map_size[1]):
                row.append(World.Cell([i, j]))
            self.game_map.append(row)

    def start_garden(self):
        count_of_plants = 3
        count_of_pests = 3
        count_of_trees = 3
        for i in range(0, count_of_pests):
            self.add_pests_on_game_map()
        for i in range(0, count_of_plants):
            self.add_plant_on_game_map()
        for i in range(0, count_of_trees):
            self.add_trees_on_game_map()
        for i in range(0, count_of_pests):
            self.add_pests_on_game_map()
        for i in range(0, count_of_plants):
            self.add_plant_on_game_map()
        self.step_print()
        
    #def check_to_add_in_cell(self):
    def find_plant_position(self):
        x = random.randint(0, self.map_size[0] - 1)
        y = random.randint(0, self.map_size[1] - 1)
        if self.game_map[x][y].check_to_add_in_cell() is False:
            return self.find_plant_position()
        else:
            position = (x, y)
            return position

    def check_to_add(self):
        a = int(self.map_size[0])
        b = int(self.map_size[1])
        if len(self.plants) >= 4 * a * b:
            return False
        else:
            return True

    def add_pests_on_game_map(self):
        if self.check_to_add() is True:
            new_plant = Pests(self.find_plant_position(), self)
            self.index += 1
            new_plant.parameters["index"] = self.index
            self.plants.append(new_plant)
            x = int(new_plant.parameters["coordinates"][0])
            y = int(new_plant.parameters["coordinates"][1])
            self.game_map[x][y].add_plant_on_cell(new_plant)
            action = 'add successfully'
        else:
            action = 'add successfully'
        return action


    def add_plant_on_game_map(self):
        if self.check_to_add() is True:
            new_plant = Carrot(self.find_plant_position(), self)
            self.index += 1
            new_plant.parameters["index"] = self.index
            self.plants.append(new_plant)
            x = int(new_plant.parameters["coordinates"][0])
            y = int(new_plant.parameters["coordinates"][1])
            self.game_map[x][y].add_plant_on_cell(new_plant)
            action = 'add successfully'
        else:
            action = 'add successfully'
        return action

    def add_trees_on_game_map(self):
        if self.check_to_add() is True:
            new_plant = Trees1(self.find_plant_position(), self)
            self.index += 1
            new_plant.parameters["index"] = self.index
            self.plants.append(new_plant)
            x = int(new_plant.parameters["coordinates"][0])
            y = int(new_plant.parameters["coordinates"][1])
            self.game_map[x][y].add_plant_on_cell(new_plant)
            action = 'add successfully'
        else:
            action = 'add successfully'
        return action
        

    def step_print(self):
        for row in self.game_map:
            for Cell in row:
                print(Cell.print_cell())

    def aging_in_map(self):
        for smth in self.plants:
            smth = smth.aging()
            if smth is not None:
                self.plants.remove(smth)
                smth.get_position()
                x = int(smth.parameters["coordinates"][0])
                y = int(smth.parameters["coordinates"][1])
                self.game_map[x][y].remove_smth_from_cell(smth)

    def plants_grow_up(self):
        for smth in self.plants:
            if smth.parameters["type_id"] == 1:
                if self.weather.parameters["weather_is"] == "sun":
                    smth = smth.get_rid_of_illness_check()
                    smth = smth.grow_up(self.count_of_days)
                if self.weather.parameters["weather_is"] == "rain":
                    smth = smth.get_illness_check()
                    smth = smth.grow_up(self.count_of_days)
                if self.weather.parameters["weather_is"] == "drought":
                    if not smth.parameters["watered"]:  #если не полито, то -10 хп и никакого роста
                        smth.parameters["life_points"] -= 10
                    if smth.parameters["watered"]:  #если полито, растём
                        smth = smth.grow_up(self.count_of_days)
                if smth is not None:
                    self.harvest_of_vegetables += 1
                    self.plants.remove(smth)
                    smth.get_position()
                    x = int(smth.parameters["coordinates"][0])
                    y = int(smth.parameters["coordinates"][1])
                    self.game_map[x][y].remove_smth_from_cell(smth)

    def trees_grow_up(self):
        for tree in self.plants:
            if tree.parameters["type_id"] == 3:
                if self.weather.parameters["weather_is"] == "sun":
                    tree = tree.get_rid_of_illness_check()
                    tree = tree.grow_up(self.count_of_days)
                if self.weather.parameters["weather_is"] == "rain":
                    tree = tree.get_illness_check()
                    tree = tree.grow_up(self.count_of_days)
                if self.weather.parameters["weather_is"] == "drought":
                    if not tree.parameters["watered"]:  #если не полито, то -20 хп и никакого роста
                        tree.parameters["life_points"] -= 20
                    if tree.parameters["watered"]:  #если полито, растём
                        tree = tree.grow_up(self.count_of_days)
                    if tree is not None:
                        self.harvest_of_apples += 1
                        return self.harvest_of_apples
                        
    def eat_plant_on_map(self):
        for pests in self.plants:
            if pests.parameters["type_id"] == 2 :
                pests.get_position()
                for plant_for_eat in self.plants:
                    if plant_for_eat.parameters["type_id"] == 1:
                        plant_for_eat.get_position()
                        if int(plant_for_eat.parameters["coordinates"][0]) == int(pests.parameters["coordinates"][0]) and int(plant_for_eat.parameters["coordinates"][1]) == int(pests.parameters["coordinates"][1]):
                            plant_for_eat = pests.attack_plant(plant_for_eat)
                            if plant_for_eat is not None:
                                self.died_from_pests += 1
                                self.plants.remove(plant_for_eat)
                                self.game_map[int(plant_for_eat.parameters["coordinates"][0])][int(plant_for_eat.parameters["coordinates"][1])].remove_smth_from_cell(plant_for_eat)
                                return self.died_from_pests

    def damage_trees_on_map(self):
        for pests in self.plants:
            if pests.parameters["type_id"] == 2:
                pests.get_position()
                for plant_for_eat in self.plants:
                    if plant_for_eat.parameters["type_id"] == 3:
                        plant_for_eat.get_position()
                        if int(plant_for_eat.parameters["coordinates"][0]) == int(pests.parameters["coordinates"][0]) and int(plant_for_eat.parameters["coordinates"][1]) == int(pests.parameters["coordinates"][1]):
                            plant_for_eat = pests.attack_plant(plant_for_eat)
                            if plant_for_eat is not None:
                                self.died_from_pests += 1
                                self.plants.remove(plant_for_eat)
           

    def opportunity_to_live_on_map(self):
        for smth in self.plants:
            smth = smth.opportunity_to_live()
            if smth is not None:
                smth.get_position()
                x = int(smth.parameters["coordinates"][0])
                y = int(smth.parameters["coordinates"][1])
                self.game_map[x][y].remove_smth_from_cell(smth)
                self.plants.remove(smth)
                if smth.parameters["type_id"] == 2:
                    self.died_from_hungry += 1
                if smth.parameters["type_id"] == 1 or smth.parameters["type_id"] == 3:
                    self.died_from_hp += 1
                

    def everydays_hungry(self):
        for pests in self.plants:
            if pests.parameters["type_id"] == 2:
                pests.parameters["hungry"] = True

    def weather_today(self):
        self.weather.what_weather_today()
        if self.weather.parameters["weather_is"] == "sun" or self.weather.parameters["weather_is"] == "drought":
            for smth in self.plants:
                smth.parameters["watered"] = False
        if self.weather.parameters["weather_is"] == "rain":
            for smth in self.plants:
                smth.parameters["watered"] = True
        return self.weather.parameters["weather_is"]

    def watering_in_map(self):
        for smth in self.plants:
            if smth.parameters["type_id"] == 1 or smth.parameters["type_id"] == 3:
                smth = smth.water()
        action = "Plants watered!"
        return action #чекаем сработало ли

    def life_cycle(self):
        self.weather_today()
        self.plants_grow_up()
        self.trees_grow_up()
        self.eat_plant_on_map()
        self.aging_in_map()
        self.opportunity_to_live_on_map()
        self.everydays_hungry()

    def step_save(self):
        file = open(r'saved_game.txt', 'wb')
        pickle.dump(self, file)
        for i in range(self.map_size[0]):  # по строке
            for j in range(self.map_size[1]):
                pickle.dump(self.game_map[i][j], file)
        for smth in self.plants:
            pickle.dump(smth, file)
        file.close()
       # print("garden is saved"

    def plants_info(self, position_x, position_y, position_z):
        info_storage = list()
        x = int(position_x)
        y = int(position_y)
        count = int(position_z)
        if int(count) <= len(self.game_map[x][y].all_in_cell):
            name = self.game_map[x][y].all_in_cell[count].parameters["name"]
            print("name:" + name)
            info_storage.append("name: " + name)
            age = self.game_map[x][y].all_in_cell[count].parameters["age"]
            print("age:" + str(age))
            info_storage.append("age: " + str(age))
            life_points = self.game_map[x][y].all_in_cell[count].parameters["life_points"]
            print("life points:" + str(life_points))
            info_storage.append("life points: " + str(life_points))
            weed = self.game_map[x][y].all_in_cell[count].parameters["weed"]
            print("weed: " + str(weed))
            info_storage.append("weed: " + str(weed))
            if int(self.game_map[x][y].all_in_cell[count].parameters["type_id"]) == 1 or int(self.game_map[x][y].all_in_cell[count].parameters["type_id"]) == 3:
                points_to_grow = self.game_map[x][y].all_in_cell[count].parameters["start_points"]
                print("points to grow up :" + str(points_to_grow))
                info_storage.append("points to grow up: " + str(points_to_grow))
                illness = self.game_map[x][y].all_in_cell[count].parameters["illness"]
                print("illness :" + str(illness))
                info_storage.append("illness: " + str(illness))
                watered = self.game_map[x][y].all_in_cell[count].parameters["watered"]
                print("watered :" + str(watered))
                info_storage.append("watered: " + str(watered))
            if int(self.game_map[x][y].all_in_cell[count].parameters["type_id"]) == 2:
                damage = self.game_map[x][y].all_in_cell[count].parameters["damage"]
                print("damage :" + str(damage))
                info_storage.append("damage: " + str(damage))
                hungry = self.game_map[x][y].all_in_cell[count].parameters["hungry"]
                print("hungry:" + str(hungry))
                info_storage.append("hungry: " + str(hungry))
            print("-------------------------------------------")
            return info_storage
        else:
            raise (print("Wrong coordinates <<z>>"))
       
    def delete_pest_from_garden(self):
        for pests in self.plants:
            if pests.parameters["type_id"] == 2:
                pests.parameters["life_points"] = 0
                pests = pests.opportunity_to_live()
                if pests is not None:
                    pests.get_position()
                    x = int(pests.parameters["coordinates"][0])
                    y = int(pests.parameters["coordinates"][1])
                    self.game_map[x][y].remove_smth_from_cell(pests)
                    self.plants.remove(pests)
   
    def weeding(self):
        for plant in self.plants:
            if plant.parameters["type_id"] == 1 or plant.parameters["type_id"] == 2 or plant.parameters["type_id"] == 3:
                plant.get_position()
                plant.parameters["weed"] = False
                x = int(plant.parameters["coordinates"][0])
                y = int(plant.parameters["coordinates"][1])
                index = plant.parameters["index"]
                count = self.game_map[x][y].get_cell_position(plant, index)
                self.game_map[x][y].delete_weed_from_cell(count, plant)
            
                    
    def getting_weed(self):
        for plant in self.plants:
            plant.parameters["weed"] = True
            plant.get_position()
            x = int(plant.parameters["coordinates"][0])
            y = int(plant.parameters["coordinates"][1])
            index = plant.parameters["index"]
            count = self.game_map[x][y].get_cell_position(plant, index)
            self.game_map[x][y].add_weed_on_cell(count, plant)
    
    def fertilizing_game_map(self):
        for plant in self.plants: 
            if plant.parameters["type_id"] == 1:
                plant.parameters["life_points"] = 100
                plant.parameters["points_to_grow_up"] += 5
                plant.parameters["illness"] = False
            if plant.parameters["type_id"] == 3:
                plant.parameters["life_points"] = 300
                plant.parameters["points_to_grow_up"] += 4
                plant.parameters["illness"] = False
    
    def garden_info(self):
        print("died from pests", self.died_from_pests)  # от вредителей в целом(все что не урожай)
        print("died from hungry", self.died_from_hungry)
        print("harvest of vegetables", self.harvest_of_vegetables)
        print("harvest of fruits", self.harvest_of_apples)
        print("died from hp", self.died_from_hp)
        

    def commands(self, command):
        try:
            # command = command.split(" ")
            if command == "garden_info":
                self.garden_info()            
                self.step_print()
            elif command == "weeding":
                for i in self.plants:
                    self.weeding()
                self.count_of_days = 0
                self.step_print()
            elif command == "next_day":
                self.count_of_global_days += 1
                self.life_cycle()
                self.count_of_days += 1
                if self.count_of_days == 3:
                    for plant in self.plants:
                        if plant.parameters["weed"] == False:
                            self.getting_weed()
                self.step_print()
            elif command == "add_plant":
                self.add_plant_on_game_map()
                self.step_print()
            elif command == "help_plants":
                self.fertilizing_game_map()
                self.step_print()
            elif command == "add_tree":
                self.add_trees_on_game_map()
                self.step_print()
            elif command == "add_pests":
                self.add_pests_on_game_map()
                self.step_print()
            elif command == "water_plants":
                self.watering_in_map()
                self.step_print()
            elif command == "delete_pests":
                for i in self.plants:
                    if i.parameters["type_id"] == 2:
                        self.delete_pest_from_garden()
                self.step_print()
            elif command == "info":
                try:
                    x = input()
                    y = input()
                    z = input()
                    if int(x) <= int(self.map_size[0]) and int(y) <= int(self.map_size[1]):
                        self.plants_info(x, y, z)
                    else:
                        raise()
                    self.step_print()
                except:
                    print("Wrong coordinates")
            elif command == "save":
                file = open(r'saved_game.txt', 'wb')
                pickle.dump(self, file)
                for i in range(self.map_size[0]):  # по строке
                    for j in range(self.map_size[1]):
                        pickle.dump(self.game_map[i][j], file)
                for smth in self.plants:
                    pickle.dump(smth, file)
                file.close()
                print("garden is saved")
                self.step_print()
            else:
                raise()
            self.step_save()
        except:
            print("Wrong command")
