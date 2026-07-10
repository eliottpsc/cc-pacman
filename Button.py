from collections.abc import Callable
from typing import Any
import pygame


class Button():
    def __init__(self, x: float, y: float, image: pygame.Surface,
                 scale: float) -> None:
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (int(x), int(y))
        self.clicked = False

    def draw(self, screen: pygame.Surface) -> None:
        _ = screen.blit(self.image, self.rect)

    def get_click(self, game, button_fun: Callable[..., Any]) -> None:
        action = False
        _ = action
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                action = True
                button_fun()

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

    def update(self) -> None:
        ...
