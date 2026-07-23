import pygame
import numpy as np
from pygame.sprite import Sprite

from Entity import Entity


class Pac(Entity, Sprite):
    def __init__(self, level) -> None:
        super().__init__(level)
        self.dead = False

    def update(self, keys: dict[int, bool], dt: int) -> None:
        new_dir = tuple(self.direction)
        if keys[pygame.K_LEFT]:
            new_dir = (0, -1)
        if keys[pygame.K_RIGHT]:
            new_dir = (0, 1)
        if keys[pygame.K_UP]:
            new_dir = (-1, 0)
        if keys[pygame.K_DOWN]:
            new_dir = (1, 0)
        if keys[pygame.K_ESCAPE]:
            self.level.current_play.game.menu_loop()
        if keys[pygame.K_k]:
            self.dead = True

        self.move_timer += dt
        if self.move_timer >= self.move_delay:
            if self.can_move(new_dir):
                self.move_timer = 0
                self.direction = np.array(new_dir)
                self.pos += self.direction

        blocksize = self.level.current_play.game.WINDOW_WIDTH // \
            self.level.current_play.game.conf.width
        self.rect = pygame.Rect(self.pos[1] * blocksize,
                                self.pos[0] * blocksize,
                                50, 50)
        pygame.draw.rect(self.level.level_surf, (220, 200, 0), self.rect, 10)
