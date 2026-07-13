#!/usr/bin/env python3
import pygame
import numpy as np
from Entity import Entity


class Ghost(Entity):
    def __init__(self, game, maze) -> None:
        super().__init__(game, maze)
        self.pos = np.array((10, 10))
        self.rect = pygame.Rect(*self.pos, 50, 50)

    def update(self, dt):
        pygame.draw.rect(self.screen, (220, 0, 200), self.rect, 10)


if __name__ == "__main__":
    pass
