import json
from typing import Any
import pygame


class Highscores():
    def __init__(self, game) -> None:
        self.game = game
        self.hs_file = 'highscores'
        self.scores = self.load()
        self.input = 'DEFAULT'
        self.input_isactive = True
        self.running = True
        self.rect: pygame.Rect = pygame.Rect(0, 0, self.game.WINDOW_WIDTH,
                                             self.game.WINDOW_HEIGHT)

    def load(self) -> Any:
        with open(self.hs_file, 'r') as f:
            return json.load(f)

    def save_new(self, name: str, score: int) -> None:
        self.scores[name] = score
        with open(self.hs_file, 'w') as f:
            json.dump(self.scores, f)

    def input_name(self, events: list[Any]) -> None:
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.input_isactive = False
                elif event.key == pygame.K_BACKSPACE:
                    self.input = self.input[:-1]
                else:
                    self.input += event.unicode

    def draw_input_box(self) -> None:
        color = (0, 0, 0)
        font = pygame.font.SysFont('comicsans', 40)
        img = font.render(self.input, True, color)
        box = img.get_rect()
        box.center = (int(self.game.WINDOW_WIDTH / 2),
                      int(self.game.WINDOW_HEIGHT / 2))
        # box = pygame.Rect(50, 50, 200, 50)
        self.game.screen.blit(img, box)

    def display(self) -> None:
        self.game.screen.fill((0, 255, 0), self.rect)
        title = pygame.transform.scale(
            pygame.image.load('assets/highscores.png'), (640, 128))
        title_rect = title.get_rect()
        title_rect.centerx = self.game.WINDOW_WIDTH / 2
        title_rect.centery = self.game.WINDOW_WIDTH / 4
        _ = self.game.screen.blit(title, title_rect)


# class InputBox(pygame.sprite.Sprite):
#     def __init__(self) -> None:
#         super().__init__()
#         self.isactive = True
#         self.color = (255, 255, 255)
#         self.background = None
#         self.pos = (50, 50)
#         self.width = 100
#         self.font = pygame.font.SysFont('comicsans', 40)
#         self.text = ''
#         self.render_text()

#     def update(self):
#         self.render_text()

#     def render_text(self):
#         t_surf = self.font.render(self.text, True,
#                                   self.color, self.background)
#         self.image = pygame.Surface(
#             (max(self.width, t_surf.get_width()+10),
#              t_surf.get_height()+10), pygame.SRCALPHA)
#         if self.background:
#             self.image.fill(self.background)
#         self.image.blit(t_surf, (5, 5))
#         pygame.draw.rect(self.image, self.color,
#                          self.image.get_rect().inflate(-2, -2), 2)
#         self.rect = self.image.get_rect(topleft=self.pos)
