#!/usr/bin/env python3
import pygame
import numpy as np
from typing import Any

from Entity import Entity


class Ghost(Entity):
    def __init__(self, level) -> None:
        super().__init__(level)
        self.level = level
        self.pos = np.array((2, 10))
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 50, 50)

    def next_move(self, pacpos: np.typing.NDArray[Any]) -> Any:
        def totuple(arr: np.typing.NDArray[Any]) -> tuple[Any]:
            return tuple(arr.tolist())
        queue = [pacpos]
        visited = [totuple(pacpos)]
        parent: dict[Any, Any] = {}

        while queue:
            curr = queue.pop(0)
            cell = self.level.maze[*curr]
            walls = format(cell, '04b')
            mask = [True if b == '0' else False for b in walls]
            dires = np.array(((0, -1), (1, 0), (0, 1), (-1, 0)))[mask]

            if np.array_equal(curr, self.pos):
                try:
                    return totuple(parent[totuple(curr)] - self.pos)
                except KeyError:
                    return (0, 0)

            for dire in dires:
                neighbor = totuple(curr + dire)
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(np.array(neighbor))
                    parent[neighbor] = curr

    def update(self, pacpos: np.typing.NDArray[Any], dt: int) -> None:
        new_dir = self.next_move(pacpos)
        self.move_timer += dt
        if self.move_timer >= self.move_delay:
            if self.can_move(new_dir):
                self.move_timer = 0
                self.direction = np.array(new_dir)
                self.pos += self.direction

        blocksize = self.level.current_play.game.WINDOW_WIDTH // \
            self.level.current_play.game.conf.width
        self.rect = pygame.Rect(self.pos[1] * blocksize,
                                self.pos[0] * blocksize,
                                50, 50)
        pygame.draw.rect(self.level.level_surf,
                         (220, 0, 200), self.rect, 10)


if __name__ == "__main__":
    pass
