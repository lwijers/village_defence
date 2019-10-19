import pygame
import random
from const import *
from game_objects import enemy


class Wave_manager():
    def __init__(self, scene):
        self.scene = scene
        self.wave_time = 5
        self.day = 1
        self.wave_number = 1
        self.start_time = pygame.time.get_ticks()
        self.time_lapsed = 0
        self.release_time = True

    def update(self):
        if self.release_time:
            self.release_wave()

        self.time_it()

    def release_wave(self):
        for i in range(0, ((self.day -1) * 10) + self.wave_number):
            self.add_enemy(
                enemy.Enemy(
                    self.side_selector(),
                    (20, 20),
                    10,
                    self.scene.village,
                    self.scene.enemies,
                    self.scene.game_data
                )
            )


    def add_enemy(self, enemy):
        self.scene.enemies.append(enemy)

    def time_it(self):
        self.release_time = False
        self.time_lapsed = round((pygame.time.get_ticks() - self.start_time) / 1000, 1)
        if self.time_lapsed >= self.wave_time:
            self.start_time = pygame.time.get_ticks()
            self.time_lapsed = 0
            self.wave_number += 1
            self.release_time = True
        if self.wave_number > 10:
            self.wave_number = 1
            self.day += 1

    def reset(self):
        self.day = 1
        self.wave_number = 1
        self.start_time = pygame.time.get_ticks()
        self.time_lapsed = 0


    def side_selector(self):
        sides = ['top', 'bot', 'left', 'right']
        side = random.choice(sides)
        if side == 'top':
            y = 0
            x = random.randrange(SW)
        elif side == 'bot':
            y = self.scene.battle_area[3]
            x = random.randrange(SW)
        elif side == 'left':
            x = 0
            y = random.randrange(self.scene.battle_area[3])
        elif side == 'right':
            x = SW
            y = random.randrange(self.scene.battle_area[3])
        return (x, y)