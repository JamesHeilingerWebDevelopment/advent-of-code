from collections import namedtuple
import re
from sys import argv
from time import time


Point = namedtuple("P", "x y")


def read_input():
    with open(argv[1], "r") as fp:
        return fp.read().split("\n")


def find_galaxy_locations(universe: list[str]) -> list[Point]:
    galaxy_locations = []

    for i in range(len(universe)):
        galaxy_locations.extend(
            Point(x=j, y=i)
            for j in [k for k in range(len(universe[i])) if universe[i][k] == "#"]
        )

    return galaxy_locations


def make_unique_pairs(locations: list[Point]) -> list[Point]:
    pairs = []
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            pairs.append(
                (locations[i], locations[j],)
            )
    return pairs


def find_empty_rows(data: list[str]) -> list[int]:
    empty_rows = []
    for i in range(len(data)):
        if "#" not in data[i]:
            empty_rows.append(i)
    return empty_rows


def find_empty_columns(data: list[str]) -> list[int]:
    empty_columns = []
    for idx in range(len(data[0])):
        temp_string = ""
        for row in data:
            temp_string += row[idx]
        if "#" not in temp_string:
            empty_columns.append(idx)
    return empty_columns


def compute_distance(p0: Point, p1: Point, rows: list[int], cols: list[int], multiplier: int) -> int:
    row_count = 0
    col_count = 0

    if p0.y <= p1.y:
        for row in rows:
            if row > p0.y and row < p1.y:
                row_count += 1
    else:
        for row in rows:
            if row > p1.y and row < p0.y:
                row_count += 1

    if p0.x <= p1.x:
        for col in cols:
            if col > p0.x and col < p1.x:
                col_count += 1
    else:
        for col in cols:
            if col > p1.x and col < p0.x:
                col_count += 1

    return abs(p0.x - p1.x) + abs(p0.y - p1.y) + (col_count * (multiplier - 1)) + (row_count * (multiplier - 1))


def find_shortest_paths_between_galaxies(universe: list[str], multiplier: int) -> int:
    total = 0

    empty_rows = find_empty_rows(universe)
    empty_columns = find_empty_columns(universe)
    galaxy_locations = find_galaxy_locations(universe)
    galaxy_pairs = make_unique_pairs(galaxy_locations)

    for pair in galaxy_pairs:
        total += compute_distance(*pair, empty_rows, empty_columns, multiplier)

    return total


def part_1(data):
    start_time = time()
    print(f"Part 1: {find_shortest_paths_between_galaxies(data, 2)} | Execution time: {time() - start_time}")


def part_2(data):
    start_time = time()
    print(f"Part 2: {find_shortest_paths_between_galaxies(data, 1000000)} | Execution time: {time() - start_time}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 9918828
    part_2(data)  # Correct answer: 692506533832
