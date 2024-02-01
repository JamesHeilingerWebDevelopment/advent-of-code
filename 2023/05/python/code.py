import copy
from collections import namedtuple
from functools import wraps
from sys import argv
from time import perf_counter, time


M = namedtuple("M", "destination source length")

BIG_MAP = {}


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
        return fp.read()


def small_mapper(name: str, val: int) -> int:
    for m in BIG_MAP[name]:
        if val >= m.source and val < m.source + m.length:
            return val + m.destination - m.source
    return val


def big_mapper(seed) -> int:
    return small_mapper(
        "humidity-to-location",
        small_mapper(
            "temperature-to-humidity",
            small_mapper(
                "light-to-temperature",
                small_mapper(
                    "water-to-light",
                    small_mapper(
                        "fertilizer-to-water",
                        small_mapper(
                            "soil-to-fertilizer",
                            small_mapper("seed-to-soil", seed),
                        ),
                    ),
                ),
            ),
        ),
    )


def parse_input(data):
    sections = data.split("\n\n")
    for section in sections:
        section_name, section_data = section.split(":")
        section_name = section_name.strip(" map")
        section_data = section_data.strip()

        if "seeds" not in section_name:
            BIG_MAP[section_name] = []
            for line in section_data.split("\n"):
                map_vals = line.split()
                BIG_MAP[section_name].append(
                    M(int(map_vals[0]), int(map_vals[1]), int(map_vals[2]))
                )
        else:
            BIG_MAP[section_name] = [int(x) for x in section_data.split()]


def seed_range_creator():
    odd_items = [BIG_MAP["seeds"][x] for x in range(len(BIG_MAP["seeds"])) if x % 2 == 0]
    even_items = [BIG_MAP["seeds"][x] for x in range(len(BIG_MAP["seeds"])) if x % 2 == 1]

    seed_ranges = []
    for start, length in zip(odd_items, even_items):
        seed_ranges.append([start, start + length])

    return seed_ranges


def seed_generator():
    odd_items = [BIG_MAP["seeds"][x] for x in range(len(BIG_MAP["seeds"])) if x % 2 == 0]
    even_items = [BIG_MAP["seeds"][x] for x in range(len(BIG_MAP["seeds"])) if x % 2 == 1]

    for start, length in zip(odd_items, even_items):
        print(f"Start: {start}, Length: {length}, Time: {time()}")
        value = copy.copy(start)
        while value < start + length:
            yield value
            value += 1


@execution_time
def part_1():
    locations = []
    for seed in BIG_MAP["seeds"]:
        locations.append(big_mapper(seed))

    return min(locations)


@execution_time
def part_2_original():
    print("\nStarting part 2! This is going to take a few hours...")

    closest_location = 9999999999999
    for seed in seed_generator():
        current_location = big_mapper(seed)
        if current_location < closest_location:
            closest_location = current_location

    return closest_location


def small_backwards_mapper(name: str, val: int) -> int:
    for m in BIG_MAP[name]:
        if val >= m.destination and val < m.destination + m.length:
            return val + m.source - m.destination
    return val


def valid_seed(ranges: list[list[int]], seed: int) -> bool:
    for range in ranges:
        start, end = range
        if seed > start and seed < end:
            return True

    return False


def big_backwards_mapper(location, seed_ranges):
    return valid_seed(
        seed_ranges,
        small_backwards_mapper(
            "seed-to-soil",
            small_backwards_mapper(
                "soil-to-fertilizer",
                small_backwards_mapper(
                    "fertilizer-to-water",
                    small_backwards_mapper(
                        "water-to-light",
                        small_backwards_mapper(
                            "light-to-temperature",
                            small_backwards_mapper(
                                "temperature-to-humidity",
                                small_backwards_mapper("humidity-to-location", location),
                            ),
                        ),
                    ),
                ),
            ),
        )
    )


@execution_time
def part_2(data):
    seed_ranges = seed_range_creator()
    location = 0
    while True:
        if big_backwards_mapper(location, seed_ranges):
            return location
        location += 1


if __name__ == "__main__":
    data = read_input()
    parse_input(data)
    part_1()  # Correct answer: 993500720
    # part_2_original()  # My original brute force solution for Part 2 took 4h 55m 52s to finish - 4:55:52
    part_2(data)  # Correct answer: 4917124
    #  Try solving using the set idea from 2023 Day 19