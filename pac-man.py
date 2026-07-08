from time import sleep
import pygame

from Config import Config
from Game import Game

if __name__ == '__main__':
    # conf = Config.load()
    # game = Game(
    #     pygame.display.set_mode((600, 600)),
    #     Config.load()
    # )
    game = Game.create()
    sleep(1)
    game.level_loop()
