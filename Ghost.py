#!/usr/bin/env python3
import pygame
import random as rd
from Entity import Entity


class Ghost(Entity):
    def __init__(self, game, maze) -> None:
        super().__init__(game, maze)
        self.move_delay /= (9 / 10)
        self.pos = (2, 10)
        self.rect = pygame.Rect(*self.pos, 50, 50)

    def choose_direction(self, pacpos):
        queue = [pacpos]
        visited = [pacpos]
        parent = {}

        while queue:
            curr = queue.pop(0)
            cell = self.maze[curr[0]][curr[1]]
            walls = format(int(cell, 16), '04b')
            mask = [True if b == '0' else False for b in walls]
            dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
            dires = [dirs[i] for i in range(4) if mask[i]]

            if curr == self.pos:
                try:
                    ax, ay = parent[curr]
                    bx, by = self.pos
                    return (ax - bx, ay - by)
                except KeyError:
                    return (0, 0)

            for dire in dires:
                neighbor = (curr[0] + dire[0], curr[1] + dire[1])
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
                    parent[neighbor] = curr


    def update(self, pacpos, dt):
        self.next_dir = self.choose_direction(pacpos)

        self.move(dt)

        self.rect = pygame.Rect(self.pos[1] * self.tile_size,
                                self.pos[0] * self.tile_size,
                                50, 50)
        pygame.draw.rect(self.screen, (220, 0, 200), self.rect, 10)


if __name__ == "__main__":
    pass
