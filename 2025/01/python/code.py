from functools import wraps
from sys import argv
from time import perf_counter


def execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        time_start = perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {result} | Execution time: {perf_counter() - time_start}")
        return result
    return wrapper


def read_input():
    with open(argv[1], "r") as fp:
        lines = fp.readlines()

    first_column = []
    second_column = []
    for line in lines:
        a, b = line.split()
        first_column.append(int(a))
        second_column.append(int(b))

    return first_column, second_column


@execution_time
def part_1(first, second):
    first.sort()
    second.sort()

    difference = 0
    for x, y in zip(first, second):
        difference += abs(y - x)

    return difference


@execution_time
def part_2(first, second):
    similarity_score = 0
    for val in first:
        similarity_score += val * second.count(val)

    return similarity_score


if __name__ == "__main__":
    a, b = read_input()
    part_1(a, b)  # Correct answer: 1151792
    part_2(a, b)  # Correct answer: 21790168