import pygame
import numpy as np
from numpy import array

class Pac():
    def __init__(self, game, maze) -> None:
        self.game = game
        self.screen: pygame.Surface = game.screen
        self.maze = np.array(maze)
        self.pos = np.array((0, 0))
        self.direction = np.array((0, 1))
        self.move_timer = 0
        self.move_delay = 360
        self.speed: float = 0.5
        self.rect = pygame.Rect(*self.pos, 50, 50)
        self.create()

    def create(self) -> None:
        _ = pygame.draw.rect(self.screen, (0, 255, 0), self.rect, 20)

    def destroy(self):
        ...

    def can_move(self, dire: tuple):
        if np.any(self.pos < 0) or np.any(self.pos >= self.maze.shape):
            return False
        cell = self.maze[*self.pos]
        walls = format(int(cell, 16), '04b')
        if dire == (-1, 0):
            return walls[3] == "0"
        if dire == (1, 0):
            return walls[1] == "0"
        if dire == (0, -1):
            return walls[0] == "0"
        if dire == (0, 1):
            return walls[2] == "0"

    def update(self, keys, dt):
        new_dir: tuple = tuple(self.direction)
        if keys[pygame.K_LEFT]:
            new_dir = (0, -1)
        if keys[pygame.K_RIGHT]:
            new_dir = (0, 1)
        if keys[pygame.K_UP]:
            new_dir = (-1, 0)
        if keys[pygame.K_DOWN]:
            new_dir = (1, 0)

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
