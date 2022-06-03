import pygame
from controller.controler import Controller
from settings.settings import *
from gui.buttons import AppButton
import pygame_widgets
from model.Gamemap import *

pygame.init()


#  checking
class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.state = 'start'
        self.garden = None
        self.controller = Controller()
        self.buttons = AppButton()
        self.info_list = []
        self.index = 0

    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.draw_start()
            if self.state == 'next_day':
                self.next_day_events()
                self.draw_next_day()
            if self.state == 'garden_info':
                self.garden_info_events()
                self.draw_garden_info()
            if self.state == 'info':
                self.info_events()
                self.draw_info()
            if self.state == 'check_info':
                self.check_info_events()
                self.check_draw_info()

    ########################     START FUNCTIONS     ########################

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def draw_start(self):
        self.screen.fill(BLACK)
        self.buttons.add_button_start_garden(20, 20, self.screen, self)
        self.buttons.add_button_load_garden(450, 20, self.screen, self)
        self.draw_buttons()
        event = pygame.event.get()
        pygame_widgets.update(event)
        pygame.display.update()

    ########################      NEXT DAY FUNCTIONS     ########################

    def next_day_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    
    def draw_everydays_weather(self):
        if self.controller.get_weather() == "sun":
            sky = pygame.image.load("images/sunny.png")
        elif self.controller.get_weather() == "drought":
            sky = pygame.image.load("images/sunny_02.png")
        elif self.controller.get_weather() == "rain":
            sky = pygame.image.load("images/rain_2.png")
        return sky
    
    def draw_everydays_carrot(self, plant):
        if plant.parameters["age"] <= 1:
            carrot = pygame.image.load("images/carrot_1.png")
        elif 1 < plant.parameters["age"] <= 2:
            carrot = pygame.image.load("images/carrot_2.png")
        elif 2 < plant.parameters["age"] <= 3:
            carrot = pygame.image.load("images/carrot_3.png")
        elif 3 < plant.parameters["age"] <= 4:
            carrot = pygame.image.load("images/carrot_4.png")
        carrot.set_colorkey(WHITE)
        return carrot
    
    def draw_everydays_tree(self, plant):
        if plant.parameters["age"] <= 1:
            carrot = pygame.image.load("images/tree_1.png")
        elif 1 < plant.parameters["age"] <= 2:
            carrot = pygame.image.load("images/tree_2.png")
        elif 2 < plant.parameters["age"] <= 3:
            carrot = pygame.image.load("images/tree_3.png")
        elif 3 < plant.parameters["age"] <= 4:
            carrot = pygame.image.load("images/tree_4.png")
        elif 4 < plant.parameters["age"] <= 5:
            carrot = pygame.image.load("images/tree_5.png")
        elif 5 < plant.parameters["age"] <= 6:
            carrot = pygame.image.load("images/tree_6.png")
        elif 6 < plant.parameters["age"] <= 7 or plant.parameters["points_to_grow_up"] <= 15:
            carrot = pygame.image.load("images/tree_7.png")
        elif 7 < plant.parameters["age"] <= 8 and plant.parameters["points_to_grow_up"] >= 15:
            carrot = pygame.image.load("images/tree_8.png")
        elif 8 < plant.parameters["age"] <= 9 and plant.parameters["points_to_grow_up"] >= 18:
            carrot = pygame.image.load("images/tree_9.png")
        elif plant.parameters["age"] > 9 and plant.parameters["points_to_grow_up"] <= 10:
            carrot = pygame.image.load("images/tree_7.png")            
        elif plant.parameters["age"] > 9 and plant.parameters["points_to_grow_up"] <= 15:
            carrot = pygame.image.load("images/tree_8.png")
        elif plant.parameters["age"] > 9 and plant.parameters["points_to_grow_up"] > 19:
            carrot = pygame.image.load("images/tree_9.png")
        carrot.set_colorkey(WHITE)
        return carrot  
    
    def draw_everydays_pest(self, plant):
        pest = pygame.image.load("images/c_pest.png")
        pest.set_colorkey(WHITE)
        return pest
    
    def draw_everydays_weed(self, plant):
        weed = pygame.image.load("images/trava.png")
        weed.set_colorkey(WHITE)
        return weed
    
    def draw_everydays_illness(self, plant):
        illness = pygame.image.load("images/illness.png")
        illness.set_colorkey(WHITE)
        return illness
    
    def draw_cell(self, plant, count_c, coord_y_0_0):
        if plant.parameters["type_id"] == 3:
            self.screen.blit(self.draw_everydays_tree(plant), (20 + count_c, coord_y_0_0- 60))
        elif plant.parameters["type_id"] == 1:
            self.screen.blit(self.draw_everydays_carrot(plant), (20 + count_c, coord_y_0_0))
        if plant.parameters["type_id"] == 3 or plant.parameters["type_id"] == 1:
            if plant.parameters["weed"]:
                self.screen.blit(self.draw_everydays_weed(plant), (20 + count_c, coord_y_0_0 + 35))
            if plant.parameters["illness"]:
                self.screen.blit(self.draw_everydays_illness(plant), (100 + count_c, coord_y_0_0 ))
        if plant.parameters["type_id"] == 2:
            self.screen.blit(self.draw_everydays_pest(plant), (45 + count_c, coord_y_0_0 ))

    def draw_next_day(self):
        self.screen.fill(BLACK)
        back = pygame.image.load("images/garden_background.png")
        self.screen.blit(back, (20, 75))
        sky = self.draw_everydays_weather()
        self.screen.blit(sky, (120, 130))
        coord_y_0_0 = 250
        coord_y_0_1 = 400
        count_c = 60
        for plant in self.controller.garden.game_map[0][0].all_in_cell:
            self.draw_cell(plant, count_c, coord_y_0_0)
            count_c += 120
        count_c = 60
        for plant in self.controller.garden.game_map[0][1].all_in_cell:
            self.draw_cell(plant, count_c, coord_y_0_1)
            count_c += 120

        self.draw_buttons()
        event = pygame.event.get()
        pygame_widgets.update(event)
        pygame.display.update()  
     ########################       GARDEN INFO FUNCTIONS      ########################

    def garden_info_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def draw_garden_info(self):
        self.screen.fill(BLACK)
        self.draw_text("harvest of fruits: ", self.screen, [20, 70], 26, WHITE, FONT)
        self.draw_text(str(self.controller.get_harvest_of_apples()), self.screen, [250, 70], 26, WHITE, FONT)
        self.draw_text("harvest of vegetables: ", self.screen, [20, 110], 26, WHITE, FONT)
        self.draw_text(str(self.controller.get_harvest_of_vegetables()), self.screen, [300, 110], 26, WHITE, FONT)
        self.draw_text("died from hungry: ", self.screen, [20, 150], 26, WHITE, FONT)
        self.draw_text(str(self.controller.get_died_from_hungry()), self.screen, [250, 150], 26, WHITE, FONT)
        self.draw_text("died from pests: ", self.screen, [20, 190], 26, WHITE, FONT)
        self.draw_text(str(self.controller.get_died_from_pests()), self.screen, [250, 190], 26, WHITE, FONT)
        self.draw_text("died from hp: ", self.screen, [20, 230], 26, WHITE, FONT)
        self.draw_text(str(self.controller.get_died_from_hp()), self.screen, [250, 230], 26, WHITE, FONT)
        self.buttons.add_button_back(20, 270, self.screen, self)
        event = pygame.event.get()
        pygame_widgets.update(event)
        pygame.display.update()
        pygame_widgets.WidgetHandler._widgets.clear()

    ########################     HELP FUNCTIONS     ########################

    def draw_text(self, words, screen, position, size, colour, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            position[0] = position[0] - text_size[0] // 2
            position[1] = position[1] - text_size[1] // 2
        screen.blit(text, position)

    ########################     BUTTONS     ########################

    def draw_buttons(self):
        self.buttons.add_button_next_day(20, 540, self.screen, self)
        self.buttons.add_button_add_plant(650, 60, self.screen, self)
        self.buttons.add_button_add_tree(650, 120, self.screen, self)
        self.buttons.add_button_weeding(650, 180, self.screen, self)
        self.buttons.add_button_delete_pests(650, 240, self.screen, self)
        self.buttons.add_button_help_plants(650, 300, self.screen, self)
        self.buttons.add_button_water_plants(650, 360, self.screen, self)
        self.buttons.add_button_garden_info(650, 420, self.screen, self)
        self.buttons.add_button_info(650, 480, self.screen, self)
        self.buttons.add_button_save(650, 540, self.screen, self)

    def button_start_garden(self):
        self.controller.garden_init(World([1, 2]))
        count_of_plants = 2
        count_of_pests = 1
        count_of_trees = 3
        for i in range(0, count_of_trees):
            self.controller.add_trees_on_game_map()
        for i in range(0, count_of_pests):
            self.controller.add_pests_on_game_map()
        for i in range(0, count_of_plants):
            self.controller.add_plant_on_game_map()
        for i in range(0, count_of_plants):
            self.controller.add_plant_on_game_map()
        self.controller.commands("next_day")
        self.state = 'next_day'

    def button_load_garden(self):
        file = open(r'saved_game.txt', 'rb')
        self.controller.garden_init(pickle.load(file))
        for i in range(0, self.controller.get_map_size(0)):
            row = list()
            for j in range(0, self.controller.get_map_size[1]):
                Сell = pickle.load(file)
                for smth in Сell.all_in_cell:
                    self.controller.plant_add(smth)
                row.append(Сell)
            self.controller.game_map_add(row)
        for smth in range(1, len(self.controller.get_list_of_plants())):
            smth = pickle.load(file)
        file.close()
        self.controller.commands("next_day")
        self.state = 'next_day'

    def button_next_day(self):
        self.controller.commands("next_day")
        self.state = 'next_day'

    def button_add_plant(self):
        self.controller.commands("add_plant")
        self.state = 'next_day'

    def button_add_tree(self):
        self.controller.commands("add_tree")
        self.state = 'next_day'

    def button_delete_pests(self):
        self.controller.commands("delete_pests")
        self.state = 'next_day'

    def button_weeding(self):
        self.controller.commands("weeding")
        self.state = 'next_day'

    def button_water_plants(self):
        self.controller.commands("water_plants")
        
    def button_help_plants(self):
        self.controller.commands("help_plants")
        self.state = 'next_day'

    def button_info(self):
        self.state = "info"

    def button_garden_info(self):
        self.state = "garden_info"

    def button_save(self):
        self.controller.commands("save")

    def button_back(self):
        self.state = "next_day"
    coords = []

    def button_1(self):
        self.coords = [0, 0]
        return self.coords

    def button_2(self):
        self.coords = [0, 1]
        return self.coords
    
    def button_01(self):
        self.index = 0
        return  self.index
    
    def button_02(self):
        self.index = 1
        return  self.index
    
    def button_03(self):
        self.index = 2
        return  self.index
    
    def button_04(self):
        self.index = 3
        return  self.index  
    
    def button_check_info(self):
        self.info_list = self.controller.plants_info(int(self.coords[0]),int(self.coords[1]),int(self.index))
        self.state = "check_info"
        
    def info_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    
    def draw_info(self):
        self.screen.fill(BLACK)
        back = pygame.image.load("images/garden_background.png")
        self.screen.blit(back, (20, 75))
        sky = self.draw_everydays_weather()
        self.screen.blit(sky, (120, 130))
        coord_y_0_0 = 250
        coord_y_0_1 = 400
        count_c = 60
        for plant in self.controller.garden.game_map[0][0].all_in_cell:
            self.draw_cell(plant, count_c, coord_y_0_0)
            count_c += 120
        count_c = 60
        for plant in self.controller.garden.game_map[0][1].all_in_cell:
            self.draw_cell(plant, count_c, coord_y_0_1)
            count_c += 120
            
        self.add_buttons_for_info()    
        event = pygame.event.get()
        pygame_widgets.update(event)
        pygame.display.update()
        pygame_widgets.WidgetHandler._widgets.clear()
        
    def add_buttons_for_info(self):
        self.buttons.add_button_1(720, 70, self.screen, self)
        self.buttons.add_button_2(780, 70, self.screen, self)
        self.buttons.add_button_01(650, 170, self.screen, self)
        self.buttons.add_button_02(720, 170, self.screen, self)
        self.buttons.add_button_03(780,170, self.screen, self )
        self.buttons.add_button_04(840,170, self.screen, self)
        self.buttons.add_button_check_info(700, 220, self.screen, self)
        self.draw_text("Find informanion about plant :", self.screen, [150, 20], 26, WHITE, FONT)
        self.draw_text("Change line: ", self.screen, [690, 20], 26, WHITE, FONT)
        self.draw_text("Change plant: ", self.screen, [690, 120], 26, WHITE, FONT)   
        
    def check_info_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False   

    def check_draw_info(self):
        y_corodinate_for_draw = 260
        x_coordiante_for_draw = 650
        for i in range(len(self.info_list)):
            self.draw_text(self.info_list[i], self.screen, [x_coordiante_for_draw, y_corodinate_for_draw], 26, WHITE, FONT)
            y_corodinate_for_draw+=30
        self.buttons.add_button_back(230, 540, self.screen, self)
        event = pygame.event.get()
        pygame_widgets.update(event)
        pygame.display.update()
        pygame_widgets.WidgetHandler._widgets.clear()
        

