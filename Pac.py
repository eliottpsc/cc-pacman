import pygame
import numpy as np
from Entity import Entity
from pygame.sprite import Sprite


class Pac(Entity, Sprite):
    def __init__(self, game, maze) -> None:
        super().__init__(game, maze)
        self.create()

    def create(self) -> None:
        _ = pygame.draw.rect(self.screen, (0, 255, 0), self.rect, 20)

    def destroy(self):
        ...

    def update(self, keys, dt):
        new_dir= tuple(self.direction)
        if keys[pygame.K_LEFT]:
            new_dir = (0, -1)
        if keys[pygame.K_RIGHT]:
            new_dir = (0, 1)
        if keys[pygame.K_UP]:
            new_dir = (-1, 0)
        if keys[pygame.K_DOWN]:
            new_dir = (1, 0)
        if keys[pygame.K_ESCAPE]:
            self.game.menu_loop()

        self.move_timer += dt
        if self.move_timer >= self.move_delay:
            if self.can_move(new_dir):
                self.move_timer = 0
                self.direction = np.array(new_dir)
                self.pos += self.direction

        blocksize = self.game.WINDOW_WIDTH // self.game.conf.width
        self.rect = pygame.Rect(self.pos[1] * blocksize,
                                self.pos[0] * blocksize,
                                50, 50)
        _ = pygame.draw.rect(self.screen, (220, 200, 0), self.rect, 10)
