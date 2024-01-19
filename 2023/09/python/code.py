from sys import argv
from time import time


def read_input():
    with open(argv[1], "r") as fp:
        return fp.read().split("\n")


def reduce_down(seq: list[int]) -> int:
    new_seq = []

    for i in range(1, len(seq)):
        new_seq.append(seq[i] - seq[i - 1])

    if not any(new_seq):
        return seq[-1]
    else:
        return seq[-1] + reduce_down(new_seq)


def part_1(data):
    start_time = time()
    total = 0

    for line in data:
        total += reduce_down([int(x) for x in line.split()])

    print(f"Part 1: {total} | Execution time: {time() - start_time}")


def reduce_down_and_back(seq: list[int]) -> int:
    new_seq = []

    for i in range(1, len(seq)):
        new_seq.append(seq[i] - seq[i - 1])

    if not any(new_seq):
        return seq[0]
    else:
        n = reduce_down_and_back(new_seq)
        return seq[0] - n


def part_2(data):
    start_time = time()
    total = 0

    for line in data:
        val = reduce_down_and_back([int(x) for x in line.split()])
        total += val

    print(f"Part 2: {total} | Execution time: {time() - start_time}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 2105961943
    part_2(data)  # Correct answer: 1019