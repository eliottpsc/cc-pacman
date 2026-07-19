import json
from typing import Any
import pygame


class Highscores():
    def __init__(self, game) -> None:
        self.game = game
        self.hs_file = 'highscores'
        self.scores = self.load()
        self.input = ''
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

    def input_name(self, events: list[Any], score: int) -> None:
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.save_new(self.input, score)
                    self.input_isactive = False
                    self.game.current_play = False
                elif event.key == pygame.K_BACKSPACE:
                    self.input = self.input[:-1]
                else:
                    self.input += event.unicode

    def draw_input_box(self, score: int) -> None:
        score_font = pygame.font.SysFont('comicsans', 100)
        score_img = score_font.render(f'SCORE: {score}', True, (255, 255, 0))
        score_box = score_img.get_rect()
        score_box.center = (int(self.game.WINDOW_WIDTH / 2),
                            int(self.game.WINDOW_HEIGHT / 5))
        self.game.screen.blit(score_img, score_box)

        prompt_font = pygame.font.SysFont('comicsans', 30)
        prompt_img = prompt_font.render('ENTER YOUR NAME:', True,
                                        (100, 100, 100))
        prompt_box = prompt_img.get_rect()
        prompt_box.center = (int(self.game.WINDOW_WIDTH / 2),
                             int(self.game.WINDOW_HEIGHT / 3))
        self.game.screen.blit(prompt_img, prompt_box)

        font = pygame.font.SysFont('comicsans', 40)
        img = font.render(self.input, True, (255, 255, 255))
        box = img.get_rect()
        box.center = (int(self.game.WINDOW_WIDTH / 2),
                      int(self.game.WINDOW_HEIGHT / 2))
        self.game.screen.blit(img, box)

    def display(self) -> None:
        # BACKGROUND
        self.game.screen.fill((0, 255, 0), self.rect)
        ml = pygame.transform.scale(
            pygame.image.load('assets/moumou-pedestal-l.png'), (244, 600))
        ml_rect = ml.get_rect()
        ml_rect.centerx = 130
        ml_rect.centery = self.game.WINDOW_HEIGHT - 400
        mr = pygame.transform.scale(
            pygame.image.load('assets/moumou-pedestal-r.png'), (244, 600))
        mr_rect = mr.get_rect()
        mr_rect.centerx = self.game.WINDOW_WIDTH - 130
        mr_rect.centery = self.game.WINDOW_HEIGHT - 400
        # TITLE
        title = pygame.transform.scale(
            pygame.image.load('assets/highscores.png'), (640, 128))
        title_rect = title.get_rect()
        title_rect.centerx = self.game.WINDOW_WIDTH / 2
        title_rect.centery = self.game.WINDOW_HEIGHT / 4
        # SCORE PANNEL
        scores_surf = pygame.Surface(
            (self.game.WINDOW_WIDTH / 2, self.game.WINDOW_HEIGHT / 2),
            pygame.SRCALPHA)
        pygame.draw.rect(scores_surf, (0, 0, 0, 128), scores_surf.get_rect())
        scores_rect = scores_surf.get_rect(
            centerx=self.game.WINDOW_WIDTH / 2,
            centery=self.game.WINDOW_HEIGHT / 1.5
        )
        # SCORES
        self.draw_score_boxes(scores_surf)

        self.game.screen.blit(title, title_rect)
        self.game.screen.blit(ml, ml_rect)
        self.game.screen.blit(mr, mr_rect)
        self.game.screen.blit(scores_surf, scores_rect)

    def draw_score_boxes(self, surf: pygame.Surface) -> None:
        color = (255, 0, 0)
        font = pygame.font.SysFont('comicsans', 60)
        dy = 0
        for score in sorted(self.scores, key=lambda s: self.scores[s],
                            reverse=True):
            text = f'{score}                {self.scores[score]}'
            img = font.render(text, True, color)
            x = int(self.game.WINDOW_WIDTH / 2)
            y = int(self.game.WINDOW_HEIGHT / 2)
            box = img.get_rect()
            box.center = (x, y + dy)
            dy += 70
            self.game.screen.blit(img, box)
