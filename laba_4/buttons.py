import pygame_widgets
from pygame_widgets.button import Button
from settings import *
import pygame

class AppButton():
    def __init__(self):
        pass
    
    def add_button_start_garden(self, h, w,screen, game):
        button_play = Button(screen,
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
                             onClick=game.button_start_garden)
    
    def add_button_load_garden(self, h, w, screen, game):
        button_play = Button(screen,
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
                             onClick=game.button_load_garden)

    def add_button_next_day(self, h, w,screen,game):
        button_play = Button(screen,
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
                             onClick=game.button_next_day)


    def add_button_add_plant(self, h, w, screen,game):
        button_play = Button(screen,
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
                             onClick=game.button_add_plant)

    def add_button_add_tree(self, h, w, screen,game):
        button_play = Button(screen,
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
                             onClick=game.button_add_tree)

    def add_button_delete_pests(self, h, w,screen,game):
        button_play = Button(screen,
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
                             onClick=game.button_delete_pests)

    def add_button_weeding(self, h, w,screen,game):
        button_play = Button(screen,
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
                             onClick=game.button_weeding)

    def add_button_water_plants(self, h, w,screen,game):
        button_play = Button(screen,
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
                             onClick=game.button_water_plants)
        
    def add_button_help_plants(self, h, w, screen,game):
        button_play = Button(screen,
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
                             onClick=game.button_help_plants)

    def add_button_info(self, h, w, screen,game):
        button_play = Button(screen,
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
                             onClick=game.button_info)

    def add_button_garden_info(self, h, w, screen,game):
        button_play = Button(screen,
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
                             onClick=game.button_garden_info)

    def add_button_save(self, h, w, screen,game):
        button_play = Button(screen,
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
                             onClick=game.button_save)

    def add_button_back(self, h, w, screen,game):
        button_play = Button(screen,
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
                             onClick=game.button_back)
        
    def add_button_1(self, h, w, screen,game):
        button_play = Button(screen,
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
                             onClick=game.button_1)
    
    def add_button_2(self, h, w, screen,game):
        button_play = Button(screen,
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
                             onClick=game.button_2)

    def add_button_01(self, h, w, screen,game):
        button_play = Button(screen,
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
                             onClick=game.button_01)
    
    def add_button_02(self, h, w, screen,game):
        button_play = Button(screen,
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
                             onClick=game.button_02)
    
    def add_button_03(self, h, w, screen,game):
        button_play = Button(screen,
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
                             onClick=game.button_03)
    
    def add_button_04(self, h, w, screen,game):
        button_play = Button(screen,
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
                             onClick=game.button_04)
        
    def add_button_check_info(self, h, w, screen,game):
        button_play = Button(screen,
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
                             onClick=game.button_check_info)