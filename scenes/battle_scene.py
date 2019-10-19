
import pygame
from ui import text, upgrade_menu
import wave_manager
from game_objects import village, mine
from const import *
from scenes.scene_template import Scene_template


class Battle_scene(Scene_template):
    def __init__(self, stage, game_data):
        Scene_template.__init__(self, stage, game_data)
        self.battle_area = pygame.Rect(0, 0, 600, 600)
        self.upgrade_area = pygame.Rect(0, 600, SW, 250)
        self.village = village.Village(self, (SW/2-15, 600/2-15), (30, 30), 90)
        self.mine = mine.Mine((SW/2-100, 600/2 - 100), (15,15), 999, self.game_data.add_gold)
        self.wave_manager = wave_manager.Wave_manager(self)
        self.upgrade_menu = upgrade_menu.Upgrade_menu(self.upgrade_area, self.game_data)
        self.enemies = []

    def soft_reset(self):
        self.village = village.Village(self, (SW / 2 - 15, 600 / 2 - 15), (30, 30), 100)
        self.mine = mine.Mine((SW / 2 - 100, 600 / 2 - 100), (15, 15), 999, self.game_data.add_gold)
        self.wave_manager = wave_manager.Wave_manager(self)
        self.enemies = []


    def process_input(self, events):
        self.upgrade_menu.process_input(events)
        pass

    def update(self):
        self.village.update()
        self.wave_manager.update()
        self.mine.update()

        for enemy in self.enemies:
            enemy.update()

    def draw(self, screen):
        screen.fill(BLACK)
        self.village.draw(screen)
        self.mine.draw(screen)
        self.upgrade_menu.draw(screen)
        # text.write(screen, 'time: {}'.format(self.wave_manager.time_lapsed), (20,20))
        text.write(screen, 'wave: {}'.format(self.wave_manager.wave_number), (20,20))
        text.write(screen, 'day: {}'.format(self.wave_manager.day), (20,40))
        text.write(screen, 'gold: {}'.format(self.game_data.gold), (SW - 20, 20), right=True)

        for enemy in self.enemies:
            enemy.draw(screen)

