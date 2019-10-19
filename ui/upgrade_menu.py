import pygame
from const import *
from ui import text

from games.spygame.spygame.main._const import SH


class Upgrade_menu():
    def __init__(self, rect, game_data):
        self.game_data = game_data
        self.pages = ['Resources', 'Village', 'other', 'test']
        self.rect = rect
        self.tab_rect = pygame.Rect(self.rect[0], self.rect[1],
                                    self.rect[2], int(self.rect[3] * 0.2))
        self.tab_bar = Tab_bar(self.tab_rect, self.pages, self)

        self.page_rect = pygame.Rect(self.rect[0], self.tab_rect.bottom,
                                    self.rect[2], self.rect[3] - self.tab_rect[3])
        self.item_rect = pygame.Rect(0, self.tab_rect.bottom,
                                     self.rect.width / 4, self.page_rect.height)
        self.current_page = Page(self.page_rect, 'Village', self)

    def process_input(self, events):
        self.tab_bar.process_input(events)
        self.current_page.process_input(events)

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.rect)
        self.tab_bar.draw(screen)
        self.current_page.draw(screen)

class Tab_bar():
    def __init__(self, rect, pages, menu):
        self.menu = menu
        self.rect = rect
        self.pages = pages
        self.bg_color = YELLOW
        self.border_color = BLACK
        self.button_width = int(self.rect.width / len(self.pages))
        self.buttons = self.create_tab_buttons()


    def create_tab_buttons(self):
        buttons = {}
        for i, page in enumerate(self.pages):
            buttons[page] = pygame.Rect(
                self.button_width * i,
                self.rect.top,
                self.button_width,
                self.rect.height
            )
        return buttons

    def process_input(self, events):
        if events.mouse.l_clicked:
            for name, button in self.buttons.items():
                if button.collidepoint(pygame.mouse.get_pos()):
                    self.menu.current_page = Page(self.menu.page_rect, name, self.menu)

    def draw(self, screen):
        for name, button in self.buttons.items():
            pygame.draw.rect(screen, self.bg_color, button)
            pygame.draw.rect(screen, self.border_color, button, 3)
            text.write(screen, name,  button.center, font_cat = 'std_black', centered = True)


class Page():
    def __init__(self, rect, page_name, menu):
        self.game_data = menu.game_data
        self.item_rect = menu.item_rect
        self.rect = menu.item_rect
        self.rect = rect
        self.bg_color = BLUE
        self.page_name = page_name
        self.page_contents = {
            'Village': ['damage', 'attack speed', 'hp', 'regeneration']
        }
        self.items = self.create_items()

    def create_items(self):
        items = []
        try:
            for i, item in enumerate(self.page_contents[self.page_name]):
                items.append(Item(
                    pygame.Rect(
                        (self.item_rect[0] + (i * self.item_rect.width),
                        self.item_rect.y),
                        self.item_rect.size),
                        item,
                        self.game_data
                     )
                )

        except KeyError:
            pass

        return items

    def process_input(self, events):
        if events.mouse.l_clicked:
            for item in self.items:
                if item.rect.collidepoint(pygame.mouse.get_pos()):
                    item.action()


    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.rect)
        text.write(screen, self.page_name, self.rect.center, font_cat='std', centered=True)
        for item in self.items:
            item.draw(screen)

class Item():
    def __init__(self, rect, name, game_data):
        self.rect = rect
        self.name = name
        self.game_data = game_data

    def action(self):
        self.game_data.upgrade(self.name)

    def draw(self, screen):
        pygame.draw.rect(screen, DARK_GREEN, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)

        text.write(
            screen,
            self.name,
            (self.rect.centerx, self.rect.top +20),
            font_cat='hdr',
            centered=True
        )
        text.write(
            screen,
            'lvl: {}'.format(self.game_data.upgrades[self.name]['lvl']),
            (self.rect.centerx, self.rect.top + 80),
            font_cat='std',
            centered=True
        )
        text.write(
            screen,
            'cost: {}'.format(self.game_data.upgrades[self.name]['cost']),
            (self.rect.centerx, self.rect.top +120),
            font_cat='std',
            centered=True
        )
        text.write(
            screen,
            'improvement: {} -> {}'.format(
                self.game_data.upgrades[self.name]['lvl'] *self.game_data.upgrades[self.name]['improv'],
                (self.game_data.upgrades[self.name]['lvl'] + 1) * self.game_data.upgrades[self.name]['improv']
            ),
            (self.rect.centerx, self.rect.top +160),
            font_cat='std',
            centered=True
        )
