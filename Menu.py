import pygame
from Button import Button


class Menu:
    def __init__(self, game) -> None:
        self.screen: pygame.Surface = game.screen
        self.width: float = game.WINDOW_WIDTH
        self.height: float = game.WINDOW_HEIGHT
        self.rect: pygame.Rect = pygame.Rect(0, 0, self.width, self.height)
        self.game = game
        self.buttons: dict[str, Button] = {}
        self.running: bool = True

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
        title = Button(self.rect.centerx, self.rect.centery / 2,
                       pygame.image.load('assets/title.png'), 2.2)
        self.buttons['title'] = title
        if self.game.current_play is True:
            continu = Button(self.rect.centerx, self.rect.centery,
                             pygame.image.load('assets/continue.png'), 1)
            self.buttons['continue'] = continu
        start = Button(self.rect.centerx, self.rect.centery * 1.2,
                       pygame.image.load('assets/start.png'), 1)
        self.buttons['start'] = start
        settings = Button(self.rect.centerx, self.rect.centery * 1.4,
                          pygame.image.load('assets/settings.png'), 1)
        self.buttons['settings'] = settings
        highscores = Button(self.rect.centerx, self.rect.centery * 1.6,
                            pygame.image.load('assets/highscores.png'), 1)
        self.buttons['highscores'] = highscores
        quit = Button(self.rect.centerx, self.rect.centery * 1.8,
                      pygame.image.load('assets/quit.png'), 1)
        self.buttons['quit'] = quit

        for button in self.buttons:
            self.buttons[button].draw(self.screen)

    def get_event(self) -> None:
        self.buttons['title'].get_click(self.game, lambda: 1)
        if self.game.current_play is True:
            self.buttons['continue'].get_click(self.game, lambda: setattr(self, 'running', False))
        self.buttons['start'].get_click(self.game, self.game.level_loop)
        self.buttons['settings'].get_click(self.game, lambda: 1)
        self.buttons['highscores'].get_click(self.game, lambda: 1)
        self.buttons['quit'].get_click(self.game, pygame.quit)

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
