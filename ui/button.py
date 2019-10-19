''' ---spygmae2d_versieIII---, created by Lennart on 3/7/2018'''
import pygame
from const import *
from ui import text

class Quick_button():
    def __init__(self, pos, text, action, size = (100,20)):

        self.action = action


        self.bg_color = BUTT_BG_COL
        self.line_color= BUTT_LI_COL

        self.text_color = BUTT_TXT_COL

        self.mo_bg_color = ((255 - self.bg_color[0]), (255 - self.bg_color[1]), 255 - (self.bg_color[2]))
        self.mo_line_color = ((255 - self.line_color[0]), (255 - self.line_color[1]), (255 - self.line_color[2]))

        self.size = size
        self.pos = pos

        self.text = text

        self.rect = pygame.Rect(self.pos, self.size)

        self.image = pygame.Surface(self.size)

        self.clicked = False
        self.mouse_hover = False


    def process_input(self, events):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.mouse_hover = True
            if events.mouse.l_clicked:
                self.on_click()

    def on_click(self):
        self.action()

    def update(self):
        if self.mouse_hover:
            self.bg_color = self.mo_bg_color
            self.line_color = self.mo_line_color
            self.text_color = self.mo_line_color
        else:
            self.bg_color = ((255 - self.mo_bg_color[0]), (255 - self.mo_bg_color[1]), (255 - self.mo_bg_color[2]))
            self.line_color = ((255 - self.mo_line_color[0]), 255 - (self.mo_line_color[1]), (255 - self.mo_line_color[2]))
            self.text_color = self.line_color


        self.mouse_hover = False
        self.clicked = False



    def draw(self, surf):
        pygame.draw.rect(self.image, self.bg_color, ((0,0), self.size))
        pygame.draw.rect(self.image, self.line_color, ((0,0), self.size), 3)
        text.write(self.image, self.text, (self.rect.width/2, (self.rect.height/2) -2) ,color = self.text_color, centered = True)
        surf.blit(self.image, self.pos)

