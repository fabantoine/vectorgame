import pygame
from pygame.locals import *

class Inbox:
    def __init__(self, surface, x, y, width, height, font, font_size, color=(255, 255, 255), max_lines=1):
        self.surface = surface
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont(font, font_size)
        self.color = color
        self.max_lines = max_lines
        self.messages = []
        self.input_active = False
        self.input_text = ""

    def add_message(self, message):
        self.messages.append(message)
        if len(self.messages) > self.max_lines:
            self.messages.pop(0)

    def start_input(self):
        self.input_active = True
        self.input_text = ""

    def handle_input(self, event):
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                self.add_message("Input: " + self.input_text)
                self.input_active = False
            elif event.key == K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            else:
                self.input_text += event.unicode

    def draw(self):
        pygame.draw.rect(self.surface, (0, 0, 0), (self.x, self.y, self.width, self.height))
        line_height = self.height // self.max_lines
        '''for i, message in enumerate(self.messages):
            text_surface = self.font.render(message, True, self.color)
            self.surface.blit(text_surface, (self.x + 10, self.y + i * line_height + 5))'''

        if self.input_active:

            pygame.draw.rect(self.surface, (255, 255, 255), (self.x + 10, self.y + self.height - 30, self.width - 20, 20))
            input_surface = self.font.render(self.input_text, True, (0, 0, 0))
            self.surface.blit(input_surface, (self.x + 12, self.y - 4 + self.height - 28))

'''# Example usage:
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

inbox = Inbox(screen, 50, 50, 100, 40, "Arial", 20)

running = True
while running:


    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_i:
                inbox.start_input()
            elif inbox.input_active:
                inbox.handle_input(event)

    inbox.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()'''

