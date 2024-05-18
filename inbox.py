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
        self.font_err = pygame.font.SysFont("Arial", 30)
        self.color = color
        self.max_lines = max_lines
        self.messages = []
        self.input_active = False
        self.syntax_error = False
        self.input_text = ""
        self.x_vector = ""
        self.y_vector = ""
        self.vector_is_defined = False

    def vector_defined(self):
        vector_values = self.messages[0].replace("(", "").replace(")", "").split(";")

        try:
            self.x_vector = int(vector_values[0].strip())
            self.y_vector = int(vector_values[1].strip())
            self.vector_is_defined = True

        except ValueError:
            # En cas d'erreur de conversion en entier
            self.syntax_error = True

    def add_message(self, message):
        self.messages.append(message)
        if len(self.messages) > self.max_lines:
            self.messages.pop(0)

    def start_input(self):
        self.vector_is_defined = False
        self.input_active = True
        self.input_text = ""
        self.syntax_error = False
        self.x_vector = ""
        self.y_vector = ""

    def handle_input(self, event):
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                self.add_message(self.input_text)
                self.input_active = False
                self.vector_defined()
            elif event.key == K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            elif len(self.input_text) < 8:
                self.input_text += event.unicode


    def draw(self):
        pygame.draw.rect(self.surface, (0, 0, 0), (self.x, self.y, self.width, self.height))
        line_height = self.height // self.max_lines
        if self.syntax_error:
            message = self.font_err.render("Erreur: Les coordonnées sont incorrectes", True, (0, 0, 0))
            self.surface.blit(message, (50, self.y + 50))
        if self.input_active:
            pygame.draw.rect(self.surface, (255, 255, 255), (self.x + 10, self.y + self.height - 30, self.width - 20, 20))
            input_surface = self.font.render(self.input_text, True, (0, 0, 0))
            self.surface.blit(input_surface, (self.x + 12, self.y - 4 + self.height - 28))
