#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple, speed: int = 5):

        super().__init__(name, position)
        self.speed = speed  # Define a velocidade de movimentação

    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        # Limita o movimento do jogador para permanecer dentro da tela
        self.keep_player_within_bounds()

    def keep_player_within_bounds(self):

        #Mantém o jogador dentro das bordas da janela.
        screen_width = pygame.display.get_surface().get_width()
        screen_height = pygame.display.get_surface().get_height()

        if self.rect.left < 0:  # Evita que passe pelo lado esquerdo
            self.rect.left = 0
        if self.rect.right > screen_width:  # Evita que passe pelo lado direito
            self.rect.right = screen_width
        if self.rect.top < 0:  # Evita que passe pela parte superior
            self.rect.top = 0
        if self.rect.bottom > screen_height:  # Evita que passe pela parte inferior
            self.rect.bottom = screen_height

