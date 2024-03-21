from sys import argv


def read_input():
    with open(argv[1], "r") as fp:
        return fp.readlines()


def part_1(data):
    horizontal = 0
    depth = 0
    for instruction in data:
        direction, unit = instruction.split()
        if direction == "forward":
            horizontal += int(unit)
        elif direction == "down":
            depth += int(unit)
        elif direction == "up":
            depth -= int(unit)
    print("Horizontal =", horizontal)
    print("Depth =", depth)
    print(f"Part 1: {horizontal * depth}")


def part_2(data):
    horizontal = 0
    depth = 0
    aim = 0
    for instruction in data:
        direction, unit = instruction.split()
        if direction == "forward":
            horizontal += int(unit)
            depth += aim * int(unit)
        elif direction == "down":
            aim += int(unit)
        elif direction == "up":
            aim -= int(unit)
    print(f"Part 2: {horizontal * depth}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 1604850
    part_2(data)  # Correct answer: 1685186100