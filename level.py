# !/usr/bin/env python
import random, os.path
# import basic pygame modules
import pygame as pg
import pygame.image
from pygame.locals import *
from settings import *
from vector import Vector

class Level:
    def __init__(self):
        self.level = 1
        self.image_cat = pygame.image.load('data/cat.png')
        self.image_cat = pygame.transform.scale(self.image_cat, (80, 80))
        self.rect_cat = self.image_cat.get_rect()
        self.image_mouse = pygame.image.load('data/mouse.png')
        self.image_mouse = pygame.transform.scale(self.image_mouse, (50, 50))
        self.rect_mouse = self.image_mouse.get_rect()
        self.font = pygame.font.SysFont("Arial", 30)
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

    def text(self):
        title_text = "CATCH THE MOUSE"
        if self.level == 1:
            self.title = self.font.render(title_text, True, (0, 0, 0))



    def draw_level(self, screen):
        screen.blit(self.image_cat, self.rect_cat)
        print(self.rect_cat.center)
        screen.blit(self.image_mouse, self.rect_mouse)
        screen.blit(self.title, (10, 10))
        self.vector.draw_vector(screen=screen, op=self.rect_cat.center)
