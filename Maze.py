import pygame

class Maze():
    """Handle loading and drawing of the maze"""
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.color: tuple[int, int, int] = (255, 0, 0)
        self.maze = self.load()

    def load(self) -> list[list[str]]:
        mazefile = open('mazefile', 'r')
        raw: list[list[str]] = []
        for row in range(self.game.conf.height):
            raw.append([])
            for col in range(self.game.conf.width + 1): # +1 to account for '\n'
                if col == self.game.conf.width:
                    _ = mazefile.read(1) # skip '\n'
                else:
                    raw[row].append(mazefile.read(1))
        return raw

    def draw_cell(self, cell: str, y: int, x: int) -> None:
        """Shape a single cell of the maze and displays it in the pygame
        display.
        -- Arguments --
            cell: the hex character encoding the walls in the cell, a string
            y: the y coordinate of the cell in the grid, an int
            x: the x coordinate of the cell in the grid, an int"""
        blocksize = int(self.game.WINDOW_WIDTH / self.game.conf.width)
        edgeN = pygame.Rect((x * blocksize), (y * blocksize), blocksize, 2)
        edgeE = pygame.Rect((x * blocksize) + (blocksize - 2),
                            (y * blocksize), 2, blocksize)
        edgeS = pygame.Rect((x * blocksize),
                            (y * blocksize) + (blocksize - 2), blocksize, 2)
        edgeW = pygame.Rect((x * blocksize), (y * blocksize), 2, blocksize)

        if int(format(int(cell, 16), '04b')[3]):
            _ = pygame.draw.rect(self.screen, self.color, edgeN, 4)
        if int(format(int(cell, 16), '04b')[2]):
            _ = pygame.draw.rect(self.screen, self.color, edgeE, 4)
        if int(format(int(cell, 16), '04b')[1]):
            _ = pygame.draw.rect(self.screen, self.color, edgeS, 4)
        if int(format(int(cell, 16), '04b')[0]):
            _ = pygame.draw.rect(self.screen, self.color, edgeW, 4)

    def draw_grid(self) -> None:
        """Calls Display.draw_cell() method on every cell of the maze."""
        for x, row in enumerate(self.maze):
            for y, cell in enumerate(row):
                self.draw_cell(cell, x, y)
