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
        self.level_generate()
        self.vector = Vector()


    def level_generate(self):
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

        if self.level == 1:
            self.title = self.font.render(title_text, True, (0, 0, 0))
            self.instruction = self.font_text.render(instruction, True, (0, 0, 0))
            self.instruction2 = self.font_text.render(instruction2, True, (0, 0, 0))
            self.instruction3 = self.font_text.render(instruction3, True, (0, 0, 0))
    def draw_level(self, screen):
        #self.animation.set_start(self.rect_cat.center)
        if self.animation.is_animated:
            self.animation.animate()
            print(f"start:{self.animation.start} end:{self.animation.end} pos:{self.animation.position_x, self.animation.position_y}")
            self.rect_cat.center = (self.animation.position_x, self.animation.position_y)

        screen.blit(self.image_cat, self.rect_cat)
        screen.blit(self.image_mouse, self.rect_mouse)
        screen.blit(self.title, (10, 10))
        screen.blit(self.instruction, (10, 200))
        screen.blit(self.instruction2, (10, 240))
        screen.blit(self.instruction3, (10, 280))
        #self.vector.draw_vector(screen=screen, op=self.rect_cat.center)
