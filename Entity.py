#!/usr/bin/env python3
import pygame

class Entity:
    def __init__(self, game, maze) -> None:
        self.game = game
        self.screen: pygame.Surface = game.screen
        self.maze = maze
        self.pos = (0, 0)
        self.direction = (0, 1)
        self.move_timer = 0
        self.move_delay = 360
        self.speed: float = 0.5
        self.rect = pygame.Rect(*self.pos, 50, 50)

    def can_move(self, dire: tuple):
        row, col = self.pos
        if not 0 <= row < len(self.maze) or not 0 <= col < len(self.maze[0]):
            return False
        cell = self.maze[row][col]
        walls = format(int(cell, 16), '04b')
        if dire == (-1, 0):
            return walls[3] == "0"
        if dire == (1, 0):
            return walls[1] == "0"
        if dire == (0, -1):
            return walls[0] == "0"
        if dire == (0, 1):
            return walls[2] == "0"

if __name__ == "__main__":
    pass
