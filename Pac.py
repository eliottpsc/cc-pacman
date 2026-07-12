import pygame

class Pac():
    def __init__(self, game, maze) -> None:
        self.game = game
        self.screen: pygame.Surface = game.screen
        self.maze = maze
        self.x: int = 0
        self.y: int = 0
        self.direction = (1, 0)
        self.speed: float = 0.5
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.create()

    def create(self) -> None:
        _ = pygame.draw.rect(self.screen, (0, 255, 0), self.rect, 20)

    def destroy(self):
        ...

    def can_move(self, dire):
        return True

    def update(self, keys):
        new_dir = self.direction
        if keys[pygame.K_LEFT]:
            new_dir = (-1, 0)
        if keys[pygame.K_RIGHT]:
            new_dir = (1, 0)
        if keys[pygame.K_UP]:
            new_dir = (0, -1)
        if keys[pygame.K_DOWN]:
            new_dir = (0, 1)

        if self.can_move(new_dir):
            self.direction = new_dir
            self.x += self.direction[0]
            self.y += self.direction[1]

        blocksize = 1 #self.game.WINDOW_WIDTH // self.game.conf.width
        self.rect = pygame.Rect(self.x * blocksize, self.y * blocksize, 50, 50)
        _ = pygame.draw.rect(self.screen, (220, 200, 0), self.rect, 10)
