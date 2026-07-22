#!/usr/bin/env python3
import pygame
import random as rd
from itertools import cycle
from Entity import Entity
from Spritesheet import Spritesheet


class Ghost(Entity):
    def __init__(self, game, maze) -> None:
        super().__init__(game, maze)
        self.move_delay /= (9 / 10)
        self.pos = (2, 10)
        self.pixel = (self.pos[0] * self.tile_size,
                      self.pos[1] * self.tile_size)
        self.rect = pygame.Rect(*self.pos, 50, 50)
        self.ss = Spritesheet("assets/pacman.png")
        self.images = cycle(self.ss.images_at([
            (0, 284, 196, 196),
            (233, 284, 196, 196),
            (465, 284, 196, 196),
            (233, 284, 196, 196),
            ]))
        self.image = next(self.images)

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

        tx, ty = self.pos[0] * self.tile_size, self.pos[1] * self.tile_size
        dx, dy = tx - self.pixel[0], ty - self.pixel[1]
        sign = ((dx > 0) - (dx < 0), (dy > 0) - (dy < 0))
        step = self.speed * dt
        self.pixel = (
                tx if abs(dx) < step else self.pixel[0] + step * sign[0],
                ty if abs(dy) < step else self.pixel[1] + step * sign[1],
                )

        rot = {(0, -1): 180, (0, 1): 0, (-1, 0): 90, (1, 0): 270}

        self.anim_timer += dt
        if self.anim_timer >= self.anim_delay:
            self.anim_timer = 0
            self.image = next(self.images)

        image = pygame.transform.rotate(self.image, rot[self.direction])
        image = pygame.transform.scale(image, (self.tile_size * 0.75,)*2)

        self.rect = pygame.Rect(self.pixel[1], self.pixel[0], *(self.tile_size * 0.75,)*2)
        self.screen.blit(image, self.rect)


if __name__ == "__main__":
    pass
