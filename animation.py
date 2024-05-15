import pygame as pg

class Animation:
    def __init__(self, start_point=(1, 1), end_point=(10, 10)):
        self.is_animated = False
        self.is_finish = False
        self.start = start_point
        self.end = end_point
        (self.position_x, self.position_y) = self.start

    def set_start(self, start_point=(1, 1)):
        self.start = start_point
        (self.position_x, self.position_y) = self.start
    def set_end(self, end_point=(10, 10)):
        self.end = end_point
    def animate(self):
        if not self.is_finish:
            if self.end[0] < self.position_x:
                self.position_x -= abs(self.start[0] - self.end[0])/100
            elif self.end[0] > self.position_x:
                self.position_x += abs(self.start[0] - self.end[0])/100
            if self.end[1] < self.position_y:
                self.position_y -= abs(self.start[1] - self.end[1])/100
            elif self.end[1] > self.position_y:
                self.position_y += abs(self.start[1] - self.end[1])/100
            if round(self.position_x) == self.end[0] and round(self.position_y) == self.end[1]:
                self.is_finish = True
                self.is_animated = False

