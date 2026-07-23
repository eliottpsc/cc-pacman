import sys
import pygame
from time import sleep
from dataclasses import dataclass
from typing import Self

from Config import Config
from Menu import Menu
from Highscores import Highscores
from CurrentPlay import CurrentPlay
from Hud import Hud


@dataclass
class Game:

    screen: pygame.Surface
    conf: Config
    playing: bool

    WINDOW_WIDTH: int = 1200
    WINDOW_HEIGHT: int = 1400

    @classmethod
    def create(cls) -> Self:
        game = cls(
            screen=pygame.display.set_mode(
                (cls.WINDOW_WIDTH, cls.WINDOW_HEIGHT)),
            conf=Config.load(),
            playing=False)
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

    def level_loop(self) -> None:
        hs = Highscores(self)
        current_play: CurrentPlay = CurrentPlay(self)

        self.playing = current_play.exists
        while self.playing and not current_play.level.pac.dead:
            # INPUT EVENTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            keys = pygame.key.get_pressed()

            # DRAW
            _ = self.screen.fill((0, 0, 0))
            hud = Hud(current_play)
            hud.draw()
            current_play.level.display()

            # COLLISIONS
            cols = pygame.sprite.spritecollide(
                current_play.level.pac,
                current_play.level.pellets, True)
            for _ in cols:
                current_play.score += 20

            # UPDATE
            current_play.level.update(keys)

            # DEATH
            while current_play.level.pac.dead and hs.input_isactive:
                _ = self.screen.fill((0, 0, 0))
                hs.input_name(pygame.event.get(), current_play.score)
                hs.draw_input_box(current_play.score)
                pygame.display.flip()
            pygame.display.flip()

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
