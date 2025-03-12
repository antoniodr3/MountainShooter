#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
import os

from pygame import Surface, Rect
from pygame.font import Font


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load(os.path.join(os.path.dirname(__file__), '../asset/MenuBg.png'))
        self.rect = self.surf.get_rect(left =0, top =0)


    def run(self, ):
        pygame.mixer_music.load((os.path.join(os.path.dirname(__file__), '../asset/Menu.mp3')))
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, text_rect=None):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        Text_rect: Rect = text_surf.get_rect(text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)




