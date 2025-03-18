#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import PLAYER_KEY_UP, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_DOWN, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple, speed: int = 5):
        super().__init__(name, position)
        self.speed = speed

    def move(self):

        keys = pygame.key.get_pressed()

        if keys[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= Entity.SPEED[self.name]
        if keys[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += Entity.SPEED[self.name]
        if keys[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= Entity.SPEED[self.name]
        if keys[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += Entity.SPEED[self.name]

        # Limita o movimento do jogador para permanecer dentro da tela
        self.keep_player_within_bounds()

    def keep_player_within_bounds(self):

        #Mantém o jogador dentro das bordas da janela.
        screen_width = pygame.display.get_surface().get_width()
        screen_height = pygame.display.get_surface().get_height()

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

