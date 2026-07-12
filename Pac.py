import pygame

class Pac():
    def __init__(self, game, maze) -> None:
        self.game = game
        self.screen: pygame.Surface = game.screen
        self.maze = maze
        self.row: int = 0
        self.col: int = 0
        self.direction = (1, 0)
        self.speed: float = 0.5
        self.rect = pygame.Rect(self.row, self.col, 50, 50)
        self.create()

    def create(self) -> None:
        _ = pygame.draw.rect(self.screen, (0, 255, 0), self.rect, 20)

    def destroy(self):
        ...

    def can_move(self, dire):
        if not 0 <= self.row < len(self.maze[0]) or not 0 <= self.col < len(self.maze):
            return False
        cell = self.maze[self.row][self.col]
        walls = format(int(cell, 16), '04b')
        if dire == (-1, 0):
            return walls[3] == "0"
        if dire == (1, 0):
            return walls[1] == "0"
        if dire == (0, -1):
            return walls[0] == "0"
        if dire == (0, 1):
            return walls[2] == "0"

    def update(self, keys):
        new_dir = self.direction
        if keys[pygame.K_LEFT]:
            new_dir = (0, -1)
        if keys[pygame.K_RIGHT]:
            new_dir = (0, 1)
        if keys[pygame.K_UP]:
            new_dir = (-1, 0)
        if keys[pygame.K_DOWN]:
            new_dir = (1, 0)

        if self.can_move(new_dir):
            self.direction = new_dir
            self.row += self.direction[0]
            self.col += self.direction[1]

        blocksize = self.game.WINDOW_WIDTH // self.game.conf.width
        self.rect = pygame.Rect(self.col * blocksize + 2, self.row * blocksize + 2, 50, 50)
        _ = pygame.draw.rect(self.screen, (220, 200, 0), self.rect, 10)
