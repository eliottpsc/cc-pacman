import pygame
from Entity import Entity


class Pac(Entity):
    def __init__(self, game, maze) -> None:
        super().__init__(game, maze)
        self.image = pygame.image.load("assets/pac.png")
        self.image = pygame.transform.scale(self.image, (50, 50))

    def choose_direction(self, keys):
        if keys[pygame.K_LEFT]:
            return (0, -1)
        if keys[pygame.K_RIGHT]:
            return (0, 1)
        if keys[pygame.K_UP]:
            return (-1, 0)
        if keys[pygame.K_DOWN]:
            return (1, 0)
        return self.direction

    def update(self, keys, dt):
        new_dir = self.choose_direction(keys)
        if keys[pygame.K_ESCAPE]:
            self.game.menu_loop()

        self.move(new_dir, dt)

        tx, ty = self.pos[0] * self.tile_size, self.pos[1] * self.tile_size
        dx, dy = tx - self.pixel[0], ty - self.pixel[1]
        sign = ((dx > 0) - (dx < 0), (dy > 0) - (dy < 0))
        step = self.speed * dt
        self.pixel = (
                tx if abs(dx) < step else self.pixel[0] + step * sign[0],
                ty if abs(dy) < step else self.pixel[1] + step * sign[1],
                )

        rot = {(0, -1): 0, (0, 1): 180, (-1, 0): 270, (1, 0): 90}
        image = pygame.transform.rotate(self.image, rot[self.direction])
        self.rect = pygame.Rect(self.pixel[1], self.pixel[0], 50, 50)
        self.screen.blit(image, self.rect)
