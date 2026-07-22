#!/usr/bin/env python3
import pygame

class Entity:
    def __init__(self, game, maze) -> None:
        self.game = game
        self.screen: pygame.Surface = game.screen
        self.maze = maze
        self.pos = (0, 0)
        self.pixel = (0, 0)
        self.direction = (0, 1)
        self.next_dir = (0, 1)
        self.move_timer = 0
        self.move_delay = 300
        self.tile_size = self.game.WINDOW_WIDTH // self.game.conf.width
        self.speed = self.tile_size / self.move_delay
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
        return False

    def move(self, dt):
        self.move_timer += dt
        if self.move_timer >= self.move_delay:
            self.move_timer = 0
            if self.can_move(self.next_dir):
                self.direction = self.next_dir
                self.pos = (self.pos[0] + self.direction[0],
                            self.pos[1] + self.direction[1])
            elif self.can_move(self.direction):
                self.pos = (self.pos[0] + self.direction[0],
                            self.pos[1] + self.direction[1])

if __name__ == "__main__":
    pass
