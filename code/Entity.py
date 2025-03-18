#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from abc import abstractmethod, ABC

import pygame


class Entity(ABC):
    SPEED = {
        "Player1": 5,
        "Player2": 5,
    }

    speed = {
        "Player1": 5,
        "Player2": 5,
    }


    def __init__(self, name: str, position: tuple):

        # Define os atributos principais
        self.name = name
        self.position = position

        # Caminho para o diretório base e para o recurso gráfico da entidade
        base_dir = os.path.dirname(os.path.abspath(__file__))
        asset_path = os.path.join(base_dir, '../asset/', f'{name}.png')

        try:
            # Tentativa de carregar a superfície da entidade
            self.surf = pygame.image.load(asset_path).convert_alpha()
        except FileNotFoundError:
            raise FileNotFoundError(f"⚠ Arquivo de imagem não encontrado: {asset_path}")
        except pygame.error as e:
            raise RuntimeError(f"⚠ Erro ao carregar o recurso '{name}': {e}")

        # Define o retângulo inicial da entidade com base na posição fornecida
        self.rect = self.surf.get_rect(topleft=position)

        self.speed = 0

    @abstractmethod
    def move(self):

        pass
