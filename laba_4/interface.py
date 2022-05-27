import pygame
from controller.controler import Controller
from settings import *
import pygame_widgets
from pygame_widgets.button import Button
from model.Gamemap import *

pygame.init()


#  checking
class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.garden = None
        self.controller = Controller()

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
        # back = pygame.image.load("images/garden_background.png")
        # self.screen.blit(back,(20, 75))
        self.add_button_start_garden(20, 20)
        self.add_button_load_garden(450, 20)
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

    def draw_next_day(self):
        self.screen.fill(BLACK)
        back = pygame.image.load("images/garden_background.png")
        self.screen.blit(back, (20, 75))
        back = pygame.image.load("images/garden_background.png")
        if self.controller.get_weather() == "sun":
            sky = pygame.image.load("images/sunny.png")
            self.screen.blit(sky, (120, 130))
        elif self.controller.get_weather() == "drought":
            sky = pygame.image.load("images/sunny_02.png")
            self.screen.blit(sky, (120, 130))
        elif self.controller.get_weather() == "rain":
            sky1 = pygame.image.load("images/rain_1.png")
            sky2 = pygame.image.load("images/rain_2.png")
            sky3 = pygame.image.load("images/rain_3.png")
            self.screen.blit(sky1, (120, 130))
            self.screen.blit(sky3, (400, 110))
            self.screen.blit(sky2, (250, 170))
        count_c = 60
        for plant in self.controller.garden.game_map[0][0].all_in_cell:
            if plant.parameters["type_id"] == 1:
                if plant.parameters["age"] <= 1:
                    carrot = pygame.image.load("images/carrot_1.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0))
                elif 1 < plant.parameters["age"] <= 2:
                    carrot = pygame.image.load("images/carrot_2.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0))
                elif 2 < plant.parameters["age"] <= 3:
                    carrot = pygame.image.load("images/carrot_3.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0))
                elif 3 < plant.parameters["age"] <= 4:
                    carrot = pygame.image.load("images/carrot_4.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0))
                if plant.parameters["weed"]:
                    weed = pygame.image.load("images/trava.png")
                    weed.set_colorkey(WHITE)
                    self.screen.blit(weed, (20 + count_c, coord_y_0_0 + 30))
                if plant.parameters["illness"]:
                    illness = pygame.image.load("images/illness.png")
                    illness.set_colorkey(WHITE)
                    self.screen.blit(illness, (100 + count_c, coord_y_0_0 ))
                count_c += 100
            elif plant.parameters["type_id"] == 3:
                if plant.parameters["age"] <= 1:
                    carrot = pygame.image.load("images/tree_1.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0))
                elif 1 < plant.parameters["age"] <= 2:
                    carrot = pygame.image.load("images/tree_2.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                elif 2 < plant.parameters["age"] <= 3:
                    carrot = pygame.image.load("images/tree_3.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                elif 3 < plant.parameters["age"] <= 4:
                    carrot = pygame.image.load("images/tree_4.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                elif 4 < plant.parameters["age"] <= 5:
                    carrot = pygame.image.load("images/tree_5.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                elif 5 < plant.parameters["age"] <= 6:
                    carrot = pygame.image.load("images/tree_6.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                elif 6 < plant.parameters["age"] <= 7 or plant.parameters["points_to_grow_up"] <= 15:
                    carrot = pygame.image.load("images/tree_7.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                elif 7 < plant.parameters["age"] <= 8 and plant.parameters["points_to_grow_up"] >= 15:
                    carrot = pygame.image.load("images/tree_8.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                elif 8 < plant.parameters["age"] <= 9 and plant.parameters["points_to_grow_up"] >= 18:
                    carrot = pygame.image.load("images/tree_9.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                elif plant.parameters["age"] > 9 and plant.parameters["points_to_grow_up"] <= 10:
                    carrot = pygame.image.load("images/tree_7.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                elif plant.parameters["age"] > 9 and plant.parameters["points_to_grow_up"] <= 15:
                    carrot = pygame.image.load("images/tree_8.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                elif plant.parameters["age"] > 9 and plant.parameters["points_to_grow_up"] > 19:
                    carrot = pygame.image.load("images/tree_9.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                if plant.parameters["weed"]:
                    weed = pygame.image.load("images/trava.png")
                    weed.set_colorkey(WHITE)
                    self.screen.blit(weed, (20 + count_c, coord_y_0_0 + 35))
                if plant.parameters["illness"]:
                    illness = pygame.image.load("images/illness.png")
                    illness.set_colorkey(WHITE)
                    self.screen.blit(illness, (100 + count_c, coord_y_0_0 ))
                count_c += 120
            elif plant.parameters["type_id"] == 2:
                pest = pygame.image.load("images/c_pest.png")
                pest.set_colorkey(WHITE)
                self.screen.blit(pest, (45 + count_c, coord_y_0_0 ))
                count_c += 120
        count_c = 60
        for plant in self.controller.garden.game_map[0][1].all_in_cell:
            if plant.parameters["type_id"] == 1:
                if plant.parameters["age"] <= 1:
                    carrot = pygame.image.load("images/carrot_1.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1))
                elif 1 < plant.parameters["age"] <= 2:
                    carrot = pygame.image.load("images/carrot_2.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1))
                elif 2 < plant.parameters["age"] <= 3:
                    carrot = pygame.image.load("images/carrot_3.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1))
                elif 3 < plant.parameters["age"] <= 4:
                    carrot = pygame.image.load("images/carrot_4.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1))
                if plant.parameters["weed"]:
                    weed = pygame.image.load("images/trava.png")
                    weed.set_colorkey(WHITE)
                    self.screen.blit(weed, (20 + count_c, coord_y_0_1 + 30))
                if plant.parameters["illness"]:
                    illness = pygame.image.load("images/illness.png")
                    illness.set_colorkey(WHITE)
                    self.screen.blit(illness, (100 + count_c, coord_y_0_1 ))
                count_c += 100
            elif plant.parameters["type_id"] == 3:
                if plant.parameters["age"] <= 1:
                    carrot = pygame.image.load("images/tree_1.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1))
                elif 1 < plant.parameters["age"] <= 2:
                    carrot = pygame.image.load("images/tree_2.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                elif 2 < plant.parameters["age"] <= 3:
                    carrot = pygame.image.load("images/tree_3.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                elif 3 < plant.parameters["age"] <= 4:
                    carrot = pygame.image.load("images/tree_4.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                elif 4 < plant.parameters["age"] <= 5:
                    carrot = pygame.image.load("images/tree_5.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                elif 5 < plant.parameters["age"] <= 6:
                    carrot = pygame.image.load("images/tree_6.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                elif 6 < plant.parameters["age"] <= 7 or plant.parameters["points_to_grow_up"] <= 15:
                    carrot = pygame.image.load("images/tree_7.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                elif 7 < plant.parameters["age"] <= 8 and plant.parameters["points_to_grow_up"] >= 15:
                    carrot = pygame.image.load("images/tree_8.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                elif 8 < plant.parameters["age"] <= 9 and plant.parameters["points_to_grow_up"] >= 18:
                    carrot = pygame.image.load("images/tree_9.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                elif plant.parameters["age"] > 9 and plant.parameters["points_to_grow_up"] <= 10:
                    carrot = pygame.image.load("images/tree_7.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                elif plant.parameters["age"] > 9 and plant.parameters["points_to_grow_up"] <= 15:
                    carrot = pygame.image.load("images/tree_8.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                elif plant.parameters["age"] > 9 and plant.parameters["points_to_grow_up"] > 19:
                    carrot = pygame.image.load("images/tree_9.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                if plant.parameters["weed"]:
                    weed = pygame.image.load("images/trava.png")
                    weed.set_colorkey(WHITE)
                    self.screen.blit(weed, (20 + count_c, coord_y_0_1 + 35))
                if plant.parameters["illness"]:
                    illness = pygame.image.load("images/illness.png")
                    illness.set_colorkey(WHITE)
                    self.screen.blit(illness, (100 + count_c, coord_y_0_1 ))
                count_c += 120
            elif plant.parameters["type_id"] == 2:
                pest = pygame.image.load("images/c_pest.png")
                pest.set_colorkey(WHITE)
                self.screen.blit(pest, (45 + count_c, coord_y_0_1 ))
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
        self.add_button_back(20, 270)
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
        self.add_button_next_day(20, 540)
        self.add_button_add_plant(650, 60)
        self.add_button_add_tree(650, 120)
        self.add_button_weeding(650, 180)
        self.add_button_delete_pests(650, 240)
        self.add_button_help_plants(650, 300)
        self.add_button_water_plants(650, 360)
        self.add_button_garden_info(650, 420)
        self.add_button_info(650, 480)
        self.add_button_save(650, 540)

    def add_button_start_garden(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             430,
                             40,
                             text='Garden simulator',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_start_garden)

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
       # self.controller.step_print()
        self.controller.commands("next_day")
        #self.controller.step_print()
       # print(str(self.controller.get_weather()))
        self.state = 'next_day'
        #print(str(self.controller.get_count_of_global_days()))

    def add_button_load_garden(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             430,
                             40,
                             text='Load saved game',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_load_garden)

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

    def add_button_next_day(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             600,
                             45,
                             text='next day',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_next_day)

    def button_next_day(self):
        self.controller.commands("next_day")
        self.state = 'next_day'


    def add_button_add_plant(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             200,
                             45,
                             text='add plant',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_add_plant)

    def button_add_plant(self):
        self.controller.commands("add_plant")
        self.state = 'next_day'
     

    def add_button_add_tree(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             200,
                             45,
                             text='add tree',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_add_tree)

    def button_add_tree(self):
        self.controller.commands("add_tree")
        self.state = 'next_day'
    

    def add_button_delete_pests(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             200,
                             45,
                             text='delete pests',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_delete_pests)

    def button_delete_pests(self):
        self.controller.commands("delete_pests")
        self.state = 'next_day'

    def add_button_weeding(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             200,
                             45,
                             text='weeding',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_weeding)

    def button_weeding(self):
        self.controller.commands("weeding")
        self.state = 'next_day'

    def add_button_water_plants(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             200,
                             45,
                             text='water plants',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_water_plants)

    def button_water_plants(self):
        self.controller.commands("water_plants")

    def add_button_help_plants(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             200,
                             45,
                             text='help plants',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_help_plants)

    def button_help_plants(self):
        self.controller.commands("help_plants")
        self.state = 'next_day'

    def add_button_info(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             200,
                             45,
                             text='info',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_info)

    def button_info(self):
        self.state = "info"

    def add_button_garden_info(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             200,
                             45,
                             text='garden info',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_garden_info)

    def button_garden_info(self):
        self.state = "garden_info"

    def add_button_save(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             200,
                             45,
                             text='save',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_save)

    def button_save(self):
        self.controller.commands("save")

    def add_button_back(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             200,
                             45,
                             text='back',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_back)

    def button_back(self):
        self.state = "next_day"
    coords = []
    def add_button_1(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             50,
                             45,
                             text='1',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_1)

    def button_1(self):
        self.coords = [0, 0]
        return self.coords
    
    def add_button_2(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             50,
                             45,
                             text='2',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_2)

    def button_2(self):
        self.coords = [0, 1]
        return self.coords

    def add_button_01(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             50,
                             45,
                             text='1',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_01)
    
    index = 0 
    
    def button_01(self):
        self.index = 0
        return  self.index
    
    def add_button_02(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             50,
                             45,
                             text='2',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_02)

    def button_02(self):
        self.index = 1
        return  self.index
    
    def add_button_03(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             50,
                             45,
                             text='3',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_03)

    def button_03(self):
        self.index = 2
        return  self.index
    
    def add_button_04(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             50,
                             45,
                             text='4',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_04)

    def button_04(self):
        self.index = 0
        return  self.index
    
    def add_button_check_info(self, h, w):
        button_play = Button(self.screen,
                             h,
                             w,
                             150,
                             45,
                             text='check info',
                             textColour=YELLOW,
                             font=pygame.font.Font('fonts/tahoma.ttf', 23),
                             fontSize=23,
                             margin=20,
                             inactiveColour=BLACK,
                             hoverColour=BLUE,
                             pressedColour=BLUE,
                             onClick=self.button_check_info)
        
    info_list = []    
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
        back = pygame.image.load("images/garden_background.png")
        if self.controller.get_weather() == "sun":
            sky = pygame.image.load("images/sunny.png")
            self.screen.blit(sky, (120, 130))
        elif self.controller.get_weather() == "drought":
            sky = pygame.image.load("images/sunny_02.png")
            self.screen.blit(sky, (120, 130))
        elif self.controller.get_weather() == "rain":
            sky1 = pygame.image.load("images/rain_1.png")
            sky2 = pygame.image.load("images/rain_2.png")
            sky3 = pygame.image.load("images/rain_3.png")
            self.screen.blit(sky1, (120, 130))
            self.screen.blit(sky3, (400, 110))
            self.screen.blit(sky2, (250, 170))
        count_c = 60
        for plant in self.controller.garden.game_map[0][0].all_in_cell:
            if plant.parameters["type_id"] == 1:
                if plant.parameters["age"] <= 1:
                    carrot = pygame.image.load("images/carrot_1.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0))
                elif 1 < plant.parameters["age"] <= 2:
                    carrot = pygame.image.load("images/carrot_2.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0))
                elif 2 < plant.parameters["age"] <= 3:
                    carrot = pygame.image.load("images/carrot_3.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0))
                elif 3 < plant.parameters["age"] <= 4:
                    carrot = pygame.image.load("images/carrot_4.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0))
                if plant.parameters["weed"]:
                    weed = pygame.image.load("images/trava.png")
                    weed.set_colorkey(WHITE)
                    self.screen.blit(weed, (20 + count_c, coord_y_0_0 + 30))
                if plant.parameters["illness"]:
                    illness = pygame.image.load("images/illness.png")
                    illness.set_colorkey(WHITE)
                    self.screen.blit(illness, (100 + count_c, coord_y_0_0 ))
                count_c += 100
            elif plant.parameters["type_id"] == 3:
                if plant.parameters["age"] <= 1:
                    carrot = pygame.image.load("images/tree_1.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0))
                elif 1 < plant.parameters["age"] <= 2:
                    carrot = pygame.image.load("images/tree_2.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                elif 2 < plant.parameters["age"] <= 3:
                    carrot = pygame.image.load("images/tree_3.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                elif 3 < plant.parameters["age"] <= 4:
                    carrot = pygame.image.load("images/tree_4.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                elif 4 < plant.parameters["age"] <= 5:
                    carrot = pygame.image.load("images/tree_5.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                elif 5 < plant.parameters["age"] <= 6:
                    carrot = pygame.image.load("images/tree_6.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                elif 6 < plant.parameters["age"] <= 7 or plant.parameters["points_to_grow_up"] <= 15:
                    carrot = pygame.image.load("images/tree_7.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                elif 7 < plant.parameters["age"] <= 8 and plant.parameters["points_to_grow_up"] >= 15:
                    carrot = pygame.image.load("images/tree_8.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                elif 8 < plant.parameters["age"] <= 9 and plant.parameters["points_to_grow_up"] >= 18:
                    carrot = pygame.image.load("images/tree_9.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                elif plant.parameters["age"] > 9 and plant.parameters["points_to_grow_up"] <= 10:
                    carrot = pygame.image.load("images/tree_7.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                elif plant.parameters["age"] > 9 and plant.parameters["points_to_grow_up"] <= 15:
                    carrot = pygame.image.load("images/tree_8.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                elif plant.parameters["age"] > 9 and plant.parameters["points_to_grow_up"] > 19:
                    carrot = pygame.image.load("images/tree_9.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_0- 50))
                if plant.parameters["weed"]:
                    weed = pygame.image.load("images/trava.png")
                    weed.set_colorkey(WHITE)
                    self.screen.blit(weed, (20 + count_c, coord_y_0_0 + 35))
                if plant.parameters["illness"]:
                    illness = pygame.image.load("images/illness.png")
                    illness.set_colorkey(WHITE)
                    self.screen.blit(illness, (100 + count_c, coord_y_0_0 ))
                count_c += 120
            elif plant.parameters["type_id"] == 2:
                pest = pygame.image.load("images/c_pest.png")
                pest.set_colorkey(WHITE)
                self.screen.blit(pest, (45 + count_c, coord_y_0_0 ))
                count_c += 120
        count_c = 60
        for plant in self.controller.garden.game_map[0][1].all_in_cell:
            if plant.parameters["type_id"] == 1:
                if plant.parameters["age"] <= 1:
                    carrot = pygame.image.load("images/carrot_1.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1))
                elif 1 < plant.parameters["age"] <= 2:
                    carrot = pygame.image.load("images/carrot_2.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1))
                elif 2 < plant.parameters["age"] <= 3:
                    carrot = pygame.image.load("images/carrot_3.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1))
                elif 3 < plant.parameters["age"] <= 4:
                    carrot = pygame.image.load("images/carrot_4.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1))
                if plant.parameters["weed"]:
                    weed = pygame.image.load("images/trava.png")
                    weed.set_colorkey(WHITE)
                    self.screen.blit(weed, (20 + count_c, coord_y_0_1 + 30))
                if plant.parameters["illness"]:
                    illness = pygame.image.load("images/illness.png")
                    illness.set_colorkey(WHITE)
                    self.screen.blit(illness, (100 + count_c, coord_y_0_1 ))
                count_c += 100
            elif plant.parameters["type_id"] == 3:
                if plant.parameters["age"] <= 1:
                    carrot = pygame.image.load("images/tree_1.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1))
                elif 1 < plant.parameters["age"] <= 2:
                    carrot = pygame.image.load("images/tree_2.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                elif 2 < plant.parameters["age"] <= 3:
                    carrot = pygame.image.load("images/tree_3.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                elif 3 < plant.parameters["age"] <= 4:
                    carrot = pygame.image.load("images/tree_4.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                elif 4 < plant.parameters["age"] <= 5:
                    carrot = pygame.image.load("images/tree_5.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                elif 5 < plant.parameters["age"] <= 6:
                    carrot = pygame.image.load("images/tree_6.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                elif 6 < plant.parameters["age"] <= 7 or plant.parameters["points_to_grow_up"] <= 15:
                    carrot = pygame.image.load("images/tree_7.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                elif 7 < plant.parameters["age"] <= 8 and plant.parameters["points_to_grow_up"] >= 15:
                    carrot = pygame.image.load("images/tree_8.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                elif 8 < plant.parameters["age"] <= 9 and plant.parameters["points_to_grow_up"] >= 18:
                    carrot = pygame.image.load("images/tree_9.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                elif plant.parameters["age"] > 9 and plant.parameters["points_to_grow_up"] <= 10:
                    carrot = pygame.image.load("images/tree_7.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                elif plant.parameters["age"] > 9 and plant.parameters["points_to_grow_up"] <= 15:
                    carrot = pygame.image.load("images/tree_8.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                elif plant.parameters["age"] > 9 and plant.parameters["points_to_grow_up"] > 19:
                    carrot = pygame.image.load("images/tree_9.png")
                    carrot.set_colorkey(WHITE)
                    self.screen.blit(carrot, (20 + count_c, coord_y_0_1- 50))
                if plant.parameters["weed"]:
                    weed = pygame.image.load("images/trava.png")
                    weed.set_colorkey(WHITE)
                    self.screen.blit(weed, (20 + count_c, coord_y_0_1 + 35))
                if plant.parameters["illness"]:
                    illness = pygame.image.load("images/illness.png")
                    illness.set_colorkey(WHITE)
                    self.screen.blit(illness, (100 + count_c, coord_y_0_1 ))
                count_c += 120
            elif plant.parameters["type_id"] == 2:
                pest = pygame.image.load("images/c_pest.png")
                pest.set_colorkey(WHITE)
                self.screen.blit(pest, (45 + count_c, coord_y_0_1 ))
                count_c += 120
        self.add_button_1(720, 70)
        self.add_button_2(780, 70)
        self.add_button_01(650, 170)
        self.add_button_02(720, 170)
        self.add_button_03(780,170 )
        self.add_button_04(840,170)
        self.add_button_check_info(700, 220)     
        self.draw_text("Find informanion about plant :", self.screen, [150, 20], 26, WHITE, FONT)
        self.draw_text("Change line: ", self.screen, [690, 20], 26, WHITE, FONT)
        self.draw_text("Change plant: ", self.screen, [690, 120], 26, WHITE, FONT)
        event = pygame.event.get()
        pygame_widgets.update(event)
        pygame.display.update()
        pygame_widgets.WidgetHandler._widgets.clear()
        
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
        self.add_button_back(230, 540)
        event = pygame.event.get()
        pygame_widgets.update(event)
        pygame.display.update()
        pygame_widgets.WidgetHandler._widgets.clear()
        

