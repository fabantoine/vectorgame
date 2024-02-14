import pygame as pg
from settings import *
from level import Level


class Landmark:
    def __init__(self):
        self.surface = pg.Surface(size=(GRID_SIZE, GRID_SIZE))
        self.surface.fill((0, 0, 0))
        #pg.init()
        self.font = pg.font.SysFont(None, 32)
        self.print_line()
        self.print_number()
        self.level = Level()


    def print_line(self):
        #X Axe
        pg.draw.line(self.surface, (255, 255, 255), (50, 450), (470, 450), width=4)
        #Y Axe
        pg.draw.line(self.surface, (255, 255, 255),(50, 30), (50 , 450), width=4)

        #grille tout les 42 pix
        for i in range(11):
            pg.draw.line(self.surface, (255, 255, 255), (50, 450-(i*offset_grid)), (470, 450-(i*offset_grid)), width=1)
            pg.draw.line(self.surface, (255, 255, 255), (50+(i*offset_grid), 30), (50+(i*offset_grid), 450), width=1)

        #Affichage numerotation
    def print_number(self):
        # x-coordinate
        self.img_txt_x = self.font.render(X_COORDINATE, True, (240, 50, 50))
        self.txt_rect_x = self.img_txt_x.get_rect()
        self.txt_rect_x.x = GRID_SURFACE[0] + GRID_SIZE - 415 - 40
        self.txt_rect_x.y = GRID_SURFACE[1] + GRID_SIZE - 40
        # y-coordinate
        self.txt_rect_y = []
        self.img_txt_y =[]
        #self.txt_rect_y.x = []
        #self.txt_rect_y.y = []
        for i in range(10):
            self.img_txt_y.append(self.font.render(Y_COORDINATE[i], True, (240, 50, 50)))
            self.txt_rect_y.append(self.img_txt_y[i].get_rect())
            self.txt_rect_y[i].x = GRID_SURFACE[0] + GRID_SIZE - 415 - 40 - 34
            self.txt_rect_y[i].y = GRID_SURFACE[1] + 22 + i*offset_grid

    def draw_landmark(self, screen):
        screen.blit(self.surface, GRID_SURFACE)
        screen.blit(self.img_txt_x, self.txt_rect_x)
        for i in range(10):
            screen.blit(self.img_txt_y[i], self.txt_rect_y[i])
        self.level.draw_level(screen)