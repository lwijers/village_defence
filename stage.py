
from const import *

from scenes import main_scene, battle_scene, game_over_scene
import game_data

class Stage():
    def __init__(self):
        self.game_data = game_data.Game_data()
        self.scenes = {
            'main' : main_scene.Main_scene(self, self.game_data),
            'battle' : battle_scene.Battle_scene(self, self.game_data),
            'game_over' : game_over_scene.Game_over_scene(self, self.game_data)
        }

        self.current_scene = self.scenes['battle']


    def select_scene(self, scene):
        self.current_scene = self.scenes[scene]

# -----------------------------------------------------------------------------------
# PUD
# -----------------------------------------------------------------------------------

    def process_input(self, events):
        self.current_scene.process_input(events)

    def update(self):
        self.current_scene.update()

    def draw(self, screen):
        self.current_scene.draw(screen)
        # screen.fill((0, 0, 0))
        # self.village.draw(screen)
        # self.mine.draw(screen)
