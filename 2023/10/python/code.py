from collections import namedtuple
from sys import argv
from time import time


Point = namedtuple("P", "row col")


def read_input():
    with open(argv[1], "r") as fp:
        return fp.read().split("\n")


def find_start(d: list[list[str]]) -> Point:
    for r in range(len(d)):
        for c in range(len(d[r])):
            if d[r][c] == "S":
                return Point(row=r, col=c)
    return Point(row=-1, col=-1)


def navigate(pipe_map, point, direction):
    if pipe_map[point.row][point.col] == "|" and direction == "U":
        return (Point(row=point.row - 1, col=point.col), "U",)
    elif pipe_map[point.row][point.col] == "|" and direction == "D":
        return (Point(row=point.row + 1, col=point.col), "D",)

    elif pipe_map[point.row][point.col] == "-" and direction == "R":
        return (Point(row=point.row, col=point.col + 1), "R",)
    elif pipe_map[point.row][point.col] == "-" and direction == "L":
        return (Point(row=point.row, col=point.col - 1), "L",)

    elif pipe_map[point.row][point.col] == "F" and direction == "L":
        return (Point(row=point.row + 1, col=point.col), "D",)
    elif pipe_map[point.row][point.col] == "F" and direction == "U":
        return (Point(row=point.row, col=point.col + 1), "R",)

    elif pipe_map[point.row][point.col] == "L" and direction == "D":
        return (Point(row=point.row, col=point.col + 1), "R",)
    elif pipe_map[point.row][point.col] == "L" and direction == "L":
        return (Point(row=point.row - 1, col=point.col), "U",)

    elif pipe_map[point.row][point.col] == "7" and direction == "R":
        return (Point(row=point.row + 1, col=point.col), "D",)
    elif pipe_map[point.row][point.col] == "7" and direction == "U":
        return (Point(row=point.row, col=point.col - 1), "L",)

    elif pipe_map[point.row][point.col] == "J" and direction == "R":
        return (Point(row=point.row - 1, col=point.col), "U",)
    elif pipe_map[point.row][point.col] == "J" and direction == "D":
        return (Point(row=point.row, col=point.col - 1), "L",)

    return Point(row=-777, col=-777)  # Should never return this. Good for debug though.


def part_1(data):
    start_time = time()
    steps = 1
    path = []

    s = find_start(data)
    pipe_piece = Point(row=s.row + 1, col=s.col)
    path.append(s)
    path.append(pipe_piece)
    direction = "D"

    while data[pipe_piece.row][pipe_piece.col] != "S":
        pipe_piece, direction = navigate(data, pipe_piece, direction)
        path.append(pipe_piece)
        steps += 1

    print(f"Part 1: {steps // 2} | Execution time: {time() - start_time}")

    return (get_outline(path), s)


def get_outline(outline_data: list[Point]) -> list[list[str]]:
    grid = []
    for y in range(140):
        row = []
        for x in range(140):
            row.append(".")
        grid.append(row)

    for point in outline_data:
        if data[point.row][point.col] == "S":
            grid[point.row][point.col] = "|"
        else:
            grid[point.row][point.col] = data[point.row][point.col]

    return grid


def part_2(data: list[list[str]], start: Point):
    start_time = time()
    count = 0

    for row in data:
        inside_loop = False
        L_pre_toggle = False
        F_pre_toggle = False
        for point in row:
            if point == "." and inside_loop:
                count += 1
            elif point == "|":
                inside_loop = not inside_loop
            elif point == "L":
                L_pre_toggle = True
            elif point == "F":
                F_pre_toggle = True
            elif point == "7" and L_pre_toggle:
                inside_loop = not inside_loop
                L_pre_toggle = False
            elif point == "J" and F_pre_toggle:
                inside_loop = not inside_loop
                F_pre_toggle = False
            elif point == "7" and F_pre_toggle:
                F_pre_toggle = False
            elif point == "J" and L_pre_toggle:
                L_pre_toggle = False

        # L--7 == toggle
        # L--J == no toggle
        # F--J == toggle
        # F--7 == no toggle

    print(f"Part 2: {count} | Execution time: {time() - start_time}")


if __name__ == "__main__":
    data = read_input()
    # Part 1 correct answer: 6599
    # Part 2 correct answer: 477
    part_2(*part_1(data))