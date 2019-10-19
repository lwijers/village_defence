import pygame
from const import *

class Powerbar():
    def __init__(self, rect, max_power, drain=True):
        self.drain = drain
        self.rect = pygame.Rect(rect)
        self.perc_rect = pygame.Rect(rect)
        self.max_power = max_power
        if self.drain:
            self.current_power = max_power
        else:
            self.current_power = 1

    def add_power(self, amount):
        self.current_power += amount
        self.update()

    def sub_power(self, amount):
        self.current_power -= amount
        self.update()

    def set_power(self, amount):
        self.current_power = amount
        self.update()

    def set_max_power(self, amount):
        self.max_power = amount

    def update(self):
        if self.current_power < 0:
            self.current_power = 0

        perc = self.current_power / self.max_power
        self.perc_rect.width = int(self.rect.width * perc)


    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)
        if self.current_power != 0:
            pygame.draw.rect(screen, GREEN, self.perc_rect)

