import pygame
from ui import text
from const import *
from game_objects.gobject_template import Gobject
from math import sin, cos, pi, atan2

class Enemy(Gobject):
    def __init__(self, pos, size, hp, target, all_enemies, game_data):
        Gobject.__init__(self, pos, size, hp)
        self.all_enemies = all_enemies
        self.game_data = game_data
        self.target = target
        self.target_rect = target.rect
        self.radius = int(self.rect.width / 2)
        self.target_center = self.target_rect.center

        self.speed = 2
        self.alive = True
        self.moving = True
        self.attacking = False
        self.dmg = 2

        self.worth = 5

    def get_angle(self, origin, target):
        x_dest = target[0] - origin[0]
        y_dest = target[1] - origin[1]
        return atan2(-y_dest, x_dest) % (2*pi)

    def project(self, pos, angle, dist):
        return (
            pos[0] + (cos(angle) * dist),
            pos[1] - (sin(angle) * dist)
        )

    def attack(self):
        self.target.hp -= self.dmg

    def kill(self):
        self.all_enemies.remove(self)
        self.game_data.add_gold(self.worth)


    def update(self):
        if self.moving:
            self.angle = self.get_angle(self.pos, self.target_center)
            self.pos = self.project(self.pos, self.angle, self.speed)
            self.rect.center = self.pos

        if self.rect.colliderect(self.target):
            self.attacking = True
            self.moving = False

        if self.attacking:
            self.attack()


        if self.hp <= 0:
            self.kill()

    def draw(self, screen):
        text.write(screen, '{}'.format(self.hp), (self.pos[0], self.pos[1] - 20), centered = True)
        pygame.draw.circle(screen, RED, self.rect.center, self.radius)

