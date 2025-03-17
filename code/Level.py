#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory

# Inicializa o Pygame corretamente
pygame.init()
pygame.mixer.init()


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []

        # Carregar o fundo do nível
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))  # Retorna uma lista

        # Carregar a nave (Player1)
        player = EntityFactory.get_entity('Player1')  # Retorna uma instância única

        if player is None:
            print("⚠ ERRO: Player1 não foi carregado corretamente!")
        elif not isinstance(player, Entity):
            print("⚠ ERRO: Player1 não é uma instância válida de Entity!")
        else:
            # Garante que a nave tenha uma superfície e um retângulo
            if hasattr(player, "surf") and hasattr(player, "rect"):
                # Define a posição inicial da nave no centro inferior da tela
                player.rect.centerx = WIN_WIDTH // 2
                player.rect.bottom = WIN_HEIGHT - 20
                self.entity_list.append(player)
                print("✅ Player1 carregado corretamente!")
            else:
                print("⚠ ERRO: Player1 não possui os atributos necessários (surf e rect)!")

        self.timeout = 20000
        self.fps_limit = 60  # Limitador de FPS

    def run(self):
        """Executa o loop principal do jogo."""
        # Gera o caminho para o arquivo de áudio
        audio_path = os.path.join(os.path.dirname(__file__), f'../asset/{self.name}.mp3')

        # Verifica se o arquivo realmente existe
        if not os.path.isfile(audio_path):
            print(f"⚠ Arquivo de áudio não encontrado: {audio_path}")
        else:
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(self.fps_limit)

            # Captura eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            # Atualiza e renderiza os elementos do jogo
            self.window.fill((0, 0, 0))

            for ent in self.entity_list:
                if hasattr(ent, "surf") and hasattr(ent, "rect"):
                    self.window.blit(source=ent.surf, dest=ent.rect)
                    ent.move()
                else:
                    print("⚠ ERRO: Uma entidade sem `surf` ou `rect` está na lista!")

            # Exibe informações do jogo na tela
            self.printed_text(clock)

            pygame.display.flip()  # Atualiza o display

        pygame.mixer.music.stop()
        pygame.quit()
        sys.exit()  # Sai do programa corretamente

    def printed_text(self, clock):
        """Exibe informações como timeout, FPS e entidades na tela."""
        self.level_text(text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000:.1f}s',
                        text_color=COLOR_WHITE, text_pos=(10, 5))
        self.level_text(text_size=14, text=f'FPS: {clock.get_fps():.0f}',
                        text_color=COLOR_WHITE, text_pos=(10, WIN_HEIGHT - 35))
        self.level_text(text_size=14, text=f'Entidades: {len(self.entity_list)}',
                        text_color=COLOR_WHITE, text_pos=(10, WIN_HEIGHT - 20))
        self.level_text(text_size=14, text=f'Limitador de FPS: {self.fps_limit}',
                        text_color=COLOR_WHITE, text_pos=(10, WIN_HEIGHT - 50))

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        """Renderiza o texto e o desenha na tela."""
        font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf = font.render(text, True, text_color)
        text_rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surf, text_rect)



