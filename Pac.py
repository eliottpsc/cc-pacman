import pygame

class Pac():
    def __init__(self, game) -> None:
        self.screen: pygame.Surface = game.screen
        self.x: float = 0
        self.y: float = 0
        self.speed: float = 0.5
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.create()

    def create(self) -> None:
        _ = pygame.draw.rect(self.screen, (0, 255, 0), self.rect, 20)

    def destroy(self):
        ...

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        _ = pygame.draw.rect(self.screen, (220, 200, 0), self.rect, 10)
