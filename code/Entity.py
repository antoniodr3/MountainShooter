#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from abc import ABC, abstractmethod

import pygame


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        # Obtendo o caminho absoluto do diretório atual do arquivo
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # Corrigindo o caminho para o diretório de assets
        asset_path = os.path.join(base_dir, '../asset/', name + '.png')

        self.name = name
        try:
            # Tentando carregar a imagem usando o caminho absoluto
            self.surf = pygame.image.load(asset_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo de imagem não encontrado: {asset_path}")

        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass