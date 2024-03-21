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
        return fp.readlines()


@execution_time
def part_1(data):
    print(f"Part 1: {None}")


@execution_time
def part_2(data):
    print(f"Part 2: {None}")


if __name__ == "__main__":
    data = read_input()
    part_1(data)  # Correct answer: 
    part_2(data)  # Correct answer: 