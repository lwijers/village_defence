import pygame

class Gobject:
    def __init__(self, pos, size, hp):
        self.pos = pos
        self.size = size
        self.hp = hp
        # self.surf = pygame.Surface(size)
        self.rect = pygame.Rect(self.pos, self.size)
        self.rect.center = self.pos

    def process_input(self, events):
        pass
    def update(self):
        pass
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
