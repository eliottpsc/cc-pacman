from time import sleep
from dataclasses import dataclass
from typing import Self
import pygame

from Config import Config
from Events import Events
from Maze import Maze
from Pac import Pac


@dataclass
class Game:

    screen: pygame.Surface
    conf: Config

    WINDOW_WIDTH: int = 1200
    WINDOW_HEIGHT: int = 1200

    @classmethod
    def create(cls) -> Self:
        game = cls(
            screen=pygame.display.set_mode(
                (cls.WINDOW_WIDTH, cls.WINDOW_HEIGHT)),
            conf=Config.load())
        sleep(1)
        game.init()
        return game

    def init(self) -> None:
        _ = pygame.init()
        pygame.display.set_caption("pac-man")
        pygame.font.init()


    def menu_loop(self):
        ...

    def level_loop(self):
        pac = Pac(self)
        maze = Maze(self)
        ev = Events(self, pac)
        pac.create()
        while True:
            ev.get()
            ev.check_held_keys()

            self.screen.fill((0, 0, 0))

            maze.draw_grid()
            pac.update()

            pygame.display.flip()

    def hiscores_loop(self):
        ...
