''' ---spygmae2d_versieIII---, created by Lennart on 3/4/2018'''
import pygame

from const import *

ui_fonts = {
    'std':      {'type': 'Century Gothic',
                'size': 18,
                'color': WHITE
            },
    'std_black' :{'type': 'Century Gothic',
               'size': 20,
               'color': BLACK
            },
    'std_white':{'type': 'Century Gothic',
                'size': 12,
                'color': WHITE
            },
    'hdr': {'type': 'Century Gothic',
                'size': 30,
                'color': WHITE
            },
}

def write(surface, text, pos, font_cat = 'std', color=False, centered = False, right=False):
    pygame.font.init()
    my_font = pygame.font.SysFont(ui_fonts[font_cat]['type'], ui_fonts[font_cat]['size'])
    my_text = str(text)

    if color == False:
        my_label = my_font.render(my_text, 1, ui_fonts[font_cat]['color'])
    else:
        my_label = my_font.render(my_text, 1, color)

    if centered == True:
        surface.blit(my_label, (pos[0] - my_label.get_width() / 2,
                                pos[1]- my_label.get_height() / 2 + 1))

    elif right == True:
        surface.blit(my_label, (pos[0] - my_label.get_width(),
                                pos[1]
                                ))
    else:
        surface.blit(my_label, (pos[0], pos[1]))
        return


