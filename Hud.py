import pygame

from CurrentPlay import CurrentPlay


class Hud():
    def __init__(self, current_play: CurrentPlay) -> None:
        self.current_play: CurrentPlay = current_play
        self.draw()

    def draw(self) -> None:
        top_surf = pygame.Surface.subsurface(
            self.current_play.game.screen, (
                0, 0, self.current_play.level.size[0] *
                self.current_play.level.blocksize, 100)
        )
        bot_surf = pygame.Surface.subsurface(
            self.current_play.game.screen, (
                0, 1300, self.current_play.level.size[0] *
                self.current_play.level.blocksize, 100)
        )
        self.top_rect: pygame.Rect = pygame.Rect(
            0, 0, self.current_play.game.WINDOW_WIDTH, 10)
        self.bot_rect: pygame.Rect = pygame.Rect(
            0, 0, self.current_play.game.WINDOW_WIDTH, 10)
        top_surf.fill((0, 255, 0))
        bot_surf.fill((0, 0, 255))

    def update(self) -> None:
        ...
