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
        self.title = Button('title', self.rect.centerx, self.rect.centery / 2,
                            pygame.image.load('assets/title.png'),
                            2.2, lambda: 1)
        self.buttons.append(self.title)
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

    def draw_text(self, text: str, font: pygame.font.Font,
                  color: tuple[int, int, int], x: float, y: float) -> None:
        img = font.render(text, True, color)
        text_rect = img.get_rect()
        text_rect.center = (int(x), int(y))
        self.screen.blit(img, text_rect)

    def draw(self) -> None:
        self.screen.fill((255, 0, 255), self.rect)

        # TEXT
        self.draw_text("WOW KILLER",
                       pygame.font.SysFont('comicsans', 40),
                       (0, 255, 0), self.width / 2, self.height / 6)

        self.draw_text("by lgrosse and eruffin",
                       pygame.font.SysFont('comicsans', 20),
                       (0, 0, 255), 75, self.game.WINDOW_HEIGHT - 15)

        # BUTTONS
        for button in self.buttons:
            button.draw(self.screen)

    def get_event(self) -> None:
        for button in self.buttons:
            button.get_click(self.game, button.func)

    def update(self) -> None:
        ...


class MenuSelector():
    def __init__(self, game) -> None:
        self.game = game
        self.screen = game.screen
        self.selected: Button
        self.image = pygame.transform.scale(
            pygame.image.load('assets/menu-select.png'),
            (40, 40))
        self.rect = self.image.get_rect()
        self.rect.centerx = (self.game.WINDOW_HEIGHT / 3.4)
        self.rect.centery = (self.game.WINDOW_HEIGHT / 2) * 1.2
        self.rect_right = self.image.get_rect()
        self.rect_right.centerx = (self.game.WINDOW_HEIGHT / 1.4)
        self.rect_right.centery = (self.game.WINDOW_HEIGHT / 2) * 1.2
