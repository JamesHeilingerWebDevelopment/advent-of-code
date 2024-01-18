from sys import argv
from time import time


def read_input():
    with open(argv[1], "r") as fp:
        return fp.readlines()


def part_1(data):
    start_time = time()
    print(f"Part 1: {None} | Execution time: {time() - start_time}")


def part_2(data):
    start_time = time()
    print(f"Part 2: {None} | Execution time: {time() - start_time}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 
    part_2(data)  # Correct answer: 