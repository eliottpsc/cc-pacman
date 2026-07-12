import sys
import pygame
from time import sleep
from dataclasses import dataclass
from typing import Never, Self
import pygame

from Config import Config
from Maze import Maze
from Menu import Menu
from Pac import Pac
from CurrentPlay import CurrentPlay

@dataclass
class Game:

    screen: pygame.Surface
    conf: Config
    current_play: bool

    WINDOW_WIDTH: int = 1200
    WINDOW_HEIGHT: int = 1200

    @classmethod
    def create(cls) -> Self:
        game = cls(
            screen=pygame.display.set_mode(
                (cls.WINDOW_WIDTH, cls.WINDOW_HEIGHT)),
            conf=Config.load(),
            current_play = False)
        sleep(1)
        game.init()
        return game

    def init(self) -> None:
        _ = pygame.init()
        pygame.display.set_caption("pac-man")
        pygame.font.init()

    def menu_loop(self) -> Never:
        menu = Menu(self)
        while True:
            menu.draw()
            menu.get_event()

            pygame.display.flip()

    def level_loop(self) -> Never:
        pac: Pac = Pac(self)
        maze: Maze = Maze(self)
        pac.create()
        current_play = CurrentPlay()
        self.current_play = current_play.exists
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            keys = pygame.key.get_pressed()

            _ = self.screen.fill((0, 0, 0))

            maze.draw_grid()
            pac.update(keys)

            pygame.display.flip()

    def hiscores_loop(self) -> None:
        ...
