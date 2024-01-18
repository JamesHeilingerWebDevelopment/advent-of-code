import copy
from collections import namedtuple
from sys import argv
from time import time


M = namedtuple("M", "destination source length")

BIG_MAP = {}


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
                        )
                    )
                )
            )
        )
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


def seed_generator():
    odd_items = [BIG_MAP["seeds"][x] for x in range(len(BIG_MAP["seeds"])) if x % 2 == 0]
    even_items = [BIG_MAP["seeds"][x] for x in range(len(BIG_MAP["seeds"])) if x % 2 == 1]

    for start, length in zip(odd_items, even_items):
        print(f"Start: {start}, Length: {length}, Time: {time()}")
        value = copy.copy(start)
        while value < start + length:
            yield value
            value += 1


def part_1():
    start_time = time()
    locations = []
    for seed in BIG_MAP["seeds"]:
        locations.append(big_mapper(seed))
    print(f"Part 1: {min(locations)} | Execution time: {time() - start_time}")


def part_2():
    start_time = time()
    print("\nStarting part 2! This is going to take a few hours...")
    closest_location = 9999999999999
    for seed in seed_generator():
        current_location = big_mapper(seed)
        if current_location < closest_location:
            closest_location = current_location
    print(f"Part 2: {closest_location} | Execution time: {time() - start_time}")


def small_backwards_mapper(name: str, val: int) -> int:
    for m in BIG_MAP[name]:
        if val >= m.destination and val < m.destination + m.length:
            return val + m.source - m.destination
    return val


def valid_seed(seed: int) -> bool:
    return False


def big_backwards_mapper(location):
    return valid_seed(
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


if __name__ == "__main__":
    data = read_input()
    parse_input(data)
    part_1()  # Correct answer: 993500720
    # Part 2 took 4h 55m 52.090323s to finish - 4:55:52.090323
    # Part 2 takes way too long to finish...
    # Ways to speed up part 2:
    #   * Can work backwards, starting from location 0 and finding the seed that matches that location.
    #        Should be quicker because I only have to search trhough ~5 million possibilities.
    #   * Try solving using the set idea from 2023 Day 19
    part_2()  # Correct answer: 4917124