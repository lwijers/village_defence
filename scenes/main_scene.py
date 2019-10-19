import pygame
from const import *
from ui import button

from scenes.scene_template import Scene_template

class Main_scene(Scene_template):
    def __init__(self, stage, game_data):
        Scene_template.__init__(self, stage, game_data)
        self.play_button = button.Quick_button(
            (SW/2, SH/2), 'PLAY', self.play
        )

    def play(self):
        '''action when play button is clicked'''
        self.stage.select_scene('battle')

    def process_input(self, events):
        self.play_button.process_input(events)

    def update(self):
        self.play_button.update()

    def draw(self, screen):
        screen.fill((0, 0, 0))
        self.play_button.draw(screen)