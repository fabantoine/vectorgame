# !/usr/bin/env python
import random, os.path
# import basic pygame modules
import pygame as pg
import pygame.image
from pygame.locals import *
from settings import *

class Level:
    def __init__(self):
        self.level = 1
        self.image_cat = pygame.image.load('venv/data/cat.png')
        self.image_cat = pygame.transform.scale(self.image_cat, (80, 80))
        self.rect_cat = self.image_cat.get_rect()
        self.image_mouse = pygame.image.load('venv/data/mouse.png')
        self.image_mouse = pygame.transform.scale(self.image_mouse, (50, 50))
        self.rect_mouse = self.image_mouse.get_rect()
        self.level_generate()

    def level_generate(self):
        self.cat_coordinates = (random.randint(0, 10), random.randint(0, 10))
        self.mouse_coordinates = (random.randint(0, 10), random.randint(0, 10))
        self.rect_cat.center = (50+(self.cat_coordinates[0]*offset_grid),450-(self.cat_coordinates[1]*offset_grid))
        self.rect_cat.x += GRID_SURFACE[0]
        self.rect_cat.y += GRID_SURFACE[1]
        self.rect_mouse.center = (50+(self.mouse_coordinates[0]*offset_grid) - 8,450-(self.mouse_coordinates[1]*offset_grid))
        self.rect_mouse.x += GRID_SURFACE[0]
        self.rect_mouse.y += GRID_SURFACE[1]

    def draw_level(self, screen):
        screen.blit(self.image_cat, self.rect_cat)
        screen.blit(self.image_mouse, self.rect_mouse)
