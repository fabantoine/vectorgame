# !/usr/bin/env python
from settings import *
import pygame as pg

class Vector:
    def __init__(self):
        self.op = (0, 0)
        self.coordinates = (0, 0)
        self.offset = offset_grid
        self.is_defined = False

    def draw_vector(self, screen, op=(0, 0), coordinates=(0, 0)):
        self.op = op
        coordinates = self.coordinates
        size = (abs(self.coordinates[0]) * self.offset, abs(self.coordinates[1]) * self.offset)
        if self.coordinates[0] == 0:
            size = (self.offset, abs(self.coordinates[1]) * self.offset)
        if self.coordinates[1] == 0:
            size = (abs(self.coordinates[0]) * self.offset, self.offset)
        self.vector_surface = pg.surface.Surface(size)
        self.vector_surface.set_colorkey((0, 0, 0))
        self.vector_surface_rect = self.vector_surface.get_rect()
        if self.coordinates[0]>0 and self.coordinates[1]<0:
            pg.draw.line(self.vector_surface, (255, 255, 255), (0, 0), size, width=5)
            pg.draw.line(self.vector_surface, (255, 255, 255), (size[0], size[1]-24), size, width=5)
            pg.draw.line(self.vector_surface, (255, 255, 255), (size[0]-24, size[1]), size, width=5)
            self.vector_surface_rect.x = op[0]
            self.vector_surface_rect.y = op[1]
        if self.coordinates[0]<0 and self.coordinates[1]>0:
            pg.draw.line(self.vector_surface, (255, 255, 255), size, (0, 0), width=5)
            pg.draw.line(self.vector_surface, (255, 255, 255), (0, 0), (24, 0), width=5)
            pg.draw.line(self.vector_surface, (255, 255, 255), (0, 0), (0, 24), width=5)
            self.vector_surface_rect.x = op[0] - size[0]
            self.vector_surface_rect.y = op[1] - size[1]
        if self.coordinates[0]<0 and self.coordinates[1]<0:
            pg.draw.line(self.vector_surface, (255, 255, 255), (size[0], 0), (0, size[1]), width=5)
            pg.draw.line(self.vector_surface, (255, 255, 255), (0, size[1]), (0, size[1]-24), width=5)
            pg.draw.line(self.vector_surface, (255, 255, 255), (0, size[1]), (24, size[1]), width=5)
            self.vector_surface_rect.x = op[0] - size[0]
            self.vector_surface_rect.y = op[1]
        if self.coordinates[0]>0 and self.coordinates[1]>0:
            pg.draw.line(self.vector_surface, (255, 255, 255), (0, size[1]), (size[0], 0), width=5)
            pg.draw.line(self.vector_surface, (255, 255, 255), (size[0], 0), (size[0]-24, 0), width=5)
            pg.draw.line(self.vector_surface, (255, 255, 255), (size[0], 0), (size[0], 24), width=5)
            self.vector_surface_rect.x = op[0]
            self.vector_surface_rect.y = op[1] - size[1]
        if self.coordinates[0] == 0:        #Vecteur vertical
            if self.coordinates[1] > 0:
                pg.draw.line(self.vector_surface, (255, 255, 255), (size[0]/2, 0), (size[0]/2, size[1]), width=5)
                pg.draw.line(self.vector_surface, (255, 255, 255), (size[0]/2, 0), (size[0], 24), width=5)
                pg.draw.line(self.vector_surface, (255, 255, 255), (size[0]/2, 0), (0, 24), width=5)
                self.vector_surface_rect.x = op[0] - size[0]/2
                self.vector_surface_rect.y = op[1] - size[1]
            if self.coordinates[1] < 0:
                pg.draw.line(self.vector_surface, (255, 255, 255), (size[0]/2, 0), (size[0]/2, size[1]), width=5)
                pg.draw.line(self.vector_surface, (255, 255, 255), (size[0]/2, size[1]), (0, size[1]-24),
                             width=5)
                pg.draw.line(self.vector_surface, (255, 255, 255), (size[0]/2, size[1]), (size[0], size[1]-24), width=5)
                self.vector_surface_rect.x = op[0] - size[0]/2
                self.vector_surface_rect.y = op[1]
        if self.coordinates[1] == 0:        #Vecteur horizontal
            if self.coordinates[0] > 0:
                pg.draw.line(self.vector_surface, (255, 255, 255), (0, size[1]/2), (size[0], size[1]/2), width=5)
                pg.draw.line(self.vector_surface, (255, 255, 255), (size[0], size[1]/2), (size[0]-24, size[1]), width=5)
                pg.draw.line(self.vector_surface, (255, 255, 255), (size[0], size[1]/2), (size[0]-24, 0), width=5)
                self.vector_surface_rect.x = op[0]
                self.vector_surface_rect.y = op[1] - size[1]/2
            if self.coordinates[0] < 0:
                pg.draw.line(self.vector_surface, (255, 255, 255), (size[0], size[1]/2), (0, size[1]/2), width=5)
                pg.draw.line(self.vector_surface, (255, 255, 255), (0, size[1]/2), (24, size[1]),
                             width=5)
                pg.draw.line(self.vector_surface, (255, 255, 255), (0, size[1]/2), (24, 0), width=5)
                self.vector_surface_rect.x = op[0] - size[0]
                self.vector_surface_rect.y = op[1] - size[1]/2
        screen.blit(self.vector_surface, self.vector_surface_rect)