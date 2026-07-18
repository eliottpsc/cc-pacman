from typing import override
import pygame
from pygame.sprite import Sprite


class Pellet(Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.color = (0, 255, 0)
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = ((x * 60) + 30, (y * 60) + 30)

    # @override
    # def update() -> None:
    #     # when pac gets on the pellet:
    #     # self.kill()
    #     ...
