import pygame
from random import randrange
import numpy as np
from typing import Any

from mazegenerator import MazeGenerator
from CurrentPlay import CurrentPlay
from Pellet import Pellet
from Pac import Pac
from Ghost import Ghost


class Level():
    def __init__(self, current_play: CurrentPlay) -> None:
        self.current_play: CurrentPlay = current_play
        self.seed: int
        self.entry: tuple[int, int]
        self.exit: tuple[int, int]
        self.size: tuple[int, int]
        self.maze: np.typing.NDArray[Any]
        self.blocksize: int
        self.level_surf: pygame.Surface
        self.pellets: Any = pygame.sprite.Group()
        self.pac: Pac
        self.ghost: Ghost

    def generate(self, seed: int, entry: tuple[int, int],
                 exit: tuple[int, int],
                 size: tuple[int, int]) -> np.typing.NDArray[Any]:
        """Generate a maze with appropriate characteristics (size, seed,
        level number) and save it in the Level instance."""
        self.seed = seed
        self.entry = entry
        self.exit = exit
        self.size = size
        self.blocksize = int(
            min(self.current_play.game.WINDOW_WIDTH,
                self.current_play.game.WINDOW_HEIGHT) / self.size[0])
        mazegen: MazeGenerator = MazeGenerator(
            size=self.size,
            perfect=False,
            entry_cell=self.entry,
            exit_cell=self.exit,
            seed=self.seed
        )
        mazegen.generate(seed)
        self.maze = np.array(mazegen.maze)
        self.gen_pellets(self.pellets)
        self.pac = Pac(self)
        self.ghost = Ghost(self)
        return self.maze

    def display(self) -> None:
        """Display the level saved in the instance."""
        self.level_surf = pygame.Surface.subsurface(
            self.current_play.game.screen, (0, 100,
                                            self.size[0] * self.blocksize,
                                            self.size[1] * self.blocksize))
        # WALLS
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                self.draw_cell(cell, x, y)
        # PELLETS
        self.pellets.update()
        self.pellets.draw(self.level_surf)

    def draw_cell(self, cell: int, x: int, y: int) -> None:
        """Shape a single cell of the maze and displays it in the pygame
        display.
        -- Arguments --
            cell: the hex character encoding the walls in the cell, a string
            y: the y coordinate of the cell in the grid, an int
            x: the x coordinate of the cell in the grid, an int"""
        color = (255, 0, 0)
        edgeN = pygame.Rect((x * self.blocksize), (y * self.blocksize),
                            self.blocksize, 2)
        edgeE = pygame.Rect((x * self.blocksize) + (self.blocksize - 2),
                            (y * self.blocksize), 2, self.blocksize)
        edgeS = pygame.Rect((x * self.blocksize),
                            (y * self.blocksize) + (self.blocksize - 2),
                            self.blocksize, 2)
        edgeW = pygame.Rect((x * self.blocksize),
                            (y * self.blocksize), 2, self.blocksize)

        if int(format(cell, '04b')[3]):
            _ = pygame.draw.rect(self.level_surf, color, edgeN, 4)
        if int(format(cell, '04b')[2]):
            _ = pygame.draw.rect(self.level_surf, color, edgeE, 4)
        if int(format(cell, '04b')[1]):
            _ = pygame.draw.rect(self.level_surf, color, edgeS, 4)
        if int(format(cell, '04b')[0]):
            _ = pygame.draw.rect(self.level_surf, color, edgeW, 4)

    def gen_pellets(self, pellets: Any) -> None:
        """Populate the maze with pellets."""
        spawn_chance = 70
        for x, row in enumerate(self.maze):
            for y, col in enumerate(row):
                new = Pellet(x, y)
                if self.maze[y][x] != 15:
                    if spawn_chance > randrange(0, 100):
                        pellets.add(new)

    def update(self, keys: dict[int, bool]) -> None:
        dt = pygame.time.Clock().tick(60)
        self.ghost.update(self.pac.pos, dt)
        self.pac.update(keys, dt)
