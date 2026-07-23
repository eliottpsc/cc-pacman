from typing import Any


class CurrentPlay:
    def __init__(self, game) -> None:
        self.game = game
        self.exists: bool = True
        self.time_elapsed: int
        self.difficulty: int
        self.level_num: int = 0
        self.level_seed: int = 0
        self.score: int = 0
        self.lives: int = 5
        self.pellets: list[tuple[int, int]]
        self.power_pellets: list[tuple[int, int]]
        self.ghost_pos: list[tuple[int, int]]
        self.level: Any
        self.gen_level()

    def gen_level(self) -> None:
        """TODO: should generate a level with characteristics depending on
        which level_num we are at"""
        from Level import Level
        self.level = Level(self)
        entry = (0, 0)
        exit = (10, 10)
        size = (20 - self.level_num, 20 - self.level_num)
        self.level.maze = self.level.generate(self.level_seed,
                                              entry, exit, size)
