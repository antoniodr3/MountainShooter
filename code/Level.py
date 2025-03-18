#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import pygame
import random

from code.Const import COLOR_WHITE, WIN_HEIGHT, WIN_WIDTH, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME
from code.Entity import Entity
from code.EntityFactory import EntityFactory

pygame.init()
pygame.mixer.init()
pygame.font.init()


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.timeout = 20000
        self.fps_limit = 60
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))  # Retorna uma lista

        # Carregar a nave
        player = EntityFactory.get_entity('Player1')  # Retorna uma instância única
        if player and hasattr(player, "surf") and hasattr(player, "rect"):
            player.rect.left = 10
            player.rect.centery = WIN_HEIGHT // 2
            self.entity_list.append(player)
            print("✅ Player1 carregado corretamente!")
        else:
            print("⚠ ERRO: Player1 não foi carregado corretamente ou está faltando atributos!")

        # Se o modo de jogo tiver 2 jogadores
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player2 = EntityFactory.get_entity('Player2')
            if player2:
                self.entity_list.append(player2)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self):
        """Executa o loop principal do jogo."""
        # Carregar e tocar música de fundo
        audio_path = os.path.join(os.path.dirname(__file__), f'../asset/{self.name}.mp3')
        if os.path.isfile(audio_path):
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play(-1)
        else:
            print(f"⚠ Arquivo de áudio não encontrado: {audio_path}")

        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(self.fps_limit)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
                elif event.type == EVENT_ENEMY:
                    self.spawn_enemy()

            self.update_screen()
            self.printed_text(clock)
            pygame.display.flip()
        pygame.mixer.music.stop()

    def spawn_enemy(self):
        """Cria inimigos e os adiciona à lista de entidades."""
        enemy1 = EntityFactory.get_entity('Enemy1')
        enemy2 = EntityFactory.get_entity('Enemy2')

        # Config Enemy1
        if enemy1 and hasattr(enemy1, "surf") and hasattr(enemy1, "rect"):
            enemy1.rect.x = WIN_WIDTH + 50
            enemy1.rect.y = random.randint(0, WIN_HEIGHT - enemy1.rect.height)
            self.entity_list.append(enemy1)
            print(f"✅ Enemy1 criado na posição: {enemy1.rect}")
        else:
            print("⚠ ERRO: Enemy1 não foi gerado corretamente ou está faltando atributos!")

        # Config Enemy2
        if enemy2 and hasattr(enemy2, "surf") and hasattr(enemy2, "rect"):
            enemy2.rect.x = WIN_WIDTH + 50
            enemy2.rect.y = random.randint(0, WIN_HEIGHT - enemy2.rect.height)
            self.entity_list.append(enemy2)
            print(f"✅ Enemy2 criado na posição: {enemy2.rect}")
        else:
            print("⚠ ERRO: Enemy2 não foi gerado ou está faltando atributos!")

    def update_screen(self):
        self.window.fill((0, 0, 0))

        for ent in self.entity_list:
            if hasattr(ent, "surf") and hasattr(ent, "rect"):
                self.window.blit(ent.surf, ent.rect)
                ent.move()
                print("⚠ ERRO: Uma entidade sem `surf` ou `rect` está na lista!")

    def printed_text(self, clock):
        """Exibe imeout, FPS e entidades."""
        fps = clock.get_fps()
        self.level_text(text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000:.1f}s',
                        text_color=COLOR_WHITE, text_pos=(10, 5))
        self.level_text(text_size=14, text=f'FPS: {fps:.0f}',
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





