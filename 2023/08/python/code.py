from functools import reduce
import re
from sys import argv
from time import time


def read_input():
    with open(argv[1], "r") as fp:
        return fp.read()


def parse_input(data: str) -> tuple[str, dict]:
    node_map = {}
    directions, raw_nodes = data.split("\n\n")

    raw_nodes = raw_nodes.split("\n")
    for raw_node in raw_nodes:
        source, destinations = raw_node.split(" = ")
        left, right = destinations.strip("()").split(", ")
        node_map[source] = (left, right,)

    return directions, node_map


def direction_generator(direction_stream: str) -> int:
    while True:
        for direction in direction_stream:
            if direction == "L":
                yield 0
            else:
                yield 1


def part_1(directions, node_map):
    start_time = time()
    count = 0
    node = "AAA"

    for direction in direction_generator(directions):
        count += 1
        node = node_map[node][direction]
        if node == "ZZZ":
            break

    print(f"Part 1: {count} | Execution time: {time() - start_time}")


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)


def lcmm(*args):
    """Return LCM of args."""
    return reduce(lcm, args)


def part_2(directions, node_map):
    start_time = time()
    count = 0
    cycle_lengths = []

    starting_nodes = [n for n in node_map if re.match(r"..A", n)]

    for node in starting_nodes:
        direction_gen = direction_generator(directions)
        cycle_nodes = []
        count = 0

        while count <= 1:
            node = node_map[node][next(direction_gen)]
            if count == 1:
                cycle_nodes.append(node)
            if re.match(r"..Z", node):
                count += 1

        cycle_lengths.append(len(cycle_nodes))

    print(f"Part 2: {lcmm(*cycle_lengths)} | Execution time: {time() - start_time}")


if __name__ == "__main__":
    direction_sequence, nodes = parse_input(read_input())
    part_1(direction_sequence, nodes)  # Correct answer: 18827
    part_2(direction_sequence, nodes)  # Correct answer: 20220305520997