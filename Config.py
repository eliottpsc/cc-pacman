import sys
from pydantic import BaseModel, Field, model_validator
from typing import Self


class Config(BaseModel):
    """Class to load and validate output settings for the maze generator.
    -- Attributes --
        width:       width of the maze (in cells)
        height:      height of the maze (in cells)
        entry:       coordinates of the starting cell (x, y)
        exit:        coordinates of the exit cell (x, y)
        output_file: file to output a hex representation of the maze to
        perfect:     single spanning tree maze if True
        seed:        used to generate the maze, random if value = None
        display:     method used to display the maze (ASCII or PYGAME)"""
    rawconf: dict[str, str] = {}
    width: int = Field(ge=1, le=100)
    height: int = Field(ge=1, le=100)
    entry: tuple[int, int]
    exit: tuple[int, int]
    output_file: str
    perfect: bool
    seed: int | None
    display: str

    @model_validator(mode='after')
    def validate_ent_ex(self) -> Self:
        """Validate the config file's data.
        Return: self"""
        if self.entry == self.exit:
            raise ValueError('entry and exit must be different')
        if self.entry[0] < 0 or self.entry[0] >= self.width:
            raise ValueError(
                f'entry x={self.entry[0]} out of range [0, {self.width})')
        if self.entry[1] < 0 or self.entry[1] >= self.height:
            raise ValueError(
                f'entry y={self.entry[1]} out of range [0, {self.height})')

        if self.exit[0] < 0 or self.exit[0] >= self.width:
            raise ValueError(
                f'exit x={self.exit[0]} out of range [0, {self.width})')
        if self.exit[1] < 0 or self.exit[1] >= self.height:
            raise ValueError(
                f'exit y={self.exit[1]} out of range [0, {self.height})')
        return self

    @classmethod
    def load(cls) -> Self:
        """Read, format and type the config data and returns it.
        Return: a Config object whose attributes contain the config data"""
        rawconf = {}
        with open(sys.argv[1]) as file:
            for line in file:
                if line[0] != '#' and '=' in line:
                    s = line.split('=')
                    rawconf[s[0]] = s[1].strip()

        return cls(
            width=int(rawconf['WIDTH']),
            height=int(rawconf['HEIGHT']),
            entry=(int(rawconf['ENTRY'].split(',')[0]),
                   int(rawconf['ENTRY'].split(',')[1])),
            exit=(int(rawconf['EXIT'].split(',')[0]),
                  int(rawconf['EXIT'].split(',')[1])),
            output_file=rawconf['OUTPUT_FILE'],
            perfect=rawconf['PERFECT'] == 'True',
            seed=int(rawconf['SEED']) if rawconf['SEED'] else None,
            display=rawconf['DISPLAY']
        )
