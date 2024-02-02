from sys import argv
from time import perf_counter
import typing


Point = typing.NamedTuple("Point", [("x", int), ("y", int)])
Step = typing.NamedTuple("Step", [("direction", str), ("distance", int), ("color", str)])


def read_input():
    data = []
    with open(argv[1], "r") as fp:
        raw_data = fp.read().split("\n")

    for line in raw_data:
        direction, distance, color = line.split()
        data.append(
            Step(direction=direction, distance=int(distance), color=color.strip("(#)"))
        )

    return data


def shoelace_formula(points: list[Point]) -> float:
    total = 0
    for i in range(len(points)):
        if i < len(points) - 1:
            total += points[i+1].x * points[i].y - points[i].x * points[i+1].y
        else:
            total += points[0].x * points[i].y - points[i].x * points[0].y
    return total / 2


def picks_theorem(area, boundary_points):
    return area + (boundary_points / 2) + 1


def part_1_original_solution(data):
    start_time = perf_counter()
    path = []
    current_point = Point(42, 275)
    for line in data:
        if line.direction == "U":
            for _ in range(line.distance):
                current_point = Point(current_point.x, current_point.y - 1)
                path.append(current_point)
        elif line.direction == "D":
            for _ in range(line.distance):
                current_point = Point(current_point.x, current_point.y + 1)
                path.append(current_point)
        elif line.direction == "R":
            for _ in range(line.distance):
                current_point = Point(current_point.x + 1, current_point.y)
                path.append(current_point)
        else:
            for _ in range(line.distance):
                current_point = Point(current_point.x - 1, current_point.y)
                path.append(current_point)

    x = []
    y = []
    plot = []
    for p in path:
        x.append(p.x)
        y.append(p.y)
    for i in range(max(y) + 2):
        plot.append([" " for j in range(max(x) + 1)])
    for point in path:
        plot[point.y][point.x] = "#"

    with open("output.txt", "w") as fh:
        for row in plot:
            fh.write("".join(row))
            fh.write("\n")
    count = 0

    for row in range(len(plot)):
        inside_loop = False
        top_flag = False
        bottom_flag = False

        for col in range(len(plot[row])):
            if plot[row][col] == " " and inside_loop:
                count += 1
                plot[row][col] = "#"
            elif plot[row][col] == " " and not inside_loop:
                top_flag = False
                bottom_flag = False
            elif plot[row][col] == "#" and plot[row - 1][col] == "#" and plot[row + 1][col] == "#":
                inside_loop = not inside_loop
                top_flag = False
                bottom_flag = False
            elif plot[row][col] == "#" and top_flag and plot[row + 1][col] == "#":
                inside_loop = not inside_loop
                top_flag = False
                bottom_flag = False
            elif plot[row][col] == "#" and bottom_flag and plot[row - 1][col] == "#":
                inside_loop = not inside_loop
                top_flag = False
                bottom_flag = False
            elif plot[row][col] == "#" and plot[row - 1][col] == "#":
                top_flag = True
            elif plot[row][col] == "#" and plot[row + 1][col] == "#":
                bottom_flag = True

    print(f"Part 1 (Original): {count + len(path)} | Execution time: {perf_counter() - start_time}")


def part_1(data):
    start_time = perf_counter()
    current_point = Point(0, 0)
    vertices = [current_point]
    perimeter_points = 0

    for step in data:
        perimeter_points += step.distance
        if step.direction == "R":
            current_point = Point(current_point.x + step.distance, current_point.y)
        elif step.direction == "D":
            current_point = Point(current_point.x, current_point.y - step.distance)
        elif step.direction == "L":
            current_point = Point(current_point.x - step.distance, current_point.y)
        else:
            current_point = Point(current_point.x, current_point.y + step.distance)
        vertices.append(current_point)

    print(f"Part 1 (Shoelace + Pick's Theorem): {int(picks_theorem(shoelace_formula(vertices), perimeter_points))} | Execution time: {perf_counter() - start_time}")


def part_2(data):
    start_time = perf_counter()
    current_point = Point(0, 0)
    vertices = [current_point]
    perimeter_points = 0

    for step in data:
        distance = int(step.color[0:5], 16)
        direction = int(step.color[5])
        perimeter_points += distance
        if direction == 0:
            current_point = Point(current_point.x + distance, current_point.y)
        elif direction == 1:
            current_point = Point(current_point.x, current_point.y - distance)
        elif direction == 2:
            current_point = Point(current_point.x - distance, current_point.y)
        else:
            current_point = Point(current_point.x, current_point.y + distance)
        vertices.append(current_point)

    print(f"Part 2: {int(picks_theorem(shoelace_formula(vertices), perimeter_points))} | Execution time: {perf_counter() - start_time}")


if __name__ == "__main__":
    data = read_input()
    part_1_original_solution(data)
    part_1(data)  # Correct answer: 
    part_2(data)  # Correct answer: 