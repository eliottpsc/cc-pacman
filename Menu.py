from collections.abc import Generator
from typing import Any, Never
import pygame
from Button import Button


class Menu:
    def __init__(self, game) -> None:
        self.screen: pygame.Surface = game.screen
        self.width: float = game.WINDOW_WIDTH
        self.height: float = game.WINDOW_HEIGHT
        self.rect: pygame.Rect = pygame.Rect(0, 0, self.width, self.height)
        self.game = game
        self.buttons: list[Button] = []
        self.running: bool = True
        # BUTTONS
        # self.title = Button('title', self.rect.centerx, self.rect.centery / 2,
        #                     pygame.image.load('assets/title.png'),
        #                     2.2, lambda: 1)
        # self.buttons.append(self.title)
        self.continu: Button | None = None
        self.start = Button('start', self.rect.centerx,
                            self.rect.centery * 1.2,
                            pygame.image.load('assets/start.png'),
                            1, self.game.level_loop)
        self.buttons.append(self.start)
        self.settings = Button('settings', self.rect.centerx,
                               self.rect.centery * 1.4,
                               pygame.image.load('assets/settings.png'),
                               1, lambda: 1)
        self.buttons.append(self.settings)
        self.highscores = Button('highscores', self.rect.centerx,
                                 self.rect.centery * 1.6,
                                 pygame.image.load('assets/highscores.png'),
                                 1, lambda: 1)
        self.buttons.append(self.highscores)
        self.quit = Button('quit', self.rect.centerx, self.rect.centery * 1.8,
                           pygame.image.load('assets/quit.png'),
                           1, pygame.quit)
        self.buttons.append(self.quit)
        self.selector: MenuSelector = MenuSelector(game, self.buttons[0])
        self.select_dir: str | None = None
        self.select_cycle = self.select()

    def draw_text(self, text: str, font: pygame.font.Font,
                  color: tuple[int, int, int], x: float, y: float) -> None:
        img = font.render(text, True, color)
        text_rect = img.get_rect()
        text_rect.center = (int(x), int(y))
        self.screen.blit(img, text_rect)

    def select(self) -> Generator[Button, Any, Never]:
        n = 0
        while True:
            if self.select_dir == 'up':
                n -= 1
                if n < 0:
                    n = len(self.buttons) - 1
            elif self.select_dir == 'down':
                n += 1
                if n > len(self.buttons) - 1:
                    n = 0
            self.selector.selected = self.buttons[n]
            self.selector.rect.centery = self.selector.selected.rect.centery
            self.selector.rect_right.centery = self.selector.selected.\
                rect.centery
            yield self.buttons[n]

    def draw(self) -> None:
        # BACKGROUND
        self.screen.fill((255, 0, 255), self.rect)
        title = pygame.transform.scale(pygame.image.load('assets/title.png'), (640, 128))
        title_rect = title.get_rect()
        title_rect.centerx = self.game.WINDOW_WIDTH / 2
        title_rect.centery = self.game.WINDOW_WIDTH / 4
        _ = self.screen.blit(title, title_rect)
        # TEXT
        self.draw_text("WOW KILLER",
                       pygame.font.SysFont('comicsans', 40),
                       (0, 255, 0), self.width / 2, self.height / 6)
        self.draw_text("by lgrosse and eruffin",
                       pygame.font.SysFont('comicsans', 20),
                       (0, 0, 255), 75, self.game.WINDOW_HEIGHT - 15)
        # BUTTONS
        if self.game.current_play is True and self.continu is None:
            self.continu = Button(
                'continu', self.rect.centerx, self.rect.centery,
                pygame.image.load('assets/continue.png'), 1,
                lambda: setattr(self, 'running', False))
            self.buttons.insert(0, self.continu)
            next(self.select_cycle)
        for button in self.buttons:
            button.draw(self.screen)
        # SELECTOR
        self.selector.draw()

    def get_event(self) -> None:
        pos = pygame.mouse.get_pos()
        for button in self.buttons:
            if button.rect.collidepoint(pos):
                self.selector.rect.centery = button.rect.centery
                self.selector.rect_right.centery = button.rect.centery
                self.selector.selected = button

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.select_dir = 'up'
                    next(self.select_cycle)
                if event.key == pygame.K_DOWN:
                    self.select_dir = 'down'
                    next(self.select_cycle)
                if event.key == pygame.K_RETURN:
                    self.selector.validate()
        for button in self.buttons:
            button.get_click(self.game, button.func)

    def update(self) -> None:
        ...


class MenuSelector():
    def __init__(self, game, initial_btn) -> None:
        self.game = game
        self.screen = game.screen
        self.selected: Button = initial_btn
        self.image = pygame.transform.scale(
            pygame.image.load('assets/menu-select.png'),
            (40, 40))
        self.rect = self.image.get_rect()
        self.rect.centerx = (self.game.WINDOW_HEIGHT / 3.4)
        self.rect.centery = (self.game.WINDOW_HEIGHT / 2) * 1.2
        self.rect_right = self.image.get_rect()
        self.rect_right.centerx = (self.game.WINDOW_HEIGHT / 1.4)
        self.rect_right.centery = (self.game.WINDOW_HEIGHT / 2) * 1.2

    def draw(self) -> None:
        _ = self.screen.blit(self.image, self.rect)
        _ = self.screen.blit(pygame.transform.flip(
            self.image, True, False), self.rect_right)

    def validate(self) -> None:
        self.selected.func()
