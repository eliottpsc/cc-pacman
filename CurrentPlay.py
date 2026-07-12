from Pac import Pac


class CurrentPlay:
    def __init__(self) -> None:
        self.exists: bool = True
        self.pac: Pac
        self.time_elapsed: int
        self.difficulty: int
        self.level: int
        self.level_seed: int
        self.score: int
        self.lives: int
        self.pellets: list[tuple[int, int]]
        self.power_pellets: list[tuple[int, int]]
        self.ghost_pos: list[tuple[int, int]]
