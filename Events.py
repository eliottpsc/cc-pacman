import sys
import pygame

from Pac import Pac


class Events():
    def __init__(self, game, pac: Pac) -> None:
        self.screen: pygame.Surface = game.screen
        self.pac: Pac = pac
        self.held_keys: list[str] = []
        self.game = game

    def get(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.held_keys.append('left')
                if event.key == pygame.K_RIGHT:
                    self.held_keys.append('right')
                if event.key == pygame.K_UP:
                    self.held_keys.append('up')
                if event.key == pygame.K_DOWN:
                    self.held_keys.append('down')
                if event.key == pygame.K_ESCAPE:
                    self.game.menu_loop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.held_keys.remove('left')
                if event.key == pygame.K_RIGHT:
                    self.held_keys.remove('right')
                if event.key == pygame.K_UP:
                    self.held_keys.remove('up')
                if event.key == pygame.K_DOWN:
                    self.held_keys.remove('down')

    def check_held_keys(self) -> None:
        for key in self.held_keys:
            if key == 'left':
                self.pac.x -= self.pac.speed
            if key == 'right':
                self.pac.x += self.pac.speed
            if key == 'up':
                self.pac.y -= self.pac.speed
            if key == 'down':
                self.pac.y += self.pac.speed
