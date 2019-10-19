import pygame
import math
from ui import text
from const import *
from game_objects.gobject_template import Gobject
from ui import powerbar

class Village(Gobject):
    def __init__(self, scene,  pos, size, hp):
        Gobject.__init__(self, pos, size, hp)
        self.scene = scene
        self.color = (255,100,0)
        self.radius = 200
        self.attack_list = []
        self.damage = self.scene.stage.game_data.upgrades['damage']['lvl'] * \
                      self.scene.stage.game_data.upgrades['damage']['improv']

        self.base_att_speed = 1
        self.att_speed_mod =  self.scene.stage.game_data.upgrades['attack speed']['lvl'] * \
                      self.scene.stage.game_data.upgrades['attack speed']['improv']
        self.base_hp = self.hp
        self.current_hp = self.base_hp
        self.max_hp = self.base_hp + self.scene.stage.game_data.upgrades['hp']['lvl'] * \
                      self.scene.stage.game_data.upgrades['hp']['improv']

        self.start_time = pygame.time.get_ticks()
        self.tracer = False # traces the bullet
        self.health_bar = powerbar.Powerbar(
            (self.rect.left, self.rect.top - 12, self.rect.width, 5),
            self.hp
        )


    def find_enemies(self, all_enemies):
        self.attack_list = []
        for enemy in all_enemies:
            dx = self.pos[0] - enemy.pos[0]
            dy = self.pos[1] - enemy.pos[1]
            dist = math.sqrt(dx * dx + dy * dy)
            if dist < self.radius + enemy.radius:
                self.add_enemy(enemy)


    def add_enemy(self, enemy):
        if enemy not in self.attack_list:
            self.attack_list.append(enemy)

    def attack(self, enemy):
        enemy.hp -= self.damage

    def update(self):
        self.damage = self.scene.stage.game_data.upgrades['damage']['lvl'] * \
                      self.scene.stage.game_data.upgrades['damage']['improv']
        self.att_speed_mod = self.scene.stage.game_data.upgrades['attack speed']['lvl'] * \
                             self.scene.stage.game_data.upgrades['attack speed']['improv']
        self.max_hp = self.base_hp + self.scene.stage.game_data.upgrades['hp']['lvl'] * \
                  self.scene.stage.game_data.upgrades['hp']['improv']

        self.health_bar.set_max_power(self.max_hp)
        self.health_bar.set_power(self.hp)
        self.find_enemies(self.scene.enemies)

        self.tracer = False

        if (pygame.time.get_ticks() - self.start_time) /1000 > self.base_att_speed - self.att_speed_mod:
            if self.attack_list:
                self.attack(self.attack_list[0])
                self.tracer = True
                self.start_time = pygame.time.get_ticks()

        if self.hp <= 0:
            self.scene.soft_reset()
            self.scene.stage.select_scene('game_over')

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.circle(screen, (255,255,255), self.rect.center, self.radius, 1)
        if self.tracer:
            pygame.draw.line(screen, YELLOW, self.rect.center, self.attack_list[0].rect.center, 2)
        self.health_bar.draw(screen)
        text.write(screen, '{}'.format(self.hp), (self.pos[0], self.rect.top - 20), centered = True)