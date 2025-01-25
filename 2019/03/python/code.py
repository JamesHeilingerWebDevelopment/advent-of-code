from sys import argv
from collections import namedtuple


Point = namedtuple("Point", "x y")


def read_input():
    with open(argv[1], "r") as fp:
        return fp.readlines()


def get_wire_path(path):
    wire_points = set()
    directions = path.split(",")
    x = 0
    y = 0
    for instruction in directions:
        direction = instruction[0]
        distance = int(instruction[1:])
        for _ in range(distance):
            if direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            elif direction == "U":
                y += 1
            elif direction == "D":
                y -= 1
            wire_points.add(Point(x, y))

    return wire_points


def get_wire_paths(paths):
    wire_paths = []

    for path in paths:
        wire_paths.append(get_wire_path(path))

    return wire_paths


def find_crossings(wire_points):
    crossings = set()
    for point in wire_points[0]:
        if point in wire_points[1]:
            crossings.add(point)

    return crossings


def manhattan_distance(p1: Point, p2: Point) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def find_shortest_manhattan_distance(crossing_list):
    data_port = Point(0, 0)
    shortest_distance = 1000000000
    for point in crossing_list:
        man_dist = manhattan_distance(data_port, point)
        if man_dist < shortest_distance:
            shortest_distance = man_dist

    return shortest_distance


def compute_wire_length_to_point(crossing, wire_path):
    length = 0
    final_length = 0
    directions = wire_path.split(",")
    x = 0
    y = 0
    for instruction in directions:
        direction = instruction[0]
        distance = int(instruction[1:])
        for _ in range(distance):
            length += 1
            if direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            elif direction == "U":
                y += 1
            elif direction == "D":
                y -= 1

            if crossing == Point(x, y):
                final_length = length
                break

    return final_length


def find_shortest_wire_distance_to_crossing(crossing_list, wire_paths):
    shortest_distance = 1000000000
    for crossing in crossing_list:
        distance = 0
        for wire_path in wire_paths:
            distance += compute_wire_length_to_point(crossing, wire_path)

        if distance < shortest_distance:
            shortest_distance = distance

    return shortest_distance


def part_1(data):
    print(f"Part 1: {find_shortest_manhattan_distance(find_crossings(get_wire_paths(data)))}")


def part_2(data):
    print(f"Part 2: {find_shortest_wire_distance_to_crossing(find_crossings(get_wire_paths(data)), data,)}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 1337
    part_2(data)  # Correct answer: 65356