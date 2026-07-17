import pygame
from Entity import Entity


class Pac(Entity):
    def __init__(self, game, maze) -> None:
        super().__init__(game, maze)
        self.image = pygame.image.load("assets/pac.png")
        self.image = pygame.transform.scale(self.image, (50, 50))

    def update(self, keys, dt):
        new_dir = self.direction
        image = self.image
        if keys[pygame.K_LEFT]:
            new_dir = (0, -1)
        if keys[pygame.K_RIGHT]:
            new_dir = (0, 1)
        if keys[pygame.K_UP]:
            new_dir = (-1, 0)
        if keys[pygame.K_DOWN]:
            new_dir = (1, 0)
        if keys[pygame.K_ESCAPE]:
            self.game.menu_loop()

        self.move_timer += dt
        if self.move_timer >= self.move_delay:
            if self.can_move(new_dir):
                self.move_timer = 0
                self.direction = new_dir
                self.pos = (self.pos[0] + self.direction[0],
                            self.pos[1] + self.direction[1])

        rot = {(0, -1): 0, (0, 1): 180, (-1, 0): 270, (1, 0): 90}
        image = pygame.transform.rotate(self.image, rot[self.direction])

        blocksize = self.game.WINDOW_WIDTH // self.game.conf.width
        self.rect = pygame.Rect(self.pos[1] * blocksize,
                                self.pos[0] * blocksize,
                                50, 50)
        self.screen.blit(image, self.rect)
#       pygame.draw.rect(self.screen, (220, 200, 0), self.rect, 10)
