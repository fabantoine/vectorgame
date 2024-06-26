# !/usr/bin/env python
import random, os.path
# import basic pygame modules
import pygame as pg
import pygame.image
from pygame.locals import *
from settings import *
from vector import Vector
from animation import Animation

class Level:
    def __init__(self):
        self.level = 1
        self.image_cat = pygame.image.load('data/cat.png')
        self.image_cat = pygame.transform.scale(self.image_cat, (80, 80))
        self.rect_cat = self.image_cat.get_rect()
        self.image_mouse = pygame.image.load('data/mouse.png')
        self.image_mouse = pygame.transform.scale(self.image_mouse, (50, 50))
        self.rect_mouse = self.image_mouse.get_rect()
        self.font = pygame.font.SysFont("Arial", 100)
        #print(pg.font.get_fonts())
        self.font_text = pg.font.SysFont("calibri", 30)
        self.init_pos_cat = (0, 0)
        self.animation = Animation()
        self.vector = Vector()

        self.need_fmessage = False
        self.need_inbox_clean = False
        self.pause = False
        self.score = 0
        self.tentative = 0
        self.level_generate()
    def level_generate(self):
        self.vector.is_defined = False
        self.animation.is_finish = False
        self.animation.is_animated = False
        self.text()
        self.cat_coordinates = (random.randint(0, 10), random.randint(0, 10))
        self.mouse_coordinates = (random.randint(0, 10), random.randint(0, 10))
        self.rect_cat.center = (50+(self.cat_coordinates[0]*offset_grid),450-(self.cat_coordinates[1]*offset_grid))
        self.rect_cat.x += GRID_SURFACE[0]
        self.rect_cat.y += GRID_SURFACE[1]
        self.rect_mouse.center = (50+(self.mouse_coordinates[0]*offset_grid) - 8,450-(self.mouse_coordinates[1]*offset_grid))
        self.rect_mouse.x += GRID_SURFACE[0]
        self.rect_mouse.y += GRID_SURFACE[1]
        self.init_pos_cat = self.rect_cat.center
        self.animation.set_start(self.init_pos_cat)



    def text(self):
        title_text = "CATCH THE MOUSE"
        instruction = "Le but est de donner les coordonnées du vecteur"
        instruction2 = "de déplacement du chat, pour qu'il attrape la souris."
        instruction3 = "Les cordonnées sont données sous la forme (x ; y)"
        score_text = f"Votre score est de {self.score *5}/20"
        tentative = f"Tentative : {self.tentative}/4"

        self.title = self.font.render(title_text, True, (200, 200, 200))
        self.instruction = self.font_text.render(instruction, True, (200, 200, 200))
        self.instruction2 = self.font_text.render(instruction2, True, (200, 200, 200))
        self.instruction3 = self.font_text.render(instruction3, True, (200, 200, 200))
        self.score_text = self.font_text.render(score_text, True, (255, 255, 255))
        self.tentative_text = self.font_text.render(tentative, True, (255, 255, 255))
    def draw_level(self, screen):
        if self.vector.is_defined and not self.animation.is_finish:
            self.vector.draw_vector(screen=screen, op=self.init_pos_cat)
        #print(self.animation.is_animated)
        if self.animation.is_animated:
            self.animation.animate()
            #print(f"start:{self.animation.start} end:{self.animation.end} pos:{self.animation.position_x, self.animation.position_y}")
            self.rect_cat.center = (self.animation.position_x, self.animation.position_y)

        screen.blit(self.image_cat, self.rect_cat)
        screen.blit(self.image_mouse, self.rect_mouse)
        screen.blit(self.title, (200, 10))
        screen.blit(self.instruction, (10, 200))
        screen.blit(self.instruction2, (10, 240))
        screen.blit(self.instruction3, (10, 280))
        screen.blit(self.score_text, (10, 650))
        screen.blit(self.tentative_text, (10, 600))
        #self.vector.draw_vector(screen=screen, op=self.rect_cat.center)
        self.win_test()
        if self.need_fmessage:
            screen.blit(self.message, (200, 450))
            self.pause = True
            self.need_fmessage = False
            self.reset()

    def reset(self):
        self.need_inbox_clean = True
        #self.inbox.input_text = ""
        #self.inbox.y_vector = ""
        #self.inbox.x_vector = ""
        #self.inbox.messages = []
        #self.inbox.vector_is_defined = False
        self.vector.is_defined = False
        self.level_generate()

    def final_message(self, win):
        self.need_fmessage = True
        self.tentative +=1
        if win:
            text1 = "Gagner !"
            self.score += 1
        else:
            text1 = "Perdu !"
        self.message = self.font.render(text1, True, (255, 255, 255))
    def win_test(self):
        if self.animation.is_finish:
            good_answer = [0, 0]
            good_answer[0] = self.mouse_coordinates[0] - self.cat_coordinates[0]
            good_answer[1] = self.mouse_coordinates[1] - self.cat_coordinates[1]
            player_answer = [0, 0]
            player_answer[0] = self.vector.coordinates[0]
            player_answer[1] = self.vector.coordinates[1]
            if player_answer == good_answer:
                self.final_message(True)
            else:
                self.final_message(False)
