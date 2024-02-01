from sys import argv
from time import time


def read_input():
    with open(argv[1], "r") as fp:
        return fp.read().split("\n")


def find_winning_combos(time, distance) -> int:
    for x in range(1, time):
        if (time - x) * x > distance:
            return time - x - x + 1
    return 1


def part_1():
    start_time = time()
    total = 1
    data = ((47, 282,), (70, 1079,), (75, 1147,), (66, 1062,),)

    for t in data:
        total *= find_winning_combos(t[0], t[1])

    print(f"Part 1: {total} | Execution time: {time() - start_time}")


def part_2():
    start_time = time()
    total = 1
    data = ((47707566, 282107911471062,),)

    for t in data:
        total *= find_winning_combos(t[0], t[1])

    print(f"Part 2: {total} | Execution time: {time() - start_time}")


if __name__ == "__main__":
    # data = read_input()
    # Finish this day by adding input parsing (currently hardcoded)
    part_1()  # Correct answer: 281600
    part_2()  # Correct answer: 33875953