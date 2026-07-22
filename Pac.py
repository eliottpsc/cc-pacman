import pygame
from itertools import cycle
from Entity import Entity
from pygame.sprite import Sprite
from Spritesheet import Spritesheet


class Pac(Entity, Sprite):
    def __init__(self, game, maze) -> None:
        super().__init__(game, maze)
        self.ss = Spritesheet("assets/pacman.png")
        self.images = cycle(self.ss.images_at([
            (0, 284, 196, 196),
            (233, 284, 196, 196),
            (465, 284, 196, 196),
            (233, 284, 196, 196),
            ]))
        self.image = next(self.images)
        #self.image = pygame.image.load("assets/pac.png")
        #self.image = pygame.transform.scale(self.image, (self.tile_size * 0.75,)*2)

    def choose_direction(self, keys):
        if keys[pygame.K_LEFT]:
            return (0, -1)
        if keys[pygame.K_RIGHT]:
            return (0, 1)
        if keys[pygame.K_UP]:
            return (-1, 0)
        if keys[pygame.K_DOWN]:
            return (1, 0)
        return self.next_dir

    def update(self, keys, dt):
        self.next_dir = self.choose_direction(keys)
        if keys[pygame.K_ESCAPE]:
            self.game.menu_loop()

        if (not self.can_move(self.direction)
            and all(p % self.tile_size == 0 for p in self.pixel)):
            self.move_timer = self.move_delay
        self.move(dt)

        tx, ty = self.pos[0] * self.tile_size, self.pos[1] * self.tile_size
        dx, dy = tx - self.pixel[0], ty - self.pixel[1]
        sign = ((dx > 0) - (dx < 0), (dy > 0) - (dy < 0))
        step = self.speed * dt
        self.pixel = (
                tx if abs(dx) < step else self.pixel[0] + step * sign[0],
                ty if abs(dy) < step else self.pixel[1] + step * sign[1],
                )

        rot = {(0, -1): 180, (0, 1): 0, (-1, 0): 90, (1, 0): 270}

        self.anim_timer += dt
        if self.anim_timer >= self.anim_delay:
            self.anim_timer = 0
            self.image = next(self.images)

        image = pygame.transform.rotate(self.image, rot[self.direction])
        image = pygame.transform.scale(image, (self.tile_size * 0.75,)*2)

        self.rect = pygame.Rect(self.pixel[1], self.pixel[0], *(self.tile_size * 0.75,)*2)
        self.screen.blit(image, self.rect)
