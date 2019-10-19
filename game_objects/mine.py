import pygame
from const import *
from game_objects.gobject_template import Gobject
from ui import powerbar

class Mine(Gobject):
    def __init__(self, pos, size, hp, add_gold):
        Gobject.__init__(self, pos, size, hp)

        self.add_gold = add_gold  # method passed in from construction, calls game_data.add_gold(amont_

        self.color = GREEN

        self.gold_amount = 1
        self.gold_time = 3
        self.start_time = pygame.time.get_ticks()

        self.powerbar = powerbar.Powerbar(
            (self.rect.left, self.rect.top - 12, self.rect.width, 5),
            self.gold_time
        )

    def earn_gold(self):
        self.add_gold(self.gold_amount)

    def update(self):
        current_time = (pygame.time.get_ticks() - self.start_time) / 1000
        self.powerbar.set_power(current_time)

        if current_time >= self.gold_time:
            self.start_time = pygame.time.get_ticks()
            self.earn_gold()

        self.powerbar.update()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        self.powerbar.draw(screen)

