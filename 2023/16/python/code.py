from dataclasses import dataclass
from sys import argv
from time import time
from typing import NamedTuple


Location = NamedTuple("Loc", [("row", int), ("col", int)])


@dataclass
class Beam:
    location: Location
    direction: str


@dataclass
class Tile:
    type: str
    up: bool
    down: bool
    left: bool
    right: bool


class Contraption:
    def __init__(self) -> None:
        self.contraption = self.create_contraption()
        self.max_row = self._highest_row()
        self.max_col = self._highest_column()
        self.energized_tiles = set()
        self.mirror_lut = {
            "/": {
                "U": "R",
                "D": "L",
                "L": "D",
                "R": "U"
            },
            "\\": {
                "U": "L",
                "D": "R",
                "L": "U",
                "R": "D"
            }
        }

    def create_contraption(self):
        with open(argv[1], "r") as fp:
            data = fp.read().split("\n")

        graph = []
        for line in data:
            graph.append([Tile(x, False, False, False, False) for x in line])

        return graph

    def update_beam(self, beam: Beam):
        self.energized_tiles.add(beam.location)
        tile = self.contraption[beam.location.row][beam.location.col]

        if beam.direction == "U" and not tile.up or beam.direction == "D" and not tile.down or beam.direction == "L" and not tile.left or beam.direction == "R" and not tile.right:
            if tile.type in ["/", "\\"]:
                beam.direction = self.mirror_lut[tile.type][beam.direction]
                return self._update_location(beam), None
            elif tile.type in ["-", "|"]:
                return self._split_beam(beam, tile)
            else:
                return self._update_location(beam), None
        else:
            return None, None

    def _highest_row(self):
        """Return the highest row."""
        return len(self.contraption[0])

    def _highest_column(self):
        """Return the highest column."""
        return len(self.contraption)

    def _update_location(self, beam: Beam):
        if beam.direction == "U":
            if beam.location.row - 1 < 0:
                return None
            else:
                return Beam(Location(beam.location.row - 1, beam.location.col), direction=beam.direction)
        elif beam.direction == "D":
            if beam.location.row + 1 >= self.max_row:
                return None
            else:
                return Beam(Location(beam.location.row + 1, beam.location.col), direction=beam.direction)
        elif beam.direction == "L":
            if beam.location.col - 1 < 0:
                return None
            else:
                return Beam(Location(beam.location.row, beam.location.col - 1), direction=beam.direction)
        else:
            if beam.location.col + 1 >= self.max_col:
                return None
            else:
                return Beam(Location(beam.location.row, beam.location.col + 1), direction=beam.direction)

    def _split_beam(self, beam: Beam, tile: Tile):
        if tile.type == "-":
            if beam.direction in ["U", "D"]:
                beam1 = Beam(beam.location, "R")
                beam2 = Beam(beam.location, "L")
                tile.up = True
                tile.down = True
                tile.left = True
                tile.right = True
                return self._update_location(beam1), self._update_location(beam2)
            else:
                if beam.direction == "U":
                    tile.up = True
                else:
                    tile.down = True
                return self._update_location(beam), None
        elif tile.type == "|":
            if beam.direction in ["L", "R"]:
                beam1 = Beam(beam.location, "U")
                beam2 = Beam(beam.location, "D")
                tile.up = True
                tile.down = True
                tile.left = True
                tile.right = True
                return self._update_location(beam1), self._update_location(beam2)
            else:
                if beam.direction == "L":
                    tile.left = True
                else:
                    tile.right = True
                return self._update_location(beam), None
        else:
            if beam.direction == "U":
                tile.up = True
            elif beam.direction == "D":
                tile.down = True
            elif beam.direction == "L":
                tile.left = True
            else:
                tile.right = True
            return self._update_location(beam), None


def create_starting_beam_list(contraption: Contraption) -> list[Beam]:
    starters = []

    # Down and up beams
    for x in range(contraption.max_col):
        starters.append(Beam(Location(0, x), "D"))
        starters.append(Beam(Location(contraption.max_row - 1, x), "U"))

    # Left and right beams
    for y in range(contraption.max_row):
        starters.append(Beam(Location(y, contraption.max_col - 1), "L"))
        starters.append(Beam(Location(y, 0), "R"))

    return starters


def part_1(contraption: Contraption, starting_beam: Beam) -> int:
    beams = [starting_beam]
    while len(beams) > 0:
        beam1, beam2 = contraption.update_beam(beams[0])
        beams = beams[1:]
        if beam1 is not None:
            beams.append(beam1)
        if beam2 is not None:
            beams.append(beam2)
    return len(contraption.energized_tiles)


def part_2():
    results = []
    starting_beam_list = create_starting_beam_list(contraption)
    for beam in starting_beam_list:
        results.append(part_1(Contraption(), beam))
    return max(results)


if __name__ == "__main__":
    start_time = time()
    contraption = Contraption()
    print(f"Part 1: {part_1(contraption, Beam(Location(0, 0), 'R'))} | Execution time: {time() - start_time}")  # Correct answer: 6605
    second_start_time = time()
    print(f"Part 2: {part_2()} | Execution time: {time() - second_start_time}")  # Correct answer: 6766
