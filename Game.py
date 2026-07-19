import sys
import pygame
from time import sleep
from dataclasses import dataclass
from typing import Never, Self

from Config import Config
from Maze import Maze
from Menu import Menu
from Pac import Pac
from Ghost import Ghost
from CurrentPlay import CurrentPlay
from Highscores import Highscores


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
            current_play=False)
        sleep(1)
        game.init()
        return game

    def init(self) -> None:
        _ = pygame.init()
        pygame.display.set_caption("pac-man")
        pygame.font.init()

    def menu_loop(self) -> None:
        menu = Menu(self)
        while True:
            if menu.running is False:
                break
            menu.draw()
            menu.get_event()

            pygame.display.flip()

    def level_loop(self) -> Never:
        hs = Highscores(self)
        pellets = pygame.sprite.Group()
        maze = Maze(self, pellets)
        pac = Pac(self, maze.load())
        ghost = Ghost(self, maze.load())
        clock = pygame.time.Clock()
        current_play = CurrentPlay()
        self.current_play = current_play.exists
        while self.current_play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            keys = pygame.key.get_pressed()

            _ = self.screen.fill((0, 0, 0))

            maze.draw_grid()
            maze.pellets.update()
            maze.pellets.draw(self.screen)
            cols = pygame.sprite.spritecollide(pac, maze.pellets, True)
            for col in cols:
                current_play.score += 20

            dt = clock.tick(60)
            ghost.update(pac.pos, dt)
            pac.update(keys, dt)
            while pac.dead and hs.input_isactive:
                _ = self.screen.fill((0, 0, 0))
                hs.input_name(pygame.event.get(), current_play.score)
                hs.draw_input_box(current_play.score)
                pygame.display.flip()
            pygame.display.flip()
        # level ends either by death or win
        # win and last lvl -> input highscore -> menu
        # win and not last lvl -> update CurrentPlay -> level_loop()
        # death -> input highscore -> menu

    def highscores_loop(self) -> None:
        hs = Highscores(self)
        while hs.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        hs.running = False
            hs.display()
            pygame.display.flip()

    def hiscores_loop(self) -> None:
        ...
