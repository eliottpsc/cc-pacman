#!/usr/bin/env python3
import pygame
import numpy as np
import random as rd
from Entity import Entity


class Ghost(Entity):
    def __init__(self, game, maze) -> None:
        super().__init__(game, maze)
        self.pos = np.array((10, 10))
        self.rect = pygame.Rect(*self.pos, 50, 50)

    def update(self, dt):
        new_dir = rd.choice(((0, -1), (0, 1), (-1, 0), (1, 0)))
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
        pygame.draw.rect(self.screen, (220, 0, 200), self.rect, 10)


if __name__ == "__main__":
    pass
