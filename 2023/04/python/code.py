from sys import argv
from time import time


def read_input():
    with open(argv[1], "r") as fp:
        return fp.read().split("\n")


def overlap(card: str) -> int:
    _, numbers = card.split(": ")
    left_side, right_side = numbers.split(" | ")
    return len(set.intersection(set(left_side.split()), set(right_side.split())))


def part_1_scoring(intersection_length: int) -> int:
    if intersection_length == 0:
        card_score = 0
    elif intersection_length == 1:
        card_score = 1
    else:
        card_score = 1 << (intersection_length - 1)
    return card_score


def part_1(data):
    start_time = time()
    total = 0

    for line in data:
        total += part_1_scoring(overlap(line))

    print(f"Part 1: {total} | Execution time: {time() - start_time}")


def recurse(index_set: list[int], full_dataset: list[str]) -> int:
    total = 0
    for idx in index_set:
        total += 1
        new_index_set = [x for x in range(idx + 1, idx + overlap(full_dataset[idx]) + 1)]
        if new_index_set:
            total += recurse(new_index_set, full_dataset)

    return total


def part_2(data):
    start_time = time()
    print(f"Part 2: {recurse([x for x in range(len(data))], data)} | Execution time: {time() - start_time}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 26914
    part_2(data)  # Correct answer: 13080971